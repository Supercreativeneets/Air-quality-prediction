# **Air Quality Prediction - Deep Learning Approach**

## Objective
The objective of this project is to investigate the performances of few Artificial Neural Network models to forecast the concentration of PM2.5​

## Approach to solving the problem
  ![Slide8](https://github.com/user-attachments/assets/11f6f525-cafd-4213-ae97-dbfc14e929ab)
  ![Slide9](https://github.com/user-attachments/assets/7d84a051-96a7-44cd-8f37-2dc7e8a9a2a6)
  ![Slide10](https://github.com/user-attachments/assets/73e53d8e-3845-4abf-bc5b-0e5b9d783720)
  ![Slide11](https://github.com/user-attachments/assets/a2f5ca1f-e24a-4b50-81de-b909ad36cd51)
  ![Slide12](https://github.com/user-attachments/assets/0f0ffc4a-86a2-4801-a11c-655ec7fdc2c5)
  ![Slide13](https://github.com/user-attachments/assets/5bd6677e-bc31-4380-b1c2-1dc9c82a9af9)
  ![Slide14](https://github.com/user-attachments/assets/8f3c81bb-18c8-47f3-8573-459d81d89e15)
  ![Slide15](https://github.com/user-attachments/assets/a902518a-6d86-437a-a348-8ee476a84d85)
      
## Model Summary
* **Baseline/Naive Forecasting**
  The approach to create a baseline for checking the performance of the models is to assume that predicted value is the last value of the sequence (Naive Forecasting).​
  Baseline Test RMSE: 23.620​
  Baseline Test MAE: 12.443​
  Baseline Test R2: 0.950

* **Multi-Layer Perceptron (MLP)**
  ![Slide21](https://github.com/user-attachments/assets/48f127e8-3664-499b-ac00-f34232b2f83a)

* **Long Short-term Memory (LSTM)**
  ![Slide22](https://github.com/user-attachments/assets/da720659-21e2-4270-8685-bc81756d9277)

* **Gated Recurrent Unit (GRU)**
  ![Slide23](https://github.com/user-attachments/assets/30e02666-3374-4562-b03c-8ac482c2f376)

## Results
  ![Slide25](https://github.com/user-attachments/assets/d7c17f3c-13bf-4abc-b85d-ee57a8c7961b)

## Inference
* This project provided an analysis and prediction study of the PM2.5 levels at Aotizhongxin station in Beijing, China using three models; MLP, LSTM, and GRU. ​LSTM performed better than all other models across RMSE, MAE, and R2 evaluation metrics.​ Actual and forecasted values subplots of LSTM model on Aotizhongxin station using test data only is shown in figure below.
![Slide28](https://github.com/user-attachments/assets/fc5392ea-585a-45bb-a2d7-513aa43a2d64)

## Comments and further works
* In this project, prediction of only one of the health affecting air pollutants (PM2.5) is carried out. However, as per WHO guidelines, the overall air quality shall be characterised by the concentration of a number of air pollutants. The key pollutants are : PM2.5, PM10, NO2, SO2, O3 and CO. A model which can predict all of the six pollutants will be more useful. A further enhancement could be to give Air Quality Index (AQI) as output, where AQI value is generated with predicted and WHO guideline values for these pollutants.
* Also, this project only consider PM2.5 prediction for subsequent 1 hr, given observation for 24hrs lag. However, hourly prediction may not be fit for purpose if the predictions is required to generate alerts and messages. So that vulnerable people can be benefitted by planning their travel to affected area along with any health advisory guidelines, like use of face mask. A multi-timesteps prediction, 12 hrs or 24 hrs will be more suitable in that case.


  
