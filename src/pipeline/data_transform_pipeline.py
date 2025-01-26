from src.config.configuration import configmanager
from src.components.datatransform import Datatransform

class DataTransformPipeline:
    def __init__(self):
        self.config_manager = configmanager()

    def run(self):
        config = self.config_manager.get_data_transform_config()
        data_ingestion = Datatransform(config)
        data_ingestion.run()
