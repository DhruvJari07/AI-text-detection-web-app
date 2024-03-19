import sys
from AI_Text_Detection import logger
from AI_Text_Detection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from AI_Text_Detection.exception import CustomException
from AI_Text_Detection.pipeline.stage_02_data_transformation import DataTransformationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys)

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj_transform = DataTransformationPipeline()
    obj_transform.main()
    X_train, y_train, X_test, y_test = obj_transform.X_train, obj_transform.y_train, obj_transform.X_test, obj_transform.y_test
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys)
