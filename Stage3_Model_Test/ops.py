"""Helper functions.

@author Zhenye Na 05/21/2018

"""


# from tqdm import tqdm
# import matplotlib.pyplot as plt

import numpy as np
import pandas as pd


# import matplotlib
# matplotlib.use('Agg')


def read_data(input_path, debug=True):
    """Read nasdaq stocks data.

    Args:
        input_path (str): directory to nasdaq dataset.

    Returns:
        X (np.ndarray): features.
        y (np.ndarray): ground truth.

    """
    df = pd.read_excel(input_path)
    df_no_date = df.drop(["Close",'Date'], axis=1)
    df_date = df['Date'].values
    X = df_no_date.values
    y = df['Close'].values
    
    return X, y,df_date

# def train_val_test_split(X, y, is_Val ,trade, trend):
    
    
#     # Train set
#     X_train = X[:243, :]
#     y_train = y[:243]
#     trade_train = trade[:243]
#     trend_train = trend[:243]
#     # Test set
#     X_test = X[243:, :] 
#     y_test = y[243:]
#     trade_test = trade[243:] 
#     trend_test = trend[243:]

#     # Val set
#     if is_Val:
#         X_val = X[243:250, :]
#         y_val = y[243:250]
#         trade_val = trade[243:250]
#         trend_val = trend[243:250]
#     else:
#         X_val = np.zeros_like(X_test)
#         y_val = np.zeros_like(y_test)
#         trade_val = np.zeros_like(trade_test)
#         trend_val = np.zeros_like(trend_test)

#     return X_train, y_train, X_test, y_test, X_val, y_val,  trade_train, trend_train, trade_test, trend_test, trade_val, trend_val