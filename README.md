# Customer Churn Prediction App

[![Streamlit](https://img.shields.io/badge/Streamlit-App-blue)](https://streamlit.io/)  
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)  

A **Streamlit web application** that predicts whether a customer is likely to churn based on their demographics and subscription data. The app uses a pre-trained machine learning model and a scaler for data preprocessing. Fun balloon animation triggers when churn is predicted as **Yes**.

Live App: https://customer-churn-prediction-cufoqxzmk3ppuxmcdjuaus.streamlit.app/

## Features
- Predict customer churn based on:
  - **Age**
  - **Gender**
  - **Tenure (months)**
  - **Monthly charges**
- Interactive Streamlit UI for easy data input
- Balloon animation for churn = **Yes**
- Quick deployment with Streamlit Community Cloud

##  Project Structure
````
customer-churn-project/
│
├── .devcontainer/
│   └── devcontainer.json
│
├── data/
│   ├── raw/
        └── customer_churn_data.csv
    └── processed/
        ├── churn_cleaned.csv
        ├── X.csv
        └──y.csv

│
├── models/
│   ├── model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   ├── 00_data_cleaning_inspection.ipynb
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_model_evaluation.ipynb
│   └── 05_inference.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
````
## Tech Stack 
- Python
- Pandas, NumPy
- Scikit-learn (SVM, preprocessing, evaluation)
- Streamlit (interactive web app)
- Git & GitHub

## Run Locally
git clone https://github.com/orishashakya/customer-churn-prediction.git
cd customer-churn-prediction
pip install -r requirements.txt
streamlit run app.py

## Author
**Orisha Shakya – BSc. CSIT | Data Science & Machine Learning**
- GitHub: https://github.com/orishashakya
- LinkedIn: https://www.linkedin.com/in/orisha-shakya/