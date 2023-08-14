# test.py
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

inputFeatures  = 4
outputFeatures = 1
lookback       = 20
#numberManeuver =480
numberPoints   =301

# Add path of NN's data to system search path
nnPath = "C:/Users/cnsyk/.spyder-py3/saved_NNs/"

#dataPathInput = "C:/TAI_IL/aircraft-models/LSTM_NDI_v1/ndi-f16-model/whole-model/Dagger/Split-S_Dagger_iter_0_to_1.mat"

# dataPathInput = "C:/Users/cnsyk/OneDrive/Desktop/scitech_last_version/rocket_all_states_V4.mat "
# dataPathInput  = "C:/TAI_IL/LSTM_Models/dataSetAllStatesSplitS1.mat"
dataPathInput = "C:/Users/cnsyk/OneDrive/Desktop/rocket_all_states_V3.mat"

#dataPathInput = "C:/TAI_IL/aircraft-models/LSTM_NDI_v1/ndi-f16-model/whole-model/Dagger/Split-S_Dagger_iter_0_to_3.mat"
#dataSetAllStatesSplitS1.mat"


sample   = hdf5storage.loadmat(dataPathInput)
# b = map(float, X_data[:,1:4])


all_data = sample['rocket_all_states_V3']
X_data = all_data[:,0:4]

Y_data = all_data[:,4]
#Y_data = X_data[:,12:16]

min_max_scalerInput     = MinMaxScaler(feature_range=(0,1))
min_max_scalerOutput    = MinMaxScaler(feature_range=(0,1))

norm_X =  min_max_scalerInput.fit_transform(X_data)

X_dataNormal  = min_max_scalerInput.fit_transform(X_data).reshape(-1, numberPoints, inputFeatures)
# Y_dataNormal  = min_max_scalerOutput.fit_transform(Y_data).reshape(-1, numberPoints, outputFeatures)
# Y_dataNormal  = min_max_scalerOutput.fit_transform(Y_data).reshape(1,-1)
Y_dataNormal = min_max_scalerOutput.fit_transform(Y_data.reshape(-1,1))                

model_file = nnPath + "modelLSTM_main.h5"
#"SplitS-AutoEncoder-V1-033-tune2-11-Subat-2-17_iter2.h5"

#"SplitS-AutoEncoder-V1-tune2-7-Subat-2-34_iter1.h5"
#"SplitS-AutoEncoder-V1-033-tune2-11-Subat-2-17_iter2.h5"
#"SplitS-AutoEncoder-V1-tune2-7-Subat-2-34.h5"
#"SplitS-Dagger-V2-5-Subat-12-22.h5"
#"SplitS-Dagger-V2-3-Subat-11-8.h5"
#"SplitS-Dagger-V1-2-Subat-22-1.h5"
#"modelV6actuators-2Subat-21-20_dagger_iter_1.h5" 
#modelV6actuators-17Ocak-23-32.h5

model      = tf.keras.models.load_model(model_file)

def run(stateHistory1):

    # stateHistory= numpy.zeros((50,17))
    stateHistory = numpy.array(stateHistory1)
    X_data_normal = min_max_scalerInput.transform(stateHistory)

    X_data_normal = X_data_normal.reshape(1,lookback,inputFeatures)

    prediction_normal = model.predict(X_data_normal)
    #♥prediction_normal = prediction_normal[0:3] #"SplitS-AutoEncoder-V1-tune2-7-Subat-2-34.h5" Autoencoder modelinde 4 çıktı var
    #print(prediction_normal)
   
    prediction_normal_rs = numpy.array(prediction_normal).reshape(1,outputFeatures)
    prediction = min_max_scalerOutput.inverse_transform(prediction_normal_rs)#numpy.squeeze(prediction_normal))
    a = prediction[0,0]
    #prediction_mat = matlab.double(prediction.tolist())
    return a

