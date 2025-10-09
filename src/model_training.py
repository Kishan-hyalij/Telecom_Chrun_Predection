import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from logger import logging
import joblib
import os

logging.info("model training start")

# Loading data set
try:
    data=pd.read_csv("data/processed/processed_data.csv")
    logging.info("Processed data read successfully")
except Exception as e:
    logging.info("Processed data reading failed")
    raise(e)

# train test split
logging.info("performing train test split")
try:
    X=data.drop('Churn',axis=1)
    Y=data['Churn']
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=42)
    logging.info("train test split successfull")
except Exception as e:
    logging.info("train test split failed")
    raise(e)

# Model building
logging.info("model building")
try:
    Model=GradientBoostingClassifier()
    Model.fit(x_train,y_train)
    model_path=os.path.join('models','GradientBoostingClassifier.joblib')
    joblib.dump(Model,model_path)
    logging.info("model building successfull")
except Exception as e:
    logging.info("model building failed")
    raise(e)

# Model Evaluation
logging.info("model evaluation")
try:
    y_predict=Model.predict(x_test)
    accscr=accuracy_score(y_test,y_predict)
    accscr_path=os.path.join('scores','accuracy_score.txt')
    with open(accscr_path, 'w') as file:
        file.write(f"Model Accuracy: {accscr:.4f}\n")
    logging.info("model evaluation successful")
except Exception as e:
    logging.info("model evaluation failed")
    raise(e)

logging.info("model training end")