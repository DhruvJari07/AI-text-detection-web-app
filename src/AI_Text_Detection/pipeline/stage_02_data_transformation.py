from AI_Text_Detection.config.configuration import ConfigurationManager
from AI_Text_Detection.components.data_transformation import DataTransformation
from AI_Text_Detection.exception import CustomException
from AI_Text_Detection import logger
import sys

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            self.X_train, self.y_train, self.X_test, self.y_test = data_transformation.initiate_data_transformation()
        except Exception as e:
            raise CustomException(e, sys)

        

"""
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj_transform = DataTransformationPipeline()
        obj_transform.main()
        X_train, y_train, X_test, y_test = obj_transform.X_train, obj_transform.y_train, obj_transform.X_test, obj_transform.y_test
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise CustomException(e, sys)

"""