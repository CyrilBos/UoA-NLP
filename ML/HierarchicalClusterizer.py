import numpy as np
import scipy as sp

import matplotlib.pyplot as plt

from sklearn.cluster import AgglomerativeClustering
from sklearn.utils.testing import SkipTest
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer

from ML.ClassifierData import ClassifierData

class WardClusterizer:
    def __init__(self, data, n_clusters, verbose=True):
        vectorizer = TfidfVectorizer(max_df=0.5, max_features=n_features,
                                     min_df=2, stop_words='english',
                                     use_idf=True)
        
        self.__data = vectorizer.fit_transform(data)
        self.__n_clusters = n_clusters;
        self.__verbose = verbose

    def compute(self, n_features, n_clusters):
        tf_idf_vectorizer = TfidfVectorizer(max_df=0.5, max_features=n_features,
                                     min_df=2, stop_words='english')

        X = tf_idf_vectorizer.fit_transform(self.__data)


        ac = AgglomerativeClustering(n_clusters=self.__n_clusters, linkage='ward', verbose=self.__verbose).fit(X)

        return ac;