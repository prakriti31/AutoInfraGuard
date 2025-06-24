import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import os

def train():
    print("🔄 Loading data...")
    df = pd.read_csv("data/job_data.csv")

    print("✅ Data loaded. Training model...")
    X = df[["experience", "education", "job_title"]]
    y = df["salary"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("edu_job", OneHotEncoder(), ["education", "job_title"])
        ],
        remainder="passthrough"
    )

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", LinearRegression())
    ])

    pipeline.fit(X, y)

    model_path = os.path.join("app", "model.joblib")
    joblib.dump(pipeline, model_path)

    print(f"✅ Model trained and saved at: {model_path}")

if __name__ == "__main__":
    train()
