from src.airline.config.configuration import ConfigurationManager
from src.airline.components.data_ingestion import DataIngestion
from src.airline.logger import logging
from src.airline.constants import CONFIG_FILE_PATH
from src.airline.exception import customException


STAGE_NAME ="Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
         pass
     
     
    def main(self):
                # Initialize Configuration Manager
        config_manager = ConfigurationManager(config_filepath=CONFIG_FILE_PATH)
        data_ingestion_config = config_manager.get_data_ingestion_config()

        # Initialize DataIngestion and Extract Data
        data_ingestion = DataIngestion(config=data_ingestion_config)

        # Extract data and save to CSV
        data_ingestion.extract_to_csv(output_dir=data_ingestion_config.root / "extracted_data")
        
        
        
        
if __name__ == "__main__":
    try:
        logging.info(f">>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<")
    except Exception as e:
        logging.error(e)
        raise(e)           

 




    