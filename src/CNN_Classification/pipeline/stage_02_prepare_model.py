from src.CNN_Classification.components.data_ingestion import DataIngestion
from src.CNN_Classification.config.configuration import ConfigurationManager
from src.CNN_Classification import logger
from src.CNN_Classification.components.prepare_model import PrepareBaseModel


STAGE_NAME = "Base Model Preparing Stage"

class ModelPrepareTrainigPipeline:
    def __init__(self):
        pass
    
    def main (self):

        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__=="__main__":
        try:
             logger.info(f'>>>> stage {STAGE_NAME} started <<<<<')
             obj = ModelPrepareTrainigPipeline()
             obj.main()
             logger.info(f'>>>> stage {STAGE_NAME} completed <<<<<')
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise e