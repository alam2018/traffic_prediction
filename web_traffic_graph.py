#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:34:26 2020

@author: mdaa
"""

#import matplotlib.pyplot as plt
##import numpy as np
#
#import pandas as pd
#
##data = pd.read_csv('/home/mdaa/eclipse-workspace/slice_resource/user_alloc_20_slice.csv', sep=';', index_col = False)
#lstm_data_valid = pd.read_csv('/home/mdaa/traffic_prediction/result/lstm/web_traffic/data/lstm_data_val.csv', sep=',', index_col = False)
#lstm_data_test = pd.read_csv('/home/mdaa/traffic_prediction/result/lstm/web_traffic/data/lstm_data_test.csv', sep=',', index_col = False)
#arima_data_valid = pd.read_csv('/home/mdaa/traffic_prediction/result/arima/web_traffic/data/new/arima_data.csv', sep=',', index_col = False)
#
#
#
#lstm_valid = []
#lstm_valid_predict = []
#lstm_test = []
#lstm_test_predict = []
#
#arima_valid = []
#arima_valid_predict = []
#
#
#lstm_valid_data = lstm_data_valid.iloc[:,0:1].values
#lstm_valid_predict_data = lstm_data_valid.iloc[:,1:2].values
#lstm_test_data = lstm_data_test.iloc[:,0:1].values
#lstm_test_predict_data = lstm_data_test.iloc[:,1:2].values
#
#
#for lstm_valid_index in range (lstm_data_valid.shape[0]):
#    lstm_valid.append (lstm_valid_data[lstm_valid_index,0])
#    lstm_valid_predict.append (lstm_valid_predict_data[lstm_valid_index,0])
#    
#for lstm_test_index in range (lstm_data_test.shape[0]):
#    lstm_test.append (lstm_test_data[lstm_test_index,0])
#    lstm_test_predict.append (lstm_test_predict_data[lstm_test_index,0])
#       
#
#arima_valid_data = arima_data_valid.iloc[:,0:1].values
#arima_valid_predict_data = arima_data_valid.iloc[:,1:2].values
#
#for arima_valid_index in range (arima_data_valid.shape[0]):
#    arima_valid.append (arima_valid_data[arima_valid_index,0])
#    arima_valid_predict.append (arima_valid_predict_data[arima_valid_index,0])
#    
#plt.plot(lstm_test, color = 'green', label = 'LSTM test data (dataset 1)', marker='+', markersize=2)
#plt.plot(lstm_test_predict, color = 'orange', label = 'LSTM prediction data (dataset 1)', marker='1', markersize=2)
#plt.plot(lstm_valid, color = 'brown', label = 'LSTM test data (dataset 2)', linestyle = '--', marker='x', markersize=2)
#plt.plot(lstm_valid_predict, color = 'red', label = 'LSTM prediction data (dataset 2)', marker='^', markersize=2)
#plt.plot(arima_valid, color = 'blue', label = 'ARIMA test data (dataset 1)', marker='*', markersize=2)
#plt.plot(arima_valid_predict, color = 'yellow', label = 'ARIMA prediction data (dataset 1)', marker='^', markersize=2)
#plt.ylim (42,50)
##plt.title('Traffic Prediction')
#plt.xlabel('Time (s)')
#plt.ylabel('Data Rate (MBps)')
#plt.grid(which='major', linestyle='-', linewidth='0.5', color='gray')
#plt.legend(loc='best', prop={'size': 6})
#plt.savefig('web_comb_result.png',bbox_inches="tight", pad_inches=0.1, dpi=300)
#plt.show()

import numpy as np
import matplotlib.pyplot as plt

lstm_data_valid = np.genfromtxt("/home/mdaa/traffic_prediction/result/lstm/web_traffic/data/lstm_data_val.csv", delimiter=',', encoding='utf8', dtype=float)
lstm_data_test = np.genfromtxt("/home/mdaa/traffic_prediction/result/lstm/web_traffic/data/lstm_data_test.csv", delimiter=',', encoding='utf8', dtype=float)
arima_data_valid = np.genfromtxt("/home/mdaa/traffic_prediction/result/arima/web_traffic/data/new/arima_data.csv", delimiter=',', encoding='utf8', dtype=float)

lstm_valid_data = lstm_data_valid[:,0:1]
lstm_valid_predict_data = lstm_data_valid[:,1:2]
lstm_test_data = lstm_data_test[:,0:1]
lstm_test_predict_data = lstm_data_test[:,1:2]

arima_valid_data = arima_data_valid[:,0:1]
arima_valid_predict_data = arima_data_valid[:,1:2]

plt.plot(lstm_test_data, color = 'green', label = 'LSTM test data (dataset 1)', marker='+', markersize=2)
plt.plot(lstm_test_predict_data, color = 'orange', label = 'LSTM prediction data (dataset 1)', marker='1', markersize=2)
plt.plot(lstm_valid_data, color = 'brown', label = 'LSTM test data (dataset 2)', linestyle = '--', marker='x', markersize=2)
plt.plot(lstm_valid_predict_data, color = 'red', label = 'LSTM prediction data (dataset 2)', marker='^', markersize=2)
plt.plot(arima_valid_data, color = 'blue', label = 'ARIMA test data (dataset 1)', marker='*', markersize=2)
plt.plot(arima_valid_predict_data, color = 'yellow', label = 'ARIMA prediction data (dataset 1)', marker='^', markersize=2)
plt.ylim (42,50)
#plt.title('Traffic Prediction')
plt.xlabel('Time (s)')
plt.ylabel('Data Rate (MBps)')
plt.grid(which='major', linestyle='-', linewidth='0.5', color='gray')
plt.legend(loc='best', prop={'size': 6})
plt.savefig('web_comb_result_new.png',bbox_inches="tight", pad_inches=0.1, dpi=300)
plt.show()

    