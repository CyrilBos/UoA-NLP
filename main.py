import nltk

from Database import DatabaseManager

from KeywordProcessor import KeywordProcessor
from LatentDirichletAllocation import LatentDirichletAllocation

from Logger import logger

def RankKeywords(docs):
    kwpcsr = KeywordProcessor(docs)

    words_occurences = kwpcsr.count_keywords()


    #print('Occurences for each stemmed and lemmatized keyword: ')
    #print(words_occurences)
    #print('Sorted by descending occurence: ')
    sorted_words = sorted(words_occurences, key=words_occurences.__getitem__, reverse=True)
    #print(sorted_words)
    return sorted_words

def LDA(docs, save_filename):
    lda = LatentDirichletAllocation(docs)
    return lda.compute(save_filename)


connect_string = "dbname=uoa-nlp user=admin"
dbmg = DatabaseManager(connect_string)
questions_db = dbmg.query("select * from questions", None, 'dict')

questions = {}

for question in questions_db:
    if question['content'] is not None:
        questions[question['question_id']] = {}
        questions[question['question_id']]['content'] = question['content']
    else:
        logger.error('Question of ID {} has no content'.format(question['question_id']))


replies_db = dbmg.query("select * from replies", None, 'dict')

replies = []

for reply in replies_db:
    if reply['text'] is not None:
        replies.append(question['text'])
    else:
        logger.error('Reply of ID {} has no text'.format(question['reply_id']))

replies_by_question_db = dbmg.query("""select reply_id, text, question_id
from replies
where question_id in
    ( select question_id
    from replies group by question_id)
    order by question_id asc""", None, 'dict')

replies_by_question = {}

for reply_by_question in replies_by_question_db:
    question_id = reply_by_question['question_id']
    if question_id not in replies_by_question.keys():
        replies_by_question[question_id] = {}
    if 'replies' not in replies_by_question[question_id].keys():
        replies_by_question[question_id]['replies'] = []

    replies_by_question[question_id]['replies'].append(reply_by_question['text'])


for question in replies_by_question:
    replies_by_question[question]['replies_keywords'] = RankKeywords(replies_by_question[question]['replies'])
    print(question)
    print(questions[question]['content'])
    #print(replies_by_question[question]['replies_keywords'])
    replies_by_question[question]['ldamodel'] = LDA(replies_by_question[question]['replies'], "lda_replies_by_question_{}".format(question))
    print(replies_by_question[question]['ldamodel'].print_topics(num_topics=-1, num_words=20))


#RankKeywords(questions)
#RankKeywords(replies)
#LDA(questions, "lda_questions")
#LDA(replies, "lda_replies")