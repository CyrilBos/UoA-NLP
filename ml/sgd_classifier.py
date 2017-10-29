import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import sklearn.linear_model
from sklearn.pipeline import Pipeline

from ml.Classifier import Classifier
from ml.ClassifierData import ClassifierData


class SGDClassifier(Classifier):
    """
    Class that uses TF-IDF vector text representation and the SGD algorithm to classify texts.
    """
    def __init__(self, data, target, target_names, alpha=.0001, n_iter=100, penalty='l2', preprocess=False):
        """
        Initializes the classifier by training it on the given data.
        :param data: text documents to train the classifier on
        :type data: list
        :param target: category indexes for each text document
        :type target: list
        :param target_names: category names
        :type target_names: list
        :param alpha: constant to multiply the regularization term (penalty)
        :type alpha: float
        :param n_iter: number of iterations of the learning process
        :type n_iter: int
        :param penalty: level of penalty to be used. Can be 'none', 'l2', 'l1', or 'elasticnet'
        :type target_names: list
        """
        super().__init__(data, target, target_names, sklearn.linear_model.SGDClassifier(alpha=alpha, n_iter=n_iter,
                                                   penalty=penalty), preprocess=preprocess)