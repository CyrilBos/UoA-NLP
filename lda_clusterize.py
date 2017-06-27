from Database.Configuration import connection_string
from Database.DatabaseHelper import DatabaseHelper
from ML.KMeansClusterizer import KMeansClusterizer

db = DatabaseHelper(connection_string)

data, target, target_names = db.get_questions_titles_by_forum()

clusterizer = KMeansClusterizer(data, target, target_names)

n_clusters = 10

km, lda, vocab = clusterizer.lda_clusterize(n_clusters, 250)

i=0

clusters = [[] for dummy in range(n_clusters)]

for cluster_number in km.labels_:
    clusters[cluster_number].append(vocab[i])
    i+=1

for cluster in clusters:
    print(cluster)

#clusterizer.print_metrics(clusters, lda)