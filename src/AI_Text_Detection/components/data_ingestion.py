import os
import sys
import gdown
from AI_Text_Detection import logger
from AI_Text_Detection.utils.common import get_size
from AI_Text_Detection.entity.config_entity import DataIngestionConfig
from AI_Text_Detection.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
     
    def download_file(self):
        '''
        Fetch data from the url
        '''

        try: 
            dataset_url = self.config.source_URL
            download_dir = self.config.raw_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,download_dir)

            logger.info(f"Downloaded data from {dataset_url} into file {download_dir}")

        except Exception as e:
            raise CustomException(e, sys)
        
    
    def initiate_data_ingestion(self):
        logger.info("Entered Data ingestion method")
        download_dir = self.config.raw_data_file
        try:
            df = pd.read_csv(download_dir)
            logger.info("Read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.config.train_data_file), exist_ok=True)
            logger.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.config.train_data_file, index=False, header=True)
            test_set.to_csv(self.config.test_data_file, index=False, header=True)
            logger.info("Ingestion process successfully completed")

            return (
                self.config.train_data_file,
                self.config.test_data_file
            )
        
        except Exception as e:
            raise CustomException(e, sys)