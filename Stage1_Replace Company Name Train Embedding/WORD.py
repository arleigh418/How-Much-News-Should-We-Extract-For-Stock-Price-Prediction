import pandas as pd
from gensim.models import Word2Vec
import jieba



article = pd.read_excel('../article set/All_File/Cut_Finish_jieba.xlsx')

sentences = article['內容'].tolist()

split_sentences = []

for i in sentences:
    split_sentences.append(i.split(' '))
# build a Word2Vce model
model = Word2Vec(split_sentences, size=500, window=10, min_count=5, workers=4,iter=10)
# save model to file
model.save("../Word_Embedding_model/word2vec_stock.model")
# load model to python
model = Word2Vec.load("../Word_Embedding_model/word2vec_stock.model")

print(model.wv['台積電'])

print('橘子',model.most_similar("橘子", topn=5))
print('鴻海',model.most_similar("鴻海", topn=5))
print('中華電信',model.most_similar("中華電信", topn=5))
print('仁寶',model.most_similar("仁寶", topn=5))
print('兆豐金',model.most_similar("兆豐金", topn=5))