import os

requirements='pip install -r requirements.txt'
data_ingestion='python src/data_ingestion.py'
data_transformation='python src/data_transformation.py'
model_training='python src/model_training.py'
model_prediction='python src/model_prediction.py'
    
scripts_to_run = [requirements,data_ingestion,data_transformation,model_training,model_prediction]

# Run each script sequentially
for script in scripts_to_run:
    print(f"--- Running {script} ---")
    try:
        os.system(f'{script}')
    except Exception as e:
        print(f"--- Error running {script}: {e} ---")
        raise(e)
print("------Program execution complited------")