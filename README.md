# "How fresh is the air? (Air Pollution Monitoring)

Prepared by: Stefan Angelov, Data Scientist
April 19, 2021

<img src="imgs/graphic.jpg" width="1000"/>


## Table of Contents

[Project Outline](#overview)<br/>
[Background & Motivation](#motivation)<br/>
[Problem](#problem)<br/>
[Solution](#solution)<br/>
[Goals](#problem)<br/>
[Data](#solution)<br/>
[Exploratory Data Analysis](#EDA)<br/>
[Data_Preparation](#data_preparation)<br/>
[LSTM Model](#lstm)<br/>
[Models Results](#results)<br/>
[Summary](#summary)<br/>
[Tools Used](#tools)<br/>
[Next Steps](#next)<br/>
[References](#references)<br/>



## <a name="overview">Project Outline</a> ##


Predicting the air pollution level. 

Highly pollution days are pretty important for all the people but extremely important for those who have asthma or trouble of breathing or are sensitive to particular matter in the air. Can Data Science and Machine Learning helps us predict what those pollution could be?


## <a name="motivation">Background & Motivation</a> ##

I have a background in Economics and Healthcare in particular sunlight therapy and selling air purifying systems.
My capstone project for the Galvanize Data Science Program was to build an early prediction model for air pollution.

I am coming from one of the most air-polluted capital in the world Sofia. Now I am living in the Bay Area and enjoying the fresh and clean ocean air ‘when there are no fires’. But I still take care of my friends and family. So I decided to create a system that can tell them few days in advance what the air quality will be. Maybe taking a vacation and go to the mountain, or maybe stay at how those days and enjoy the clean air from the home air purifying system.

So my motivation for the project stems from the fact that air pollution is responsible for 4 million deaths per year according to the World Health Organization (WHO) and is a leading cause of death across the globe, and contributes to stroke, heart disease, lung cancer, and other respiratory illness.
No wonder we should dedicate resources to understand and monitor air quality in our cities and neighborhoods. This should help authorities in urban planning as they can decide where to plant trees, build green spaces and manage traffic. Also, it can make us all aware of the impact of air pollution in our everyday life, which is critical to our health. 

California ever since 2018 they have been played wildfires, people evacuated.I remember last year was my second year living in the Bay Area and for the first time I have to experience the wildfires and this amount of toxic air. I have been waiting 3-4 days to air go better but this never happened so I decided to go to Utah for two weeks until the situation gets better. If I knew in advance the quality of the air, I’ve might go earlier and prevent be exposed to pollution for those 4 days.

## <a name="problem">Problem</a> ##

Air pollution causes a lot of horrible diseases, slowly damaging your lungs and cardiovascular system. So if you a vulnerable you don’t want to get exposed to that. 

Statistically, nine out of ten people worldwide are exposed to high levels of air pollutants that lead to serious health problems. The simple act of breathing results in early deaths for millions of people and harms billions more. In fact, since the end of 2018, the WHO has dubbed air pollution the “new tobacco”, while the EU is calling it the “biggest environmental risk” to public health.

Due to the major consequences of air pollution on human health, this problem is resulting in a major public crisis that requires immediate attention. Nowadays, the prediction of air quality has been a potential research area. There exist several methods in the literature, but the focus of this work is based on the prediction of air quality using time series analysis. 


## <a name="solution">Solution</a> ##

In this project, I approach air pollution from a different angle. I want to introduce and discuss the concept of crowdsourcing air quality monitoring. For those unfamiliar with the concept of crowdsourcing, it is about engaging the public to achieve a common goal. We can achieve this by dividing the work among participants into small tasks; in this case, collect air quality measurements. I aim to use crowdsourcing in a smart way to build up an accurate air pollution heat-map with the use of Artificial Intelligence (AI).

A lot of big data have been collected in the past few years. The problem is not of the amount of data we have but rather the methods we use to forecast pollution.
The goal of this project is to explore the air quality of the Beijing suburbs.

## <a name="goals">Goals</a> ##

Starting prototype on the Beijing air quality dataset but my ultimate goal is to apply the model on the air data quality for San Francisco.

## <a name="data">Data</a> ##

This Data set considers 6 main air pollutants and 6 relevant meteorological variables at multiple sites in Beijing.It covers the daily data between the years 2013 – 2017 for Beijing. Air quality data are collected at outdoor monitors across Beijing and can be download from UCI (UC Irvine Machine Learning Repository) web site https://archive.ics.uci.edu/ml/datasets/Beijing+Multi-Site+Air-Quality+Data

O3 (Ozone)

PM (Particle pollution or particulate matter)

CO (carbon monoxide)

SO2 (sulfur dioxide)

NO2 (nitrogen dioxide)

<img src="imgs/pollutants.jpg" width="410"/> <img src="imgs/stations.png" width="321"/>

## <a name="EDA">Exploratory Data Analysis</a> ##

Conducted Exploratory Analysis and Visualization using Pandas and Seaborn on the Beijing PM2.5 Dataset
Scaled, encoded, and converted the Time Series data into Supervised Learning data to feed the LSTM network
Evaluated by combining the forecast with the test dataset, inverting the scaling, and achieving a test RMSE of 49.60 compare to the based model of 50.12.
This is a dataset that reports on the weather and the level of pollution each hour for five years at the US embassy in Beijing, China.

From the beginning, I took one element that extremely important most specifically PM2.5 pollution (particulars matter 2.5 microns or less) while ignoring some of the others then use only one ML model(LSTM one to one).



<img src="imgs/pm10.png" width="1200"/>
<img src="imgs/o3.png" width="1200"/>
<img src="imgs/co.png" width="1200"/>
<img src="imgs/so2.png" width="1100"/>




## <a name="data_preparation">Data Preparation</a> ##

My data collection process involves first

## <a name="lstm">LSTM Model</a> ##

* Many to Many LSTM for PM2.5 on a daily base

Daily
<img src="imgs/daily_1.png" width="900"/>
<img src="imgs/daily_2.png" width="900"/>


Monthly one to one LSTM only for PM2.5

<img src="imgs/monthly.png" width="900"/>

* Monthly many to many LSTM for PM2.5, PM10, SO2, NO2, CO,O3
<img src="imgs/monthly1.png" width="900"/>
<img src="imgs/monthly2.png" width="900"/>


This analysis has been carried out using univariate( one to one) and multivariate( many to many) techniques namely LSTM(long short term memory networks). To perform the experimental work, the dataset of Aotizhongxin has been considered because all the stations looked pretty similar to mine, the same pattern is repeating. 

Recurrent neural networks like the Long Short-Term Memory network or LSTM is a special kind of recurrent neural network capable of learning short-term dependencies and remembering information for long periods as its default behavior. I first conducted an LSTM one-to-one model for PM2.5 and after that many to many with 6 of the features.


## <a name="results">Models Results</a> ##

Baseline Model for PM2.5 daily base

<img src="imgs/baseline_pm25.png" width="700"/>

LSTM one to one for PM2.5 daily base

<img src="imgs/lstm_pm25.png" width="700"/>

Baseline Model on daily base

<img src="imgs/daily_baseline.png" width="700"/>

LSTM many to many on daily base

<img src="imgs/daily_lstm.png" width="700"/>

My current methodology has been to build predictive models that use the air-quality dataset to minimize the RMSE(root mean square error). That metric will tell me how effective my model is at producing a prediction that a detected air is highly polluted.

I found the most effective the LSTM
So here is a close overlook of 

I’ve got this model is predicting one hour. This is what it looks like on years with test data. For this NO2, CO, it predicts very well, but for these particular ones, it does. 
It seems to predict very well when there is a clear seasonal pattern, if we look at SO2 there is a clear peak once a year and it seems to go slightly less each year. It’s start’s big 2014 and it’s less 2015 and the model is capturing that very well. The same is with O3 is predicting the seasonal trend. But is struggling with data… and interestingly enough the CO prediction looks like they should be correct, there is a little bit of a pick at 2014 and 205 and an even bigger pick in 2016 so predicted an even bigger pick in 2017 but it wasn’t. So I’ve read a little bit if China changed some regulation for CO emissions and it ends up that According to the US Energy Information Administration, China is ramping up its use of natural gas. Compared to coal, natural gas emits 50 to 60 percent less carbon during the combustion process. The predicting accurately got the trend of the increasing spikes. The model seems to make a sensible prediction based on the previous data. 

As you can see at the graph PM2.5 and PM10 
The model predicts some of the pollutions in the airway better than the others.

It’s doing very good on O3, we can see there is a clear seasonal pattern and predicts it well
It’s relatively good at CO and over-predicted it a little bit.

These are the once that I’ve predicted the best


## <a name="summary">Summary</a> ##
My results imply the following:
1. Generally my models predict


As air quality has been improved and there are still pollutants (ozone, NO2, and PM2.5) retain at high AQI. Efforts should continuously be made to reduce them. How can we make a difference? Drive less, use less electricity, don't burn wood or trash, support measures in your community that can cut air pollution, etc.


## <a name="tools">Tools Used</a> ##

Python:
Data Gathering: Pandas
Data Analysis: Google Colab, Tensor Flow, Pandas, Scikit-Learn, NLTK

Visualization:
Data Visualization: Matplotlib

## <a name="next">Next Steps</a>
Potential future directions include the following:
* Including the weather data because the weather is highly correlated with pollution. I think that would be incredibly helpful in adding predictive power.
* Build a front-end, web page using a flask app that can show the prediction for end users.

## <a name="references">References</a> ##


Zhang, S., Guo, B., Dong, A., He, J., Xu, Z. and Chen, S.X. (2017) Cautionary Tales on Air-Quality Improvement in Beijing. Proceedings of the Royal Society A, Volume 473, No. 2205, Pages 20170457.


Citation Request:

Zhang, S., Guo, B., Dong, A., He, J., Xu, Z. and Chen, S.X. (2017) Cautionary Tales on Air-Quality Improvement in Beijing. Proceedings of the Royal Society A, Volume 473, No. 2205, Pages 20170457.