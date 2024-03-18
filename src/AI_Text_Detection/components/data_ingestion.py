import os
import gdown
from AI_Text_Detection import logger
from AI_Text_Detection.utils.common import get_size
from AI_Text_Detection.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
     
    def download_file(self):
        '''
        Fetch data from the url
        '''

        try: 
            dataset_url = self.config.source_URL
            download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,download_dir)

            logger.info(f"Downloaded data from {dataset_url} into file {download_dir}")

        except Exception as e:
            raise e