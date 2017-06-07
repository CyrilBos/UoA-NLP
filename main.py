import logging

import nltk
from Database import DatabaseManager

logger = logging.getLogger()

connect_string = "dbname=uoa-nlp user=admin"
dbmg = DatabaseManager(connect_string)
result = dbmg.query("select * from questions", None, 'dict')
print('Questions contained in the database: ')
print(result)

#following code was copied from https://gist.github.com/alexbowe/879414#gistcomment-1704727
# and corrected by myself to run with newer NLTK versions
lemmatizer = nltk.WordNetLemmatizer()
stemmer = nltk.stem.porter.PorterStemmer()

# Used when tokenizing words
sentence_re = r'(?:(?:[A-Z])(?:.[A-Z])+.?)|(?:\w+(?:-\w+)*)|(?:\$?\d+(?:.\d+)?%?)|(?:...|)(?:[][.,;"\'?():-_`])'

# Taken from Su Nam Kim Paper...
grammar = r"""
    NBAR:
        {<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns

    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}  # Above, connected with in/of/etc...
"""
chunker = nltk.RegexpParser(grammar)



from nltk.corpus import stopwords
stopwords = stopwords.words('english')


def leaves(tree):
    """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    for subtree in tree.subtrees(lambda t: t.label() == 'NP'):
        yield subtree.leaves()

def normalise(word):
    """Normalises words to lowercase and stems and lemmatizes it."""
    word = word.lower()
    word = stemmer.stem(word)
    word = lemmatizer.lemmatize(word)
    return word

def acceptable_word(word):
    """Checks conditions for acceptable word: length, stopword."""
    accepted = bool(2 <= len(word) <= 40
        and word.lower() not in stopwords)
    return accepted


def get_terms(tree):
    for leaf in leaves(tree):
        term = [ normalise(w) for w,t in leaf if acceptable_word(w) ]
        yield term

#my own modifications to count occurences

words_occurences = {}

for question in result:
    text = question['content']
    if (text):
        print('Processing following content:')
        print(question['question_id'], text)
        toks = nltk.regexp_tokenize(text, sentence_re)
        postoks = nltk.tag.pos_tag(toks)

        print('POS-tagged words: ')
        print(postoks)

        tree = chunker.parse(postoks)
        terms = get_terms(tree)
        for term in terms:
            for word in term:
                if word in words_occurences:
                    words_occurences[word] += 1
                else:
                    words_occurences[word] = 1
    else:
        logger.error('Question of ID {} has no content'.format(question['question_id']))

print('Occurences for each stemmed and lemmatized keyword: ')
print(words_occurences)
print('Sorted by descending occurence: ')
print(sorted(words_occurences, key=words_occurences.__getitem__, reverse=True))