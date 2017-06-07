import nltk

from Database import DatabaseManager

from KeywordProcessor import KeywordProcessor

from Logger import logger




connect_string = "dbname=uoa-nlp user=admin"
dbmg = DatabaseManager(connect_string)
result = dbmg.query("select * from questions", None, 'dict')
print('Questions contained in the database: ')
print(result)

docs = []

for question in result:
    if question['content'] is not None:
        docs.append(question['content'])
    else:
        logger.error('Question of ID {} has no content'.format(question['question_id']))

print(docs)

kwpcsr = KeywordProcessor(docs)


words_occurences = kwpcsr.count_keywords()



print('Occurences for each stemmed and lemmatized keyword: ')
print(words_occurences)
print('Sorted by descending occurence: ')
print(sorted(words_occurences, key=words_occurences.__getitem__, reverse=True))