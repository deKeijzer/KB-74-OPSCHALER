import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import numpy as np
from tqdm import tqdm
import dask.dataframe as dd

from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout, Flatten
from keras.layers.recurrent import LSTM
from keras.layers import Dense, Conv1D, MaxPool2D, Flatten, Dropout, Conv2D, MaxPooling2D, TimeDistributed
from keras.callbacks import EarlyStopping, TensorBoard
from keras.optimizers import Adam, SGD, Nadam
from time import time
from livelossplot import PlotLossesKeras
from keras.layers.advanced_activations import LeakyReLU, PReLU
import tensorflow as tf
from keras.utils.training_utils import multi_gpu_model
from tensorflow.python.client import device_lib
from sklearn.preprocessing import StandardScaler

from keijzer import *

mpl.style.use('default')
#%matplotlib notebook
#%matplotlib inline
sns.set()

# Setup multi GPU usage
num_gpu = setup_multi_gpus()

df = pd.read_csv('//datc//opschaler//combined_gas_smart_weather_dfs//processed/all_dwellings_combined_hour.csv', delimiter='\t', parse_dates=['datetime'])
df = df.set_index(['datetime'])
df = df.dropna()

# Get an hour dataframe
df = resample_df(df, 'H', combine_all_dwellings=True)

# Get all the data out of datetime
# Could also get holiday data: https://stackoverflow.com/questions/29688899/pandas-checking-if-a-date-is-a-holiday-and-assigning-boolean-value
df['hour'] = df.index.hour #create column containing the hour
df['dayofweek'] = df.index.dayofweek
df['season'] = (df.index.month%12 + 3)//3 # Calculates the season (categorical)

df['month'] = df.index.month
#df['week'] = df.index.week
#df['day'] = df.index.day
#df['year'] = df.index.year

df['month_end'] = df.index.is_month_end
df['month_start'] = df.index.is_month_start
df['quarter_end'] = df.index.is_quarter_end
df['quarter_start'] = df.index.is_quarter_start

data = df
#data = data.drop(['eMeter', 'eMeterReturn', 'eMeterLow', 'eMeterLowReturn', 'gasMeter', 'dwelling'], axis=1) # Not needed
data = data.drop(['dwelling'], axis=1) # Not needed
data = data.drop(['WW', 'VV', 'P', 'DR', 'SQ', 'TD', 'T10', 'FX'], axis=1) # Drop weather columns which contain correlated information, keep only one type
#sns.heatmap(data.corr(), annot=True)

#data = data.drop(['ePower', 'ePowerReturn'], axis=1) # Drop if want to predict gasPower
data = data.drop(['ePowerReturn'], axis=1)


# Drop columns with that have a |corr| > 0.1 with T
data = data.drop(['U', 'N', 'Q', 'DD'], axis=1)


#data = data[data['T'] < 0] #filter data based on condition
#data = data.reset_index()
magnitude = 1
data['gasPower'] = data['gasPower']*10**magnitude
data = data.dropna()

fig = create_corr_matrix(data, '', True, size=(5,5))

print('Len of data: ', len(data))

"""
Add a copy of gasPower column, so previous gasPower values are also in X_reshaped
"""
data['gasPower_copy'] = data['gasPower']

data.head()

"""
Ideally would want to one-hot-encode season/month also?
But this does not make sense if like 4 (one hot encoded) months are none existant in the training set?
In the end maybe one hot encode all the datetime info + one hot encode houses based on their groups (energy label, area etc.).
"""

#columns_to_cat = ['year', 'month', 'day', 'hour', 'dayofweek', 'season']
columns_to_cat = ['hour', 'dayofweek', 'season', 'month', 'month_end', 'month_start', 'quarter_end', 'quarter_start']
data[columns_to_cat] = data[columns_to_cat].astype('category') # change datetypes to category

data = pd.get_dummies(data, columns=columns_to_cat) # One hot encoding the categories
data.head()

look_back = 5*24 # D -> 5, H -> 5*24
num_features = data.shape[1] - 1
output_dim = 1
test_size = 0.7 # This acctually is the train size, oops.
target_column = 'gasPower'

