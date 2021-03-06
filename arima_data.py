# -*- coding: utf-8 -*-
"""arima_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/alam2018/ml_prediction_m1/blob/master/arima_data.ipynb
"""

#from google.colab import drive
#drive.mount('/content/drive')

#Define if the simulation is for uRLLC or eMBB slice
web_traffic = True
m2m = False
m2m_model1 = False

# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
#from google.colab import files
import pandas as pd

# Importing the training set
if web_traffic == True:
    eMBB = True
    if eMBB == True:
#        dataset_train = pd.read_csv('/home/mdaa/traffic_prediction/dataSet/web_traffic/train/traffic_simulation.csv', sep=';')
         dataset_train = pd.read_csv('/home/mdaa/traffic_prediction/dataSet/web_traffic2/train/traffic_simulation_100usr.csv', sep=';')
    else:
        dataset_train = pd.read_csv('/content/drive/My Drive/Colab Notebooks/traffic_prediction/data_URLLC/traffic_simulation.csv', sep=';')
        
if m2m == True:
    if m2m_model1 == True:
        dataset_train = pd.read_csv('/home/mdaa/traffic_prediction/dataSet/m2m_traffic/model_1/traffic_simulation_3000_1800usr.csv', sep=';')
    else:
        dataset_train = pd.read_csv('/home/mdaa/traffic_prediction/dataSet/m2m_traffic/model_2/traffic_simulation_3000_1800usr.csv', sep=';')

#Insert a new column containing the 'byte' value converted to 'MB' for training
dataset_train['TotalData_Mb'] = dataset_train.iloc[:, 2].values / 1000000

training_set = dataset_train.iloc[:, 4].values
training_set = training_set.reshape(-1,1)

#Prepare training and test dataset
prediction_size = 60
X = training_set
#train_size = int (round(len(X) * 0.7))
if web_traffic == True:
    train_size = 7000
if m2m == True:
    train_size = 2000
validation_start = train_size
validation_end = train_size + prediction_size
test_size = train_size + prediction_size

train = X[0:train_size]
#test = X[train_size:test_size] 
test = X[validation_start:validation_end]
predictions = []

#Prepare ARIMA model
from statsmodels.tsa.arima_model import ARIMA

import itertools
p=d=q=range(0,10)
pdq = list(itertools.product(p,d,q))
#temp_pdq = [(0, 0, 0)]
#temp_pdq = [(5, 1, 3)]
#print (pdq)

import warnings
warnings.filterwarnings('ignore')
temp_aic = 1000000000000

#for param in pdq:
#    try:
#        model_arima = ARIMA(train,order=param)
#        model_arima_fit = model_arima.fit()
#        print(param,model_arima_fit.aic)
#        if model_arima_fit.aic > 0:
#            if model_arima_fit.aic < temp_aic:
#                temp_aic = model_arima_fit.aic
#                temp_pdq = param
#    except:
#        continue

for param in pdq:
    try:
        model_arima = ARIMA(train,order=param)
        model_arima_fit = model_arima.fit()
        print(param,model_arima_fit.aic)
        if model_arima_fit.aic < temp_aic:
            temp_aic = model_arima_fit.aic
            temp_pdq = param
    except:
        continue

print (temp_pdq, temp_aic)

#p,d,q  p = periods taken for autoregressive model
#d -> Integrated order, difference
# q periods in moving average model
#model_arima = ARIMA(train,order=(5, 1, 3))
model_arima = ARIMA(train,order=temp_pdq)
model_arima_fit = model_arima.fit(disp=0)
#print(model_arima_fit.aic)

predictions= model_arima_fit.forecast(steps=prediction_size)[0]

#print (predictions)

# Visualising the results
if web_traffic == True:
    plt.plot(test, color = 'red', label = 'Validaation Traffic')
    plt.plot(predictions, color = 'blue', label = 'Predicted traffic')
    plt.ylim (44,50)
    plt.title('Traffic Prediction (ARIMA)')
    plt.xlabel('Time Index (s)')
    plt.ylabel('Data (MBps)')
    plt.legend(loc='best', prop={'size': 6})
    plt.savefig('arima_valData_data.png',bbox_inches="tight", pad_inches=0, dpi=300)
    plt.show()
elif m2m == True:
#    init_val = 0;
#    x_val = []
#    for loop in range (prediction_size):
#        x_val.append(init_val)
#        init_val += 0.1
#    plt.plot(x_val, test, color = 'red', label = 'Validaation Traffic')
#    plt.plot(x_val, predictions, color = 'blue', label = 'Predicted traffic')
    plt.plot(test, color = 'red', label = 'Validation Traffic')
    plt.plot(predictions, color = 'blue', label = 'Predicted traffic')
    plt.ylim (0,5)
    plt.title('Traffic Prediction (ARIMA)')
    plt.xlabel('Time Index (s)')
    plt.ylabel('Data (MBps)')
    plt.legend(loc='best', prop={'size': 6})
    plt.savefig('arima_valData_data.png',bbox_inches="tight", pad_inches=0, dpi=300)
    plt.show()
    
