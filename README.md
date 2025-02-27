# **Air Quality Prediction - Deep Learning Approach**

## Objective
The objective of this project is to investigate the performances of few Artificial Neural Network models to forecast the concentration of PM2.5​

## Approach to solving the problem
![Slide1](https://github.com/user-attachments/assets/9d90ff1d-fd5e-43dd-be61-9e7924c43dc8)

## Model Summary
* **Baseline/Naive Forecasting**
  The approach to create a baseline for checking the performance of the models is to assume that predicted value is the last value of the sequence (Naive Forecasting).​
  Baseline Test RMSE: 23.620​
  Baseline Test MAE: 12.443​
  Baseline Test R2: 0.950

* **Multi-Layer Perceptron (MLP)**

* **Long Short-term Memory (LSTM)**

* **Gated Recurrent Unit (GRU)**

## Results

## Inference
* This project provided an analysis and prediction study of the PM2.5 levels at Aotizhongxin station in Beijing, China using three models; MLP, LSTM, and GRU. ​LSTM performed better than all other models across RMSE, MAE, and R2 evaluation metrics.​ Actual and forecasted values subplots of LSTM model on Aotizhongxin station using test data only is shown in figure below.


## Comments and further works
* In this project, prediction of only one of the health affecting air pollutants (PM2.5) is carried out. However, as per WHO guidelines, the overall air quality shall be characterised by the concentration of a number of air pollutants. The key pollutants are : PM2.5, PM10, NO2, SO2, O3 and CO. A model which can predict all of the six pollutants will be more useful. A further enhancement could be to give Air Quality Index (AQI) as output, where AQI value is generated with predicted and WHO guideline values for these pollutants.
* Also, this project only consider PM2.5 prediction for subsequent 1 hr, given observation for 24hrs lag. However, hourly prediction may not be fit for purpose if the predictions is required to generate alerts and messages. So that vulnerable people can be benefitted by planning their travel to affected area along with any health advisory guidelines, like use of face mask. A multi-timesteps prediction, 12 hrs or 24 hrs will be more suitable in that case.


  
