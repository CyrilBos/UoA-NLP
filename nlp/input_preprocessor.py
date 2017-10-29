import nltk
from nltk.corpus import stopwords

class InputPreprocessor:
    """
    Class that preprocesses documents using NLTK chunker, lemmatizer, stemmer and stop-words.
    """
    def __init__(self, doc_set):
        """
        Initializes the new InputPreprocessor instance with the given set of documents.
        :param doc_set: set of documents
        :type doc_set: list
        """
        self.__doc_set = doc_set

        self.__grammar = r"""
    NBAR:
        {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns

    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
"""
        self.__chunker = nltk.RegexpParser(self.__grammar)
        # Used when tokenizing words
        self.__sentence_re = r'(?:(?:[A-Z])(?:.[A-Z])+.?)|(?:\w+(?:-\w+)*)|(?:\$?\d+(?:.\d+)?%?)|(?:...|)(?:[][.,;"\'?():-_`])'
        self.__lemmatizer = nltk.WordNetLemmatizer()
        self.__stemmer = nltk.stem.porter.PorterStemmer()

        self.__stopwords = stopwords.words('english')

    def leaves(self, tree):
        """Finds NP (nounphrase) leaf nodes of a chunk tree."""
        for subtree in tree.subtrees(lambda t: t.label() == 'NP'):
            yield subtree.leaves()

    def stem(self, word):
        """Stems the given word."""
        return self.__stemmer.stem(word)

    def normalise(self, word):
        """Normalises words by lowercasing, stemming and lemmatizing it."""
        word = word.lower()
        word = self.__stemmer.stem(word)
        word = self.__lemmatizer.lemmatize(word)
        return word

    def acceptable_word(self, word):
        """Checks conditions for acceptable word: length, stopword."""
        accepted = bool(2 <= len(word) <= 40
                        and word.lower() not in self.__stopwords)
        return accepted

    def get_terms(self, tree):
        """Get the terms from the given tree."""
        for leaf in self.leaves(tree):
            term = [self.normalise(w) for w, t in leaf if self.acceptable_word(w)]
            yield term

    def tokenize(self, doc):
        """Process the given doc and returns its tokens.
        :return: the processed tokens
        :rtype: list
        """
        return nltk.regexp_tokenize(doc, self.__sentence_re)


    def preprocess_terms(self):
        """
        Preprocess the terms in the set of documents using the above functions.
        :return: the processed terms
        :rtype: list
        """
        doc_terms = []
        for doc in self.__doc_set:
            #print('Preprocessing terms of following content:')
            #print(doc)
            doc_terms.append(self.get_terms(self.__chunker.parse(nltk.tag.pos_tag(self.tokenize(doc)))))
        return doc_terms