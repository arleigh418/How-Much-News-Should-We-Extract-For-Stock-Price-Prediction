"""
Reference  https://github.com/Zhenye-Na/DA-RNN
"""
# -*- coding: utf-8 -*-


#training data = 2017/06/14 ~ 2019/02/21 415 data
#test data = 2019/02/22 ~ 2019/07/25

from ops import *
from torch.autograd import Variable

import torch
from torch import cuda
# torch.cuda.is_available()
import numpy as np
from torch import nn
from torch import optim
import torch.nn.functional as F
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from model import LSTM


def count_values(truth,pred):
    count_avg = 0
    assert len(truth)==len(pred)
    for x in range(len(truth)):
        count_avg+=abs(truth[x]-pred[x])
    return count_avg/len(truth)
    

learning_rate = 0.01
num_epochs = 5000
input_size = 563
hidden_size = 128
num_classes = 1
timesteps = seq_length = 7
num_layers = 1  # number of layers in RNN


# euc_result_fasttext_avg= []
# cos_result_fasttext_avg =[]
# manha_result_fasttext_avg = []

# euc_result_word2vec_avg= []
# cos_result_word2vec_avg =[]
# manha_result_word2vec_avg = []

count_per = ['100','75','50','25'] 
count_way = ['cos','euc','manha']
count_model = ['fastText','word2vec']
count_method = ['add'] #'avg',
count_com = ['6180','2886','2317','2324','2412'] #
count_name = ['橘子','兆豐金','鴻海','仁寶','中華電信'] #,
count_word = ['article_stop_word','article set']


for word in count_word:
    for com in range(len(count_name)):
        record_text= []
        test_result = []
        euc_result_fasttext_add = []
        cos_result_fasttext_add =[]
        manha_result_fasttext_add = []

        euc_result_word2vec_add = []
        cos_result_word2vec_add =[]
        manha_result_word2vec_add = []
        for method in count_method:
            for model_use in count_model:
                for way in count_way:
                    for per in count_per:
                        try:
                            print('Infomation :',word,' | ',com,' | ',method,' | ',model_use,' | ',way,' | ',per)
                            data= pd.read_excel(f"../{word}/{count_com[com]}Final_Result_intro/{method}_method_file/{way}/{way}{per}_{model_use}_final{count_name[com]}.xlsx", debug=False)
                            df_no_date = data.drop(["Close",'Date'], axis=1)
                            x = df_no_date.values
                            y = data['Close'].values 

                            dataX = []
                            dataY = []
                            for i in range(0, len(y) - seq_length):
                                _x = x[i:i + seq_length]
                                _y = y[i + seq_length]  # Next close price
                                dataX.append(_x)
                                dataY.append(_y)

                            train_size = int(len(dataY) * 0.7)
                            dev_size = int((len(dataY) - train_size)*0.5)
                            test_size = int(len(dataY) - train_size - dev_size)


                            testX = torch.Tensor(np.array(dataX[train_size+dev_size:len(dataX)]))
                            testX = Variable(testX)
                            testY = torch.Tensor(np.array(dataY[train_size+dev_size:len(dataX)]))
                            testY = Variable(testY)
                            print(f"../{word}/{count_com[com]}Final_Result_intro/model/{method}_method_model/{way}{per}{model_use}model_{method}.pkl")
                            lstm = LSTM(num_classes, input_size, hidden_size, num_layers)
                                # y_train = model.train()
                            lstm.load_state_dict(torch.load(f"../{word}/{count_com[com]}Final_Result_intro/model/{method}_method_model/{way}{per}{model_use}model_{method}.pkl"))
                            

                            test_predict = lstm(testX)
                            result = count_values(testY,test_predict)
                            
                            record_text.append(f"../{word}/{count_com[com]}Final_Result_intro/model/{method}_method_model/{way}{per}{model_use}model_{method}.pkl")
                            test_result.append(result.item())
                            
                            if way == 'euc' and model_use =='fastText' and method =='add':
                                euc_result_fasttext_add.append(result)
                            elif way == 'cos' and model_use =='fastText' and method =='add':
                                cos_result_fasttext_add.append(result)
                            elif way == 'manha' and model_use =='fastText' and method =='add':
                                manha_result_fasttext_add.append(result)

                            elif way == 'euc' and model_use =='word2vec' and method =='add':
                                euc_result_word2vec_add.append(result)
                            elif way == 'cos' and model_use =='word2vec' and method =='add':
                                cos_result_word2vec_add.append(result)
                            elif way == 'manha' and model_use =='word2vec' and method =='add':
                                manha_result_word2vec_add.append(result)

                            # elif way == 'euc' and model_use =='fastText' and method =='avg':
                            #     euc_result_fasttext_avg.append(result)
                            # elif way == 'cos' and model_use =='fastText' and method =='avg':
                            #     cos_result_fasttext_avg.append(result)
                            # elif way == 'manha' and model_use =='fastText' and method =='avg':
                            #     manha_result_fasttext_avg.append(result)

                            # elif way == 'euc' and model_use =='word2vec' and method =='avg':
                            #     euc_result_word2vec_avg.append(result)
                            # elif way == 'cos' and model_use =='word2vec' and method =='avg':
                            #     cos_result_word2vec_avg.append(result)
                            # elif way == 'manha' and model_use =='word2vec' and method =='avg':
                            #     manha_result_word2vec_avg.append(result)
                            else:
                                print('Others error')
            
                        except ArithmeticError:
                            print('錯誤，停止')
                            exit()

        storage = pd.DataFrame()
        storage['method'] = record_text
        storage['result'] = test_result
        storage.to_excel(f'{word}_{count_com[com]}Record_intro.xlsx')
                        
        fig3 = plt.figure()
        plt.title(u'{0}.TW - Model Predict Result({1})_Company Intorduction'.format(count_com[com],word))
        plt.xlabel(u'Percentage of News Data Extraction / Using Model')
        plt.ylabel(u"Average Error of Predict Result")
        plt.grid(True)
        
        plt.plot(count_per,euc_result_fasttext_add,'g-',label = 'euc_result_f_add')
        plt.plot(count_per,cos_result_fasttext_add, 'r-',label = 'cos_result_f_add')
        plt.plot(count_per,manha_result_fasttext_add, 'b',label = 'manha_result_f_add')

        plt.plot(count_per,euc_result_word2vec_add,'tan',label = 'euc_result_w_add')
        plt.plot(count_per,cos_result_word2vec_add, 'm',label = 'cos_result_w_add')
        plt.plot(count_per,manha_result_word2vec_add, 'aqua',label = 'manha_result_w_add')

        # plt.plot(count_per,euc_result_fasttext_avg,'navy',label = 'euc_result_f_avg')
        # plt.plot(count_per,cos_result_fasttext_avg, 'black',label = 'cos_result_f_avg')
        # plt.plot(count_per,manha_result_fasttext_avg, 'brown',label = 'manha_result_f_avg')

        # plt.plot(count_per,euc_result_word2vec_avg,'cyan',label = 'euc_result_w_avg')
        # plt.plot(count_per,cos_result_word2vec_avg, 'crimson',label = 'cos_result_w_avg')
        # plt.plot(count_per,manha_result_word2vec_avg, 'coral',label = 'manha_result_w_avg')

        plt.legend(loc='best')
        plt.savefig(f"../test_result/{count_com[com]}TW/{count_com[com]}lstm_{word}_intro.png")
        plt.close(fig3)


