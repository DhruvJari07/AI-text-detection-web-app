import os
import sys
from AI_Text_Detection import logger
from AI_Text_Detection.utils.common import lower_case, remove_punctuation, remove_stopwords, remove_tags
from AI_Text_Detection.exception import CustomException
from AI_Text_Detection.entity.config_entity import DataTransformationConfig
import pandas as pd
import nltk
nltk.download('stopwords')
nltk.download('punkt')

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def initiate_data_transformation(self):
        '''
        Transform the data and train the model
        '''
        try: 
            train_df = pd.read_csv(self.config.train_data_file)
            test_df = pd.read_csv(self.config.test_data_file) 
            logger.info(f"train and test dataframe loaded")
            logger.info(f"Data transformation initiated")
            train_df["text"]=train_df["text"].apply(remove_tags)
            train_df["text"]=train_df["text"].apply(remove_punctuation)
            train_df["text"]=train_df["text"].apply(lower_case)
            train_df["text"]=train_df["text"].apply(remove_stopwords)
            test_df["text"]=test_df["text"].apply(remove_tags)
            test_df["text"]=test_df["text"].apply(remove_punctuation)
            test_df["text"]=test_df["text"].apply(lower_case)
            test_df["text"]=test_df["text"].apply(remove_stopwords)
            X_train = train_df["text"]
            y_train = train_df["generated"]
            X_test = test_df["text"]
            y_test = test_df["generated"]
            logger.info(f"Data transformation completed")
            return X_train, y_train, X_test, y_test

        except Exception as e:
            raise CustomException(e, sys)