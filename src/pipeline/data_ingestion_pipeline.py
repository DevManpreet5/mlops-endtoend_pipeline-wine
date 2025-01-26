
from src.config.configuration import configmanager
from src.components.dataingestion import DataIngestion

class DataIngestionPipeline:
    def __init__(self):
        self.config_manager = configmanager()

    def run(self):
        config = self.config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config)
        data_ingestion.run()
