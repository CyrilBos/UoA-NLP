from multiprocessing import Process

from gensim.models import doc2vec

from database.database_helper import DatabaseHelper
from nlp.input_preprocessor import InputPreprocessor


class SimilarityComputingThread(Process):
    """
    Class to be instantiated 8 times to compute the similarity faster.
    """
    __docs = []
    __id = -1
    __model = None

    def __init__(self, model, docs, id):
        self.__model = model
        self.__docs = docs
        self.__id = id
        super(SimilarityComputingThread, self).__init__()

    def run(self):
        length = len(self.__docs)
        sub_index = (self.__id) * int(length/8)
        working_docs = self.__docs[sub_index:sub_index + int(length/8)]
        print(len(working_docs))
        file = open("similarity_res_th_{}.txt".format(self.__id), 'w+')
        for doc in working_docs:
            file.write("NEW_QUESTION" + doc + "\n")
            for other_doc in self.__docs:
                if doc != other_doc:
                    s1 = set(doc.split()).intersection(self.__model.wv.vocab)
                    s2 = set(other_doc.split()).intersection(self.__model.wv.vocab)
                    similarity = self.__model.n_similarity(s1, s2)
                    if similarity > 0.95:
                        print(similarity)
                        file.write(str(similarity) + other_doc + "\n")

connect_string = "dbname=uoa-nlp user=admin"
db = DatabaseHelper(connect_string)

questions_db = db.select_query("select question_id, content from question", None, fetch_to_dict=True)

questions_content = []
tagged_questions = []

tokenizer = InputPreprocessor(None)

###tokenize the data before applying the model

for question in questions_db:
    if question['content'] is not None:
        questions_content.append(question['content'])
        tokens = tokenizer.tokenize(question['content'])
        tagged_questions.append(doc2vec.TaggedDocument(words=tokens, tags=[question['questiony_id']]))


model = doc2vec.Doc2Vec(documents=tagged_questions, workers=8)
##############################################

### compute the similarity of each question with every other question ###
for content in questions_content:
    print("NEW QUESTION", content)
    for other_content in questions_content:
        if content != other_content:
            s1 = set(content.split()).intersection(model.wv.vocab)
            s2 = set(other_content.split()).intersection(model.wv.vocab)
            similarity = model.n_similarity(s1, s2)
            if similarity >= 0.995:
                print(similarity, other_content)

"""
for i in range(0,8):
    th = SimilarityComputingThread(model, questions, i)
    th.start()
"""
