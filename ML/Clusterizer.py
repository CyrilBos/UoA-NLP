import lda

import numpy as np
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



class Clusterizer:
    """
    This class uses KMeans to compute clusters of text documents and extract their features either using
    - IDF with an hashing option
    - an LDA topics representation of the set of documents
    """

    def __init__(self, data, target, target_names, n_features=100, n_components=0, use_hashing=False, use_idf=True,
                 verbose=True):
        """
        init function for the clusterizer

        :param data: the text documents
        :type data: Union[list, tuple]
        :param target: is an array or tuple that holds the index of each document to the labels
        (target[0]=0 means the first data comes from the first target)
        :type target: Union[list, tuple]
        :param target_names: is an array ro tuple that holds the labels names (i.e the forums names)
        :type target_names: Union[list, tuple]
        """
        self.__dataset = ClassifierData(data, target, target_names)
        print("%d documents" % len(self.__dataset.data))
        print("%d categories" % len(self.__dataset.target_names))

        self.__labels = self.__dataset.target
        self.__true_k = np.unique(self.__dataset.target).shape[0]

        self.__n_features = n_features
        self.__n_components = n_components
        self.__use_hashing = use_hashing
        self.__use_idf = use_idf
        self.__verbose = verbose

    def lda_clusterize(self, n_clusters, n_iter):
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
        if n_clusters != -1:
            self.__true_k = n_clusters
        print("Extracting features from the training dataset using a sparse vectorizer")
        if self.__use_hashing:
            if self.__use_idf:
                # Perform an IDF normalization on the output of HashingVectorizer
                hasher = HashingVectorizer(n_features=self.__n_features,
                                           stop_words='english', non_negative=True,
                                           norm=None, binary=False)
                vectorizer = make_pipeline(hasher, TfidfTransformer())
            else:
                vectorizer = HashingVectorizer(n_features=self.__n_features,
                                               stop_words='english',
                                               non_negative=False, norm='l2',
                                               binary=False)
        else:
            vectorizer = TfidfVectorizer(max_df=0.5, max_features=self.__n_features,
                                         min_df=2, stop_words='english',
                                         use_idf=self.__use_idf)
        X = vectorizer.fit_transform(self.__dataset.data)

        # ("done in %fs" % (time() - t0))
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
                    verbose=self.__verbose, n_jobs=8)

        print("Clustering sparse data with %s" % km)
        km.fit(X)

        if not self.__use_hashing:
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
        return  metrics.homogeneity_score(self.__labels, km.labels_), \
                metrics.completeness_score(self.__labels, km.labels_), \
                metrics.v_measure_score(self.__labels, km.labels_), \
                metrics.adjusted_rand_score(self.__labels, km.labels_), \
                metrics.silhouette_score(X, km.labels_, sample_size=1000)



    def print_metrics(self, km, X):
        print("Homogeneity: %0.3f" % metrics.homogeneity_score(self.__labels, km.labels_))
        print("Completeness: %0.3f" % metrics.completeness_score(self.__labels, km.labels_))
        print("V-measure: %0.3f" % metrics.v_measure_score(self.__labels, km.labels_))
        print("Adjusted Rand-Index: %.3f"
              % metrics.adjusted_rand_score(self.__labels, km.labels_))
        print("Silhouette Coefficient: %0.3f"
              % metrics.silhouette_score(X, km.labels_, sample_size=1000))
