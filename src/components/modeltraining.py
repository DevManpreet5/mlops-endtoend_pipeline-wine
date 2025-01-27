import os
import pandas as pd
from src.entity.config_entity import Modeltraining
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
import joblib

class ModelTrainingcomponent:
    def __init__(self, config: Modeltraining):
        self.config = config
    
    def modeltrain(self):
        ada_boost_model = self.config.model(base_estimator=self.config.base_estimator(max_depth=self.config.max_depth), random_state=self.config.random_state)

        param_grid = {
        'n_estimators': [50, 100, 200],             
        'learning_rate': [0.01, 0.1, 1],             
        'loss': ['linear', 'square', 'exponential']   }

        grid_search = GridSearchCV(estimator=ada_boost_model, param_grid=param_grid, 
                           scoring='neg_mean_squared_error', cv=5, n_jobs=-1, verbose=2)

        train_path=os.path.join(self.config.dataset_path,self.config.file_name_train)
        train=pd.read_csv(train_path)

        test_path=os.path.join(self.config.dataset_path,self.config.file_name_test)
        test=pd.read_csv(test_path)

        y_train = train['Class'] 
        X_train = train.drop('Class', axis=1)

        y_test = test['Class'] 
        X_test = test.drop('Class', axis=1)

        grid_search.fit(X_train, y_train)
        best_model = grid_search.best_estimator_
        y_pred = best_model.predict(X_test)

        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = mse ** 0.5
        r2 = r2_score(y_test, y_pred)

        metrics = {
            "Mean Absolute Error": mae,
            "Mean Squared Error": mse,
            "Root Mean Squared Error": rmse,
            "R^2 Score": r2
        }
        metrics_save_path = os.path.join(self.config.model_path, self.config.metrics_file)
        pd.DataFrame([metrics]).to_json(metrics_save_path, orient="records", indent=4)

        hyperparameterpath=os.path.join(self.config.model_path,self.config.hyperparameter_file)
        pd.DataFrame([grid_search.best_params_]).to_json(hyperparameterpath,orient='records',indent=4)


        model_save_path = os.path.join(self.config.model_path, self.config.model_name)
        joblib.dump(best_model, model_save_path)




   

    def run(self):
         self.modeltrain()
         print('saved Model')

       
