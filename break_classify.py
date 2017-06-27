import random

from nltk.tokenize import sent_tokenize

from Database.DatabaseHelper import DatabaseHelper
from Database.Configuration import connection_string

from ML.Classifier import Classifier
from ML.KMeansClusterizer import KMeansClusterizer
from ML.Recommender import Recommender


dbmg = DatabaseHelper(connection_string)
#retrieves the training data set
questions_sentences = dbmg.my_query(
    "select * from training_data join training_data_categories on training_data_categories.training_data_categories_id = training_data.training_data_categories_id", None,
    fetch_to_dict=True)

#retrieves the training data set categories
categories = dbmg.my_query('select * from training_data_categories order by training_data_categories_id', None, fetch_to_dict=True)

questions = dbmg.get_questions_content()

dbmg.close()


### Prepare the Classifier data ###
data = []
target = []
target_names = []

for category in categories:
    target_names.append(category['category_name'])

for question_sentence in questions_sentences:
    data.append(question_sentence['content'])
    target.append(question_sentence['training_data_categories_id'])

###################################

forum_question_classifier = Classifier(data, target, target_names)

print('Precision of the classifier on its training data set: ', forum_question_classifier.evaluate_precision())

### predict the category of every question, appending it into the corresponding list of the dictionary ###

predicted_categories = {'context':[], 'problem':[], 'code':[], 'question':[], 'outroduction':[]}

for question in questions:
    for sentence in sent_tokenize(question):
        predicted_category_i = forum_question_classifier.predict([sentence])[0]
        predicted_categories[forum_question_classifier.target_names[predicted_category_i]].append(sentence)

for category in predicted_categories:
    print('####Category: ' + category)
    for i in range(10):
        print(predicted_categories[category][i])

##########################################################################################################


### Compute and print clusters ###
cluster_data = {'context':[], 'problem':[], 'code':[], 'question':[], 'outroduction':[]}
cluster_target = {'context':[], 'problem':[], 'code':[], 'question':[], 'outroduction':[]}
cluster_target_names = []
category_i = 0

question_recommender = Recommender()

for category in predicted_categories:
    #cluster_target_names.append(category)
    for sentence in predicted_categories[category]:
        cluster_data[category].append(sentence)
        cluster_target[category].append(category_i)
    n_clusters = int(len(cluster_data[category]) / 3)
    clusterizer = KMeansClusterizer(cluster_data[category], cluster_target[category], [category], n_features=10)

    km, X = clusterizer.idf_clusterize(n_clusters=n_clusters)

    clusters = [[] for dummy in range(n_clusters)]
    i = 0
    for cluster_num in km.labels_:
        clusters[cluster_num].append(cluster_data[category][i])
        i += 1

    n = 0

    save_file = open('broken_idf_clusters_{}_{}.txt'.format(category, n_clusters), 'w')

    for cluster in clusters:
        if len(cluster) > 1:
            print('CLUSTER {}'.format(n))
            save_file.write('CLUSTER {}\n'.format(n))
            for doc in cluster:
                print(doc)
                save_file.write(doc + '\n')
        n += 1

    recommend_data = {'id':[], 'description':[]}

    for i in range(len(cluster_data[category])):
        recommend_data['id'].append(i)
        recommend_data['description'].append(cluster_data[category][i])

    question_recommender.train(recommend_data)

    rnd = random.randint(0, 20)
    for item_to_recommend_index in range(rnd, rnd + rnd):
        print("Current item: ", recommend_data['description'][item_to_recommend_index])
        recommended_items = question_recommender.predict(recommend_data['id'][item_to_recommend_index], 5)
        print("Recommended items: ")
        for recommended_item in recommended_items:
            print(recommend_data['description'][recommend_data['id'].index(int(recommended_item[1]))])

    category_i += 1

#clusterizer.print_metrics(km, X)