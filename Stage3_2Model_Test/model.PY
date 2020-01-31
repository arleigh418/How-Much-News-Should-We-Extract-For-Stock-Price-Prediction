import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
import os
import matplotlib
import pandas as pd


import matplotlib.pyplot as plt



def count_values(truth,pred):
    count_avg = 0
    
    assert len(truth)==len(pred)
    for x in range(len(truth)):
        count_avg+=abs(truth[x]-pred[x])
    return count_avg/len(truth)



def MinMaxScaler(data):
    data = np.array(data)
    numerator = data - np.min(data, 0)
    denominator = np.max(data, 0) - np.min(data, 0)
    # noise term prevents the zero division
    return numerator / (denominator + 1e-7)

class LSTM(nn.Module):

    def __init__(self, num_classes, input_size, hidden_size, num_layers):
        super(LSTM, self).__init__()
        self.num_classes = num_classes
        self.num_layers = num_layers
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.seq_length = seq_length
        # Set parameters for RNN block
        # Note: batch_first=False by default.
        # When true, inputs are (batch_size, sequence_length, input_dimension)
        # instead of (sequence_length, batch_size, input_dimension)
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size,
                            num_layers=num_layers, batch_first=True)
        # Fully connected layer
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        # Initialize hidden and cell states
        h_0 = Variable(torch.zeros(
            self.num_layers, x.size(0), self.hidden_size))
        c_0 = Variable(torch.zeros(
            self.num_layers, x.size(0), self.hidden_size))

        # Propagate input through LSTM
        _, (h_out, _) = self.lstm(x, (h_0, c_0))
        h_out = h_out.view(-1, self.hidden_size)
        out = self.fc(h_out)
        return out
'''
    def inint_state(self,h,c):
        return torch.zero_(Variable(h)) , torch.zero_(Variable(c))
'''
# train Parameters
learning_rate = 0.01
num_epochs = 5000
input_size = 563
hidden_size = 128
num_classes = 1
timesteps = seq_length = 7
num_layers = 1  # number of layers in RNN

# # Open, High, Low, Volume, Close

count_way = ['euc','cos','manha']
count_per = ['100','75','50','25']
count_model = ['fastText','word2vec']
folder = ['article_stop_word','article set'] #article_stop_word
stock = ['2412','2317','2886','2324','6180']
stock_name = ['中華電信','鴻海','兆豐金','仁寶','橘子'] 

# for st in range(len(stock)):
#     for fo in folder:
#         for way in count_way:
#             for per in count_per:
#                 for model_use in count_model:
#                     data= pd.read_excel(f'../{fo}/{stock[st]}Final_Result_intro/add_method_file/{way}/{way}{per}_{model_use}_final{stock_name[st]}.xlsx')
#                     df_no_date = data.drop(["Close",'Date'], axis=1)

#                     x = df_no_date.values
#                     y = data['Close'].values 
#                     # x = MinMaxScaler(x)
#                     # y = MinMaxScaler(y)
                    
#                     # build a dataset
#                     dataX = []
#                     dataY = []
#                     for i in range(0, len(y) - seq_length):
#                         _x = x[i:i + seq_length]
#                         _y = y[i + seq_length]  # Next close price
#                         # print(_x, "->", _y)
#                         dataX.append(_x)
#                         dataY.append(_y)

#                     # train/test split
                    
#                     train_size = int(len(dataY) * 0.7)
#                     dev_size = int((len(dataY) - train_size)*0.5)
#                     test_size = int(len(dataY) - train_size - dev_size)
                    
#                     trainX = torch.Tensor(np.array(dataX[0:train_size]))
#                     trainX = Variable(trainX)

#                     devX = torch.Tensor(np.array(dataX[train_size:train_size+dev_size]))
#                     devX = Variable(devX)

#                     testX = torch.Tensor(np.array(dataX[train_size+dev_size:len(dataX)]))
#                     testX = Variable(testX)


#                     trainY = torch.Tensor(np.array(dataY[0:train_size]))
#                     trainY = Variable(trainY)

#                     devY = torch.Tensor(np.array(dataY[train_size:train_size+dev_size]))
#                     devY = Variable(devY)

#                     testY = torch.Tensor(np.array(dataY[train_size+dev_size:len(dataX)]))
#                     testY = Variable(testY)


#                     # Instantiate RNN model
#                     lstm = LSTM(num_classes, input_size, hidden_size, num_layers)
      
#                     # Set loss and optimizer function
#                     criterion = torch.nn.MSELoss()    # mean-squared error for regression
#                     optimizer = torch.optim.Adam(lstm.parameters(), lr=learning_rate)

#                     best_dev_values = 999999
#                     config = 0
#                     # Train the model
#                     for epoch in range(num_epochs):
#                         outputs = lstm(trainX)
#                         # print(trainX.size())
#                         optimizer.zero_grad()
#                         # obtain the loss function
#                         loss = criterion(outputs, trainY)
#                         loss.backward()
#                         optimizer.step()
#                         if epoch % 100 == 0 and epoch>=100:
        
#                             print("Epoch: %d, loss: %1.5f" % (epoch, loss.item()/len(trainY)))
#                         dev = lstm(devX)
                            
#                         dev_values = count_values(devY,dev)

#                         if dev_values<best_dev_values:
#                             config = 0
#                             lstm.eval()
#                             best_dev_values=dev_values
#                             torch.save(lstm.state_dict(), f'../{fo}/{stock[st]}Final_Result_intro/model/add_method_model/{way}{per}{model_use}model_add.pkl')
#                             print('Saving model , Best model : %2f' % best_dev_values)
#                         else:
#                             config+=1
#                             print('Model no update times:',config)

#                         if config > 30:
#                             break

#                     print("Learning finished!",stock_name[st],fo,way,per,model_use)




# # Test the model
# # lstm.eval()
# # test_predict = lstm(testX)

# # # Plot predictions
# # test_predict = test_predict.data.numpy()
# # testY = testY.data.numpy()
# # plt.plot(testY)
# # plt.plot(test_predict)
# # plt.title('2317 Stock Prediction Result - FastText Method')
# # plt.xlabel("Time Period")
# # plt.ylabel("Stock Price")
# # plt.show()
