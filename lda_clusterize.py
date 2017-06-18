from Database.DatabaseHelper import DatabaseHelper
from ML.Clusterizer import Clusterizer

connect_string = "dbname=uoa-nlp user=admin"
db = DatabaseHelper(connect_string)

data, target, target_names = db.get_questions_by_forum()

clusterizer = Clusterizer(data, target, target_names)

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