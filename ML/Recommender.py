import pandas as pd
import redis
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class Recommender:
    SIMKEY = 'p:smlr:%s'

    def __init__(self):
        self.__r = redis.Redis(unix_socket_path='/tmp/redis.sock')

    def train(self, ds):
        ds = pd.DataFrame(ds)
        tf = TfidfVectorizer(analyzer='word',
                                     ngram_range=(1, 3),
                                     min_df=0,
                                     stop_words='english')
        tfidf_matrix = tf.fit_transform(ds['description'])

        cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

        for idx, row in ds.iterrows():
            similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
            similar_items = [(cosine_similarities[idx][i], ds['id'][i])
                                     for i in similar_indices]

            # First item is the item itself, so remove it.
            # This 'sum' is turns a list of tuples into a single tuple:
                    # [(1,2), (3,4)] -> (1,2,3,4)
            flattened = sum(similar_items[1:], ())
            self.__r.zadd(Recommender.SIMKEY % row['id'], *flattened)


    def predict(self, item_id, num):
        """
        Couldn't be simpler! Just retrieves the similar items and
        their 'score' from redis.

        :param item_id: string
        :param num: number of similar items to return
        :return: A list of lists like: [["19", 0.2203],
        ["494", 0.1693], ...]. The first item in each sub-list is
        the item ID and the second is the similarity score. Sorted
        by similarity score, descending.
        """

        return self.__r.zrange(Recommender.SIMKEY % item_id,
                              0,
                              num - 1,
                              withscores=True,
                              desc=True)

recommender = Recommender()