import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Churn Predictor", layout="centered")

st.title("Customer Churn Predictor")
st.write("Enter customer information and get a churn prediction.")

# Load pipeline trained in Notebook 02
pipeline = joblib.load("model/churn_pipeline.joblib")

# Load dataset only to build the same input columns + options
df = pd.read_csv("data/churn.csv")
X = df.drop(columns=["Churn"])

st.subheader("Customer info")
user_input = {}

for col in X.columns:
    if X[col].dtype == "object":
        options = sorted(X[col].dropna().unique().tolist())
        user_input[col] = st.selectbox(col, options)
    else:
        min_val = float(X[col].min())
        max_val = float(X[col].max())
        default_val = float(X[col].median())
        user_input[col] = st.number_input(col, min_value=min_val, max_value=max_val, value=default_val)

if st.button("Predict Churn"):
    input_df = pd.DataFrame([user_input])

    pred = pipeline.predict(input_df)[0]
    proba = pipeline.predict_proba(input_df)[0]
    classes = pipeline.classes_
    pred_index = list(classes).index(pred)
    pred_proba = proba[pred_index]

    st.success(f"Prediction: {pred}")
    st.write(f"Confidence (probability): {pred_proba:.2%}")
