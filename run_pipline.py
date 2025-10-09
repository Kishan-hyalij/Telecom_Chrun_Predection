import os

requirements='pip install -r ../Telecom_Chrun_Predection/requirements.txt'
data_ingestion='python ../Telecom_Chrun_Predection/src/data_ingestion.py'
data_transformation='python ../Telecom_Chrun_Predection/src/data_transformation.py'
model_training='python ../Telecom_Chrun_Predection/src/model_training.py'
    
scripts_to_run = [requirements,data_ingestion,data_transformation,model_training]

# Run each script sequentially
for script in scripts_to_run:
    print(f"--- Running {script} ---")
    try:
        os.system(f'{script}')
    except Exception as e:
        print(f"--- Error running {script}: {e} ---")
        raise(e)
print("------Program execution complited------")