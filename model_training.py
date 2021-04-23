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

def fit_LSTM(scaled_train_data, time_steps, n_features, batch_size = 6, activation = 'relu', epochs = 10):

    generator = TimeseriesGenerator(data = scaled_train_data, targets = scaled_train_data, length = time_steps, batch_size = batch_size)
    model = Sequential()
    model.add(LSTM(units = 200, activation = activation, input_shape = (time_steps, n_features)))
    model.add(Dropout(0.25))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit_generator(generator, epochs = epochs)
    
    return model


def predict_LSTM(scaled_train_data, scaler, train_data, test_data, time_steps, n_features, lstm_model):

    pred_list = []
    batch = scaled_train_data[-time_steps:].reshape(1, time_steps, n_features)

    for i in range(time_steps):
        pred_list.append(lstm_model.predict(batch)[0])
        batch = np.append(batch[:, 1:,:], [[pred_list[i]]], axis = 1)

    df_predict = pd.DataFrame(scaler.inverse_transform(pred_list), index=test_data.index, columns = ['Predictions'])
    
    return df_predict


def transform_data(train_data):

    scaler = MinMaxScaler()
    scaler.fit(train_data)
    
    return scaler.transform(train_data), scaler 


if __name__ == '__main__'
    train_PM25 = pd.read_csv('dataset/daily/train/train_PM2.5.csv', parse_dates = [0], index_col = [0])
    test_PM25 = pd.read_csv('dataset/daily/test/test_PM2.5.csv', parse_dates = [0], index_col = [0])

    scaled_train_PM25, scaler = transform_data(train_PM25)

    time_steps = 365
    n_feature = 1
    model = fit_LSTM(scaled_train_PM25, time_steps, n_feature)

    predictions = predict_LSTM(scaled_train_PM25, scaler, train_PM25, test_PM25,time_steps, n_feature, model)