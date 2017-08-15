from sklearn.cluster import DBSCAN
from sklearn.feature_extraction.text import TfidfVectorizer
import csv

from ML.Clusterizer import Clusterizer
from NLP.InputPreprocessor import InputPreprocessor


class DBSCANClusterizer(Clusterizer):
    def compute(self, eps=0.3, min_samples=10):
        dbscan = DBSCAN(eps=0.3, min_samples=min_samples, n_jobs=self.__jobs, algorithm='ball_tree').fit(self.__data.toarray())
        self.__labels = dbscan.labels_

        return dbscan

    def print_clusters(self, min_len=2):
        clusters = {}
        n = 0
        for item in self.__labels:  # put clusters in a dict
            if item in clusters:
                clusters[item].append(self.__data[n])
            else:
                clusters[item] = [self.__data[n]]
            n += 1

        for item in clusters:  # print off every cluster larger than parameter provided
            c_len = len(clusters[item])
            if (c_len >= min_len):
                print("Cluster ", item)
                for i in range(0, c_len):
                    print("   ", clusters[item][i])
                    if (i > 10):
                        break

    def print_to_file(self):

        clusters = {}
        n = 0
        for item in self.__labels:  # put clusters in a dict
            if item in clusters:
                clusters[item].append(self.__data[n])
            else:
                clusters[item] = [self.__data[n]]
            n += 1

        with open('DBSCAN_Clusters.csv', 'w') as f:
            w = csv.DictWriter(f, clusters.keys())
            w.writeheader()
            w.writerow(clusters)
