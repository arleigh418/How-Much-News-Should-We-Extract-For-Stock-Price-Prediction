import os

def mkdir(path):
    path=path.strip()
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    else:
        print('Folder is exist')
        
folder_up =[ 'article set','article_stop_word']
stock = ['/2317','/2324','/2412','/2886','/6180']

intro_or_not = ['Final_Result','Final_Result_intro']

add_method_folder = ['/add_method_file']
method = ['/cos','/euc','/manha']


#Deal Result file in article set and article_stop_word
for up in folder_up:
    for stock_name in stock:   
        for intro in intro_or_not:
            for add_folder in add_method_folder:
                for model_method in method:
                    mkdir(f'{up}{stock_name}{intro}{add_folder}{model_method}')



for up in folder_up:
    for stock_name in stock:   
        for intro in intro_or_not:
            mkdir(f'{up}{stock_name}{intro}/model/add_method_model')


os.makedirs('Word_Embedding_model')


#Deal Test result folder
for stock_name in stock:
    mkdir(f'test_result/{stock_name}TW')