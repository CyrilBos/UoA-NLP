from sklearn.cluster import AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from itertools import cycle

from ML.Clusterizer import Clusterizer


class AffinityPropagationClusterizer(Clusterizer):
    def compute(self, n_features, max_iter=100):
        tf_idf_vectorizer = TfidfVectorizer(max_df=0.5, max_features=n_features,
                                     min_df=2, stop_words='english')

        X = tf_idf_vectorizer.fit_transform(self._data)

        af = AffinityPropagation(preference=-50, max_iter=max_iter, verbose=self._verbose).fit(X)

        cluster_centers_indices = af.cluster_centers_indices_
        labels = af.labels_

        n_clusters = len(cluster_centers_indices)

        print(n_clusters)