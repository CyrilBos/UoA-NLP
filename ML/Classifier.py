import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

from ML.ClassifierData import ClassifierData


class Classifier:
    def __init__(self, data, target, target_names):
        self.__clf_data = ClassifierData(data, target, target_names)
        text_clf = Pipeline([('vect', CountVectorizer()),
                             ('tfidf', TfidfTransformer()),
                             ('clf', SGDClassifier(alpha=.0001, n_iter=50,
                                                   penalty='l2')),
                             ])

        self.__text_clf = text_clf.fit(self.__clf_data.data, self.__clf_data.target)

    @property
    def data(self):
        return self.__clf_data.data

    @property
    def target(self):
        return self.__clf_data.target

    @property
    def target_names(self):
        return self.__clf_data.target_names

    def evaluate_precision(self):
        return np.mean(self.predict(self.__clf_data.data) == self.__clf_data.target)

    def predict(self, question):
        return self.__text_clf.predict(question)




