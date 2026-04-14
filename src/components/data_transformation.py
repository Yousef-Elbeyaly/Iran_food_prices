import os
import sys
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.utils import save_object
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_ob_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_obj(self):
        try:
            numerical_columns = ['is_war', 'month', 'day']
            categorical_columns = ['category', 'commodity', 'unit']
            
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder', OneHotEncoder(sparse_output=False, handle_unknown='ignore')),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )
            
            logging.info("Numerical columns encoding completed")
            logging.info("Categorical columns encoding completed")

            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline', num_pipeline, numerical_columns),
                    ('cat_pipeline', cat_pipeline, categorical_columns)
                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            
            def transform_data(data):
                data['date'] = pd.to_datetime(data['date'])
                cols_to_drop = ['market_id', 'latitude', 'longitude', 'admin1', 'admin2', 'market', 'priceflag', 'pricetype', 'currency']
                data_cleaned = data.drop(columns=cols_to_drop)
                data_final = data_cleaned.copy()
                war_start_date = pd.Timestamp("2026-02-28")
                data_final['is_war'] = data_final['date'].apply(lambda x: 1 if x >= war_start_date else 0)
                data_final['month'] = data_final['date'].dt.month
                data_final['day'] = data_final['date'].dt.day
                data_final = data_final.drop(columns=['date', 'price', 'commodity_id'])
            
                return data_final.reset_index(drop=True)
            
            train_df = transform_data(train_df)
            test_df = transform_data(test_df)

            preprocessing_obj = self.get_data_transformer_obj()

            target_column_name = "usdprice"

            input_feature_train_df = train_df.drop(columns=[target_column_name], axis = 1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis = 1)
            target_feature_test_df = test_df[target_column_name]
            logging.info("Applying preprocessing object on training and testing dataframes.")
            
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
            
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]
            logging.info("Saved preprocessing object.")

            save_object(
                file_path = self.data_transformation_config.preprocessor_ob_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_ob_file_path
            )

        except Exception as e:
            raise CustomException(e, sys)