from src.CNN_Classification.components.data_ingestion import DataIngestion
from src.CNN_Classification.config.configuration import ConfigurationManager
from src.CNN_Classification import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainigPipeline:
    def __init__(self):
        pass
    
    def main (self):
        
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__=="__main__":
        try:
             logger.info(f'>>>> stage {STAGE_NAME} started <<<<<')
             obj = DataIngestionTrainigPipeline()
             obj.main()
             logger.info(f'>>>> stage {STAGE_NAME} completed <<<<<')
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise e