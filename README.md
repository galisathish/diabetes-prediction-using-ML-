# diabetes-prediction-using-ML

# 🩺 Diabetes Prediction Web App

## 📌 Project Overview
This project is a simple, interactive web application built with **Streamlit** that predicts whether a person is likely to have diabetes based on various health-related inputs. It leverages a pre-trained machine learning model for making predictions.

---

## 📁 Project Structure

- `app.py`: Streamlit-based web app script.
- `diabetes_prediction_model.pkl`: Pre-trained ML model used for inference.
- `diabetes_prediction_dataset.csv`: Original dataset used for training.
- `base.ipynb`: Notebook used for EDA, feature engineering, and model training.

---

## ⚙️ Features

- Intuitive UI to collect user inputs.
- User input fields:
  - Age
  - Hypertension (Yes/No)
  - Heart Disease (Yes/No)
  - BMI
  - HbA1c Level
  - Blood Glucose Level
  - Gender (Female, Male, Other)
  - Smoking History (various categories)
- Encodes inputs for compatibility with the ML model.
- Displays the prediction result: ✅ **Positive** or ❌ **Negative**.

---

## 🧠 Model Details

- Pre-trained binary classification model stored in `.pkl` format.
- One-hot encoding used for categorical features.
- Model accepts a Pandas DataFrame with encoded inputs for prediction.

---

# Install Required Packages
Make sure you have Python installed. Then run:

pip install streamlit pandas

# Run the App
streamlit run app.py

# 🛠 Dependencies
Python 3.x
streamlit
pandas
pickle (built-in Python module)

# Notes
Keep app.py, diabetes_prediction_model.pkl, and any required files in the same directory.
Make sure the model file matches the input encoding used in app.py.



