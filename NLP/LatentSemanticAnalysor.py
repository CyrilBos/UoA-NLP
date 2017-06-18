import gensim
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer

from NLP.InputPreprocessor import InputPreprocessor


class LatentSemanticAnalyser:
    def __init__(self, doc_set):
        self.__doc_set = doc_set
        self.__preprocessor = InputPreprocessor(doc_set)


    def compute(self, topics, save_filename):
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
