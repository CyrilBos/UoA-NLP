from sklearn.feature_extraction.text import TfidfVectorizer
import csv, time
from NLP.InputPreprocessor import InputPreprocessor
from ML.SilhouetteValidator import SilhouetteValidator

class Clusterizer:
    def __init__(self, data, n_features=10, preprocess=False, jobs=1, verbose=True):
        print("Running Clusterizer")
        self._clusters = None
        self._labels = []
        self._data = data
        self._verbose = verbose
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
        #clusters = [[] for dummy in range(len(labels))]
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

    def print_clusters(self, filename=None):
        if filename:
            file = open(filename, 'w')
        clusters = self.get_clusters()
        n = 0
        for cluster in clusters:
            print('##### CLUSTER {} #####'.format(n))
            if filename:
                file.write('##### CLUSTER {} #####\n'.format(n))
            for item in clusters[cluster]: 
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

    def get_avg_sihouette(self):
        validator = SilhouetteValidator(len(self._labels), self._preprocessed_data, self._labels)
        validator.compute()

