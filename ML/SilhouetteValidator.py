import numpy as np
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_samples, silhouette_score

class SilhouetteValidator:
    def __init__(self, n_clusters, data, labels):
        
        self.__n_clusters = n_clusters
        self.__data = data
        self.__labels = labels

        return

    def compute(self):
        silhouette_avg = silhouette_score(self.__data, self.__labels, sample_size = 1000)
        print("For n_clusters =", self.__n_clusters,
              " The average silhouette_score is :", silhouette_avg)

        # Compute the silhouette scores for each sample
        #sample_silhouette_values = silhouette_samples(X, cluster_labels)

        return silhouette_avg
