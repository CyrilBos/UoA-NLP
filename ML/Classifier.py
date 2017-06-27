import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline

from ML.ClassifierData import ClassifierData


class Classifier:
    """
    Class that uses TF-IDF vector text representation and the SGD algorithm to classify texts.
    """
    def __init__(self, data, target, target_names):
        """
        Initializes the classifier by training it on the given data.
        :param data: text documents to train the classifier on
        :type data: list
        :param target: category indexes for each text document
        :type target: list
        :param target_names: category names
        :type target_names: list
        """
        self.__clf_data = ClassifierData(data, target, target_names)
        text_clf = Pipeline([('vect', CountVectorizer()),
                             ('tfidf', TfidfTransformer()),
                             ('clf', SGDClassifier(alpha=.0001, n_iter=100,
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
        """
        Evaluates the precision of the classifier by running its prediction on the training data set
        :return: the percentage of correctly predicted categories
        :rtype: float
        """
        return np.mean(self.predict(self.__clf_data.data) == self.__clf_data.target)

    def predict(self, data):
        """
        Predicts the category of the data parameter.
        :param data: text document
        :type data: str
        :return: the predicted category index
        :rtype: int
        """
        return self.__text_clf.predict(data)




