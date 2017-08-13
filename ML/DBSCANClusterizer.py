from sklearn.cluster import DBSCAN
from sklearn.feature_extraction.text import TfidfVectorizer

from ML.Clusterizer import Clusterizer
from NLP.InputPreprocessor import InputPreprocessor


class DBSCANClusterizer(Clusterizer):
    def compute(self, eps=0.3, min_samples=10):
        dbscan = DBSCAN(eps=0.3, min_samples=min_samples, n_jobs=self.__jobs, algorithm='ball_tree').fit(self.__data.toarray())
        self.__labels = dbscan.labels_

        return dbscan

