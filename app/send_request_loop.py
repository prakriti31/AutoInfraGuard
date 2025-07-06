import time
import random
import requests

URL = "http://localhost:8000/predict"

job_titles = [
    "Data Scientist", "ML Engineer", "Backend Developer",
    "Cloud Architect", "DevOps Engineer", "Software Engineer", "AI Researcher"
]
educations = ["PhD", "Master", "Bachelor", "High School"]

def generate_random_input():
    return {
        "job_title": random.choice(job_titles),
        "education": random.choice(educations),
        "experience": round(random.uniform(0.5, 10), 1)
    }

if __name__ == "__main__":
    print("📡 Sending continuous predictions to FastAPI server...")
    while True:
        data = generate_random_input()
        try:
            res = requests.post(URL, json=data)
            try:
                response_json = res.json()
                print(f"✅ [{res.status_code}] Input: {data} ➡️ Predicted: {response_json}")
            except Exception:
                print(f"❌ [{res.status_code}] Failed to parse JSON. Response: {res.text}")
        except Exception as e:
            print(f"❌ Request failed: {str(e)}")

        time.sleep(2)  # Adjust frequency as needed
