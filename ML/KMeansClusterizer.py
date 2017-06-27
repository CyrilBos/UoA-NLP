import numpy as np

import lda

from gensim import matutils
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import HashingVectorizer, TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer

from NLP.LatentDirichletAllocation import LatentDirichletAllocation
from ML.ClassifierData import ClassifierData



class KMeansClusterizer:
    """
    This class uses KMeans to compute clusters of text documents and extract their features either using
    - TF-IDF vector representation
    - LDA topics representation
    """

    def __init__(self, data, target, target_names, n_features=100, n_components=0,
                 verbose=True):
        """
        Initializes the new KMeansClusterizer instance with the given data and parameters.

        :param data: the text documents
        :type data: Union[list, tuple]
        :param target: holds the target_names index of each document
        (target[0]=0 means the first data comes from the first target)
        :type target: Union[list, tuple]
        :param target_names: is an array ro tuple that holds the labels names (i.e the forums names)
        :type target_names: Union[list, tuple]
        :param n_features: number of features to compute for each cluster
        :type n_features: int
        :param verbose: set to True to print details on the KMeans clusterization
        :type verbose: bool
        """
        self.__dataset = ClassifierData(data, target, target_names)
        print("%d documents" % len(self.__dataset.data))
        print("%d categories" % len(self.__dataset.target_names))

        self.__labels = self.__dataset.target
        self.__true_k = np.unique(self.__dataset.target).shape[0]

        self.__n_features = n_features
        self.__n_components = n_components

        self.__verbose = verbose

    def lda_clusterize(self, n_clusters, n_iter):
        """
        Computes the LDA representation of the data then clusters them with the given parameters.
        :param n_clusters: Number of wanted clusters
        :type n_clusters: int
        :param n_iter: Number of iterations of the clusterization
        :type n_iter: int
        :return: a tuple (clusters, lda model, lda vocabulary)
        :rtype: tuple
        """
        model = lda.LDA(n_topics=self.__n_features, n_iter=n_iter, random_state=1)
        my_lda = LatentDirichletAllocation(self.__dataset.data)
        corpus, vocab = my_lda.get_corpus_and_dictionary()

        document_term_matrix = matutils.corpus2dense(corpus, len(vocab), len(corpus)).astype(int)

        model.fit(document_term_matrix)
        lda_rep = model.doc_topic_

        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        kmeans.fit(lda_rep)
        return kmeans, lda_rep, vocab

    def idf_clusterize(self, n_clusters=-1):
        """
        Computes TF-IDF vectors of the documents and clusters them using KMeans.
        :param n_clusters: number of wanted clusters
        :return: tuple (clusters, feature list)
        """
        if n_clusters != -1:
            self.__true_k = n_clusters
        print("Extracting features from the training dataset using a sparse vectorizer")

        vectorizer = TfidfVectorizer(max_df=0.5, max_features=self.__n_features,
                                         min_df=2, stop_words='english')
        X = vectorizer.fit_transform(self.__dataset.data)

        print("n_samples: %d, n_features: %d" % X.shape)
        print()

        if self.__n_components:
            print("Performing dimensionality reduction using LSA")
            # Vectorizer results are normalized, which makes KMeans behave as
            # spherical k-means for better results. Since LSA/SVD results are
            # not normalized, we have to redo the normalization.
            svd = TruncatedSVD(self.__n_components)
            normalizer = Normalizer(copy=False)
            lsa = make_pipeline(svd, normalizer)

            X = lsa.fit_transform(X)

            explained_variance = svd.explained_variance_ratio_.sum()
            print("Explained variance of the SVD step: {}%".format(
                int(explained_variance * 100)))

            print()

        km = KMeans(n_clusters=self.__true_k, init='k-means++', max_iter=100, n_init=10,
                    verbose=self.__verbose, n_jobs=-1)

        print("Clustering sparse data with %s" % km)

        km.fit(X)

        print("Top terms per cluster:")

        if self.__n_components:
            original_space_centroids = svd.inverse_transform(km.cluster_centers_)
            order_centroids = original_space_centroids.argsort()[:, ::-1]
        else:
            order_centroids = km.cluster_centers_.argsort()[:, ::-1]

            terms = vectorizer.get_feature_names()
            for i in range(self.__true_k):
                print("Cluster %d:" % i, end='')
                for ind in order_centroids[i, :10]:
                    print(' %s' % terms[ind], end='')
                print()

        return km, X

    def get_metrics(self, km, X):
        """
        Computes and returns the metrics using km and X as ground truth
        :param km: Ground truth KMeans clusters
        :param X: Ground truth feature list
        :return:
        """
        return  metrics.homogeneity_score(self.__labels, km.labels_), \
                metrics.completeness_score(self.__labels, km.labels_), \
                metrics.v_measure_score(self.__labels, km.labels_), \
                metrics.adjusted_rand_score(self.__labels, km.labels_), \
                metrics.silhouette_score(X, km.labels_, sample_size=1000)



    def print_metrics(self, km, X):
        """
        Print the metrics using km and X as ground truth
        :param km: Ground truth KMeans clusters
        :param X: Ground truth feature list
        :return:
        """
        print("Homogeneity: %0.3f" % metrics.homogeneity_score(self.__labels, km.labels_))
        print("Completeness: %0.3f" % metrics.completeness_score(self.__labels, km.labels_))
        print("V-measure: %0.3f" % metrics.v_measure_score(self.__labels, km.labels_))
        print("Adjusted Rand-Index: %.3f"
              % metrics.adjusted_rand_score(self.__labels, km.labels_))
        print("Silhouette Coefficient: %0.3f"
              % metrics.silhouette_score(X, km.labels_, sample_size=1000))
