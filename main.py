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
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys)
