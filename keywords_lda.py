from Database.DatabaseHelper import DatabaseHelper
from Database.Configuration import connection_string
from NLP.KeywordExtractor import KeywordExtractor

from Logger import logger
from NLP.LatentDirichletAllocation import LatentDirichletAllocation
from NLP.LatentSemanticAnalysor import LatentSemanticAnalyser


def rankKeywords(docs):
    """
    Sorts the extracted keywords from docs by frequency and returns the result
    :param docs: documents
    :type docs: list
    :return: sorted words by frequency
    :rtype: list
    """
    kwpcsr = KeywordExtractor(docs)

    words_occurences = kwpcsr.count_keywords()


    #print('Occurences for each stemmed and lemmatized keyword: ')
    #print(words_occurences)
    #print('Sorted by descending occurence: ')
    sorted_words = sorted(words_occurences, key=words_occurences.__getitem__, reverse=True)
    #print(sorted_words)
    return sorted_words

def LDA(docs, topics, passes, save_filename):
    lda = LatentDirichletAllocation(docs)
    return lda.compute(topics, passes, save_filename)

def LSA(docs, topics, save_filename):
    lsi = LatentSemanticAnalyser(docs)
    return lsi.compute(topics, save_filename)


dbmg = DatabaseHelper(connection_string)
#replies_db = dbmg.select_query("select * from reply", None, fetch_to_dict=True)
questions = dbmg.select_query("""select * from question join forum_details on
                                question.forum_details_id = forum_details.forum_details_id
                                where community_id = %s
                              """, dbmg.get_community_id('Business'), fetch_to_dict=True)
#replies_by_question_db = dbmg.select_query("""select reply_id, text, question_id
#from reply
#where question_id in
#    ( select question_id
#    from replyvgroup by question_id)
#    order by question_id asc""", None, fetch_to_dict=True)

#replies_question_forum = dbmg.get_replies_question_forum()
dbmg.close()

questions_contents = []

for question in questions:
    questions_contents.append(question['content'])





#replies = []

"""
for reply in replies_db:
    if reply['text'] is not None:
        replies.append(reply['text'])
    else:
        logger.error('Reply of ID {} has no text'.format(reply['reply_id']))

replies_by_question = {}

for reply_by_question in replies_by_question_db:
    question_id = reply_by_question['question_id']
    if question_id not in replies_by_question.keys():
        replies_by_question[question_id] = {}
    if 'replies' not in replies_by_question[question_id].keys():
        replies_by_question[question_id]['replies'] = []

    replies_by_question[question_id]['replies'].append(reply_by_question['text'])
"""


######################

#for question in replies_by_question:
    #replies_by_question[question]['replies_keywords'] = RankKeywords(replies_by_question[question]['replies'])
    #print(question)
    #print(questions[question]['content'])
    #print(replies_by_question[question]['replies_keywords'])
    #replies_by_question[question]['ldamodel'] = LDA(replies_by_question[question]['replies'], "lda_replies_by_question_{}".format(question))
    #print(replies_by_question[question]['ldamodel'].print_topics(num_topics=-1, num_words=20))



#print(rankKeywords(questions_contents))
model, crp, dic = LDA(questions_contents, 20, 10, 'lda-saves/lsa-questions')

for topic in model.show_topics():
    print(topic[0], topic[1])

# print(RankKeywords(replies))

#for forum in replies_question_forum:
    #texts = []
    #for question in replies_question_forum[forum]:
    #    for reply_text in replies_question_forum[forum][question]['replies_text']:
    #        texts.append(reply_text)
    #lda, crps, dict = LDA(texts, 100, 20, "lda-saves/lda_replies_question_forum_{}".format(forum))

    #print(lda.print_topics(num_topics=-1, num_words=-1))

#lsi, crps, dict = LSA(questions_contents, 400, 'lda-saves/lsi-questions')