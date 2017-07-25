import random

import numpy as np
from nltk.tokenize import sent_tokenize

from Database.DatabaseHelper import DatabaseHelper
from Database.Configuration import connection_string
from ML.DBSCANClusterizer import DBSCANClusterizer
from ML.DecisionTreeClassifier import C45DecisionTreeClassifier

from ML.SGDClassifier import SGDClassifier
from ML.KMeansClusterizer import KMeansClusterizer
from ML.Recommender import Recommender


dbmg = DatabaseHelper(connection_string)
questions = dbmg.get_questions_content()
data, target, target_names = dbmg.get_training_data('Business')

###################################

forum_question_classifier = C45DecisionTreeClassifier(data, target, target_names) #SGDClassifier(data, target, target_names)

print('Precision of the classifier on its training data set: ', forum_question_classifier.evaluate_precision())

### predict the category of every question, appending it into the corresponding list of the dictionary ###

predicted_categories = {}
cluster_data = {}
cluster_target = {}
for category_name in target_names:
    predicted_categories[category_name] = []
    cluster_data[category_name] = []
    cluster_target[category_name] = []


for question in questions:
    for sentence in sent_tokenize(question):
        predicted_category_i = forum_question_classifier.predict([sentence])[0]
        predicted_categories[forum_question_classifier.target_names[predicted_category_i]].append(sentence)

for category in predicted_categories:
    print('####Category: ' + category)
    nb = 10 if len(predicted_categories[category]) >= 10 else len(predicted_categories[category])
    for i in range(nb):
        print(predicted_categories[category][i])

##########################################################################################################


### Compute and print clusters ###
cluster_target_names = []
category_i = 0

#question_recommender = Recommender()

for category in predicted_categories:
    if len(predicted_categories[category]) > 0:
        #cluster_target_names.append(category)
        for sentence in predicted_categories[category]:
            cluster_data[category].append(sentence)
            cluster_target[category].append(category_i)
        #Split the set of documents into clusters of ~3 documents
        n_clusters = int(len(cluster_data[category]) / 3)

        clusterizer = KMeansClusterizer(cluster_data[category], cluster_target[category], [category])
        #clusterizer = DBSCANClusterizer(cluster_data[category])
        km, X = clusterizer.lda_clusterize(n_clusters=n_clusters, n_features=20, max_iter=1)
        clusterizer.print_to_file('broken_idf_clusters_{}_{}.txt'.format(category, n_clusters), cluster_data[category], n_clusters, km)
        #db = clusterizer.compute()

        #core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        #core_samples_mask[db.core_sample_indices_] = True
        #labels = db.labels_

        ## Number of clusters in labels, ignoring noise if present.
        #n_clusters = len(set(labels)) - (1 if -1 in labels else 0)

        #clusters = [cluster_data[category][labels == i] for i in range(n_clusters)]

        """#Seems too heavy to run
        #"Clustering" the documents using a recommender
        recommend_data = {'id':[], 'description':[]}

        for i in range(len(cluster_data[category])):
            recommend_data['id'].append(i)

            recommend_data['description'].append(cluster_data[category][i])

        question_recommender.train(recommend_data)

        save_file = open('broken_idf_recommendations_{}.txt'.format(category), 'w')
        rnd = random.randint(0, 20)
        for item_to_recommend_index in range(rnd, rnd + rnd):
            print("Current item: ", recommend_data['description'][item_to_recommend_index])
            save_file.write("Current item: " + recommend_data['description'][item_to_recommend_index])
            recommended_items = question_recommender.predict(recommend_data['id'][item_to_recommend_index], 5)
            print("Recommended items: ")
            for recommended_item in recommended_items:
                print(recommend_data['description'][recommend_data['id'].index(int(recommended_item[1]))])
                save_file.write(recommend_data['description'][recommend_data['id'].index(int(recommended_item[1]))])

        category_i += 1
        """