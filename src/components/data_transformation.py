import os
import sys
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder

from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_ob_file_path = os.path.join('artifacts', 'preprocessor.pk1')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformation()

    def get_transformer_obj(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)