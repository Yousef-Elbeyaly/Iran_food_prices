import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException

class TrainPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        try:
            ingestion = DataIngestion()
            train_path, test_path = ingestion.initiate_data_ingestion()

            transformation = DataTransformation()
            train_arr, test_arr, _ = transformation.initiate_data_transformation(train_path, test_path)

            trainer = ModelTrainer()
            r2_score = trainer.initiate_model_trainer(train_arr, test_arr)
            
            print(f"Model Training Completed! R2 Score: {r2_score}")
            return r2_score

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = TrainPipeline()
    obj.run_pipeline()