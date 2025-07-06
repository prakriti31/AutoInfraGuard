import os
import subprocess
import logging
import shutil
from app.logger import get_logger
from app.rca_engine import run_rca
from app.model import train  # Phase 1 retraining logic

logger = get_logger("auto_healer")

DRIFT_THRESHOLD = 0.2
MODEL_PATH = "models/salary_model.pkl"
BACKUP_MODEL = "models/backups/salary_model_v1.pkl"

def restore_model():
    logger.warning("⏪ Rolling back to backup model...")
    shutil.copy(BACKUP_MODEL, MODEL_PATH)

def retrain_model():
    logger.info("🔁 Drift detected. Retraining model...")
    train()

def recreate_directories():
    logger.warning("🛠️ Recreating missing directories...")
    subprocess.run(["bash", "app/recovery_scripts/recreate_dirs.sh"])

def auto_heal(log_path="logs/sample.log"):
    issues = run_rca(log_path)

    for issue in issues:
        if issue["category"] == "Drift" and issue["severity"] == "high":
            retrain_model()

        elif issue["category"] == "Infra" and "missing directory" in issue["description"].lower():
            recreate_directories()

        elif issue["category"] == "Model" and "corrupt" in issue["description"].lower():
            restore_model()

        else:
            logger.info(f"ℹ️ Manual review needed for issue: {issue['error']}")

if __name__ == "__main__":
    auto_heal()
