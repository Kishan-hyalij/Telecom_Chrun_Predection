import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from logger import logging
import joblib
import os

# data processing
logging.info("Preprocessing start")
data=pd.read_csv("data/processed/data.csv")
data.drop(columns=['customerID'],axis=1,inplace=True)
data.replace({'TotalCharges':{' ':0}},inplace=True)
data['TotalCharges']=data['TotalCharges'].astype('float')
catcol=['gender','Partner','Dependents','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','Churn']
logging.info("Preprocessing ends")

# saving encoders
logging.info("saving encoders")
all_encoders=[]
for i in catcol:
    encoder=LabelEncoder()
    data[i]=encoder.fit_transform(data[i])
    all_encoders.append(f'{i}{encoder}')

encoders_path=os.path.join('models',"encoders.joblib")
joblib.dump(all_encoders,encoders_path)
logging.info("encoders saved")