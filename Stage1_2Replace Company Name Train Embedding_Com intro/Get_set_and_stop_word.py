import pandas as pd
import re
'''
Testing status
'''
def clean_stop_word_and_set(all_article,news_time):
    after_deal_article = []
    stopword = []
    count = 1
    with open('../Stage1_2Replace Company Name Train Embedding/stop_words.txt', 'r', encoding='UTF-8') as file:
        for data in file.readlines():
            data = data.strip()
            stopword.append(data) 
    for article in all_article:
        article = article.split(' ') 
        filter_article = set(list(filter(lambda a: a not in stopword and a != '\n', article)))
        wd_join= " ".join(id for id in filter_article)   
        after_deal_article.append(wd_join)
        count_dealing = (count/len(news_time))*100
    
        print('共處理:',count_dealing,'| 長度:',len(after_deal_article))
        count+=1
    return after_deal_article


def clean_stop_word(all_article,news_time):
    after_deal_article = []
    stopword = []
    count = 1
    with open('../Stage1_2Replace Company Name Train Embedding/stop_words.txt', 'r', encoding='UTF-8') as file:
        for data in file.readlines():
            data = data.strip()
            stopword.append(data) 
    for article in all_article:
        article = article.split(' ') 
        filter_article = list(filter(lambda a: a not in stopword and a != '\n', article))
        wd_join= " ".join(id for id in filter_article)   
        after_deal_article.append(wd_join)
        count_dealing = (count/len(news_time))*100

        print('共處理:',count_dealing,'| 長度:',len(after_deal_article))
        count+=1

    return after_deal_article


article  = pd.read_excel('../article set/All_File/Cut_Finish_jieba.xlsx') 
all_article = article['內容'].tolist()
news_time = article['時間'].tolist()
deal_all_article = clean_stop_word_and_set(all_article,news_time)
deal_all_article_stop_word =  clean_stop_word(all_article,news_time)

print(len(deal_all_article))
# print(len(news_time))
storage = pd.DataFrame()
storage['內容'] = deal_all_article
storage['時間'] = news_time

storage2 = pd.DataFrame()
storage2['內容'] = deal_all_article_stop_word
storage2['時間'] = news_time

storage.to_excel('../article set/All_File/Final_Clean_Article.xlsx')
storage2.to_excel('../article_stop_word/All_File/Final_Clean_Article.xlsx')