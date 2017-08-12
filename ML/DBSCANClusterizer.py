from sklearn.cluster import DBSCAN
from sklearn.feature_extraction.text import TfidfVectorizer


class DBSCANClusterizer:
    def __init__(self, data, n_features=10, jobs=1):
        self.__data = data
        self.__features = n_features
        self.__jobs = jobs

    def compute(self, eps=0.3, min_samples=10):       
        tf_idf_vectorizer = TfidfVectorizer(max_df=0.5, max_features=self.__features,
                                     min_df=2, stop_words='english',
                                     use_idf=True)

        X = (tf_idf_vectorizer.fit_transform(self.__data)).toarray()

        self.__db = DBSCAN(eps=0.3, min_samples=min_samples, n_jobs=self.__jobs, algorithm='ball_tree').fit(X)
    	
        return self.__db

    def printClusters(self, min_len = 2):
        labels = (self.__db).labels_
       
        clusters = {}
        n = 0
        for item in labels:		# put clusters in a dict
            if item in clusters:
                clusters[item].append(self.__data[n])
            else:
                clusters[item] = [self.__data[n]]
            n += 1

        for item in clusters:         # print off every cluster larger than parameter provided
            c_len = len(clusters[item])
            if(c_len >= min_len):
                print("Cluster ", item)
                for i in range(0,c_len):
                    print("   ", clusters[item][i])
                    if (i > 10):
                        break;
