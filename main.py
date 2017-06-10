import nltk
import pyLDAvis

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

def LDA(docs, topics, passes, save_filename):
    lda = LatentDirichletAllocation(docs)
    return lda.compute(topics, passes, save_filename)


connect_string = "dbname=uoa-nlp user=admin"
dbmg = DatabaseManager(connect_string)
replies_db = dbmg.query("select * from replies", None, 'dict')
questions_db = dbmg.query("select * from questions", None, 'dict')

questions = {}

for question in questions_db:
    if question['content'] is not None:
        questions[question['question_id']] = {}
        questions[question['question_id']]['content'] = question['content']
    else:
        logger.error('Question of ID {} has no content'.format(question['question_id']))



replies = []

print(replies_db)

for reply in replies_db:
    if reply['text'] is not None:
        replies.append(reply['text'])
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


#for question in replies_by_question:
    #replies_by_question[question]['replies_keywords'] = RankKeywords(replies_by_question[question]['replies'])
    #print(question)
    #print(questions[question]['content'])
    #print(replies_by_question[question]['replies_keywords'])
    #replies_by_question[question]['ldamodel'] = LDA(replies_by_question[question]['replies'], "lda_replies_by_question_{}".format(question))
    #print(replies_by_question[question]['ldamodel'].print_topics(num_topics=-1, num_words=20))


replies_question_forum_db = dbmg.query("""select *
from replies
join questions on questions.question_id = replies.question_id
join forum_details on questions.forum_detail_id = forum_details.forum_detail_id
""", None, dict)

replies_question_forum = {}
for reply_question_forum in replies_question_forum_db:
    forum_id = reply_question_forum[10]
    if forum_id not in replies_question_forum.keys():
        replies_question_forum[forum_id] = {}
    question_id = reply_question_forum[4]
    if question_id not in replies_question_forum[forum_id].keys():
        replies_question_forum[forum_id][question_id] = {}
        replies_question_forum[forum_id][question_id]['replies_text'] = []
    replies_question_forum[forum_id][question_id]['replies_text'].append(reply_question_forum[1])
    #if question_id in questions.keys():
    #    print(questions[question_id]['content'])
    #print('DBD', replies_question_forum[forum_id][question_id]['replies_text'])


#RankKeywords(questions)

# print(RankKeywords(replies))
#LDA(questions, "lda_questions")
for forum in replies_question_forum:
    texts = []
    for question in replies_question_forum[forum]:
        for reply_text in replies_question_forum[forum][question]['replies_text']:
            texts.append(reply_text)
    lda, ftg, osef = LDA(texts, 100, 20, "lda-saves/lda_replies_question_forum_{}".format(forum))

    #print(lda.print_topics(num_topics=-1, num_words=-1))