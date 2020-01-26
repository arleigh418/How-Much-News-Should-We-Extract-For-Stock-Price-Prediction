import pandas as pd
from ta import *
folder = ['article set','article_stop_word']
#1.Read file and use ta fundtion
for fo in folder: 
    df = pd.read_csv(f'../{fo}/All_File/2412.TW.csv', sep=',')
    df = df.dropna(how='any')
    df = add_all_ta_features(df, "Open", "High", "Low", "Close", "Volume", fillna=True)

    #2.Remove unnane column and store file
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df.to_csv(f'../{fo}/All_File/2412_ta.TW.csv')