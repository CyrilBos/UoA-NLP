from nlp.input_preprocessor import InputPreprocessor

class KeywordExtractor:
    """
    Class that preprocess a set of documents and extracts its keywords based on the frequency of each term.
    """
    def __init__(self, doc_set):
        """
        Initializes the new KeywordExtractor instance with the given set of documents.
        :param doc_set: set of documents
        :type doc_set: list
        """
        self.__doc_set = doc_set
        self.__preprocessor = InputPreprocessor(doc_set)

    def count_keywords(self):
        """
        Counts the occurences of each preprocessed term in the set of documents.
        :return: every term with its number of occurences
        :rtype: dict
        """
        words_occurences = {}
        terms = self.__preprocessor.preprocess_terms()

        for term in terms:
            for word in term:
                for occurence in word:
                    if occurence in words_occurences:
                        words_occurences[occurence] += 1
                    else:
                        words_occurences[occurence] = 1

        return words_occurences