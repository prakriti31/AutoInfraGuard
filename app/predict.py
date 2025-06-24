import joblib
import pandas as pd

model = joblib.load("app/model.joblib")

def predict_salary(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return round(prediction, 2)
# app/predict.py

import joblib
import pandas as pd

model = joblib.load("app/model.joblib")  # Make sure this file exists

def predict_salary(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return round(prediction, 2)
