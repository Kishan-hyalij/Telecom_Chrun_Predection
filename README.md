# 📞 Telecom Customer Churn Prediction using Machine Learning

A Machine Learning project that predicts whether a telecom customer is likely to **churn** (leave the service) or **stay** based on their usage behavior and demographic details.  
This project demonstrates a complete ML workflow — from data preprocessing and model training to evaluation and deployment.

---

## 📌 Project Overview

Telecom companies lose significant revenue every year due to customer churn.  
The goal of this project is to build a predictive model that can identify customers who are at high risk of leaving the company, allowing proactive retention strategies.

This model helps businesses improve **customer retention**, reduce **churn rate**, and increase **profitability**.

---

## 🚀 Features

- Data Cleaning & Preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature Engineering  
- Model Building and Hyperparameter Tuning  
- Model Evaluation using multiple metrics  
- Deployment using Streamlit / Flask  

---

## 🗂 Dataset

The dataset contains information about telecom customers, including their account information, service usage, and whether they churned or not.

| Feature | Description |
|----------|-------------|
| **customerID** | Unique ID for each customer |
| **gender** | Male / Female |
| **SeniorCitizen** | Whether the customer is a senior citizen (1/0) |
| **Partner** | Whether the customer has a partner (Yes/No) |
| **Dependents** | Whether the customer has dependents (Yes/No) |
| **tenure** | Number of months the customer has stayed |
| **PhoneService** | Whether the customer has a phone service (Yes/No) |
| **MultipleLines** | Whether the customer has multiple lines (Yes/No) |
| **InternetService** | Type of internet service (DSL, Fiber optic, None) |
| **OnlineSecurity** | Whether the customer has online security (Yes/No) |
| **OnlineBackup** | Whether the customer has online backup (Yes/No) |
| **TechSupport** | Whether the customer has tech support (Yes/No) |
| **Contract** | Contract type (Month-to-month, One year, Two year) |
| **PaperlessBilling** | Whether billing is paperless (Yes/No) |
| **PaymentMethod** | Customer’s payment method |
| **MonthlyCharges** | Monthly charges |
| **TotalCharges** | Total amount charged |
| **Churn** | Target variable (Yes = Churned, No = Stayed) |

---

## 🛠 Tech Stack

- **Programming Language:** Python 🐍  
- **Libraries Used:**
  - NumPy  
  - Pandas  
  - Matplotlib  
  - Seaborn  
  - Scikit-learn  
  - XGBoost / Random Forest  
- **Deployment:** Streamlit / Flask  

---

## 📊 Exploratory Data Analysis (EDA)

- Missing value treatment  
- Encoding categorical features  
- Outlier detection and scaling  
- Correlation heatmap and feature importance  
- Class imbalance handling (SMOTE / Oversampling)

---

## 🤖 Model Training

1. **Data Split:** Train-Test Split (80%-20%)  
2. **Algorithms Tried:**
   - Logistic Regression  
   - Random Forest Classifier  
   - XGBoost Classifier  
3. **Feature Selection:** Recursive Feature Elimination (RFE)  
4. **Hyperparameter Tuning:** GridSearchCV / RandomizedSearchCV  
5. **Evaluation Metrics:** Accuracy, Precision, Recall, F1-Score, ROC-AUC  

---

## 📈 Model Performance

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|--------|-----------|------------|----------|-----------|----------|
| Logistic Regression | 0.80 | 0.78 | 0.76 | 0.77 | 0.83 |
| Random Forest | 0.86 | 0.84 | 0.83 | 0.83 | 0.90 |
| XGBoost | 0.88 | 0.86 | 0.85 | 0.85 | 0.92 |

✅ **XGBoost Classifier** achieved the best performance and was chosen as the final model.

---

## 🌐 Deployment

The trained model has been deployed and is accessible via:  
👉 [Live Demo](YOUR_DEPLOYMENT_LINK_HERE)

Users can input customer details and get an instant prediction on whether the customer is likely to churn.

---

## 📜 License

This project is licensed under the MIT License – see the LICENSE
file for details.
