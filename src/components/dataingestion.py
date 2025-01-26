import os
import pandas as pd
from sklearn.model_selection import train_test_split
import requests
from src.entity.config_entity import Ingestionclassconfig

class DataIngestion:
    def __init__(self, config: Ingestionclassconfig):
        self.config = config

    def download_dataset(self):
        os.makedirs(self.config.raw_dataset_dir, exist_ok=True)
        file_path = os.path.join(self.config.raw_dataset_dir, self.config.dataset_name)
        response = requests.get(self.config.dataset_url)
        with open(file_path, "wb") as file:
            file.write(response.content)
        return file_path

    def load_data(self, file_path):
        return pd.read_csv(file_path)

    def split_data(self, df):
        train, test = train_test_split(
            df,
            test_size=self.config.test_size,
            random_state=self.config.random_state,
        )
        return train, test

    def save_data(self, data, file_name):
        os.makedirs(self.config.processed_dataset_dir, exist_ok=True)
        path = os.path.join(self.config.processed_dataset_dir, file_name)
        data.to_csv(path, index=False)

    def run(self):
        dataset_path = self.download_dataset()
        df = self.load_data(dataset_path)
        train, test = self.split_data(df)
        self.save_data(train, "train.csv")
        self.save_data(test, "test.csv")
