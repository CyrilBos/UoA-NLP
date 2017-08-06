from sklearn.cluster import DBSCAN
from sklearn.feature_extraction.text import TfidfVectorizer

from NLP.InputPreprocessor import InputPreprocessor


class DBSCANClusterizer:
    def __init__(self, data, n_features=10, preprocess=False, jobs=1):
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
        self.__data = vectorizer.fit_transform(data)
        self.__jobs = jobs

    def compute(self, eps=0.3, min_samples=10):
        return DBSCAN(eps=0.3, min_samples=min_samples, n_jobs=self.__jobs, algorithm='ball_tree').fit(self.__data)
