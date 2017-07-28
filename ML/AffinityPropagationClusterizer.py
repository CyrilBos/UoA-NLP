from sklearn.cluster import AffinityPropagation
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from itertools import cycle

class AffinityPropagationClusterizer:
    def __init__(self, data, verbose=True):
        self.__data = data
        self.__verbose = verbose

    def compute(self, n_features, max_iter=100):
        tf_idf_vectorizer = TfidfVectorizer(max_df=0.5, max_features=n_features,
                                     min_df=2, stop_words='english')

        X = tf_idf_vectorizer.fit_transform(self.__data)

        af = AffinityPropagation(preference=-50, max_iter=max_iter, verbose=self.__verbose).fit(X)

        cluster_centers_indices = af.cluster_centers_indices_
        labels = af.labels_

        n_clusters = len(cluster_centers_indices)

        print(n_clusters)

        plt.close('all')
        plt.figure(1)
        plt.clf()

        colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
        for k, col in zip(range(n_clusters), colors):
            class_members = labels == k
            cluster_center = X[cluster_centers_indices[k]]
            plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
            plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                     markeredgecolor='k', markersize=14)
            for x in X[class_members]:
                plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

        plt.title('Estimated number of clusters: %d' % n_clusters)
        plt.show()