import joblib
import pandas as pd

model = joblib.load("app/model.joblib")

def predict_salary(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return max(round(prediction, 2), 0.0)  # Prevent negative salaries

