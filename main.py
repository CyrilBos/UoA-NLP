import nltk
from Database import DatabaseManager

connect_string = "dbname=uoa-nlp user=admin"
dbmg = DatabaseManager(connect_string)
result = dbmg.query("select * from forum_details", None)
print(result)
