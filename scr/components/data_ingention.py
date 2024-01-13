import sys
import os
from scr.exception import CustomeException
from scr.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngentionConfig:

    train_data_path = os.path.join("artifect" , "train.csv")
    test_data_path = os.path.join("artifect" , "test.csv")
    raw_data_path = os.path.join("artifect" , "raw_data.csv")

class DataConfig:

    def __init__(self):
        self.ingention_config = DataIngentionConfig()

    def initiate_data_ingention(self):
        logging.info("Enter the data ingention")
        try:
            logging.info("Data reading initiated")
            df = pd.read_csv("notebook\data\cardekho_data.csv")

            logging.info("train_test_split initiated")
            train_data,test_data = train_test_split(df,test_size = 0.3,random_state=42)

            os.makedirs(os.path.dirname(self.ingention_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingention_config.raw_data_path,index = False,header=True)

            train_data.to_csv(self.ingention_config.train_data_path,index = False,header=True)

            test_data.to_csv(self.ingention_config.test_data_path,index = False,header=True)
            
            logging.info("Ingention of the data")

            return (
                self.ingention_config.train_data_path,
                self.ingention_config.test_data_path
            )

        except Exception as e:
            raise CustomeException(e,sys)
        
if __name__ == "__main__":
    obj = DataConfig()
    obj.initiate_data_ingention()