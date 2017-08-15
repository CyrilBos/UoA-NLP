import numpy as np


from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer

from ML.Clusterizer import Clusterizer
from ML.SilhouetteValidator import SilhouetteValidator
from NLP.LatentDirichletAllocation import LatentDirichletAllocation


class KMeansClusterizer(Clusterizer):
    """
    This class uses KMeans to compute clusters of text documents and extract their features either using
    - TF-IDF vector representation
    - LDA topics representation
    """

    def __init__(self, data, target, target_names, n_features, preprocess=False, jobs=1, verbose=True):
        """
        Initializes the new KMeansClusterizer instance with the given data and parameters.

        :param data: the text documents
        :type data: Union[list, tuple]
        :param target: holds the target_names index of each document
        (target[0]=0 means the first data comes from the first target)
        :type target: Union[list, tuple]
        :param target_names: is an array ro tuple that holds the labels names (i.e the forums names)
        :type target_names: Union[list, tuple]
        :param jobs: number of parallel threads used to compute. Should be number of CPU cores - 1
        :type jobs: int
        :param verbose: set to True to print details on the KMeans clusterization
        :type verbose: bool
        """

        super().__init__(data, n_features=n_features, preprocess=preprocess, jobs=jobs, verbose=verbose)

        self.__target = target
        self.__target_names = target_names

        self.__labels = self.__target
        self.__true_k = np.unique(self.__target).shape[0]

        self.__jobs = jobs
        self.__verbose = verbose

    def idf_clusterize(self, n_components=None, n_clusters=-1, max_iter=5):
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
        if n_clusters != -1:
            self.__true_k = n_clusters

        if n_components:
            # Vectorizer results are normalized, which makes KMeans behave as
            # spherical k-means for better results. Since LSA/SVD results are
            # not normalized, we have to redo the normalization.
            svd = TruncatedSVD(n_components)
            normalizer = Normalizer(copy=False)
            lsa = make_pipeline(svd, normalizer)

            self.__preprocessed_data = lsa.fit_transform(self.__preprocessed_data)

            explained_variance = svd.explained_variance_ratio_.sum()
            print("Explained variance of the SVD step: {}%".format(
                int(explained_variance * 100)))

            print()

        km = KMeans(n_clusters=self.__true_k, init='k-means++', max_iter=max_iter, n_init=10,
                    verbose=self.__verbose, n_jobs=self.__jobs)

        print("Clustering sparse data with %s" % km)

        km.fit(self.__preprocessed_data)

        self.__labels = km.labels_

        return km

    def lda_clusterize(self, n_features=20, n_clusters=-1, lda_iter=5, max_iter=5):
        """
        Computes TF-IDF vectors of the documents and clusters them using KMeans.
        :param n_clusters: number of wanted clusters
        :return: tuple (clusters, feature list)
        """
        if n_clusters != -1:
            self.__true_k = n_clusters
        print("Extracting features from the training dataset using a sparse vectorizer")

        lda = LatentDirichletAllocation(self.__preprocessed_data, self.__jobs)
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

        km = KMeans(n_clusters=self.__true_k, init='k-means++', max_iter=max_iter, n_init=1,
                    verbose=self.__verbose, n_jobs=self.__jobs)

        print("Clustering sparse data with %s" % km)

        self.__processed_data = km.fit(X)

        self.__X = X

        return km, self.__processed_data

    def print_to_file(self, filename, cluster_category_data, n_clusters):
        clusters = [[] for dummy in range(n_clusters)]

        i = 0
        for cluster_num in self.__labels:
            clusters[cluster_num].append(cluster_category_data[i])
            i += 1

        n = 0

        save_file = open(filename, 'w')

        for cluster in clusters:
            if len(cluster) > 1:
                # print('CLUSTER {}'.format(n))
                save_file.write('CLUSTER {}\n'.format(n))
                for doc in cluster:
                    # print(doc)
                    save_file.write(doc + '\n')
            n += 1

    def get_metrics(self, km, X):
        """
        Computes and returns the metrics using km and X as ground truth
        :param km: Ground truth KMeans clusters
        :param X: Ground truth feature list
        :return:
        """
        return metrics.homogeneity_score(self.__labels, km.labels_), \
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

    def silhouette_validate(self):
        validator = SilhouetteValidate()
        validator.compute(self.__X, self.__true_k, self.__labels)
