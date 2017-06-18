from Database.DatabaseManager import DatabaseManager
from ML.Classifier import Classifier

connect_string = "dbname=uoa-nlp user=admin"
dbmg = DatabaseManager(connect_string)
questions_forum_db = dbmg.my_query(
    "select * from questions join forum_details on forum_details.forum_details_id = questions.forum_details_id", None,
    fetch_to_dict=True)
dbmg.close()

data = []
target = []
target_names = [] # type('Bunch', (), {'data':[], 'target':[], 'target_names':[]})
# questions = {'data':[], 'target':[], 'target_names':[]}

for question_forum in questions_forum_db:
    content = question_forum['content']
    if question_forum['name'] not in target_names:
        target_names.append(question_forum['name'])
    if content is not None:
        data.append(content)
        target.append(target_names.index(question_forum['name']))

forum_question_classifier = Classifier(data, target, target_names)

print('Precision of the classifier: ', forum_question_classifier.evaluate_precision())

new_question = ["I am having issues with tokens"]

predicted_forum_i = forum_question_classifier.predict(new_question)
print(predicted_forum_i[0])
print(forum_question_classifier.target_names)
print(forum_question_classifier.target_names[predicted_forum_i[0]])