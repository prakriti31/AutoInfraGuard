import pandas as pd
import random
import numpy as np
from faker import Faker

fake = Faker()

job_titles = [
    "Data Scientist", "ML Engineer", "Software Engineer", "DevOps Engineer",
    "Backend Developer", "AI Researcher", "Cloud Architect", "Data Engineer"
]

education_levels = ["High School", "Bachelor", "Master", "PhD"]

def generate_dataset(n, drift=False):
    data = []
    for _ in range(n):
        title = random.choice(job_titles)
        education = random.choices(education_levels, weights=[1, 4, 3, 2])[0]
        if drift:
            # Make experience skew slightly lower
            exp = max(0, np.random.normal(loc=2, scale=1.5))
        else:
            exp = max(0, np.random.normal(loc=5, scale=2.0))

        # Salary depends on title and experience
        base = {
            "Data Scientist": 120000,
            "ML Engineer": 130000,
            "Software Engineer": 110000,
            "DevOps Engineer": 105000,
            "Backend Developer": 100000,
            "AI Researcher": 135000,
            "Cloud Architect": 140000,
            "Data Engineer": 115000,
        }[title]

        modifier = 1 + (exp / 10) + (0.1 if education == "PhD" else 0)
        salary = round(base * modifier + random.gauss(0, 5000), 2)

        data.append({
            "job_title": title,
            "education": education,
            "experience": round(exp, 1),
            "salary": salary
        })

    return pd.DataFrame(data)

# Create and save
train_df = generate_dataset(10000, drift=False)
live_df = generate_dataset(10000, drift=True)

train_df.to_csv("data/job_data.csv", index=False)
live_df.to_csv("data/live_data.csv", index=False)

print("✅ Datasets generated at data/job_data.csv and data/live_data.csv")
