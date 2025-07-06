def run_pipeline():
    from generate_datasets import generate_dataset
    from model import train
    from drift_detector import generate_combined_drift_report

    print("▶️ Generating data...")
    generate_dataset(10000, drift=False)
    generate_dataset(10000, drift=True).to_csv("data/live_data.csv", index=False)


    print("▶️ Training model...")
    train()

    print("▶️ Checking drift...")
    generate_combined_drift_report("data/job_data.csv", "data/live_data.csv", "reports/drift_report.html")

if __name__ == "__main__":
    run_pipeline()
