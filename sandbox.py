"""
import pyLDAvis.gensim
import gensim
#import graphlab

topics = 100
passes = 20

save_filename = "lda-saves/lda_replies_question_forum_2287_{}_{}".format(topics, passes)

dictionary = gensim.corpora.Dictionary.load(save_filename + ".dict")
corpus = gensim.corpora.MmCorpus(save_filename + ".mm")
ldamodel = gensim.models.LdaMulticore.load(save_filename + ".model")

vis_data = pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary)
pyLDAvis.display(vis_data)
#pyLDAvis.enable_notebook(vis_data)
pyLDAvis.show(vis_data)
"""
import numpy as np
import lda

X = lda.datasets.load_reuters()
vocab = lda.datasets.load_reuters_vocab()
titles = lda.datasets.load_reuters_titles()
print(X.shape)
print(X.sum())
model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
model.fit(X)  # model.fit_transform(X) is also available
topic_word = model.topic_word_  # model.components_ also works
n_top_words = 8
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))