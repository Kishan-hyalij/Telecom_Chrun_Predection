import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import StackingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import mlflow
import dagshub

dagshub.init(repo_owner='Kishan-hyalij', repo_name='Telecom_Chrun_Predection', mlflow=True)
mlflow.set_tracking_uri('https://dagshub.com/Kishan-hyalij/Telecom_Chrun_Predection.mlflow')
mlflow.set_experiment("best-model-selection1")

data=pd.read_csv("data/processed/processed_data.csv")

X=data.drop('Churn',axis=1)
Y=data['Churn']

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=42)

with mlflow.start_run():

    Logistic_Regression=LogisticRegression(max_iter=1000)
    SV_Classifier=SVC()
    KNeighbors_Classifier=KNeighborsClassifier()
    RandomForest_Classifier=RandomForestClassifier()
    GradientBoosting_Classifier=GradientBoostingClassifier()
    XGB_Classifier=XGBClassifier()

    Model=GradientBoosting_Classifier

    Model.fit(x_train,y_train)
    mlflow.sklearn.log_model(Model,f'{Model}')

    y_predict=Model.predict(x_test)
    accscr=accuracy_score(y_test,y_predict)
    mlflow.log_metric('accuracy',accscr)