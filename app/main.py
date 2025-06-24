from fastapi import FastAPI
from pydantic import BaseModel
from app.predict import predict_salary
import pandas as pd
from fastapi.responses import FileResponse, HTMLResponse
from app.drift_detector import generate_combined_drift_report
import os

app = FastAPI()

class InputData(BaseModel):
    experience: int
    education: str
    job_title: str

@app.get("/")
def home():
    return {"message": "Welcome to AutoInfraGuard - Drift Monitor"}

@app.get("/generate-drift-report")
def generate_drift():
    generate_combined_drift_report("data/job_data.csv", "data/live_data.csv", "reports/drift_report.html")
    return {"status": "Report generated"}

@app.get("/view-drift-report", response_class=HTMLResponse)
def view_report():
    path = "reports/drift_report.html"
    if not os.path.exists(path):
        return HTMLResponse("<h1>Report not found. Please generate it first.</h1>")
    with open(path, "r") as f:
        return HTMLResponse(content=f.read())

@app.get("/download-drift-report")
def download_pdf():
    path = "reports/drift_report.pdf"
    if os.path.exists(path):
        return FileResponse(path, media_type="application/pdf", filename="drift_report.pdf")
    else:
        return {"error": "PDF not found. Run /generate-drift-report first."}


@app.post("/predict")
def get_prediction(data: InputData):
    input_dict = data.dict()
    prediction = predict_salary(input_dict)

    # Save to live_data.csv
    new_row = {
        "experience": input_dict["experience"],
        "education": input_dict["education"],
        "job_title": input_dict["job_title"],
        "salary": prediction
    }

    file_path = "data/live_data.csv"
    df = pd.DataFrame([new_row])

    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, index=False)

    return {"predicted_salary": prediction}
