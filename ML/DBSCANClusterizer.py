from sklearn.cluster import DBSCAN
from sklearn.feature_extraction.text import TfidfVectorizer


class DBSCANClusterizer:
    def __init__(self, data, n_features=10):
        vectorizer = TfidfVectorizer(max_df=0.5, max_features=n_features,
                        min_df=2, stop_words='english',
                        use_idf=True)
        self.__data = vectorizer.fit_transform(data)

    def compute(self):
        return DBSCAN(eps=0.3, min_samples=10).fit(self.__data)
