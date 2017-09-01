import sys, os, configparser
import Utils.GenerateConfig as ConfigGen
import numpy as np
from nltk.tokenize import sent_tokenize

from Database.DatabaseHelper import DatabaseHelper
from Database.Configuration import connection_string
from ML.AffinityPropagationClusterizer import AffinityPropagationClusterizer
from ML.DBSCANClusterizer import DBSCANClusterizer
from ML.DecisionTreeClassifier import C45DecisionTreeClassifier
from ML.HierarchicalClusterizer import HierarchicalClusterizer
from ML.SGDClassifier import SGDClassifier
from ML.KMeansClusterizer import KMeansClusterizer

configfile_name = "config.ini"
# Check if there is already a configurtion file
if not os.path.isfile(configfile_name):
    ConfigGen.GenerateConfig(configfile_name);

config = configparser.ConfigParser()
config.read(configfile_name)

try:
    printToFile = int(config['printing']['print_to_file'])
    printToCSV = int(config['printing']['print_to_csv'])

    preprocess = int(config['other']['preprocess'])
    n_features = int(config['other']['n_features'])
    jobs = int(config['other']['jobs'])
    verbose = int(config['other']['verbose'])
    ignored_categories = (config['other']['ignored_categories'])

    if (config['data']['data_source'] == "xero"):
        dbmg = DatabaseHelper(connection_string)
        questions = dbmg.get_questions_content()
        data, target, target_names = dbmg.get_training_data(config['data']['training_data'])
    else:
        print("invalid Data source")
        exit()
except:
    os.remove(configfile_name)
    ConfigGen.GenerateConfig(configfile_name)
    print("Config corrupted. File has been reset, please try again")
    exit()

algo_opt = sys.argv[1]

###################################

forum_question_classifier = C45DecisionTreeClassifier(data, target, target_names, preprocess=preprocess) #SGDClassifier(data, target, target_names)
forum_question_classifier.train()
print('Precision of the classifier on its training data set: ', forum_question_classifier.evaluate_precision(1))

n_splits = 20
print("{}-Fold precision evaluation on the training data set: \n".format(n_splits), forum_question_classifier.evaluate_precision(n_splits))

### predict the category of every question, appending it into the corresponding list of the dictionary ###

predicted_categories = {}
cluster_data = {}
cluster_target = {}
for category_name in target_names:
    predicted_categories[category_name] = []
    cluster_data[category_name] = []
    cluster_target[category_name] = []


for question in questions:
    question = question.replace('.', '. ').replace('.  ', '. ').replace('?', '? ').replace('?  ', '? ').replace('!', '! ').replace('!  ', '! ')
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

#question_recommender = Recommender()

def kmeans(data, target, target_names):
    n_clusters = int(len(data) / 3)
    clusterizer = KMeansClusterizer(data, target, target_names, n_features=n_features, preprocess=preprocess, jobs=jobs, verbose=verbose)
    clusterizer.lda_clusterize(n_clusters=n_clusters, n_features=20, max_iter=1)
    if (printToFile):
        clusterizer.print_to_file('kmeans_{}_{}.txt'.format(category, n_clusters), cluster_data[category],
                              n_clusters)
    #get_avg_sihouette()
    return clusterizer


def dbscan(data, category):
    clusterizer = DBSCANClusterizer(data, n_features=n_features, preprocess=preprocess, jobs=jobs, verbose=verbose)
    db = clusterizer.compute(eps=0.5, min_samples=5)
    
    if (printToFile):
        clusterizer.print_clusters('dbscan_{}_{}'.format(category, len(clusterizer.get_clusters())))

    return clusterizer


def affinity(data, target, target_names):
    clusterizer = AffinityPropagationClusterizer(data)
    clusterizer.compute(n_features=10, max_iter=1)
    return clusterizer

def hierarchical(data, linkage):
    n_clusters = int(len(data) / 30)
    clusterizer = HierarchicalClusterizer(data, n_clusters, linkage=linkage)
    hl = clusterizer.compute()
    labels = hl.labels_
    print("Nuber of data points: ", labels.size)
    print("Number of clusters: ", np.unique(labels).size)
    
    if (printToFile):
        clusterizer.print_clusters('hierarchical_{}_{}_{}'.format(linkage, category, n_clusters))


    return clusterizer

for category in predicted_categories:
    if len(predicted_categories[category]) > 0 and category not in ignored_categories:
        #cluster_target_names.append(category)
        for sentence in predicted_categories[category]:
            cluster_data[category].append(sentence)
            cluster_target[category].append(category)

        if algo_opt == 'kmeans':
            clusterizer = kmeans(cluster_data[category], cluster_target[category], [category])
        elif algo_opt == 'dbscan':
            clusterizer = dbscan(predicted_categories[category], category)
        elif algo_opt == 'hierarchical':
            clusterizer = hierarchical(cluster_data[category], 'ward')
        elif algo_opt == 'affinity':
            clusterizer = affinity(cluster_data[category], cluster_target[category], [category])
        else:
            print('Unrecognized algorithm argument. Please provide one of these as first argument of this script: kmeans, dbscan, hierarchical, affinity')
            exit()

        if (printToCSV):
            clusterizer.print_to_csv();

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
