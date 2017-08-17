import numpy as np
import csv

from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer

from ML.Clusterizer import Clusterizer

class HierarchicalClusterizer(Clusterizer):
    def __init__(self, data, n_clusters, n_features=10, preprocess=False, linkage = 'ward', verbose=True, jobs=1):
        super().__init__(data, n_features=n_features, verbose=verbose, jobs=jobs, preprocess=preprocess)
        self.__n_clusters = n_clusters
        self.__linkage = linkage

    def compute(self):
        self.__ac = AgglomerativeClustering(n_clusters=self.__n_clusters, linkage=self.__linkage).fit(self._preprocessed_data.toarray())
        
        return self.__ac