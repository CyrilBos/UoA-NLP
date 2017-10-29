from database.database_helper import DatabaseHelper
from database.configuration import connection_string

from ml.kmeans_clusterizer import KMeansClusterizer

import collections

n_clusters = 300

db = DatabaseHelper(connection_string)

data, target, target_names = db.get_questions_titles_by_forum(community_name='Business')

###Clusterization
clusterizer = KMeansClusterizer(data, n_features=100, jobs=3)

km = clusterizer.lsa_clusterize(n_clusters=n_clusters, n_components=20, max_iter=2)

clusterizer.print_clusters()

sizes = {}
clusters = clusterizer.get_clusters()

for cluster in clusters.items():
    cluster_length = len(cluster[1])
    if cluster_length in sizes:
        sizes[cluster_length] += 1
    else:
        sizes[cluster_length] = 1

sizes = collections.OrderedDict(sorted(sizes.items()))

for cluster_size, cluster_length in sizes.items():
    print('number of clusters of size {}: {} percentage of clusters: {}'.format(cluster_size, cluster_length,
                                                                                cluster_length / n_clusters * 100))
