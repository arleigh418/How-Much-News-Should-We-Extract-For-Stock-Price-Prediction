# How-Much-News-Should-We-Extract-For-Stock-Price-Prediction
## Please refer project paper : https://github.com/arleigh418/How-Much-News-Should-We-Extract-For-Stock-Price-Prediction/blob/master/Test%20Result%20Report.pdf
# First of all
1. You can refer Test Result Report.pdf, we record in detail how we do it and the results.
2. Please run os_folder_create.py first, it will help you create folder.

# Overview
As this project name, this project plan to answer this question : how much news should we extract for stock price prediction.
This project use finance news and stock price as features, and we convert word to vector,then we conut the relation between target article and each finance news.

# Process Flow
Here provide simple flow to show how we do it, and you can find it in report file.
![image](https://github.com/arleigh418/How-Much-News-Should-We-Extract-For-Stock-Price-Prediction/blob/master/img/flow.png)

# Relation method
You must be confuse: What is relation method?And what is target article? 

As 0verview mention, we convert word to vector, and we count distance in vector space with some algorithms like Manhattan Distance or Euclidean Distance between target article and each finance news.

And what is target article?In this experiment, we define two different scopes for target aritlce(we call it "center"),one is target company name(e.g. 台積電) vector as center, another is target company introduction in Wiki.

# Experiment Setting
Target company: 2412TW、2317TW、2886TW、2324TW、6180TW

Deep Learning model : LSTM

Word Embedding model : word2vec、fastText

Vector Distance: Manhattan Distance、Euclidean Distance、Cosine Similarity

Article Dealing : Just use a stop words dictionary 、 Stop word dictionary+Getting Set for each word.

# Code Description
1. You can run : run_all.py in Stage3_Model_Test and Stage3_2Model_Test, I have arranged how to execute.
2. What is different between Stage3_Model_Test and Stage3_2Model_Test and also other folders? The folders name with 1_2 or 2_2 or 3_2 mean we use target company introduction in wiki as the center, and others like 1_ or 2_ or 3_ mean using target company name as center.
3. In run_all.py , Data Prepare1-4 just need to execute once,no matter how many times you want to run this project(Assuming you haven't changed anything),but Data Prepare5 in run_all.py in Stage3_2Model_Test is not found in Stage3_Model_Test, if you first run the run_all.py in Stage3_Model_Test, then you need to execute Data Prepare5 once when running run_all.py in Stage3_2Model_Test.
4. Folder : test_result store predict line chart.

You can replace others deep learning model like DA-RNN or others you like, and you can also try other distance algorithm like Chebyshev Distance or Hamming Distance.

If you have any qeustions, please contact me for free, and welcome any discussions!
