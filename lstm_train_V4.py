# -*- coding: utf-8 -*-
"""

@author: cnsyk
"""

"""Python module demonstrates passing MATLAB types to Python functions"""
import tensorflow as tf
#import scipy.io as sio
import numpy 
#import matlab
#import sys
import hdf5storage
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.backend import clear_session

clear_session()

inputFeatures  = 5
outputFeatures = 2
lookback       = 20
#numberManeuver =480
numberPoints   =301

# Add path of NN's data to system search path
nnPath = "C:/Users/cnsyk/.spyder-py3/LSTM_training/"
dataPathInput = "C:/Users/cnsyk/OneDrive/Desktop/FINAL_rocket_all_states.mat"

sample   = hdf5storage.loadmat(dataPathInput)


all_data = sample['FINAL_rocket_all_states']
X_data = all_data[:,0:5]

Y_data = all_data[:,5:7]

min_max_scalerInput     = MinMaxScaler(feature_range=(0,1))
min_max_scalerOutput    = MinMaxScaler(feature_range=(0,1))

norm_X =  min_max_scalerInput.fit_transform(X_data)

X_dataNormal  = min_max_scalerInput.fit_transform(X_data).reshape(-1, numberPoints, inputFeatures)
# Y_dataNormal  = min_max_scalerOutput.fit_transform(Y_data).reshape(-1, numberPoints, outputFeatures)
# Y_dataNormal  = min_max_scalerOutput.fit_transform(Y_data).reshape(1,-1)
#Y_dataNormal = min_max_scalerOutput.fit_transform(Y_data.reshape(-1,1))                
Y_dataNormal = min_max_scalerOutput.fit_transform(Y_data)    

model_file = nnPath + "modelLSTM_main.h7"

model      = tf.keras.models.load_model(model_file)

def run(stateHistory1):

    stateHistory = numpy.array(stateHistory1)
    X_data_normal = min_max_scalerInput.transform(stateHistory)
    X_data_normal = X_data_normal.reshape(1,lookback,inputFeatures)

    prediction_normal = model.predict(X_data_normal)
    
    prediction_normal_rs = numpy.array(prediction_normal).reshape(1,outputFeatures)
    prediction = min_max_scalerOutput.inverse_transform(prediction_normal_rs)#numpy.squeeze(prediction_normal))
    a = prediction[0,0]
    #b = prediction[0,1]
    #prediction_mat = matlab.double(prediction.tolist())
    return a

def runv2(stateHistory1):

    # stateHistory= numpy.zeros((50,17))
    stateHistory = numpy.array(stateHistory1)
    X_data_normal = min_max_scalerInput.transform(stateHistory)

    X_data_normal = X_data_normal.reshape(1,lookback,inputFeatures)

    prediction_normal = model.predict(X_data_normal)
    
    prediction_normal_rs = numpy.array(prediction_normal).reshape(1,outputFeatures)
    prediction = min_max_scalerOutput.inverse_transform(prediction_normal_rs)#numpy.squeeze(prediction_normal))
    #a = prediction[0,0]
    b = prediction[0,1]
    #prediction_mat = matlab.double(prediction.tolist())
    return b
