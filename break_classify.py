from Database.DatabaseHelper import DatabaseHelper
from ML.Classifier import Classifier

from nltk.tokenize import sent_tokenize


connect_string = "dbname=uoa-nlp user=admin"
dbmg = DatabaseHelper(connect_string)
questions_sentences = dbmg.my_query(
    "select * from training_data join training_data_categories on training_data_categories.training_data_categories_id = training_data.training_data_categories_id", None,
    fetch_to_dict=True)

questions = dbmg.get_questions_content()

dbmg.close()

data = []
target = []
target_names = []
for question_sentence in questions_sentences:
    if question_sentence['category_name'] not in target_names:
        target_names.append(question_sentence['category_name'])
    data.append(question_sentence['content'])
    target.append(question_sentence['training_data_categories_id'])

forum_question_classifier = Classifier(data, target, target_names)

print('Precision of the classifier: ', forum_question_classifier.evaluate_precision())

predicted_categories = {'introduction':[], 'problem':[], 'code':[], 'question':[], 'outroduction':[]}

for question in questions:
    for sentence in sent_tokenize(question):
        predicted_category_i = forum_question_classifier.predict([sentence])[0]
        predicted_categories[forum_question_classifier.target_names[predicted_category_i]].append(sentence)

for category in predicted_categories:
    print('####Category: ' + category)
    for i in range(10):
        print(predicted_categories[category][i])