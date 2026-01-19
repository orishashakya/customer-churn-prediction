# Customer Churn Prediction App

[![Streamlit](https://img.shields.io/badge/Streamlit-App-blue)](https://streamlit.io/)  
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)  

A **Streamlit web application** that predicts whether a  customer is likely to churn using a pre-trained Random Forest model. Users provide demographic and subscription data, and the app predicts churn probability with an interactive interface. Fun balloon animation triggers if churn is predicted as **Yes**.

Live App: https://customer-churn-prediction-cufoqxzmk3ppuxmcdjuaus.streamlit.app/

## Features
- Predict customer churn based on:
  - **Age**
  - **Gender**
  - **Tenure (months)**
  - **Monthly charges**
- Interactive Streamlit UI for easy data input
- Balloon animation for churn = **Yes**
- Handles imbalanced classes with class weighting
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
- Scikit-learn (Random Forest, preprocessing, evaluation)
- Streamlit (interactive web app)
- Git & GitHub

## Run Locally
git clone https://github.com/orishashakya/customer-churn-prediction.git
cd customer-churn-prediction
pip install -r requirements.txt
streamlit run app.py

## Author
**Orisha Shakya | Data Science & Machine Learning**
- GitHub: https://github.com/orishashakya
- LinkedIn: https://www.linkedin.com/in/orisha-shakya/