#plt.savefig('arima_valData_data.png',bbox_inches="tight", pad_inches=0, dpi=300)
#plt.show()

from sklearn.metrics import mean_squared_error

from math import sqrt

mse = mean_squared_error(test, predictions)

rmse = sqrt(mse)

print('RMSE: %f' % rmse)


#print (predictions.shape)
#X_test = np.reshape(test, (np.product(test.shape),))
#
#df = pd.DataFrame(list(zip(X_test, predictions)),
#              columns=['Test Packet Size (MB)','Predicted Packet Size (MB)'])

# Importing the test dataset
if web_traffic == True:
    eMBB = True
    if eMBB == True:
#        dataset_test = pd.read_csv('/home/mdaa/traffic_prediction/dataSet/web_traffic/test/traffic_simulation.csv', sep=';')
        dataset_test = pd.read_csv('/home/mdaa/traffic_prediction/dataSet/web_traffic2/test/traffic_simulation_100usr.csv', sep=';')
    else:
        dataset_test = pd.read_csv('/content/drive/My Drive/Colab Notebooks/traffic_prediction/data_URLLC/traffic_simulation.csv', sep=';')
        
if m2m == True:
#    m2m_model1 = False
    if m2m_model1 == True:
        dataset_test = pd.read_csv('/home/mdaa/traffic_prediction/dataSet/m2m_traffic/model1_test/traffic_simulation_3000_1800usr.csv', sep=';')
    else:
        dataset_test = pd.read_csv('/home/mdaa/traffic_prediction/dataSet/m2m_traffic/model2_test/traffic_simulation_3000_1800usr.csv', sep=';')

        
#Insert a new column containing the 'byte' value converted to 'MB' for training
dataset_test['TotalData_Mb'] = dataset_test.iloc[:, 2].values / 1000000

test_set = dataset_test.iloc[:, 4].values
test_set = test_set.reshape(-1,1)

test_data_train = test_set[0:train_size]
test_data_test = test_set[validation_start:validation_end]
predictions_test = []
        

model_arima = ARIMA(test_data_train,order=temp_pdq)
model_arima_fit = model_arima.fit(disp=0)

predictions_test= model_arima_fit.forecast(steps=prediction_size)[0]

# Visualising the results
if web_traffic == True:
    plt.plot(test_data_test, color = 'red', label = 'Test Traffic')
    plt.plot(predictions_test, color = 'blue', label = 'Predicted traffic')
    plt.ylim (44,50)
    plt.title('Traffic Prediction (ARIMA)')
    plt.xlabel('Time Index (s)')
    plt.ylabel('Data (MBps)')
    plt.legend(loc='best', prop={'size': 6})
    plt.savefig('arima_valData_data.png',bbox_inches="tight", pad_inches=0, dpi=300)
    plt.show()
elif m2m == True:
#    init_val = 0;
#    x_val = []
#    for loop in range (prediction_size):
#        x_val.append(init_val)
#        init_val += 0.1
#    plt.plot(x_val, test, color = 'red', label = 'Test Traffic')
#    plt.plot(x_val, predictions, color = 'blue', label = 'Predicted traffic')
    plt.plot(test_data_test, color = 'red', label = 'Test Traffic')
    plt.plot(predictions_test, color = 'blue', label = 'Predicted traffic')
    plt.ylim (0,6)
    plt.title('Traffic Prediction (ARIMA)')
    plt.xlabel('Time Index (s)')
    plt.ylabel('Data (MBps)')
    plt.legend(loc='best', prop={'size': 6})
    plt.savefig('arima_testData_data.png',bbox_inches="tight", pad_inches=0, dpi=300)
    plt.show()
    
mse = mean_squared_error(test_data_test, predictions_test)

rmse = sqrt(mse)

print('RMSE test data: %f' % rmse)

#print (predictions.shape)
X_val = np.reshape(test, (np.product(test.shape),))
X_test = np.reshape(test_data_test, (np.product(test_data_test.shape),))

df = pd.DataFrame(list(zip(X_val, predictions, X_test, predictions_test)),
              columns=['Validation Data (MB)','Predicted data (MB)', 'Test data (MB)', 'Predicted data (MB)'])
df.to_csv("arima_result.csv", index = None, header=True)