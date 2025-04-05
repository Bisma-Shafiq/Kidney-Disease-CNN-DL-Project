from src.CNN_Classification.config.configuration import ConfigurationManager
from src.CNN_Classification import logger
from src.CNN_Classification.components.model_training import Training

STAGE_NAME = "Model Training Stage"

class ModelTrainigPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__=="__main__":
        try:
             logger.info(f'>>>> stage {STAGE_NAME} started <<<<<')
             obj = ModelTrainigPipeline()
             obj.main()
             logger.info(f'>>>> stage {STAGE_NAME} completed <<<<<')
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise e
        