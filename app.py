import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Churn Predictor")
st.title("Customer Churn Predictor")

# Load the model
pipeline = joblib.load("model/churn_pipeline.joblib")

# Load the data
df = pd.read_csv("data/churn_cleaned.csv")

# Prepare the feature dataframe
X = df.drop(columns=["Churn"])

# User input form
st.subheader("Customer info")

user_input = {
    "gender": st.selectbox("Gender", sorted(X["gender"].unique())),
    "SeniorCitizen": st.selectbox("Senior Citizen", sorted(X["SeniorCitizen"].unique())),
    "Partner": st.selectbox("Partner", sorted(X["Partner"].unique())),
    "tenure": st.number_input("Tenure (months)", min_value=int(X["tenure"].min()), max_value=int(X["tenure"].max()), value=1),
    "PhoneService": st.selectbox("Phone Service", sorted(X["PhoneService"].unique())),
    "MultipleLines": st.selectbox("Multiple Lines", sorted(X["MultipleLines"].unique())),
    "InternetService": st.selectbox("Internet Service", sorted(X["InternetService"].unique())),
    "Contract": st.selectbox("Contract", sorted(X["Contract"].unique())),
    "PaymentMethod": st.selectbox("Payment Method", sorted(X["PaymentMethod"].unique())),
    "MonthlyCharges": st.number_input("Monthly Charges", min_value=float(X["MonthlyCharges"].min()), max_value=float(X["MonthlyCharges"].max()), value=float(X["MonthlyCharges"].mean())),
    "TotalCharges": st.number_input("Total Charges", min_value=float(X["TotalCharges"].min()), max_value=float(X["TotalCharges"].max()), value=float(X["TotalCharges"].mean())),
}

# Predict button
if st.button("Predict Churn"):
    # Create a DataFrame from user input
    input_df = pd.DataFrame([user_input], columns=X.columns)

    # Make prediction
    pred = pipeline.predict(input_df)[0]

    # Display prediction
    st.success(f"Prediction: {pred}")

    # Probability of churn
    pred_proba = pipeline.predict_proba(input_df)[0][1]  

    # Display confidence
    st.write(f"Confidence: {pred_proba:.2%}")   