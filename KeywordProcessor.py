from InputPreprocessor import InputPreprocessor

class KeywordProcessor:
    def __init__(self, doc_set):
        self.__doc_set = doc_set
        self.__preprocessor = InputPreprocessor(doc_set)

    def count_keywords(self):
        words_occurences = {}
        terms = self.__preprocessor.preprocess_terms()

        for term in terms:
            for word in term:
                for something in word:
                    if something in words_occurences:
                        words_occurences[something] += 1
                    else:
                        words_occurences[something] = 1

        return words_occurences