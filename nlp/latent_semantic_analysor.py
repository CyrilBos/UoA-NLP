import gensim
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer

from nlp.input_preprocessor import InputPreprocessor


class LatentSemanticAnalyser:
    def __init__(self, doc_set):
        """
       Initalizes the new LSA instance with the given set of documents.
       :param doc_set: set of documents
       :type doc_set: list
       """
        self.__doc_set = doc_set
        self.__preprocessor = InputPreprocessor(doc_set)


    def compute(self, topics, save_filename):
        """
        Preprocess the set of documents into a BOW representation and then
        computes the LSA model and returns it along with the corpus and dictionary.
        :param topics: number of wanted topics
        :type topics: int
        :param save_filename: filename to save the model to
        :type save_filename: str
        :return: a tuple (model, corpus, dictionary)
        :rtype: tuple
        """
        texts = []

        tokenizer = RegexpTokenizer(r'\w+')

        # create English stop words list
        en_stop = stopwords.words('english')

        # Create p_stemmer of class PorterStemmer
        p_stemmer = PorterStemmer()

        for i in self.__doc_set:
            # clean and tokenize document string
            raw = i.lower()
            tokens = tokenizer.tokenize(raw)

            # remove stop words from tokens
            stopped_tokens = [i for i in tokens if not i in en_stop]

            # stem tokens
            stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

            # add tokens to list
            texts.append(stemmed_tokens)

        # turn our tokenized documents into a id <-> term dictionary
        dictionary = gensim.corpora.Dictionary(texts)

        # convert tokenized documents into a document-term matrix
        corpus = [dictionary.doc2bow(text) for text in texts]

        # generate LDA model
        lsi_model = gensim.models.LsiModel(corpus, num_topics=topics, id2word=dictionary)

        save_filename += "_{}".format(topics)

        dictionary.save(save_filename + ".dict")
        gensim.corpora.MmCorpus.save_corpus(save_filename + ".mm", corpus, id2word=dictionary)
        lsi_model.save(save_filename + ".model")

        return lsi_model, corpus, dictionary
