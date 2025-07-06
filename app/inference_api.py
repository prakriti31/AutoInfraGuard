import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from datetime import datetime

app = FastAPI()

# Load the trained model (with pipeline and schema)
model_bundle = joblib.load("models/salary_model.pkl")
pipeline = model_bundle["model"]

# Input schema
class InputData(BaseModel):
    job_title: str
    education: str
    experience: float

# Predict route
@app.post("/predict")
def predict_salary(data: InputData):
    try:
        print("📥 Received data:", data.dict())
        
        # Convert to DataFrame
        input_df = pd.DataFrame([data.dict()])
        print("📊 DataFrame:\n", input_df)

        # Predict
        predicted_salary = pipeline.predict(input_df)[0]
        print("💰 Prediction:", predicted_salary)

        # Logging prediction to SQLite
        conn = sqlite3.connect("monitoring/metrics.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS predictions (
                timestamp TEXT,
                job_title TEXT,
                education TEXT,
                experience REAL,
                predicted_salary REAL
            )
        """)
        cursor.execute("""
            INSERT INTO predictions (timestamp, job_title, education, experience, predicted_salary)
            VALUES (?, ?, ?, ?, ?)
        """, (
            datetime.now().isoformat(),
            data.job_title,
            data.education,
            data.experience,
            round(float(predicted_salary), 2)
        ))
        conn.commit()
        conn.close()

        return {"predicted_salary": round(float(predicted_salary), 2)}

    except Exception as e:
        print("❌ Error during prediction:", e)
        return {"error": str(e)}

# Route to view last 10 predictions
@app.get("/metrics")
def view_logged_metrics():
    conn = sqlite3.connect("monitoring/metrics.db")
    df = pd.read_sql_query("SELECT * FROM predictions ORDER BY timestamp DESC LIMIT 10", conn)
    conn.close()
    return df.to_dict(orient="records")
