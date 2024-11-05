import os 
from src.ElectricityBill import logging
import pandas as pd 
from src.ElectricityBill.entity.configuration_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config 
    
    # Method to validate all columns of the dataset against the specified schema 
    def validate_columns(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    logging.error(f"Column {col} is not present in the schema")

                    # Write validation status to the status file 
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(str(validation_status))
                    return validation_status
                
                else:
                    validation_status = True
                    logging.info(f"Column {col} is present in the schema")
                    
                    # Write validation status to the status file
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(str(validation_status))
                    return validation_status

            return validation_status
        
        except Exception as e:
            raise e
        
    # Method to validate the data types of all columns 
    def validate_data_types(self) -> bool:
        try:
            validation_status = None
            # Read the csv file 
            data = pd.read_csv(self.config.unzip_data_dir)
            # Get all column names and their corresponding data types from the schema
            all_cols = list(data.columns)

                # Check if the data types of columns in the dataset match those specified in the schema
            for col in all_cols:
                if data[col].dtype!= self.config.all_schema[col]:
                    validation_status = False
                    logging.error(f"Data type of column {col} does not match the schema")
                    
                    # Write validation status to the status file
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(str(validation_status))
                    return validation_status
                
                else:
                    validation_status = True
                    logging.info(f"Data type of column {col} matches the schema")

                    # Write validation status to the status file
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(str(validation_status))
            return validation_status
        
        except Exception as e:
            raise e
