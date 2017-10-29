import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline

from ml.classifier import Classifier
from nlp.input_preprocessor import InputPreprocessor
from Utils.logger import logger

from ml.classifier_data import ClassifierData


class C45DecisionTreeClassifier(Classifier):
    """
    Class that uses TF-IDF vector text representation and the SGD algorithm to classify texts.
    """
    def __init__(self, data, target, target_names, preprocess=False):
        """
        Initializes the classifier by training it on the given data.
        :param data: text documents to train the classifier on
        :type data: list
        :param target: category indexes for each text document
        :type target: list
        :param target_names: category names
        :type target_names: list
        """
        super().__init__(data, target, target_names, DecisionTreeClassifier(criterion='entropy'), preprocess=preprocess)





