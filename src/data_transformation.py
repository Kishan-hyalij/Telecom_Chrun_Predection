import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from logger import logging
import joblib
import os

logging.info("Data transformation start")

# data processing
logging.info("Preprocessing start")
try:
    data=pd.read_csv("data/processed/data.csv")
    data.drop('customerID',axis=1,inplace=True)
    data.replace({'TotalCharges':{' ':0}},inplace=True)
    data['TotalCharges']=data['TotalCharges'].astype('float')
    catcol=['gender','Partner','Dependents','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','Churn']
    logging.info("Preprocessing successful")
except Exception as e:
    logging.info("Preprocessing fail")
    raise(e)

# saving encoders
logging.info("saving encoders")
try:
    all_encoders=[]
    for i in catcol:
        encoder=LabelEncoder()
        data[i]=encoder.fit_transform(data[i])
        all_encoders.append(f'{i}{encoder}')

    encoders_path=os.path.join('models',"encoders.joblib")
    joblib.dump(all_encoders,encoders_path)
    logging.info("encoders saved")
except Exception as e:
    logging.info("saving encoders failed")
    raise(e)

# Saving processed data
logging.info("start saving processed csv")
try:
    processed_data_path=os.path.join('data','processed','processed_data.csv')
    data.to_csv(processed_data_path,index=False,header=True)
    logging.info("processed data saved")
except Exception as e:
    logging.info("saving processed data failed")
    raise(e)

logging.info("Data transformation end")