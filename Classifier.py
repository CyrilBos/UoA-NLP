from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

import numpy as np

from Database import DatabaseManager
from Logger import logger


from sklearn.pipeline import Pipeline


class Classifier:
    class ClassifierData:
        __data = []
        __target = []
        __target_names = []

        def __init__(self, data, target, target_names):
            self.__data = data
            self.__target = target
            self.__target_names = target_names

        @property
        def data(self):
            return self.__data

        @property
        def target(self):
            return self.__target

        @property
        def target_names(self):
            return self.__target_names


    def __init__(self, data, target, target_names):
        self.__clf_data = Classifier.ClassifierData(data, target, target_names)

    @property
    def data(self):
        return self.__clf_data.data

    @property
    def target(self):
        return self.__clf_data.target

    @property
    def target_names(self):
        return self.__clf_data.target_names

connect_string = "dbname=uoa-nlp user=admin"
dbmg = DatabaseManager(connect_string)
questions_forum_db = dbmg.query(
    "select * from questions join forum_details on forum_details.forum_details_id = questions.forum_details_id", None,
    'dict')
dbmg.close()

data = []
target = []
target_names = [] # type('Bunch', (), {'data':[], 'target':[], 'target_names':[]})
# questions = {'data':[], 'target':[], 'target_names':[]}

for question_forum in questions_forum_db:
    content = question_forum['text']
    if question_forum['name'] not in target_names:
        target_names.append(question_forum['name'])
    if content is not None:
        data.append(content)
        target.append(target_names.index(question_forum['name']))

questions = Classifier(data, target, target_names)
"""
for forum in questions_by_forum:
    print('FORUM', forum)
    for question in questions_by_forum[forum]:
        print(question)
"""

text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(alpha=.0001, n_iter=50,
                                           penalty='l2')),
                     ])


text_clf = text_clf.fit(questions.data, questions.target)

predicted = text_clf.predict(questions.data)
print(np.mean(predicted == questions.target))

doc_predict = ["I am having issues with api authentication"]

sup = text_clf.predict(doc_predict)
print(sup)
print(questions.target_names)
print(questions.target_names[sup[0]])
