from sklearn.feature_extraction.text import TfidfVectorizer

from NLP.InputPreprocessor import InputPreprocessor


class Clusterizer:
    def __init__(self, data, n_features=10, preprocess=False, jobs=1, verbose=True):
        self.__labels = []
        self.__data = data
        self.__verbose = verbose
        if preprocess:
            analyzer = TfidfVectorizer.build_analyzer()
            ipp = InputPreprocessor(None)
            def preprocess(doc):
                return [ipp.normalise(word) for word in analyzer(doc)]

            vectorizer = TfidfVectorizer(max_df=0.5, max_features=n_features,
                                         min_df=2, stop_words='english',
                                         use_idf=True, analyzer=preprocess)

        else:
            vectorizer = TfidfVectorizer(max_df=0.5, max_features=n_features,
                                     min_df=2, stop_words='english',
                                     use_idf=True)
        self.__preprocessed_data = vectorizer.fit_transform(data)
        self.__jobs = jobs

    @classmethod
    def get_clusters_from_labels(self, items, labels):
        clusters = [[] for dummy in range(len(labels))]
        for i in range(len(labels)):
            clusters[labels[i]] = items[i]
        return clusters

    def get_clusters(self):
        return self.get_clusters_from_labels(self.__data, self.__labels)

    def print_clusters(self, filename=None):
        if filename:
            file = open(filename, 'w')

        for cluster in self.get_clusters():
            for item in cluster:
                print(item)
                if filename:
                    file.write(item + '\n')

