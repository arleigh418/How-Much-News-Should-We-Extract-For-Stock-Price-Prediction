import os

print('---------------------------Data Prepare1--------------------------- ')
with open('D:/Stock_News_Extract_Method_lstm_Github/Stage1_Replace Company Name Train Embedding/Cut_word.py','r',encoding='utf-8') as f:
    exec(f.read())

print('---------------------------Data Prepare2--------------------------- ')
with open('D:/Stock_News_Extract_Method_lstm_Github/Stage1_Replace Company Name Train Embedding/FAST.py','r',encoding='utf-8') as f:
    exec(f.read())

print('---------------------------Data Prepare3--------------------------- ')
with open('D:/Stock_News_Extract_Method_lstm_Github/Stage1_Replace Company Name Train Embedding/WORD.py','r',encoding='utf-8') as f:
    exec(f.read())

print('---------------------------Data Prepare4--------------------------- ')
with open('D:/Stock_News_Extract_Method_lstm_Github/Stage1_Replace Company Name Train Embedding/Get_set_and_stop_word.py','r',encoding='utf-8') as f:
    exec(f.read())


print('Data Prepare Over......')

print('---------------------------Start 1--------------------------- ')
with open('D:/Stock_News_Extract_Method_lstm_Github/Stage1_Replace Company Name Train Embedding/Count_cos.py','r',encoding='utf-8') as f:
    exec(f.read())
print('---------------------------Start 2--------------------------- ')
with open('D:/Stock_News_Extract_Method_lstm_Github/Stage1_Replace Company Name Train Embedding/Count_euc.py','r',encoding='utf-8') as f:
    exec(f.read())
print('---------------------------Start 3--------------------------- ')
with open('D:/Stock_News_Extract_Method_lstm_Github/Stage1_Replace Company Name Train Embedding/Count_manha.py','r',encoding='utf-8') as f:
    exec(f.read())
print('---------------------------Start 4--------------------------- ')
with open('D:/Stock_News_Extract_Method_lstm_Github/Stage2_Count TA & Merge Stock Price And Article/Get_ta.py','r',encoding='utf-8') as f:
    exec(f.read())
print('---------------------------Start 5--------------------------- ')

with open('D:/Stock_News_Extract_Method_lstm_Github/Stage2_Count TA & Merge Stock Price And Article/add_method_merge_file.py','r',encoding='utf-8') as f:
    exec(f.read())
    
print('---------------------------Start 6--------------------------- ')
with open('D:/Stock_News_Extract_Method_lstm_Github/Stage3_Model_Test/model.PY','r',encoding='utf-8') as f:
    exec(f.read())