# -*- coding: utf-8 -*-
"""rocket_LSTM.ipynb

*Import* *Libraries*
"""

from keras.models import Sequential, Model
from keras.layers import Flatten, Dense, Input
from keras import regularizers
from sklearn import preprocessing
from keras.layers import LSTM
from keras import callbacks
from keras.optimizers import Adam
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""Load test and training data"""

## train data is collected after the pitch deflection is applied on the system
#  during 5 seconds of period
# columns("vtot,aoa,q,def")
# last colum is the value of the target variable  =  pitch deflection (deg)
x_data_train = pd.read_csv("FINAL_all_data_.csv", header=None)# (num_sim,time_step,n_features)(100,500,4)

# Data Properties
num_sim_train = 100
num_sim_test = 20
input_features = 3
output_features = 1
sample_train = 200
x_data_train.values.shape

## Preprocessing the data
x_data_train_normal = preprocessing.MinMaxScaler().fit_transform(x_data_train.values[:,1:4])#(19999, 5)
print('x_data_train_normal',x_data_train_normal.shape) # (20000,4)
y_data_train_normal = preprocessing.MinMaxScaler().fit_transform(x_data_train.values[:,4].reshape(-1,1))
print('y_data_train_normal',y_data_train_normal.shape)# (20000,1)

## Reshape the data
x_data_3d = x_data_train_normal.reshape(num_sim_train,sample_train,input_features)
y_data_3d = y_data_train_normal.reshape(num_sim_train,sample_train,output_features)
print('x_data_3d',x_data_3d.shape) # (100, 200, 3)
print('y_data_3d',y_data_3d.shape) # (100, 200, 1)
x_data_3d

from google.colab import drive
drive.mount('/content/drive')

"""Data Generator for LSTM network"""

lookback = 20
number_points = 200
def data_set(x,y,lookback,num_sim_train,number_points):
  count = 0
  x_batch = np.empty([30000,lookback,3])
  y_batch = np.empty([30000,1])

  for num_sim in range(num_sim_train):
     for  i in range(number_points - lookback):
        x_batch[count,:,0:3] =  x[num_sim,i:i+lookback,:].reshape(1,lookback,3)
        y_batch[count,:] = y[num_sim,i + lookback,:]
        count+=1

  return x_batch[0:count,:,:], y_batch[0:count,:]

"""Batch Generator"""

lookback = 20
x_batch, y_batch = data_set(x_data_3d,y_data_3d,lookback,num_sim_train,number_points)
x_batch.shape
#y_batch.shape

"""Append Data"""

x_batch = np.concatenate((x_batch),axis = 0)
y_batch = np.concatenate((y_batch),axis=0)
print('x_batch shape:',x_batch.shape )
print('y_batch shape:',y_batch.shape )

"""Adjust the traning and test data together"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train,y_test = train_test_split(x_batch,y_batch,
                                                   test_size = 0.05,
                                                   shuffle = True,
                                                   random_state = 42)

encoder_input = Input(shape=(lookback, 3), name='encoder_input')
encoded_1     = LSTM(64,  return_sequences  = True,   name = 'LSTM1')(encoder_input)
encoded_2     = LSTM(32,  return_sequences  = False,   name = 'LSTM2')(encoded_1)
dense1 = Dense(16,activation = 'relu', name= 'dense1')(encoded_2)
out1 = Dense(1, activation='relu', name= 'out1')(dense1)

modelLSTM = Model(encoder_input,[out1])
optimizer = Adam(lr=0.01)
modelLSTM.compile(optimizer = optimizer, loss = 'mse')

EarylStop = callbacks.EarlyStopping(monitor='val_loss', min_delta=0,patience=30, verbose=0,mode = 'auto')
history = modelLSTM.fit(x_train,y_train,
                        epochs = 100,
                        batch_size = 64,
                        validation_split = 0.25,
                        callbacks = [ EarylStop])

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Total Loss')
plt.ylabel('mse loss')
plt.xlabel('epoch')
plt.legend(['Train','Test'])
plt.show()

x_predict = x_data_train.values[100,1:4]
x_predict  =  x_predict.reshape(3,1)
x_train
X = x_data_3d[99,0:20,:].reshape(1,20,3)
X.shape
out_predict = modelLSTM.predict(x_test[0:10,:,:])
y_test[0:10]
print(out_predict)

out_predict = modelLSTM.predict(x_test[0:10,:,:])
print(y_test[0:10])
