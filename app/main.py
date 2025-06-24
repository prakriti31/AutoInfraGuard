from fastapi import FastAPI
from pydantic import BaseModel
from app.predict import predict_salary

app = FastAPI()  # ← This is what Uvicorn is looking for

class InputData(BaseModel):
    experience: int
    education: str
    job_title: str

@app.post("/predict")
def get_prediction(data: InputData):
    result = predict_salary(data.dict())
    return {"predicted_salary": result}
