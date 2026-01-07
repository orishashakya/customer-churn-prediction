# Gender -> 1 Female, 0 Male
# Churn  -> 1 Yes, 0 No
# Feature Order: Age, Gender, Tenure, MonthlyCharges

import streamlit as st
import joblib
import numpy as np
import os

# -------- Load model & scaler safely --------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # customer-churn-project
scaler = joblib.load(os.path.join(BASE_DIR, "notebooks", "scaler.pkl"))
model = joblib.load(os.path.join(BASE_DIR, "notebooks", "model.pkl"))

# -------- App UI --------
st.title("Customer Churn Prediction App")
st.divider()
st.write("Enter customer details below and click **Predict** to check churn probability.")
st.divider()

# -------- User Inputs --------
age = st.number_input("Age", min_value=10, max_value=100, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
tenure = st.number_input("Tenure (months)", min_value=0, max_value=130, value=10)
monthly_charge = st.number_input(
    "Monthly Charges",
    min_value=30.0,
    max_value=150.0,
    value=70.0
)

st.divider()

# -------- Prediction --------
if st.button("Predict"):
    gender_encoded = 1 if gender == "Female" else 0

    X = np.array([[age, gender_encoded, tenure, monthly_charge]])
    X_scaled = scaler.transform(X)

    prediction = model.predict(X_scaled)[0]
    result = "Yes" if prediction == 1 else "No"

    st.subheader("Prediction Result")
    st.success(f"Customer Churn: **{result}**")

    # -------- Balloons effect if churn is Yes --------
    if result == "Yes":
        st.balloons()
else:
    st.info("Please enter values and click **Predict**.")
