import sys
import os
sys.path.append(os.path.abspath('/home/neetikayadav3732/Air_Quality_project/src'))

import numpy as np 
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler


from exception import CustomException
from logger import logging
from utils import save_object

from dataclasses import dataclass


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")
    
class InterpolateImputer(BaseEstimator, TransformerMixin):
                def __init__(self, method='linear', limit_direction='forward', axis=0):
                    self.method = method
                    self.limit_direction = limit_direction
                    self.axis = axis
                def fit(self, X, y=None):
                    return self  # Nothing to do in fit
    
                def transform(self, X):
                    return X.interpolate(method=self.method, limit_direction=self.limit_direction, axis=self.axis)
            
class WindDirectionEncoder(BaseEstimator, TransformerMixin):
                def __init__(self, angle_mapping):
                    self.angle_mapping = angle_mapping
                    
                def fit(self, X, y=None):
                    return self  # Nothing to do in fit
    
                def transform(self, X):
                    # Mapping wind direction categories to angles
                    angles = np.array([self.angle_mapping[direction] for direction in X.squeeze()])
                    sin_Theta = np.sin(np.radians(angles))
                    cos_Theta = np.cos(np.radians(angles))
                    return np.column_stack((sin_Theta, cos_Theta))

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data trnasformation
        
        '''
        try:
            numerical_columns = ['PM2.5','PM2.5_Chan','PM2.5_Ding','PM2.5_Dong','PM2.5_Guan','PM2.5_Guch',
                                 'PM2.5_Huai','PM2.5_Nong','PM2.5_Shun','PM2.5_Tian','PM2.5_Wanl','PM2.5_Wans',
                                'PM10','NO2','CO','TEMP','PRES','DEWP','RAIN','WSPM' ]
            categorical_columns = ['wd']          
            
            angle_mapping = {'N': 0,
                             'NNE': 22.5,
                             'NE': 45,
                             'ENE': 67.5,
                             'E': 90,
                             'ESE': 112.5,
                             'SE': 135,
                             'SSE': 157.5,
                             'S': 180,
                             'SSW': 202.5,
                             'SW': 225,
                             'WSW': 247.5,
                             'W': 270,
                             'WNW': 292.5,
                             'NW': 315,
                             'NNW': 337.5,
                             'N': 360
                            }
            
                       
            # Create pipeline
            num_pipeline = Pipeline(steps=
                                    [('imputer', InterpolateImputer(method='linear', limit_direction='forward', axis=0))]
                                   )
            
                                      
            cat_pipeline=Pipeline(steps=
                                  [("imputer",SimpleImputer(strategy="most_frequent")),
                                   ("wd_encoder",WindDirectionEncoder(angle_mapping))]
                                 )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,val_path,test_path):

        try:
            train_df=pd.read_csv(train_path, index_col=None, header=0)
            val_df=pd.read_csv(val_path, index_col=None, header=0)
            test_df=pd.read_csv(test_path, index_col=None, header=0)

            logging.info("Reading train, val and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            input_train_df=train_df.drop(columns=['date','No','year','month','day','hour','SO2', 'O3','station'],axis=1)
                        
            input_val_df=train_df.drop(columns=['date','No','year','month','day','hour','SO2', 'O3','station'],axis=1)
            
            input_test_df=test_df.drop(columns=['date','No','year','month','day','hour','SO2', 'O3','station'],axis=1)
            

            logging.info(
                f"Applying preprocessing object on training, validation and testing dataframe."
            )

            input_train_arr=preprocessing_obj.fit_transform(input_train_df)
                            
            input_val_arr=preprocessing_obj.transform(input_val_df)
                        
            input_test_arr=preprocessing_obj.transform(input_test_df)
                       
            # Scale and Re-structure into windows of 24 hrs

            scaler = MinMaxScaler(feature_range=(0,1))

            train_arr = scaler.fit_transform(input_train_arr)
            val_arr = scaler.transform(input_val_arr) 
            test_arr = scaler.transform(input_test_arr)

            train_arr = np.array(np.split(train_arr, len(train_arr) / 24))
            val_arr = np.array(np.split(val_arr, len(val_arr) / 24))
            test_arr = np.array(np.split(test_arr, len(test_arr) / 24))
            
            
            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                val_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        
        except Exception as e:
            raise CustomException(e,sys)
            
            