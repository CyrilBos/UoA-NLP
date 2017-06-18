from Database.DatabaseHelper import DatabaseHelper
from ML.Clusterizer import Clusterizer

connect_string = "dbname=uoa-nlp user=admin"
db = DatabaseHelper(connect_string)

data, target, target_names = db.get_questions_by_forum()

clusterizer = Clusterizer(data, target, target_names, use_idf=True)

n_clusters = 2000
km, x = clusterizer.idf_clusterize(n_clusters=n_clusters)#n_clusters

clusters = [[] for dummy in range(n_clusters)]
i=0
for cluster_num in km.labels_:
    clusters[cluster_num].append(data[i])
    i+=1

n=0
for cluster in clusters:
    if len(cluster) > 1:
        print('CLUSTER {}'.format(n))
        for doc in cluster:
            print(doc)
    n+=1

clusterizer.print_metrics(km, x)