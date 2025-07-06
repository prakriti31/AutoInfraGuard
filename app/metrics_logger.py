import sqlite3
from datetime import datetime

def log_prediction(input_data: dict, prediction: float):
    conn = sqlite3.connect("monitoring/metrics.db")
    c = conn.cursor()

    # 👇 This creates the table with correct schema if not exists
    c.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            job_title TEXT,
            education TEXT,
            experience REAL,
            predicted_salary REAL,
            timestamp TEXT
        )
    """)

    c.execute("""
        INSERT INTO predictions (job_title, education, experience, predicted_salary, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (
        input_data["job_title"],
        input_data["education"],
        input_data["experience"],
        prediction,
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    conn.close()
