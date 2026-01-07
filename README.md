# Customer Churn Prediction App

[![Streamlit](https://img.shields.io/badge/Streamlit-App-blue)](https://streamlit.io/)  
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)  

A **Streamlit web application** that predicts whether a customer is likely to churn based on their demographics and subscription data. The app uses a pre-trained machine learning model and a scaler for data preprocessing. Fun balloon animation triggers when churn is predicted as **Yes**.

---

## 🔹 Features

- Predict customer churn based on:
  - **Age**
  - **Gender**
  - **Tenure (months)**
  - **Monthly charges**
- Interactive Streamlit UI for easy data input
- Balloon animation for churn = **Yes**
- Quick deployment with Streamlit Community Cloud

---

## 🔹 Project Structure

customer-churn-project/
│
├─ app.py # Main Streamlit application
├─ notebooks/
│ ├─ scaler.pkl # Pre-trained scaler
│ └─ best_model.pkl # Pre-trained ML model
├─ requirements.txt # Python dependencies
└─ README.md # Project overview