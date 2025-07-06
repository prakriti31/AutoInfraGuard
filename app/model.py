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

    # Define categorical and numerical columns
    categorical_cols = ["education", "job_title"]
    numerical_cols = ["experience"]

    # Preprocessor with OneHotEncoder (with ignore for unknowns)
    preprocessor = ColumnTransformer(
        transformers=[
            ("edu_job", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
        ],
        remainder="passthrough"  # Pass 'experience' through
    )

    # Full pipeline
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", LinearRegression())
    ])

    pipeline.fit(X, y)

    # Save pipeline and metadata
    os.makedirs("models", exist_ok=True)
    model_path = os.path.join("models", "salary_model.pkl")

    joblib.dump({
        "model": pipeline,
        "columns": X.columns.tolist(),        # For schema enforcement
        "categorical": categorical_cols,
        "numerical": numerical_cols
    }, model_path)

    print(f"✅ Model trained and saved at: {model_path}")

if __name__ == "__main__":
    train()
