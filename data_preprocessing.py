'''
@Author: Stefan Angelov
@Created: 04/23/2021
@Purpose: Predicting the air pollution
'''

import pandas as pd
import numpy as np
import os
import math
import glob
import matplotlib.pyplot as plt


file_path = 'data/PRSA_Data_Aotizhongxin_20130301-20170228.csv'
wanted_col = ['PM2.5','PM10','SO2','NO2','CO','O3']

dtrain_dir = 'dataset/daily/train'
dtest_dir = 'dataset/daily/test'
mtrain_dir = 'dataset/monthly/train'
mtest_dir = 'dataset/monthly/test'


def load_dataset():

    df = pd.read_csv(file_path)
    print(df.head())

    return df


def datetime_index_column(df):

    df['Date-Time'] = pd.date_range(start = '2013-03-01 00:00:00',
        end = '2017-02-28 23:00:00',freq ='H')
    df.set_index('Date-Time', drop = True, inplace = True)

    return df


def data_frames(cleaned_df):

    df_PM25 = cleaned_df[['PM2.5']]
    df_PM10 = cleaned_df[['PM10']]
    df_SO2 = cleaned_df[['SO2']]
    df_NO2 = cleaned_df[['NO2']]
    df_CO = cleaned_df[['CO']]
    df_O3 = cleaned_df[['O3']]

    return [df_PM25, df_PM10, df_SO2, df_NO2, df_CO, df_O3]


def resample_data(dfs, freq = 'D'):

    if freq == 'D':
        return [each_df.resample(freq).mean() for each_df in dfs] 
    else:
        return [each_df.resample('D').max().resample(freq).mean() for each_df in dfs]


def train_test_split(dfs, train_end_index = '2016-02-29', test_start_index = '2016-03-01', freq = 'D'):

    if freq == 'M':
        test_start_index = '2016-03'
        train_end_index = '2016-02'
        
    return [(each_df[:train_end_index], each_df[test_start_index:]) for each_df in dfs]


def create_dataset_directories():
    os.mkdir('dataset/daily')
    os.mkdir('dataset/monthly')


def save_train_test_data(train_test_list, train_dir, test_dir):

    for each_train_test in train_test_list:
        filename = each_train_test[0].columns.values[0]
        (each_train_test[0].reset_index()).to_csv(os.path.join(train_dir, 'train_'+filename+'.csv'), index = False)
        (each_train_test[1].reset_index()).to_csv(os.path.join(test_dir, 'test_'+filename+'.csv'), index = False)

        

if __name__ == '__main__':
    df = load_dataset()
    df = datetime_index_column(df)
    df = df[wanted_col]
    cleaned_df = df.interpolate()
    del df
    df_list = data_frames(cleaned_df)

    df_PM25, df_PM10, df_SO2, df_NO2, df_CO, df_O3 = resample_data(df_list)
    dfm_PM25, dfm_PM10, dfm_SO2, dfm_NO2, dfm_CO, dfm_O3 = resample_data(df_list, freq = 'MS')

    df_list = [df_PM25, df_PM10, df_SO2, df_NO2, df_CO, df_O3]
    dfm_list = [dfm_PM25, dfm_PM10, dfm_SO2, dfm_NO2, dfm_CO, dfm_O3]

    dtrain_test_list = train_test_split(df_list)
    mtrain_test_list = train_test_split(dfm_list)

    save_train_test_data(dtrain_test_list, dtrain_dir, dtest_dir)
    save_train_test_data(mtrain_test_list, mtrain_dir, mtest_dir)







