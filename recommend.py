import random

from database.configuration import connection_string
from database.database_manager import DatabaseManager
from ml.recommender import Recommender
from Utils.logger import logger

dbmg = DatabaseManager(connection_string)
questions_db = dbmg.select_query(
    "select * from replies", None,
    fetch_to_dict=True)
dbmg.close()

data = {'id':[], 'description':[]}

for question in questions_db:
    content = question['text']
    if content is None:
        content = ""
        logger.error("Question of id {} does not have content".format(question['replies_id']))
    data['id'].append(question['replies_id'])
    data['description'].append(content)

question_recommender = Recommender()
question_recommender.train(data)

rnd = random.randint(0, 20)
for item_to_recommend_index in range(rnd, rnd+rnd):

    print("Current item: ", data['description'][item_to_recommend_index])
    recommended_items = question_recommender.predict(data['id'][item_to_recommend_index], 5)
    print("Recommended items: ")
    for recommended_item in recommended_items:
        print(data['description'][data['id'].index(int(recommended_item[1]))])

