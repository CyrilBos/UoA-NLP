from Database.DatabaseHelper import DatabaseHelper
from ML.Classifier import Classifier

from nltk.tokenize import sent_tokenize

from ML.Clusterizer import Clusterizer

connect_string = "dbname=uoa-nlp user=admin"
dbmg = DatabaseHelper(connect_string)
questions_sentences = dbmg.my_query(
    "select * from training_data join training_data_categories on training_data_categories.training_data_categories_id = training_data.training_data_categories_id", None,
    fetch_to_dict=True)

categories = dbmg.my_query('select * from training_data_categories order by training_data_categories_id', None, fetch_to_dict=True)

questions = dbmg.get_questions_content()

dbmg.close()

data = []
target = []
target_names = []

for category in categories:
    target_names.append(category['category_name'])

for question_sentence in questions_sentences:
    data.append(question_sentence['content'])
    target.append(question_sentence['training_data_categories_id'])

forum_question_classifier = Classifier(data, target, target_names)

print('Precision of the classifier on its training data set: ', forum_question_classifier.evaluate_precision())

predicted_categories = {'context':[], 'problem':[], 'code':[], 'question':[], 'outroduction':[]}

for question in questions:
    for sentence in sent_tokenize(question):
        predicted_category_i = forum_question_classifier.predict([sentence])[0]
        predicted_categories[forum_question_classifier.target_names[predicted_category_i]].append(sentence)

for category in predicted_categories:
    print('####Category: ' + category)
    for i in range(10):
        print(predicted_categories[category][i])


cluster_data = []
cluster_target = []
cluster_target_names = []
category_i = 0

for category in predicted_categories:
    cluster_target_names.append(category)
    for sentence in predicted_categories[category]:
        cluster_data.append(sentence)
        cluster_target.append(category_i)
    category_i += 1


clusterizer = Clusterizer(cluster_data, cluster_target, cluster_target_names, n_features=10)

n_clusters = 4000

km, X = clusterizer.idf_clusterize(n_clusters=n_clusters)

clusters = [[] for dummy in range(n_clusters)]
i=0
for cluster_num in km.labels_:
    clusters[cluster_num].append(cluster_data[i])
    i+=1

n=0

save_file = open('broken_idf_clusters_{}.txt'.format(n_clusters), 'w')

for cluster in clusters:
    if len(cluster) > 1:
        print('CLUSTER {}'.format(n))
        save_file.write('CLUSTER {}\n'.format(n))
        for doc in cluster:
            print(doc)
            save_file.write(doc + '\n')
    n+=1

#clusterizer.print_metrics(km, X)