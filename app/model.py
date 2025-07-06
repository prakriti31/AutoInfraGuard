import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import os

from app.logger import get_logger

# Initialize logger
logger = get_logger(__name__, "logs/train.log")

def train():
    try:
        logger.info("🔄 Loading data...")
        df = pd.read_csv("data/job_data.csv")

        logger.info("✅ Data loaded. Starting model training...")
        X = df[["experience", "education", "job_title"]]
        y = df["salary"]

        # Define categorical and numerical columns
        categorical_cols = ["education", "job_title"]
        numerical_cols = ["experience"]

        # Preprocessor with OneHotEncoder (ignore unknown categories)
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
            "columns": X.columns.tolist(),
            "categorical": categorical_cols,
            "numerical": numerical_cols
        }, model_path)

        logger.info(f"✅ Model trained and saved at: {model_path}")

    except Exception as e:
        logger.exception("❌ Training failed due to an exception.")

if __name__ == "__main__":
    train()
