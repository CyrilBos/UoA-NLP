import nltk
from nltk.corpus import stopwords

class InputPreprocessor:
    def __init__(self, doc_set):
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

    def normalise(self, word):
        """Normalises words to lowercase and stems and lemmatizes it."""
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
        for leaf in self.leaves(tree):
            term = [self.normalise(w) for w, t in leaf if self.acceptable_word(w)]
            yield term


    def preprocess_terms(self):
        doc_terms = []
        for doc in self.__doc_set:
            print('Preprocessing terms of following content:')
            print(doc)
            toks = nltk.regexp_tokenize(doc, self.__sentence_re)
            postoks = nltk.tag.pos_tag(toks)

            print('POS-tagged words: ')
            print(postoks)

            tree = self.__chunker.parse(postoks)
            doc_terms.append(self.get_terms(tree))
        return doc_terms