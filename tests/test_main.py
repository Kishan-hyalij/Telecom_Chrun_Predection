import os
import joblib
import pandas as pd
import pytest
import numpy as np

# Paths to saved model and encoders
MODEL_PATH = "models/GradientBoostingClassifier.joblib"
ENCODER_PATH = "models/encoders.joblib"

# Sample test data
SAMPLE_DATA = {
    'gender': ['Male'],
    'SeniorCitizen': [0],
    'Partner': ['Yes'],
    'Dependents': ['No'],
    'tenure': [12],
    'PhoneService': ['Yes'],
    'MultipleLines': ['No'],
    'InternetService': ['Fiber optic'],
    'OnlineSecurity': ['No'],
    'OnlineBackup': ['Yes'],
    'DeviceProtection': ['No'],
    'TechSupport': ['No'],
    'StreamingTV': ['Yes'],
    'StreamingMovies': ['No'],
    'Contract': ['Month-to-month'],
    'PaperlessBilling': ['Yes'],
    'PaymentMethod': ['Electronic check'],
    'MonthlyCharges': [70.35],
    'TotalCharges': [840.5],
}



# ----------------------------- #
# Utility Functions
# ----------------------------- #

def load_object(path):
    """Load a serialized object (model, scaler, etc.)"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, 'rb') as f:
        return joblib.load(f)


def preprocess_input(data, encoders):
    """Preprocess input data before prediction."""
    df = pd.DataFrame(data)

    # Identify categorical and numerical columns
    cat_cols = ['gender','Partner','Dependents','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod']

    # Encode categorical columns
    for i, encoder in enumerate(encoders):
        column_to_encode = cat_cols[i]
        df[column_to_encode] = encoder.transform(df[column_to_encode])

    return df


# ----------------------------- #
# Tests
# ----------------------------- #

def test_model_file_exists():
    """Ensure model and preprocessing files exist."""
    assert os.path.exists(MODEL_PATH), "Model file missing!"
    assert os.path.exists(ENCODER_PATH), "Encoder file missing!"


def test_model_prediction():
    """Test model prediction pipeline."""
    # Load model and preprocessors
    model = joblib.load(MODEL_PATH)
    encoders = joblib.load(ENCODER_PATH)

    # Prepare data
    X_test = preprocess_input(SAMPLE_DATA,encoders)

    # Make prediction
    pred = model.predict(X_test)

    # Validate output
    assert len(pred) == 1, "Prediction length mismatch!"
    assert pred[0] in [0, 1], "Invalid prediction output!"
    print(f"✅ Model Prediction Successful: {pred[0]}")


def test_input_schema():
    """Validate input schema consistency."""
    df = pd.DataFrame(SAMPLE_DATA)
    expected_cols = 19
    assert df.shape[1] == expected_cols, "Input schema mismatch!"


if __name__ == "__main__":
    print("\n...Running tests for Telecom Churn Prediction System...\n")
    pytest.main([__file__])
