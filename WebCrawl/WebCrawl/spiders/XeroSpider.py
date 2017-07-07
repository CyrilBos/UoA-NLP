# -*- coding: utf-8 -*-
import datetime
import scrapy
from scrapy.spiders import Spider


import psycopg2
connection_string = 'dbname=uoa-xero user=admin'


class XeroSpider(Spider):
    name = "XeroSpider"
    forum_number = -1

    data = {}

    def closed(self, reasaon):
        self.update_database()

    def start_requests(self):
        urls = [
            'https://community.xero.com/?domain=business'
        ]
        #start = datetime.datetime.now()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        #end = datetime.datetime().now()

        #print('Crawling, parsing and DB updating done in', end - start)

    def parse(self, response):
        print("PARSING FORUM: " + response.url)

        for topic in response.css('td.topicName'):
            forum_name = topic.css('a::text').extract_first()
            self.data[forum_name] = {}

            self.data[forum_name]['replies_number'] = \
                response.css('td.replies'.format(self.forum_number - 1)).css('a::text').extract()[self.forum_number]
            self.forum_number += 1

            link = topic.css('a::attr(href)').extract_first()
            self.data[forum_name]['url'] = link

            yield response.follow(link, self.parse_forum_page, meta={'forum_name': forum_name})

    def parse_forum_page(self, response):
        forum_name = response.meta['forum_name']
        print("PARSING PAGE: " + response.url)
        self.data[forum_name]['discussions'] = {}

        for discussion in response.xpath('//tr[re:test(@id, "question_\d*")]'):
            id = discussion.xpath('./@id').extract_first()
            id = id[id.index('_') + 1:]
            if id not in self.data[forum_name]['discussions'].keys():
                self.data[forum_name]['discussions'][id] = {}

            title = discussion.css('div > a::text').extract_first().strip()
            url = discussion.css('div > a::attr(href)').extract_first()
            self.data[forum_name]['discussions'][id]['title'] = title
            self.data[forum_name]['discussions'][id]['url'] = url

            yield response.follow(self.data[forum_name]['discussions'][id]['url'], self.parse_discussion,
                                  meta={'forum_name': forum_name, 'discussion_id': id, 'title': title, 'url': url})

        next_forum_page = response.css('div.topicPages').xpath('./a[contains(@class, "right")]/@href').extract_first()
        yield response.follow(next_forum_page, self.parse_forum_page, meta={'forum_name': forum_name})

    def parse_discussion(self, response):
        forum_name = response.meta['forum_name']
        id = response.meta['discussion_id']
        print("PARSING DISCUSSION: " + response.url)

        if id not in self.data[forum_name]['discussions'].keys():
            self.data[forum_name]['discussions'][id] = {}

            self.data[forum_name]['discussions'][id]['title'] = response.meta['title']
            self.data[forum_name]['discussions'][id]['url'] = response.meta['url']

        self.data[forum_name]['discussions'][id]['content'] = response.css(
            'div#currentDetails::text').extract_first().strip()
        self.data[forum_name]['discussions'][id]['date'] = response.css(
            'div#MainQuestion span.date::attr("title")').extract_first()

        author = response.css(
            'div#MainQuestion p.author a.profile::text').extract_first()
        if author is None:
            author = response.css(
            'div#MainQuestion p.author::text').extract_first()
        self.data[forum_name]['discussions'][id]['author'] = author.strip()

        self.data[forum_name]['discussions'][id]['replies'] = {}

        best_slct = response.css('div#BestAnswer')
        best_id = best_slct.xpath('./div[re:test(@id, "answer\d*only")]/@id').extract_first()
        if best_id:

            best_id = best_id[best_id.index('r') + 1:best_id.index('o')]
            best_author = best_slct.css( 'a#author::text').extract_first()
            if best_author is None:
                best_author = best_slct.css('p.author::text').extract_first()

            self.data[forum_name]['discussions'][id]['best_reply'] = {'id': best_id,
                                                                      'content': ''.join(best_slct.css(
                                                                          'div.answerContent::text').extract()),
                                                                      'author': best_author.strip(),
                                                                      'date': best_slct.css('p.author span.date::attr("title")').extract_first()}

        for reply in response.css('div#Answers > div.answer'):
            reply_id = reply.css('::attr(id)').extract_first()
            if reply_id is not None:
                reply_id = reply_id[reply_id.index('r') + 1:]

                reply_author = reply.css('a#author::text').extract_first()
                if reply_author is None:
                    reply_author = reply.css('p.author::text').extract_first()

                self.data[forum_name]['discussions'][id]['replies'][reply_id] = {'content': ''.join(reply.css(
                    'div.answerContent::text').extract()),
                                                                                 'author': reply_author.strip(),
                                                                                 'date': reply.css('p.author span.date::attr("title")').extract_first()}

    def update_database(self):
        conn = psycopg2.connect(connection_string)
        cur = conn.cursor()

        forum_query = 'insert into forum_details values(default, %s, %s, %s)'
        reply_query = 'insert into reply values (default, %s, %s, %s, %s, %s)'
        question_query = 'insert into question values (default, %s, %s, %s, %s, %s, %s) returning question_id'

        print(forum_query, reply_query, question_query)
        for forum in self.data:
            print(self.data[forum].keys())
            cur.execute(forum_query, (forum, self.data[forum]['url'], '0'))
            print(forum)
            print(type(forum))
            forum_id = cur.execute('select forum_details_id from forum_details where name = %s', (forum,))
            print('select forum_details_id where name = {}'.format(forum))
            for discussion in self.data[forum]['discussions']:
                print(question_query % (self.data[forum]['discussions'][discussion]['title'],
                                             self.data[forum]['discussions'][discussion]['date'],
                                             self.data[forum]['discussions'][discussion]['author'], forum_id,
                                             self.data[forum]['discussions'][discussion]['content'],
                                             self.data[forum]['discussions'][discussion]['url']))
                cur.execute(question_query, (self.data[forum]['discussions'][discussion]['title'],
                                             self.data[forum]['discussions'][discussion]['date'],
                                             self.data[forum]['discussions'][discussion]['author'], forum_id,
                                             self.data[forum]['discussions'][discussion]['content'],
                                             self.data[forum]['discussions'][discussion]['url']))
                question_id = cur.fetchone()[0]
                print(self.data[forum]['discussions'][discussion].keys())
                if 'best_reply' in self.data[forum]['discussions'][discussion].keys():
                    print(reply_query % (self.data[forum]['discussions'][discussion]['best_reply']['content'],
                                              self.data[forum]['discussions'][discussion]['best_reply']['date'],
                                              self.data[forum]['discussions'][discussion]['best_reply']['author'],
                                              question_id, True))
                    cur.execute(reply_query, (self.data[forum]['discussions'][discussion]['best_reply']['content'],
                                              self.data[forum]['discussions'][discussion]['best_reply']['date'],
                                              self.data[forum]['discussions'][discussion]['best_reply']['author'],
                                              question_id, True))
                for reply in self.data[forum]['discussions'][discussion]['replies']:
                    print(reply_query % (self.data[forum]['discussions'][discussion]['replies'][reply]['content'],
                                              self.data[forum]['discussions'][discussion]['replies'][reply]['date'],
                                              self.data[forum]['discussions'][discussion]['replies'][reply]['author'],
                                              question_id, False))
                    cur.execute(reply_query, (self.data[forum]['discussions'][discussion]['replies'][reply]['content'],
                                              self.data[forum]['discussions'][discussion]['replies'][reply]['date'],
                                              self.data[forum]['discussions'][discussion]['replies'][reply]['author'],
                                              question_id, False))
                cur.close()
                conn.close()