import sys 
import pandas as pd

from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts\model.pkl'
            preprocessor_path = 'artifacts\preprocessor.pkl'
            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
            category: str,
            commodity: str,
            unit: str,
            is_war: int,
            month: int,
            day: int):
        
        self.category = category
        self.commodity = commodity
        self.unit = unit
        self.is_war = is_war
        self.month = month
        self.day = day

    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "category": [self.category],
                "commodity":[self.commodity],
                "unit":[self.unit],
                "is_war":[self.is_war],
                "month":[self.month],
                "day":[self.day]
            }

            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)        
