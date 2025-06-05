import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('diabetes_prediction_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

st.title("Diabetes Prediction App")

# Collecting user inputs
age = st.number_input("Enter Age:", min_value=0, max_value=120, value=30, step=1)
hypertension = st.selectbox("Do you have hypertension?", ["No", "Yes"])
heart_disease = st.selectbox("Do you have heart disease?", ["No", "Yes"])
bmi = st.number_input("Enter BMI:", min_value=0.0, max_value=100.0, value=25.0, step=0.1)
HbA1c_level = st.number_input("Enter HbA1c Level:", min_value=0.0, max_value=20.0, value=5.5, step=0.1)
blood_glucose_level = st.number_input("Enter Blood Glucose Level:", min_value=0, max_value=600, value=100, step=1)
gender = st.selectbox("Select Gender:", ["Female", "Male", "Other"])
smoking_history = st.selectbox("Smoking History:", ["No Info", "current", "ever", "former", "never", "not current"])

# Encoding inputs
user_input = pd.DataFrame([{
    'age': age,
    'hypertension': 1 if hypertension == "Yes" else 0,
    'heart_disease': 1 if heart_disease == "Yes" else 0,
    'bmi': bmi,
    'HbA1c_level': HbA1c_level,
    'blood_glucose_level': blood_glucose_level,
    'gender_Female': 1 if gender == "Female" else 0,
    'gender_Male': 1 if gender == "Male" else 0,
    'gender_Other': 1 if gender == "Other" else 0,
    'smoking_history_No Info': 1 if smoking_history == "No Info" else 0,
    'smoking_history_current': 1 if smoking_history == "current" else 0,
    'smoking_history_ever': 1 if smoking_history == "ever" else 0,
    'smoking_history_former': 1 if smoking_history == "former" else 0,
    'smoking_history_never': 1 if smoking_history == "never" else 0,
    'smoking_history_not current': 1 if smoking_history == "not current" else 0
}])

# Make prediction
if st.button("Predict Diabetes"):
    prediction = loaded_model.predict(user_input)
    result = "Positive" if prediction[0] == 1 else "Negative"
    st.success(f"Predicted Diabetes Outcome: {result}")