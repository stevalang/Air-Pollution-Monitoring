'''
@Author: Stefan Angelov
@Created: 04/23/2021
@Purpose: Predicting the air pollution
'''

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.preprocessing.sequence import TimeseriesGenerator
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error,  mean_absolute_error
import os
import tensorflow as tf

def fit_LSTM(scaled_train_data, time_steps, n_features, batch_size = 6, activation = 'relu', epochs = 10):

    generator = TimeseriesGenerator(data = scaled_train_data, targets = scaled_train_data, length = time_steps, batch_size = batch_size)
    model = Sequential()
    model.add(LSTM(units = 200, activation = activation, input_shape = (time_steps, n_features)))
    model.add(Dropout(0.25))
    model.add(Dense(6))
    model.compile(optimizer='adam', loss='mse')
    model.fit_generator(generator, epochs = epochs)
    
    return model

def transform_data(train_data):

    scaler = MinMaxScaler()
    scaler.fit(train_data)
    
    return scaler.transform(train_data), scaler 


def predict_LSTM(scaled_train_data, scaler, train_data, test_data, time_steps, n_features, lstm_model):

    pred_list = []
    batch = scaled_train_data[-time_steps:].reshape(1, time_steps, n_features)

    for i in range(time_steps):
        pred_list.append(lstm_model.predict(batch)[0])
        batch = np.append(batch[:, 1:,:], [[pred_list[i]]], axis = 1)

    df_predict = pd.DataFrame(scaler.inverse_transform(pred_list), index=test_data.index, columns = ['Predictions'])
    
    return df_predict

def LSTM_evaluate(train_data, test_data, df_predict ):
    
    plt.figure(figsize = (20, 5))
    plt.plot(train_data.index, train_data, label = 'Train')
    plt.plot(test_data.index, test_data, label = 'Test')
    plt.plot(df_predict.index, df_predict, label = 'Prediction')
    plt.legend(loc='best', fontsize='xx-large')
    print('\nPredictions of ',train_data.columns.values[0])
    plt.show()

if __name__ == '__main__':
    ############################ USER INPUT #############################
    train_PM25 = pd.read_csv('dataset/daily/train/train_PM2.5.csv', parse_dates = [0], index_col = [0])
    test_PM25 = pd.read_csv('dataset/daily/test/test_PM2.5.csv', parse_dates = [0], index_col = [0])
    train_PM10 = pd.read_csv('dataset/daily/train/train_PM10.csv', parse_dates = [0], index_col = [0])
    test_PM10 = pd.read_csv('dataset/daily/test/test_PM10.csv', parse_dates = [0], index_col = [0])
    train_SO2 = pd.read_csv('dataset/daily/train/train_SO2.csv', parse_dates = [0], index_col = [0])
    test_SO2 = pd.read_csv('dataset/daily/test/test_SO2.csv', parse_dates = [0], index_col = [0])
    train_NO2 = pd.read_csv('dataset/daily/train/train_NO2.csv', parse_dates = [0], index_col = [0])
    test_NO2 = pd.read_csv('dataset/daily/test/test_NO2.csv', parse_dates = [0], index_col = [0])
    train_CO = pd.read_csv('dataset/daily/train/train_CO.csv', parse_dates = [0], index_col = [0])
    test_CO = pd.read_csv('dataset/daily/test/test_CO.csv', parse_dates = [0], index_col = [0])
    train_O3 = pd.read_csv('dataset/daily/train/train_O3.csv', parse_dates = [0], index_col = [0])
    test_O3 = pd.read_csv('dataset/daily/test/test_O3.csv', parse_dates = [0], index_col = [0])
    ######################################################################
    list_test = [test_PM25, test_PM10, test_SO2, test_NO2, test_CO, test_O3]
    list_train = [train_PM25, train_PM10, train_SO2, train_NO2, train_CO, train_O3]

    scaled_train_PM25, scaler = transform_data(train_PM25)
    scaled_train_PM10, scaler = transform_data(train_PM10)
    scaled_train_SO2, scaler = transform_data(train_SO2)
    scaled_train_NO2, scaler = transform_data(train_NO2)
    scaled_train_CO, scaler = transform_data(train_CO)
    scaled_train_PM10, scaler = transform_data(train_PM10)
    scaled_train_O3, scaler = transform_data(train_O3)


    list_scaled_train = [scaled_train_PM25, scaled_train_PM10, scaled_train_SO2, scaled_train_NO2,
     scaled_train_CO, scaled_train_O3]

    all_attributes = []
    joined_element = []

    for i in range(0, len(scaled_train_O3)):
        for j in range(0, len(list_scaled_train)):
            joined_element = np.append(joined_element, list_scaled_train[j][i])
        all_attributes.append(joined_element)
        joined_element = []

    time_steps = 365
    n_feature = 6
    model = fit_LSTM(np.array(all_attributes), time_steps, n_feature)

    model.save('trained_model.h5', model)
    LSTM_evaluate(train_data, test_data, df_predict )
    # model = tf.keras.models.load_model('trained_model.h5')

