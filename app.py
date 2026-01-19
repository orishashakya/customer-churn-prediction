# Gender -> 1 Female, 0 Male
# Churn  -> 1 Yes, 0 No
# Feature Order: Age, Gender, Tenure, MonthlyCharges

import streamlit as st
import joblib
import numpy as np
import os

# -------- Load model safely --------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "models", "model.pkl"))  # Random Forest

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

    # Probability of churn
    churn_prob = model.predict_proba(X)[0][1]

    # Custom threshold for imbalanced data
    THRESHOLD = 0.65
    prediction = 1 if churn_prob >= THRESHOLD else 0

    result = "Yes" if prediction == 1 else "No"

    st.subheader("Prediction Result")
    st.success(f"Customer Churn: **{result}**")
    st.write(f"Churn Probability: {churn_prob:.2f}")

    if result == "Yes":
        st.balloons()
