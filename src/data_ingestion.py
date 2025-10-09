# Importing Libraries
import numpy as np
import pandas as pd
from logger import logging
import os

logging.info("data ingestion start")

# Data Collection
logging.info("reading data")
try:
    Data=pd.read_csv('data/raw/Telco-Customer-Churn.csv')
    logging.info("data read successfully")
except Exception as e:
            logging.info("data read failed")
            raise(e)

# Saving data csv
try:
    logging.info("saving csv")
    file_path=os.path.join('data','processed')
    os.makedirs(file_path,exist_ok= True)
    processed_data_path=os.path.join(file_path,"data.csv")
    Data.to_csv(processed_data_path,index=False,header=True)
    logging.info("csv saved")
except Exception as e:
        logging.info("csv not saved")
        raise(e)

logging.info("data ingestion end")