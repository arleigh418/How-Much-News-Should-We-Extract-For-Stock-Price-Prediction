import wikipedia
import pandas as pd


def clean_stop_word(all_article):
    after_deal_article = []
    stopword = []
    with open('../Stage1_2Replace Company Name Train Embedding/stop_words.txt', 'r', encoding='UTF-8') as file:
        for data in file.readlines():
            data = data.strip()
            stopword.append(data) 
    for article in all_article:
        article = article.split(' ') 
        filter_article = list(filter(lambda a: a not in stopword and a != '\n', article))
        wd_join= " ".join(id for id in filter_article)   
        after_deal_article.append(wd_join)

    return after_deal_article


import jieba
from pandas import ExcelWriter
jieba.load_userdict("../Stage1_2Replace Company Name Train Embedding/new_words.txt")


def parsing(document):
    store_list = []
    seg_full = jieba.cut(document , cut_all=False)
    x = ' '.join(seg_full)
    store_list.append(x)
    return store_list

wikipedia.set_lang("zh")

com_list= ['遊戲橘子','鴻海','中華電信','仁寶','兆豐金']

for word in com_list:
    print('Start dealing company:',word)
    com_use_list=[]
    store = pd.DataFrame()
    keyword=wikipedia.page(word)
    content = keyword.content
    content = content.replace('=','')
    com_use_list.append(content.replace('\n',''))
    for cut in com_use_list:    
        store_list = parsing(cut)
    final_company_intro = clean_stop_word(store_list)
    store['Com_intro'] = final_company_intro
    store.to_excel(f'../article set/All_File/{word}_intro.xlsx')
    store.to_excel(f'../article_stop_word/All_File/{word}_intro.xlsx')

    