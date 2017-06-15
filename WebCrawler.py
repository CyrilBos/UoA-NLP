import scrapy
from scrapy.selector import Selector


class XeroSpider(scrapy.Spider):
    name = 'xerospider'
    start_urls = ['https://community.xero.com/?domain=business']
    forum_number = 0

    def parse(self, response):
        hxs = Selector(response)
        print(hxs.xpath('//td.replies'))
        for topic in response.css('td.topicName'):
            self.forum_number += 1
            print(response.xpath('//td.replies[{}]'.format(self.forum_number-1)).extract_first())
            yield {'forum_name': topic.css('a::text').extract_first(), "replies_nb": topic.xpath('//td.replies[{}]'.format(self.forum_number-1)).css('a::text').extract_first()}


        for next_page in response.css('td.topicName > a'):
            yield response.follow(next_page, self.parse)