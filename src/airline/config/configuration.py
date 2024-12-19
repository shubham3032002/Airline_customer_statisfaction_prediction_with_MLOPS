
from src.airline.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.airline.utils.comman import read_yaml_file, create_directories
from src.airline.entity.config_entity import DataIngestionConfig
from pathlib import Path
class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH):
        self.config = read_yaml_file(config_filepath)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config["data_ingestion"]
        create_directories([config["root_dir"]])

        return DataIngestionConfig(
            root=Path(config["root_dir"]),
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"],
            table_name=config["table_name"],
            local_data_file=Path(config["local_data_file"]),
        )