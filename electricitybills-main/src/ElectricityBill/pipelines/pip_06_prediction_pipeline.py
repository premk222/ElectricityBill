import numpy as np 
import pandas as pd 
import pathlib as Path 
import os 
import sys 

from src.ElectricityBill import logging
from src.ElectricityBill.exception import FileOperationError
from src.ElectricityBill.utils.commons import load_object

# Create a class to make the predictions using trained model 

class PredictionPipeline:
    def __init__(self):
        pass 

    def make_predictions(self, features):
        try:
            # log message 
            logging.info("Making Predictions")
            
            model_path = os.path.join("artifacts", "model_trainer", "model.joblib")
            preprocessor_path= os.path.join("artifacts", "data_transformation", "preprocessor_obj.joblib")

            # Load the preprocessor object 
            preprocessor_obj = load_object(file_path=preprocessor_path)
            # Load the trained model
            model = load_object(file_path=model_path)

            # Transform the features 
            features_transformed = preprocessor_obj.transform(features)
            # Make the predictions 
            predictions = model.predict(features_transformed)

            return predictions
        
        except Exception as e:
            raise FileOperationError(e, sys)

# Create a class to represent the input features 

class CustomData:
    def __init__(self, **kwargs):
        # Initiate the attributes using kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    # Define a method to convert data object to a dataframe 
    def get_data_as_dataframe(self):
        try:
            # log message 
            logging.info("Converting data object to a dataframe")
            # Convert the data object to a dataframe 
            data_dict = {key: [getattr(self, key)] for key in vars(self)}

            # Convert the dictionary to dataframe in the return  
            return pd.DataFrame(data_dict)
        
        except Exception as e:
            raise FileOperationError(e, sys)
           




