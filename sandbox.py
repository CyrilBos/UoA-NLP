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