X_train, y_train, X_test, y_test = df_to_lstm_format(df=data, test_size=test_size, look_back=look_back, target_column=target_column, scale_X=True)
X_train.shape

X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], X_train.shape[2], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], X_test.shape[2], 1)
X_train.shape

def mape(y_true, y_pred):
    import keras.backend as K
    """
    Returns the mean absolute percentage error.
    For examples on losses see:
    https://github.com/keras-team/keras/blob/master/keras/losses.py
    """
    return (K.abs(y_true - y_pred) / K.abs(y_pred)) * 100

def smape(y_true, y_pred):
    import keras.backend as K
    """
    Returns the Symmetric mean absolute percentage error.
    For examples on losses see:
    https://github.com/keras-team/keras/blob/master/keras/losses.py
    """
    return (K.abs(y_pred - y_true) / ((K.abs(y_true) + K.abs(y_pred))))*100

"""
For info on batch normalization: https://github.com/ducha-aiki/caffenet-benchmark/blob/master/batchnorm.md
CuDNN.... Use GPU implementations of .... model, this speeds up the training.
"""

from keras.layers import InputLayer, ConvLSTM2D, Reshape, GRU
from keras.layers.normalization import BatchNormalization

input_shape = (X_train.shape[1], X_train.shape[2], X_train.shape[3])

dropout = 0.2


model = Sequential()

# Input shape: (samples, time, channels, rows, cols) see: https://keras.io/layers/recurrent/#convlstm2d
model.add(Conv2D(
        filters=16,
        kernel_size=(50, 50),
        input_shape=input_shape,
        padding='same', kernel_initializer='TruncatedNormal'))
model.add(LeakyReLU())
model.add(BatchNormalization())
model.add(Dropout(dropout))

model.add(Conv2D(
        filters=16,
        kernel_size=(40, 40),
        input_shape=input_shape,
        padding='same', kernel_initializer='TruncatedNormal'))
model.add(LeakyReLU())
model.add(BatchNormalization())
model.add(Dropout(dropout))

model.add(MaxPooling2D(pool_size=(2, 2))) # Increases training speed by 2.5 times!

#model.add(MaxPooling2D(pool_size=(15, 15)))
#model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

conv_output = model.output_shape
print(conv_output)

model.add(Reshape((conv_output[1], conv_output[2]*conv_output[3])))

# Input should be: (batch_size, timesteps, input_dim)
model.add(GRU(64, return_sequences=False))
model.add(LeakyReLU())
model.add(Dropout(dropout))

#model.add(Flatten())
#print('Flatten Output: ' , model.output_shape)

model.add(Dense(128))
model.add(LeakyReLU())
model.add(Dropout(dropout))

model.add(Dense(64))
model.add(LeakyReLU())
model.add(Dropout(dropout))

model.add(Dense(units=output_dim, kernel_initializer='TruncatedNormal'))


#print(model.summary())

multi_model = multi_gpu_model(model, gpus=num_gpu)

"""
Look back , 5
nodes, 35

More only makes the model more complex and harder/slower to train
"""

epochs = 500 #135
bs = 10
lr = 1e-3

# 0.05 0.9 0 True
#sgd = SGD(lr=lr, momentum=0.9, decay=0, nesterov=True) # 0.005
sgd = SGD(lr=lr)
adam = Adam(lr=lr)

epoch_size = 3

# For more info see: https://www.jeremyjordan.me/nn-learning-rate/
# Not applying it correctly? 19-11-2018 20.24
schedule = SGDRScheduler(min_lr=1e-4, # Pick the range where LR is ideal
                         max_lr=5e-2,
                         steps_per_epoch=np.ceil(epoch_size/bs),
                         lr_decay=0.9,
                         cycle_length=5,
                         mult_factor=1.5)

# compile & fit
multi_model.compile(optimizer=sgd, loss = ['mse'], metrics=[mape, smape, 'mse'])

early_stopping_monitor = EarlyStopping(patience=5000)


multi_model.fit(X_train, y_train, epochs=epochs, batch_size=bs, validation_data=(X_test, y_test),
         verbose=2, callbacks=[PlotLossesKeras(), early_stopping_monitor])