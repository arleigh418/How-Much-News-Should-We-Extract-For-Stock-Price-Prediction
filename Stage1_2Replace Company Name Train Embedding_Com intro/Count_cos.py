# -*- coding: utf-8 -*-
import gensim
import pandas as pd

import re 
import numpy as np
from gensim.models import Word2Vec
from gensim.models import FastText

#1.Function for counting cosine 
def cos_sim(vector1, vector2):  
    
    cos=np.dot(vector1,vector2)/(np.linalg.norm(vector1)*(np.linalg.norm(vector2)))
    return cos

#2.Function for getting sum of each word from news
def count_vector(model, words): 
    vect_list = []
    vec = np.zeros(500) 
    for w in words:
       
        try:    
           vec = vec + model.wv[w]
        except:
            continue
    return vec


#3.Making Company list and model list for next step
com_list = ['中華電信','鴻海','兆豐金','仁寶','橘子'] 
com_list_num = ['2412','2317','2886','2324','6180']
model_list = ['fastText_stock','word2vec_stock'] 
percentage = ['0','25','50','75'] 
folder = ['article set','article_stop_word']


#4.Call step1 & step2 Function and loop for getting doc2vec、fastTest、word2vec article vector and store file
for fo in folder:
    for company in range(len(com_list)):
        for model_use in model_list:
            for per in percentage:
                per = int(per)
                article  = pd.read_excel(f'../{fo}/All_File/Final_Clean_Article.xlsx')
                article_center =pd.read_excel(f'../{fo}/All_File/{com_list[company]}_intro.xlsx') 

                all_article = article['內容'].tolist()
                news_time = article['時間'].tolist()

                all_article_center = article_center['Com_intro'].tolist()
                
                if model_use =='fastText_stock':
                    model = FastText.load('../Word_Embedding_model/{}.model'.format(model_use))
                else:
                    model = Word2Vec.load('../Word_Embedding_model/{}.model'.format(model_use))
                print('Using Model : ','../Word_Embedding_model/{}.model'.format(model_use))
                
                
                score = [] # for cos
                Article_vector = [] # for article vector
                Article_extract = [] #for target article
                Article_vector_extract = [] # for target article vector
                Article_time_extract = [] # for target article time

                for y in all_article_center:
                    y = y.split(' ')
                    tmp_storage_y = []
                    for words in y:
                        tmp_storage_y.append(re.sub(r'[_"\-;%()（）《》|+&=*%.,!，、?:#$@\[\]「/」]', '', words))

                    article_center_vec = count_vector(model,tmp_storage_y)
                

                for x in all_article:
                    x = x.split(' ')
                    tmp_storage = []
                    for word in x:
                        tmp_storage.append(re.sub(r'[_"\-;%()（）《》|+&=*%.,!，、?:#$@\[\]「/」]', '', word))
                    article_vec = count_vector(model,tmp_storage)
                    Article_vector.append(article_vec)
                
                    cos  = cos_sim(article_vec,article_center_vec)
                    score.append(cos)
                    # print(cos)

                article_standard_use = np.array(score)
                print('Target Percentage : ',per)
                article_standard = np.percentile(article_standard_use , (per), interpolation='midpoint') #get the target data with percetage by cos
                for x in range(len(score)):
                    if score[x] > article_standard:
                        Article_extract.append(all_article[x])
                        Article_vector_extract.append(Article_vector[x])
                        Article_time_extract.append(news_time[x])
                        # print('Target Cos Value : ',score[x],'Filter Standard : ',article_standard)
                    else:
                        continue

                columns_vec_name = []
                for x in range(500):
                    columns_vec_name.append('vector{}'.format(x))
                pd_data = pd.DataFrame()
                verify = len(Article_vector_extract)/len(all_article)
                print('verify:Get',verify,'News')
                print('Start Dealing Excel......')
                pd_data['內容'] = Article_extract
                pd_data['時間'] = Article_time_extract
                
                pd_data_vector = pd.DataFrame(Article_vector_extract,columns = columns_vec_name)
                pd_concat = pd.concat([pd_data,pd_data_vector], axis=1)
                pd_concat.to_excel(f'../{fo}/All_File/{com_list_num[company]}TW_intro/cos/cos{str(100-int(per))}%_{model_use}_{com_list[company]}.xlsx')
                print('Finish')

    


    