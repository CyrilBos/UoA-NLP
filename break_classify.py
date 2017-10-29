import sys, os, configparser
import Utils.generate_config as ConfigGen
import numpy as np
from nltk.tokenize import sent_tokenize

from database.database_helper import DatabaseHelper
from database.configuration import connection_string
from ml.affinity_propagation_clusterizer import AffinityPropagationClusterizer
from ml.dbscan_clusterizer import DBSCANClusterizer
from ml.decision_tree_classifier import C45DecisionTreeClassifier
from ml.hierarchical_clusterizer import HierarchicalClusterizer
from ml.sgd_classifier import SGDClassifier
from ml.kmeans_clusterizer import KMeansClusterizer


def print_usage():
    print(
        'Unrecognized algorithm argument. Please provide one of these as first argument of this script: kmeans, dbscan, hierarchical, affinity')


configfile_name = "config.ini"
# Check if there is already a configurtion file
if not os.path.isfile(configfile_name):
    ConfigGen.GenerateConfig(configfile_name)

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
        classifier_training_data, target, target_names = dbmg.get_training_data(config['data']['training_data'])
    else:
        print("invalid Data source")
        exit()
except:
    os.remove(configfile_name)
    ConfigGen.GenerateConfig(configfile_name)
    print("Config corrupted. File has been reset, please try again")
    exit()

if len(sys.argv) < 2:
    print_usage()
    exit()

algo_opt = sys.argv[1]

###################################

decision_tree_classifier = C45DecisionTreeClassifier(classifier_training_data, target, target_names,
                                                     preprocess=preprocess)
sgd_classifier = SGDClassifier(classifier_training_data, target, target_names, preprocess=preprocess)
decision_tree_classifier.train()
sgd_classifier.train()
print('Precision of the classifier on its training data set: ', decision_tree_classifier.kfold_cross_validation(1))

n_splits = 20
print("{}-Fold evaluation on the training data set: {}\n".format(n_splits,
                                                                 sgd_classifier.kfold_cross_validation(
                                                                     n_splits)))

testing_percentage = 0.8

print("Training on {}% of the data (={} docs out of {}) and computing prediction accuracy on the rest".format(
    testing_percentage * 100, int(testing_percentage * len(classifier_training_data)), len(classifier_training_data)))

print("SGD Classifier: {} ".format(sgd_classifier.accuracy_performance(testing_percentage=testing_percentage) * 100))

print("Decision Tree Classifier: {}".format(
    decision_tree_classifier.accuracy_performance(testing_percentage=testing_percentage) * 100))
exit()

### predict the category of every question, appending it into the corresponding list of the dictionary ###

predicted_categories = {}
cluster_data = {}
cluster_target = {}
for category_name in target_names:
    predicted_categories[category_name] = []
cluster_data[category_name] = []
cluster_target[category_name] = []

max_questions = 1000  # this is to make it run faster for testing, remove during normal runs
for question in questions[:max_questions]:
    question = question.replace('.', '. ').replace('.  ', '. ').replace('?', '? ').replace('?  ', '? ').replace('!',
                                                                                                                '! ').replace(
        '!  ', '! ')
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

# question_recommender = Recommender()

def kmeans(data, target, target_names):
    preprocess = 0
    n_clusters = int(len(data) / 10)
    clusterizer = KMeansClusterizer(data, target, target_names, n_features=n_features, preprocess=preprocess, jobs=jobs,
                                    verbose=verbose)
    clusterizer.lda_clusterize(n_clusters=n_clusters, n_features=20, kmeans_iter=1)
    if (printToFile):
        clusterizer.print_clusters('kmeans_{}_{}.txt'.format(category, n_clusters))
    clusterizer.get_avg_silhouette()
    return clusterizer


def dbscan(data, category):
    clusterizer = DBSCANClusterizer(data, n_features=n_features, preprocess=preprocess, jobs=jobs, verbose=verbose)
    db = clusterizer.compute(eps=0.5, min_samples=5)

    sihouette = clusterizer.get_avg_silhouette();

    if (printToFile):
        clusterizer.print_clusters('dbscan_{}_{}'.format(category, len(clusterizer.get_clusters())))

    return clusterizer


def affinity(data, target, target_names):
    clusterizer = AffinityPropagationClusterizer(data)
    clusterizer.compute(n_features=10, max_iter=1)
    return clusterizer


def hierarchical(data, linkage):
    n_clusters = int(len(data) / 10)
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
        # cluster_target_names.append(category)
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
            print_usage()
            exit()

        if (printToCSV):
            clusterizer.print_to_csv()
