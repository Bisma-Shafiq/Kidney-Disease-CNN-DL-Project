from src.CNN_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainigPipeline
from src.CNN_Classification.pipeline.stage_02_prepare_model import ModelPrepareTrainigPipeline
from src.CNN_Classification.pipeline.stage_03_model_training import ModelTrainigPipeline
from src.CNN_Classification import logger


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f'>>>> stage {STAGE_NAME} started <<<<<')
    data_ingestion = DataIngestionTrainigPipeline()
    data_ingestion.main()
    logger.info(f'>>>> stage {STAGE_NAME} completed <<<<<')
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Base Model Preparing Stage"

try:
    logger.info(f'>>>> stage {STAGE_NAME} started <<<<<')
    prepare_model = ModelPrepareTrainigPipeline()
    prepare_model.main()
    logger.info(f'>>>> stage {STAGE_NAME} completed <<<<<')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training Stage"

try:
    logger.info(f'>>>> stage {STAGE_NAME} started <<<<<')
    model_training = ModelTrainigPipeline()
    model_training.main()
    logger.info(f'>>>> stage {STAGE_NAME} completed <<<<<')
except Exception as e:
    logger.exception(e)
    raise e