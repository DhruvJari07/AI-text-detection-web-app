from AI_Text_Detection.config.configuration import ConfigurationManager
from AI_Text_Detection.components.model_trainer import ModelTraining
from AI_Text_Detection.exception import CustomException
from AI_Text_Detection import logger
from AI_Text_Detection.pipeline.stage_02_data_transformation import DataTransformationPipeline
import sys


STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self, X_train, y_train, X_test, y_test):
        try:
            config = ConfigurationManager()
            model_training_config = config.get_model_training_config()
            model_training = ModelTraining(config=model_training_config)
            model_pipeline = model_training.create_model_pipeline()
            model_accuracy = model_training.initiate_model_training(X_train, y_train, X_test, y_test, model_pipeline)
            return model_accuracy
            
        except Exception as e:
            raise CustomException(e, sys)
        
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



    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj_train = ModelTrainingPipeline()
        model_accuracy = obj_train.main(X_train, y_train, X_test, y_test)
        print(model_accuracy)
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise CustomException(e, sys)