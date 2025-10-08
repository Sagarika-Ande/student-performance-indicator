import sys

from sklearn.model_selection import GridSearchCV

from src.exception import CustomException
from src.logger import logging



def hyper_parameter_tuning(X_train,y_train,X_test,y_test,models,cv=3,n_jobs = 4):
    
    try:
        params={
            "Random Forest":{
                # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                
                # 'max_features':['sqrt','log2',None],
                'n_estimators': [8,16,32,64,128,256]
            },
            "Decision Tree": {
                'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                # 'splitter':['best','random'],
                # 'max_features':['sqrt','log2'],
            },
            
            "Gradient Boosting":{
                # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                'learning_rate':[.1,.01,.05,.001],
                'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                # 'criterion':['squared_error', 'friedman_mse'],
                # 'max_features':['auto','sqrt','log2'],
                'n_estimators': [8,16,32,64,128,256]
            },
            "K-Neighbors Regressor": {},
            "Linear Regression":{},
            "XGB Regressor":{
                'learning_rate':[.1,.01,.05,.001],
                'n_estimators': [8,16,32,64,128,256]
            },
            "CatBoosting Regressor":{
                'depth': [6,8,10],
                'learning_rate': [0.01, 0.05, 0.1],
                'iterations': [30, 50, 100]
            },
            "AdaBoost Regressor":{
                'learning_rate':[.1,.01,0.5,.001],
                # 'loss':['linear','square','exponential'],
                'n_estimators': [8,16,32,64,128,256]
            }
        }

        logging.info("Hyperparameter tuning has started")
        tuned_models = {}
        
        for model_name, model in models.items():
            logging.info(f"Hyperparameter tuning for {model_name} has started")
            
            param_grid = params.get(model_name,{})

            if not param_grid:
                model.fit(X_train,y_train)
                tuned_models[model_name] = model

            
            grid = GridSearchCV(
                estimator=model,
                param_grid=param_grid,
                cv = cv,
                n_jobs=n_jobs,
                verbose=1,
                scoring="r2"
            )

            grid.fit(X_train,y_train)

            logging.info(f"Best parameters for {model_name}: {grid.best_params_}")

            tuned_models[model_name] = grid.best_estimator_

        return tuned_models



    except Exception as e:
        raise CustomException(e,sys)
         
