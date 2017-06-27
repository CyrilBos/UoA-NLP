from Database.DatabaseHelper import DatabaseHelper
from Database.Configuration import connection_string
from NLP.KeywordProcessor import KeywordProcessor

from Logger import logger
from NLP.LatentDirichletAllocation import LatentDirichletAllocation
from NLP.LatentSemanticAnalysor import LatentSemanticAnalyser


def rankKeywords(docs):
    kwpcsr = KeywordProcessor(docs)

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
replies_db = dbmg.my_query("select * from replies", None, fetch_to_dict=True)
questions_db = dbmg.my_query("select * from questions", None, fetch_to_dict=True)
replies_by_question_db = dbmg.my_query("""select replies_id, text, questions_id
from replies
where questions_id in
    ( select questions_id
    from replies group by questions_id)
    order by questions_id asc""", None, fetch_to_dict=True)

replies_question_forum = dbmg.get_replies_question_forum()

questions_content = dbmg.get_questions_content()

dbmg.close()

questions = {}

for question in questions_db:
    if question['content'] is not None:
        questions[question['questions_id']] = {}
        questions[question['questions_id']]['content'] = question['content']
    else:
        logger.error('Question of ID {} has no content'.format(question['questions_id']))



replies = []

for reply in replies_db:
    if reply['text'] is not None:
        replies.append(reply['text'])
    else:
        logger.error('Reply of ID {} has no text'.format(reply['replies_id']))

replies_by_question = {}

for reply_by_question in replies_by_question_db:
    question_id = reply_by_question['questions_id']
    if question_id not in replies_by_question.keys():
        replies_by_question[question_id] = {}
    if 'replies' not in replies_by_question[question_id].keys():
        replies_by_question[question_id]['replies'] = []

    replies_by_question[question_id]['replies'].append(reply_by_question['text'])




#for question in replies_by_question:
    #replies_by_question[question]['replies_keywords'] = RankKeywords(replies_by_question[question]['replies'])
    #print(question)
    #print(questions[question]['content'])
    #print(replies_by_question[question]['replies_keywords'])
    #replies_by_question[question]['ldamodel'] = LDA(replies_by_question[question]['replies'], "lda_replies_by_question_{}".format(question))
    #print(replies_by_question[question]['ldamodel'].print_topics(num_topics=-1, num_words=20))




    #if question_id in questions.keys():
    #    print(questions[question_id]['content'])
    #print('DBD', replies_question_forum[forum_id][question_id]['replies_text'])


#RankKeywords(questions)

# print(RankKeywords(replies))
#LDA(questions, "lda_questions")
#for forum in replies_question_forum:
    #texts = []
    #for question in replies_question_forum[forum]:
    #    for reply_text in replies_question_forum[forum][question]['replies_text']:
    #        texts.append(reply_text)
    #lda, crps, dict = LDA(texts, 100, 20, "lda-saves/lda_replies_question_forum_{}".format(forum))

    #print(lda.print_topics(num_topics=-1, num_words=-1))

lsi, crps, dict = LSA(questions_content, 400, 'lda-saves/lsi-questions')