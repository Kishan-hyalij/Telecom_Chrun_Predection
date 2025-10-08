# Importing Libraries
import numpy as np
import pandas as pd
from logger import logging
import os

# Data Collection
logging.info("reading data")
Data=pd.read_csv('data/raw/Telco-Customer-Churn.csv')
logging.info("data read successfully")

# Setting path to save data csv 
logging.info("path setting-up")
processed_data=os.path.join('data','processed')
os.makedirs(processed_data,exist_ok=True)
processed_data_path=os.path.join('data','processed',"data.csv")
logging.info("path set")

# Saving data csv
logging.info("saving csv")
Data.to_csv(processed_data_path)
logging.info("csv saved")