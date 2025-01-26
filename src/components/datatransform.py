import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.entity.config_entity import TransformationConfig

class Datatransform:
    def __init__(self, config: TransformationConfig):
        self.config = config

    def scale_fxn(self):
        filepath_train=os.path.join(self.config.dataset_path,self.config.file_name_train)
        df_train=pd.read_csv(filepath_train)

        filepath_test=os.path.join(self.config.dataset_path,self.config.file_name_test)
        df_test=pd.read_csv(filepath_test)

        scaler = StandardScaler()
        df_train[self.config.features_to_scale] = scaler.fit_transform(df_train[self.config.features_to_scale])
        df_test[self.config.features_to_scale] = scaler.transform(df_test[self.config.features_to_scale])
        return df_train , df_test


    def run(self):
         df_train,df_test = self.scale_fxn()
         print('transformed')
         return df_train,df_test
       
