import numpy as np

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer

from ml.Clusterizer import Clusterizer
from NLP.LatentDirichletAllocation import LatentDirichletAllocation


class KMeansClusterizer(Clusterizer):
    """
    This class uses KMeans to compute clusters of text documents and extract their features either using
    - TF-IDF vector representation
    - LDA topics representation
    """

    def lsa_clusterize(self, n_components, n_clusters, max_iter=5):
        """
        Computes the TF-IDF representation of the data then clusters them with the given parameters.
        :param n_clusters: Number of wanted clusters
        :type n_clusters: int
        :param max_iter: Number of iterations of the clusterization
        :type max_iter: int
        :param n_features: Number of features to compute with TF-IDF
        :type max_iter: int
        :param n_components: Number of components used for SVD dimensionality reduction
        :type max_iter: int
        :return: a tuple (clusters, lda model, lda vocabulary)
        :rtype: tuple
        """


        # Vectorizer results are normalized, which makes KMeans behave as
        # spherical k-means for better results. Since LSA/SVD results are
        # not normalized, we have to redo the normalization.
        svd = TruncatedSVD(n_components)
        normalizer = Normalizer(copy=False)
        lsa = make_pipeline(svd, normalizer)

        preprocessed_data = lsa.fit_transform(self._preprocessed_data)

        explained_variance = svd.explained_variance_ratio_.sum()
        print("Explained variance of the SVD step: {}%".format(
            int(explained_variance * 100)))

        print()

        km = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=max_iter, n_init=10,
                    verbose=self._verbose, n_jobs=self._jobs)

        print("Clustering sparse data with %s" % km)

        km.fit(preprocessed_data)

        self._labels = km.labels_

        return km

    def lda_clusterize(self, n_features, n_clusters, lda_iter=5, kmeans_iter=5):
        """
        Computes TF-IDF vectors of the documents and clusters them using KMeans.
        :param n_clusters: number of wanted clusters
        :return: tuple (clusters, feature list)
        """
        print("Extracting features from the training dataset using a sparse vectorizer")

        lda = LatentDirichletAllocation(self._data, self._jobs)
        lda_model, corpus, vocab = lda.compute(n_features, lda_iter)

        X = []
        lda_corpus = lda_model[corpus]
        for doc in lda_corpus:
            scores_vector = []
            for topic_score in doc:
                scores_vector.append(topic_score[1])
            while len(scores_vector) < n_features:
                scores_vector.append(0)
            X.append(scores_vector)
        X = np.array(X)

        print("n_samples: %d, n_features: %d" % X.shape)

        km = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=kmeans_iter, n_init=1,
                    verbose=self._verbose, n_jobs=self._jobs)

        
        print("Clustering sparse data with %s" % km)

        self.__processed_data = km.fit(X)
        self._labels = km.labels_
        return km, self.__processed_data
    
    def get_metrics(self, km, X):
        """
        Computes and returns the metrics using km and X as ground truth
        :param km: Ground truth KMeans clusters
        :param X: Ground truth feature list
        :return:
        """
        return metrics.homogeneity_score(self._labels, km.labels_), \
               metrics.completeness_score(self._labels, km.labels_), \
               metrics.v_measure_score(self._labels, km.labels_), \
               metrics.adjusted_rand_score(self._labels, km.labels_), \
               metrics.silhouette_score(X, km.labels_, sample_size=1000)

    def print_metrics(self, km, X):
        """
        Print the metrics using km and X as ground truth
        :param km: Ground truth KMeans clusters
        :param X: Ground truth feature list
        :return:
        """
        print("Homogeneity: %0.3f" % metrics.homogeneity_score(self._labels, km.labels_))
        print("Completeness: %0.3f" % metrics.completeness_score(self._labels, km.labels_))
        print("V-measure: %0.3f" % metrics.v_measure_score(self._labels, km.labels_))
        print("Adjusted Rand-Index: %.3f"
              % metrics.adjusted_rand_score(self._labels, km.labels_))
        print("Silhouette Coefficient: %0.3f"
              % metrics.silhouette_score(X, km.labels_, sample_size=1000))
