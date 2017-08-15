import numpy as np
import csv
from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer

from ML.ClassifierData import ClassifierData

class HierarchicalClusterizer:
    def __init__(self, data, n_clusters, linkage = 'ward'):
        self.__n_clusters = n_clusters
        self.__data = data
        self.__linkage = linkage

    def compute(self, n_features):

        tf_idf_vectorizer = TfidfVectorizer(max_df=0.5, max_features=n_features,
                                     min_df=2, stop_words='english')


        X = (tf_idf_vectorizer.fit_transform(self.__data)).toarray()

        self.__ac = AgglomerativeClustering(n_clusters=self.__n_clusters, linkage=self.__linkage).fit(X)
        
        return self.__ac

    def print_clusters(self, min_len = 2):
        labels = (self.__ac).labels_
       
        clusters = {}
        n = 0
        for item in labels:		# put clusters in a dict
            if item in clusters:
                clusters[item].append(self.__data[n])
            else:
                clusters[item] = [self.__data[n]]
            n += 1

        for item in clusters:         # print off every cluster larger than parameter provided
            c_len = len(clusters[item])
            if(c_len >= min_len):
                print("Cluster ", item)
                for i in range(0,c_len):
                    print("   ", clusters[item][i])
                    if (i > 10):
                        break;


        #cluster_0 = np.where(clusters==0)
        #X_cluster_0 = X[cluster_0]
        #print(X_cluster_0)
        

	
        #for i in range(self.__n_clusters):
        #   print("Cluster %d:" % i, end='')
        #   print(' %s ' % terms[0])

    def print_to_file(self):
        labels = (self.__db).labels_
       
        clusters = {}
        n = 0
        for item in labels:     # put clusters in a dict
            if item in clusters:
                clusters[item].append(self.__data[n])
            else:
                clusters[item] = [self.__data[n]]
            n += 1

        with open('Hierarchical_Clusters.csv', 'w') as f: 
            w = csv.DictWriter(f, clusters.keys())
            w.writeheader()
            w.writerow(clusters)
