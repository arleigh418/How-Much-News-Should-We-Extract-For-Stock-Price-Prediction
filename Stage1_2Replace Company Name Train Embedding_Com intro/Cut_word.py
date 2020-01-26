import pandas as pd
x = pd.read_excel('../article set/All_File/Final.xlsx' , encoding = 'utf-8')
sentences = x['內容'].tolist()
news_time = x['時間'].tolist()

After_replace = []
C = 0
for i in sentences:
    #鴻海
    i = i.replace('鴻海科技集團','鴻海')
    i = i.replace('鴻海科技','鴻海')
    i = i.replace('鴻海精密','鴻海')
    i = i.replace('Foxconn Technology Group','鴻海')
    i = i.replace('Foxconn','鴻海')
    i = i.replace('富士康','鴻海')
    i = i.replace('鴻海 (2317-TW)','鴻海')
    i = i.replace('鴻海 (2317)','鴻海')
    i = i.replace('鴻海塑膠','鴻海')
    i = i.replace('鴻海精密工業股份有限公司','鴻海')
    i = i.replace('2317','鴻海')
    i = i.replace('2317-TW','鴻海')
    #台積電
    i = i.replace('台灣積體電路製造股份有限公司','台積電')
    i = i.replace('台灣積體電路製造','台積電')
    i = i.replace('台灣積體電路製造公司','台積電')
    i = i.replace('Taiwan Semiconductor Manufacturing','台積電')
    i = i.replace('Taiwan Semiconductor Manufacturing Company','台積電')
    i = i.replace('TSMC','台積電')
    i = i.replace('台積電 (2330-TW)','台積電')
    i = i.replace('2330','台積電')
    i = i.replace('台積電(2330)','台積電')
    i = i.replace('2330.TW','台積電')
    i = i.replace('2330-TW ','台積電')
    #仁寶
    i = i.replace('仁寶電腦','仁寶')
    i = i.replace('仁寶電腦工業股份有限公司','仁寶')
    i = i.replace('Compal Electronics','仁寶')
    i = i.replace('仁寶 (2324-TW)','仁寶')
    i = i.replace('Compal Electronics, Inc.','仁寶')
    i = i.replace('Compal Electronics,Inc.','仁寶')
    i = i.replace('Compal Electronics,Inc','仁寶')
    i = i.replace('仁寶 (2324)','仁寶')
    i = i.replace('2324-TW','仁寶')
    i = i.replace('2324','仁寶')
    #中華電信
    i = i.replace('中華電','中華電信')
    i = i.replace('中華電 (2412-TW)','中華電信')
    i = i.replace('中華電信 (2412-TW)','中華電信')
    i = i.replace('中華電信 (2412)','中華電信')
    i = i.replace('中華電 (2412)','中華電信')
    i = i.replace('中華雲市集','中華電信')
    i = i.replace('2412','中華電信')
    i = i.replace('2412-TW','中華電信')
    i = i.replace('中華電信 (2412)','中華電信')
    i = i.replace('CHT','中華電信')
    #兆豐金
    i = i.replace('兆豐金融控股','兆豐金')
    i = i.replace('兆豐金控','兆豐金')
    i = i.replace('兆豐國際商業銀行','兆豐金')
    i = i.replace('兆豐金控 (2886-TW)','兆豐金')
    i = i.replace('兆豐金控 (2886)','兆豐金')
    i = i.replace('2886-TW','兆豐金')
    i = i.replace('2886','兆豐金')
    i = i.replace('兆豐證券','兆豐金')
    i = i.replace('兆豐票券金融','兆豐金')
    i = i.replace('兆豐產物保險','兆豐金')
    i = i.replace('兆豐國際證券投資信託','兆豐金')
    i = i.replace('兆豐創業投資','兆豐金')
    i = i.replace('兆豐期貨','兆豐金')
    i = i.replace('兆豐國際商業銀行股份有限公司','兆豐金')
    i = i.replace('兆豐銀','兆豐金')
    i = i.replace('兆豐銀行','兆豐金')
    C+=1
    After_replace.append(i)
    print('處理了:',C,'篇 | 共有 :',len(sentences),'篇')

Storge_replace_sentence = pd.DataFrame()
Storge_replace_sentence['內容'] = After_replace
Storge_replace_sentence['時間'] = news_time


Storge_replace_sentence.to_excel('../article set/All_File/Replace_over.xlsx')
Storge_replace_sentence.to_excel('../article_stop_word/All_File/Replace_over.xlsx')

import jieba
from pandas import ExcelWriter
jieba.load_userdict("../Stage1_2Replace Company Name Train Embedding/new_words.txt")

x = pd.read_excel('../article set/All_File/Replace_over.xlsx' , encoding = 'utf-8')
sentences = x['內容'].tolist()
news_time = x['時間'].tolist()
gg = []

def parsing(document):
    seg_full = jieba.cut(document , cut_all=False)
    x = ' '.join(seg_full)
    gg.append(x)


for i in sentences:
    parsing(i)

pd_cut = pd.DataFrame()
pd_cut['內容'] = gg
pd_cut['時間'] = news_time

pd_cut.to_excel('../article set/All_File/Cut_Finish_jieba.xlsx')
pd_cut.to_excel('../article_stop_word/All_File/Cut_Finish_jieba.xlsx')




 



























