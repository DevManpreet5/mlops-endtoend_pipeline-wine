from src.config.configuration import configmanager
from src.components.modeltesting import Modeltestingcomponent

class testingpipeline:
    def __init__(self):
        self.config_manager = configmanager()

    def run(self):
        config = self.config_manager.get_data_training_config()
        data_ingestion = Modeltestingcomponent(config)
        data_ingestion.run()
