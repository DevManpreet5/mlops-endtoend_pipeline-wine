import yaml
from src.entity.config_entity import Ingestionclassconfig , TransformationConfig


class configmanager:
    def __init__(self,config_path='config.yaml',param_path='params.yaml'):
        self.config=self.read_yaml(config_path)
        self.params=self.read_yaml(param_path)
    
    @staticmethod
    def read_yaml(path):
        with open(path,'r') as file:
            return yaml.safe_load(file)
    
    def get_data_ingestion_config(self):
        config = self.config["data_ingestion"]
        params = self.params["data_ingestion"]
        return Ingestionclassconfig(
            dataset_url=config["dataset_url"],
            raw_dataset_dir=config["raw_dataset_dir"],
            processed_dataset_dir=config["processed_dataset_dir"],
            dataset_name=config["dataset_name"],
            test_size=params["test_size"],
            random_state=params["random_state"],
        )
    
    def get_data_transform_config(self):
        config = self.config["data_transformation"]
        return TransformationConfig(
            dataset_path=config["dataset_path"],
            output_dir=config["output_dir"],
            file_name=config["file_name"],
            features_to_scale=config["features_to_scale"],
        )

        
    def printvals(self):
        print(self.config,self.params)

