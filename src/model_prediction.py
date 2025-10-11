import numpy as np
from logger import logging
import joblib

# Loading models
logging.info("loading Model")
try:
    model_path='models/GradientBoostingClassifier.joblib'
    Model=joblib.load(model_path)
    logging.info("model loaded successfully")
except Exception as e:
    logging.info("model loading failed")

# Generating output
try:
    input1=np.array([0.00,0.00,1.00,1.00,27.00,1.00,0.00,0.00,2.00,2.00,2.00,2.00,0.00,0.00,1.00,0.00,3.00,66.15,1874.45]).reshape(1,-1)
    input2=np.array([1.00,1.00,1.00,0.00,2.00,1.00,0.00,1.00,0.00,0.00,2.00,0.00,2.00,2.00,0.00,1.00,1.00,95.50,181.65]).reshape(1,-1)

    pred1=Model.predict(input1)
    pred2=Model.predict(input2)

    print(pred1) # 0
    print(pred2) # 1
    logging.info("model prediction successful")
except Exception as e:
    logging.info("prediction failed")
    raise(e)