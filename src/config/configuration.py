import yaml
from src.entity.config_entity import Ingestionclassconfig , TransformationConfig ,  Modeltraining , Modelevaluating


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
            file_name_train=config["file_name_train"],
            file_name_test=config["file_name_test"],
            features_to_scale=config["features_to_scale"],
        )
    
    def get_data_training_config(self):
        config = self.config["model_training"]
        params=self.params["model_training"]
        return Modeltraining(
            model= config["model"],
            dataset_path=config["dataset_path"],
            file_name_train=config["file_name_train"],
            file_name_test=config["file_name_test"],
            model_path=config["model_path"],
            model_name=config["model_name"],
            base_estimator=config["base_estimator"],
            max_depth=config["max_depth"],
            random_state=config["max_depth"],
            learning_rate=params["learning_rate"],
            loss=params["loss"],
            n_estimators=params["n_estimators"],
            hyperparameter_file= config["hyperparameter_file"]
        )
    
    def get_data_evaluating(self):
        config = self.config["model_evaluating"]
        return Modelevaluating(
            test_dir= config["test_dir"],
            model_path=config["model_path"],
            model_name=config["model_name"],
            metrics_file=config["metrics_file"],
            tracking_uri=config["tracking_uri"]


        )

    
        
    def printvals(self):
        print(self.config,self.params)

