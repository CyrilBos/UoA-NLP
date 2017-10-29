import gensim
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer

from nlp.InputPreprocessor import InputPreprocessor


class LatentDirichletAllocation:
    """
    Implementation of the LDA algorithm to extract topic from a given set of documents.
    """

    def __init__(self, doc_set, workers=1):
        """
        Initalizes the new LDA instance with the given set of documents.
        :param doc_set: set of documents
        :type doc_set: list
        """
        self.__doc_set = doc_set
        self.__workers = workers

    def get_corpus_and_dictionary(self):
        """
        Preprocess the set of documents to compute then return the corpus and the related dictionary.
        :return: a tuple (corpus, dictionary). corpus is the bag of words representation of the documents
        and dictionary translates ids into terms.
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
            #print(i)
            #print(type(i))
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

        corpus = [dictionary.doc2bow(text) for text in texts]

        return corpus, dictionary

    def compute(self, topics, passes):
        """
        Preprocess the set of documents into a BOW representation and then
        computes the LDA model and returns it along with the corpus and dictionary.
        :param topics: number of wanted topics
        :type topics: int
        :param passes: number of times the algorithm will be executed
        :type passes: int
        :param save_filename: filename to save the model to
        :type save_filename: str
        :return: a tuple (model, corpus, dictionary)
        :rtype: tuple
        """

        corpus, dictionary = self.get_corpus_and_dictionary()
        ldamodel = gensim.models.LdaMulticore(corpus, num_topics=topics, id2word=dictionary, passes=passes,
                                              workers=self.__workers)

        return ldamodel, corpus, dictionary

    def save_to_file(self, filename, model, corpus, dictionary):
        """
                Saves model, dictionary and corpus to files, appending .model, .dict and .mm to filename.
                :param filename: number of wanted topics
                :type filename: str
                :param model: number of times the algorithm will be executed
                :type model: gensim.models.ldamodel.LdaModel
                :param corpus: filename to save the model to
                :type corpus: gensim.corpora.MmCorpus
                :param dictionary: filename to save the model to
                :type dictionary: gensim.corpora.Dictionary
                """
        gensim.corpora.MmCorpus.save_corpus(filename + ".mm", corpus, id2word=dictionary)
        dictionary.save(filename + ".dict")
        model.save(filename + ".model")
