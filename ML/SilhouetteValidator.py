import numpy as np
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_samples, silhouette_score

class SilhouetteValidator:
    def __init__(self):
        return

    def compute(self, n_clusters, data, labels):
        silhouette_avg = silhouette_score(X, cluster_labels)
        print("For n_clusters =", n_clusters,
              " The average silhouette_score is :", silhouette_avg)

        # Compute the silhouette scores for each sample
        #sample_silhouette_values = silhouette_samples(X, cluster_labels)

        return silhouette_avg
