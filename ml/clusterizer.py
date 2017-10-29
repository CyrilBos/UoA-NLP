from sklearn.feature_extraction.text import TfidfVectorizer
import csv, time
from nlp.input_preprocessor import InputPreprocessor
from ml.silhouette_validator import SilhouetteValidator

class Clusterizer:
    def __init__(self, data, n_features=10, preprocess=False, jobs=1, verbose=True):
        self._clusters = None
        self._labels = []
        self._data = data
        self._verbose = verbose

        self._n_features = n_features
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
        self._preprocessed_data = vectorizer.fit_transform(self._data)
        self._jobs = jobs

    @classmethod
    def get_clusters_from_labels(self, items, labels):
        clusters = {}
        for i in range(len(labels)):
            if labels[i] not in clusters:
                clusters[labels[i]] = []
            clusters[labels[i]].append(items[i])
        self._clusters = clusters
        return clusters

    def get_clusters(self):
        if self._clusters:
            return self._clusters
        else:
            return self.get_clusters_from_labels(self._data, self._labels)

    def print_clusters(self, minimum_length=2, maximum_length=20, filename=None):
        if filename:
            file = open(filename, 'w')
        clusters = self.get_clusters()
        n = 0
        for cluster_id in clusters:
            if maximum_length >= len(clusters[cluster_id]) >= minimum_length:
                print('##### CLUSTER {} #####'.format(n))
                if filename:
                    file.write('##### CLUSTER {} #####\n'.format(n))
                for item in clusters[cluster_id]:
                    print(item)
                    if filename:
                        file.write(item + '\n')
            n += 1

    def print_to_csv(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = 'clusters-' + timestr + '.csv'
        clusters = self.get_clusters()

        with open(filename, 'w', newline="") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in clusters.items():
                writer.writerow([key, value])

    def get_avg_silhouette(self):
        validator = SilhouetteValidator(len(self._labels), self._preprocessed_data, self._labels)
        validator.compute()

