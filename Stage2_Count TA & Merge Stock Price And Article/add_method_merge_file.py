#2019/09/16 Arleigh Chang

import pandas as pd
import numpy as np
import time


#Function for getting sum of each day word emb
def sum_of_each_day_vector(news_public_day , df_vector):
    Each_date_vector = []
    Each_date =[]
    for i in range(len(news_public_day)):
        if i==0:
            vector_sum = np.zeros(500)
            vector_sum = vector_sum+df_vector[i]
        elif news_public_day[i] == news_public_day[i-1]:
            vector_sum = vector_sum+df_vector[i]
        elif news_public_day[i] != news_public_day[i-1]:
            Each_date.append(news_public_day[i-1])
            Each_date_vector.append(vector_sum)
            vector_sum = np.zeros(500)
            vector_sum = vector_sum+df_vector[i]
        elif news_public_day[i] != news_public_day[i-1] and news_public_day[i] != news_public_day[i-2] :
            print('Unknown Error')
            exit()
    return Each_date_vector,Each_date


#Function for normalize price data day format
def replace_date(price_day):
    replace_price_date = []
    for i in price_day:
        replace_price_date.append(i.replace('-','/'))
    return replace_price_date

count_per =  ['100','75','50','25'] 
count_way = ['euc','manha','cos']
count_model = ['fastText','word2vec']
folder = ['article set','article_stop_word']
com_list = ['中華電信','鴻海','兆豐金','仁寶','橘子'] 
com_list_num = ['2412','2317','2886','2324','6180']

#Function for news public day not in trading day(like holiday),add it to the last trading day for next trading day prediciton.
for fo in folder:
    for com in range(len(com_list)):
        for model in count_model:
            for way in count_way:
                for per in count_per:
                #Read Excel - stock price and word emb file
                    price_data  = pd.read_csv(f'../{fo}/All_File/{com_list_num[com]}_ta.TW.csv')
                    word_emb_data = pd.read_excel(f'../{fo}/All_File/{com_list_num[com]}TW/{way}/{way}{per}%_{model}_stock_{com_list[com]}.xlsx')
                    
                    print('Start merge file:{0} / {1} / {2}'.format(model,way,per))
                    price_data = price_data.loc[:, ~price_data.columns.str.contains('^Unnamed')]
                    #Deal with word emb file from datafrem to numpy for operation
                    df_vector = word_emb_data.drop(['內容'],axis = 1)
                    df_vector = df_vector.drop(['時間'],axis = 1)
                    df_vector = df_vector.loc[:, ~df_vector.columns.str.contains('^Unnamed')]
                    df_vector = df_vector.values

                    #Get Stock Price Date and word emb file date for operation
                    x_date = price_data['Date'].tolist()
                    y_date = word_emb_data['時間'].tolist()

                    replace_price_date = replace_date(x_date)
                    Each_date_vector , Each_date = sum_of_each_day_vector(y_date , df_vector)
                    Each_date_vector , Each_date = list(Each_date_vector),list(Each_date)
                    # Merge file + add  no trading day to last trading day + 
                    columns_vec_name = []
                    for x in range(500):
                        columns_vec_name.append('vector{}'.format(x))

                    pd_word_emb = pd.DataFrame(Each_date_vector , columns = columns_vec_name)
                    pd_word_emb['Date'] = Each_date
                    price_data['Date'] = replace_price_date

                    pd_merge = pd.merge(price_data,pd_word_emb, on=['Date'],how='outer')
                    pd_merge['Date'] = pd.to_datetime(pd_merge['Date'])

                    pd_merge.sort_values('Date', inplace=True)


                    pd_merge_count_date = pd_merge['Date'].tolist()

                    pd_merge_use = pd_merge.drop(['Date'],axis = 1)
                    df_value= pd_merge_use.values

                    all_columns_name = list(pd_merge_use.columns) 

                    final_deal = []
                    final_date = []
                    continue_control = []

                    #四個狀況 : 


                    for i in range(len(pd_merge_count_date)):

                        if i >=len(pd_merge_count_date)-1 :
                            break

                        elif np.isnan(df_value[i][0]) == True and np.isnan(df_value[i+1][0]) == True:  # --> 今天沒開市，明天也沒開市
                            continue_control.append('No trade')
                        
                    
                        elif np.isnan(df_value[i][0]) == False and np.isnan(df_value[i+1][0]) == False: #1. --> 今明天皆有交易,pass
                            final_deal.append(df_value[i])
                            final_date.append(pd_merge_count_date[i])
                            continue_control.clear()

                    
                        elif np.isnan(df_value[i][0]) == False and np.isnan(df_value[i+1][0]) == True: #預計明天休市，今天先pass
                            continue

                        elif np.isnan(df_value[i][0]) == True and np.isnan(df_value[i+1][0]) == False:  #今天沒開市，但明天有開了
                            continue_control.append('No trade')
                            df_value_add = np.zeros(564)
                            for x in range(len(continue_control)):
                                where_are_nan_sun = np.isnan(df_value[i-x]) 
                                df_value[i-x][where_are_nan_sun] = 0
                                df_value_add+=df_value[i-x]

                                
                            df_value_merge = df_value[i-len(continue_control)] + df_value_add
                            final_deal.append(df_value_merge)
                            final_date.append(pd_merge_count_date[i-len(continue_control)])
                            continue_control.clear()
                        
                        
                        else:  
                            print('有無考慮到的情況，立即停止，錯誤日期:',pd_merge_count_date[i])
                            exit()
                    
                    final_merge_file = pd.DataFrame(final_deal,columns = all_columns_name)

                    final_merge_file['Date'] = final_date
                    final_merge_file[all_columns_name] = final_deal
                    final_merge_file.to_excel(f'../{fo}/{com_list_num[com]}Final_Result/add_method_file/{way}/{way}{per}_{model}_final{com_list[com]}.xlsx',index=False)


