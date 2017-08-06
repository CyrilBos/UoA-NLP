import numpy as np

from sklearn.cluster import AgglomerativeClustering
from sklearn.utils.testing import SkipTest
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer

from ML.ClassifierData import ClassifierData

class HierarchicalClusterizer:
    def __init__(self, data, n_clusters, linkage = 'ward', verbose=True):
        self.__n_clusters = n_clusters;
        self.__verbose = verbose
        self.__data = data
        self.__linkage = linkage

    def compute(self, n_features):

        tf_idf_vectorizer = TfidfVectorizer(max_df=0.5, max_features=n_features,
                                     min_df=2, stop_words='english')

        X = tf_idf_vectorizer.fit_transform(self.__data)

        ac = AgglomerativeClustering(n_clusters=self.__n_clusters, linkage=self.__linkage, verbose=self.__verbose).fit(X)

        label = ac.labels_

        return ac;