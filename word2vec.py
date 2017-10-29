from multiprocessing import Process

from gensim.models import word2vec

from database.database_helper import DatabaseHelper


class SimilarityComputingThread(Process):
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

questions = db.get_questions_content()

sentences = word2vec.Text8Corpus('text8')
#model = word2vec.Word2Vec(questions, sg=1, workers=8)

#model = word2vec.Word2Vec(sentences)
#model.save("dupes.model")
model = word2vec.Word2Vec.load("dupes.model")

for i in range(0,8):
    th = SimilarityComputingThread(model, questions, i)
    th.start()

"""
for question in questions:
    print("NEW_QUESTION", question)
    for other_question in questions:
        if question != other_question:
            s1 = set(question.split()).intersection(model.wv.vocab)
            s2 = set(other_question.split()).intersection(model.wv.vocab)
            similarity = model.n_similarity(s1, s2)
            if similarity >= 0.95:
                print(similarity, other_question)
"""