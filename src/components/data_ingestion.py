import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import customException
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self):
        self.train_data_path = os.path.join("artifacts", "train.csv")
        self.test_data_path = os.path.join("artifacts", "test.csv")
        self.raw_data_path = os.path.join("artifacts", "raw.csv")

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        try:
            logging.info("Reading data using pandas from local system")

            data_path = os.path.join(os.getcwd(), "notebook", "data", "income_cleandata.csv")
            
            if not os.path.exists(data_path):
                logging.error(f"File not found: {data_path}")
                raise FileNotFoundError(f"File not found: {data_path}")
            
            data = pd.read_csv(data_path)  
            logging.info("Data reading completed")

            os.makedirs(os.path.dirname(self.raw_data_path), exist_ok=True)
            data.to_csv(self.raw_data_path, index=False)
            logging.info("Data saved to raw data path")

            train_set, test_set = train_test_split(data, test_size=0.3, random_state=42)

            train_set.to_csv(self.train_data_path, index=False, header=True)
            test_set.to_csv(self.test_data_path, index=False, header=True)

            logging.info("Data ingestion completed")

            return self.train_data_path, self.test_data_path

        except FileNotFoundError as e:
            raise customException(e, sys)
        except Exception as e:
            logging.error("Error occurred during data ingestion")
            raise customException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
