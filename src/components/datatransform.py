import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.entity.config_entity import TransformationConfig

class Datatransform:
    def __init__(self, config: TransformationConfig):
        self.config = config

    def scale_fxn(self):
        filepath=os.path.join(self.config.dataset_path,self.config.file_name)
        df=pd.read_csv(filepath)
        scaler = StandardScaler()
        df[self.config.features_to_scale] = scaler.fit_transform(df[self.config.features_to_scale])
        return df


    def run(self):
         df = self.scale_fxn()
         print('transformed')
         return df
       
