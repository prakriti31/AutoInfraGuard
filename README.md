# AutoInfraGuard
Self-Healing ML Pipeline Debugger for Production Systems


## 🔥 Project Idea: **AutoInfraGuard – Self-Healing ML Pipeline Debugger for Production Systems**

### 🔍 What it is:

A **self-healing, explainable ML infra watchdog** that detects, diagnoses, and recovers failing stages in large-scale ML pipelines (e.g., feature drift, data skew, stale models, training-serving skew), **with NLP-powered root-cause explanations** and automatic recovery workflows.

### 🧠 Why it's valuable:

Most ML infra teams (like LinkedIn's) struggle with:

* Hidden bugs in production pipelines
* Model degradation over time
* Lack of explainability for failures
* Tedious debugging of pipeline stages

This solves **real pain points** and shows a **unique blend** of:

* Infra engineering (monitoring, alerting, containerization)
* ML ops (tracking drift/skew, model freshness)
* NLP (interpreting logs, summarizing errors)
* Autonomy (automated fixes or recommendations)

---

## 🛠️ Core Features:

1. **Live Monitoring Layer**:

   * Hooks into ML pipeline components (e.g., feature store, model trainer, inference service)
   * Tracks anomalies in input distributions, training/serving skew, latency, and failure rates

2. **Explainable Error Layer (NLP)**:

   * Uses transformer-based summarizers on logs (e.g., BART or Longformer)
   * Classifies and ranks root causes
   * Auto-generates natural language "postmortems"

3. **Auto-Recovery/Recommendation Layer**:

   * Restarts stages, clears caches, retriggers model training, or suggests interventions
   * Uses rules + lightweight RL to learn optimal fixes

4. **Dashboard + Alerts**:

   * Visualizes drift, errors, model freshness, infra metrics
   * Slack/email alerts with English explanations

---

## 💡 Novelty:

* Not just a monitoring tool—**it self-heals**
* Combines **infra + ML + NLP** in one package
* Auto-explains *why* your pipeline broke, like a junior infra engineer
* Could plug into **LinkedIn’s Feature Store or Unified AI Infra**

---

## 🔧 Tech Stack:

* **Languages**: Python, Go (optional for speed)
* **ML**: scikit-learn, XGBoost, transformers (HuggingFace), Prometheus
* **Infra**: Docker, Kubernetes, Apache Airflow, MLflow, Grafana
* **NLP**: Log summarization using fine-tuned transformer models
* **Serving**: FastAPI or gRPC for API endpoints
* **Database**: PostgreSQL for logs and metrics, Redis for quick lookups

---

## 📈 Bonus:

* Add **LinkedIn API integration** to monitor scraping or spam detection systems
* Open-source it as a plug-in tool for Airflow or Kubeflow → **community impact**

---

Absolutely. Here's a **step-by-step implementation roadmap** to build **AutoInfraGuard**, broken down into **phases with specific tasks**, so you can steadily build and show off this powerful project.

---

## 🧱 PHASE 1: Setup a Simulated ML Pipeline (Baseline)

### ✅ Goal:

Build a minimal, modular ML pipeline you can later debug and monitor.

### 🛠️ Tasks:

1. **Choose a small ML task** (e.g., job title prediction, salary estimation, etc.)
2. Create a pipeline with:

   * Data ingestion (CSV/streaming)
   * Feature engineering
   * Model training (scikit-learn or XGBoost)
   * Inference API (FastAPI or Flask)
3. Containerize it with **Docker**.
4. Add **Airflow/Kubeflow** or even custom DAG logic to simulate a real pipeline.
5. Store metrics (latency, drift, etc.) in **Prometheus** or **SQLite/Postgres**.

---

## 🧠 PHASE 2: Drift & Skew Detector

### ✅ Goal:

Detect model drift and training-serving skew.

### 🛠️ Tasks:

1. Add a **feature distribution tracker** using:

   * JS divergence / Wasserstein distance
   * Compare training vs. live data
2. Monitor:

   * Data type mismatches
   * Missing features
   * Unexpected value ranges
3. Add a small **Grafana dashboard** to visualize distributions.

💡 **Tools**: `evidently`, `river`, `scikit-multiflow`, `drift-detection methods` (DDM, ADWIN)

---

## 🔍 PHASE 3: NLP-Powered Log Summarizer

### ✅ Goal:

Use NLP to summarize errors/failures in natural language.

### 🛠️ Tasks:

1. Log different pipeline errors: data schema mismatches, model failure, timeouts
2. Store logs in a structured form
3. Train/fine-tune an NLP summarizer:

   * Use a BART or T5 model on synthetic logs + explanations
   * Alternatively use prompt-based summarization (OpenAI, Claude, etc.)
4. Output:

   * English explanation of what failed
   * Suggested causes

💡 Dataset idea: create a small JSON dataset of errors → explanations, then fine-tune a model.

---

## 🤖 PHASE 4: Auto-Recovery Engine

### ✅ Goal:

Build logic to auto-fix or recommend fixes.

### 🛠️ Tasks:

1. Define **trigger conditions** (e.g., drift threshold > 0.2)
2. Define **action mappings**:

   * Drift → retrain model
   * Schema mismatch → rollback to previous schema
   * Crash → restart Docker container
3. Implement in logic in Python with Airflow hooks or shell scripts
4. Optional: use **Reinforcement Learning (Q-learning)** to improve fix choice over time

---

## 📊 PHASE 5: Alerting and Dashboard

### ✅ Goal:

Visual + Alert system to monitor everything.

### 🛠️ Tasks:

1. Connect pipeline + metrics to **Prometheus**
2. Build Grafana dashboard:

   * Drift timelines
   * Failure rates
   * Model freshness
3. Integrate email/Slack alerts with natural language summaries

---

## 🌐 Bonus PHASE 6: LinkedIn Relevance Layer

> Showcase you understand LinkedIn’s mission!

### 🛠️ Ideas:

* Integrate with **LinkedIn job data** (via scraping or Open Data) and use your infra to debug a job-matching model
* Add a “resume score predictor” and track drift over time (seasonal skills)
* Build an ML system to auto-detect spam comments/posts (simulate trust & safety)

---

## 🧪 Tech Stack Summary:

| Layer          | Tooling                                     |
| -------------- | ------------------------------------------- |
| Pipeline Logic | Airflow/Kubeflow + Docker                   |
| Model/ML       | scikit-learn, XGBoost, PyTorch, HuggingFace |
| Monitoring     | Prometheus + Grafana                        |
| NLP            | BART, T5, LLM APIs (OpenAI/Claude)          |
| Recovery Logic | Python Rules Engine or RL + Bash            |
| Infra          | FastAPI, Flask, Kubernetes (optional)       |
| Storage        | PostgreSQL, Redis, S3 (optional)            |

---

## 🎯 Deliverables by End:

* GitHub repo with full infra + logs + NLP
* Screencast or demo video (2–3 mins)
* PDF project architecture + a Notion-style design doc
* Optional: Deploy on GCP or AWS (bonus points)

---

Here’s a clean and concise **README** section with instructions to run **Phase 1** of your **AutoInfraGuard** project.

---

## 🚀 AutoInfraGuard – Phase 1: ML Pipeline with FastAPI

This phase sets up a simple modular ML pipeline for predicting salary based on job title, education, and experience. It includes model training, an inference API using FastAPI, and Docker support.

---

## 📁 Project Structure

```
AutoInfraGuard/
├── app/
│   ├── inference_api.py       # FastAPI server with prediction & metrics API
│   ├── metrics_logger.py      # Logs prediction metrics to SQLite DB
│   ├── send_request_loop.py   # Simulates continuous POST requests to /predict
├── data/
│   └── job_data.csv           # Training data
├── models/
│   └── salary_model.pkl       # Saved ML pipeline with schema
├── monitoring/
│   └── metrics.db             # SQLite DB with 'predictions' table
├── Dockerfile
├── requirements.txt
├── train_model.py             # Trains and exports the model
└── README.md                  # Project guide (this file)
```

---

## 🧠 1. Train the Model

Before anything, train the model using the provided data.

```bash
python train_model.py
```

This will create:

* `models/salary_model.pkl` (scikit-learn pipeline)
* Logs schema columns for encoding consistency

---

## 🚀 2. Run FastAPI Server

Start the API server:

```bash
uvicorn app.inference_api:app --reload --port 8000
```

This will expose:

| Endpoint   | Method | Description                      |
| ---------- | ------ | -------------------------------- |
| `/predict` | POST   | Make a salary prediction         |
| `/metrics` | GET    | View last 10 predictions from DB |

---

## 🧪 3. Make a Test Prediction

Use `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"job_title": "Data Scientist", "education": "PhD", "experience": 4.7}'
```

✅ This will:

* Return a predicted salary
* Log the prediction in `monitoring/metrics.db` if logging is enabled

---

## 📊 4. Enable Logging (Metrics DB)

The system logs all predictions to a SQLite database table named `predictions`.

### 🔁 To simulate and test prediction logging:

```bash
python app/send_request_loop.py
```

This will send continuous mock requests to the server and log them.

---

## 📂 5. View Logs from SQLite

You can directly inspect the logged data:

```bash
sqlite3 monitoring/metrics.db
sqlite> SELECT * FROM predictions;
```

Each entry contains:

* Timestamp
* Input payload (job title, education, experience)
* Predicted salary

---

## 🐳 6. Run with Docker

### 🧱 Build Docker Image

```bash
docker build -t autoinfraguard .
```

### ▶️ Run Container

```bash
docker run -p 8000:8000 autoinfraguard
```

By default, Docker runs the FastAPI server inside the container.

### 🔄 Send Test Request

On your host machine:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"job_title": "ML Engineer", "education": "Bachelor", "experience": 3.5}'
```

---

## ⚙️ Dockerfile

Make sure your `Dockerfile` looks like this:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.inference_api:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 📦 requirements.txt

```txt
fastapi
uvicorn
pydantic
scikit-learn
joblib
pandas
requests
```

---

## 🔐 Notes

* SQLite file (`monitoring/metrics.db`) must persist across restarts if using Docker (use volumes).
* You can mount `monitoring/` as a volume:

  ```bash
  docker run -p 8000:8000 -v $(pwd)/monitoring:/app/monitoring autoinfraguard
  ```

---

## ✅ Optional: Reset DB Table

```bash
sqlite3 monitoring/metrics.db

sqlite> DROP TABLE IF EXISTS predictions;

sqlite> CREATE TABLE predictions (
  timestamp TEXT,
  job_title TEXT,
  education TEXT,
  experience REAL,
  predicted_salary REAL
);
```

---

## 📬 API Reference

### `/predict` — POST

**Input JSON**:

```json
{
  "job_title": "Data Scientist",
  "education": "PhD",
  "experience": 4.7
}
```

**Response JSON**:

```json
{
  "predicted_salary": 188340.35
}
```

---

### `/metrics` — GET

**Returns** last 10 logged predictions.

```json
[
  {
    "timestamp": "2025-07-06T13:44:32.318264",
    "job_title": "ML Engineer",
    "education": "Bachelor",
    "experience": 3.5,
    "predicted_salary": 183423.64
  },
  ...
]
```

---

## 🧹 Troubleshooting

| Issue                             | Fix                                                        |
| --------------------------------- | ---------------------------------------------------------- |
| `table predictions has no column` | Drop and recreate table manually (see above)               |
| `/metrics` returns empty          | Ensure `/predict` is called and logging is enabled         |
| Docker SQLite DB empty            | Use `-v $(pwd)/monitoring:/app/monitoring` to persist data |
| Continuous logging not happening  | Run `send_request_loop.py` script or manually POST         |
| `model["model"].predict` fails    | Ensure input encoding matches training pipeline            |

---

Great! Here's a clean and professional section you can add to your `README.md` to explain how to run the **logging-enabled training phase** in your project:

---

## 📝 How to Run: Model Training with Real-Time Logging

### 🛠️ Train the Model

Navigate to the project root and run the model training using:

```bash
python -m app.train_model
```

This will:

* Load training data from `data/job_data.csv`
* Train a `LinearRegression` model
* Save the model to `models/salary_model.pkl`
* Log progress and errors to `logs/train.log` in real-time

### 📡 Live Log Monitoring (Optional)

To watch logs update in real time:

```bash
tail -f logs/train.log
```

---

### 🗂️ Output Files

| File                      | Description                            |
| ------------------------- | -------------------------------------- |
| `models/salary_model.pkl` | Trained model pipeline (with metadata) |
| `logs/train.log`          | Log file with real-time training logs  |


1. ✅ Run the summarizer:

```bash
python -m app.log_summarizer logs/sample.log
```

2. ✅ Open the generated HTML report:

```bash
open reports/log_summary.html  # macOS
# Or: start reports/log_summary.html  # Windows
```

---

### 🔐 Set Your OpenAI Key

Create a `.env` file or export the key:

```bash
export OPENAI_API_KEY=sk-xxxx
```

---

### 💡 Example Output

✅ Clean, visual report like:

```
📄 Log Summary: sample.log

❌ Errors (3)
- ImportError: cannot import name X
  💡 Fix Suggestion: Try using 'from module import Y' instead...

⚠️ Warnings (2)
- Deprecated API used...

📘 Tracebacks (1)
- File "abc.py", line 24...
```

---

### 🛠️ Dependencies

```bash
pip install openai jinja2
```

---

Here’s your updated **README section for Phase 5: Self-Healing Automation** for your **AutoInfraGuard** project:

---

## 🧠 Phase 5: Self-Healing Automation

AutoInfraGuard now supports **automatic root cause analysis (RCA)** and **self-healing actions** based on log diagnostics. It attempts to classify and fix pipeline errors using LLMs and rule-based strategies.

---

### ✅ Features

* Runs RCA on the latest logs
* Classifies and extracts root causes
* Suggests fixes using OpenAI (LLM-powered)
* Executes auto-healing logic for certain issues
* Logs actions and flags manual intervention when needed

---

### 🛠️ How to Run Phase 5

Ensure your `.env` contains your OpenAI key:

```bash
OPENAI_API_KEY=sk-xxxxx...
```

Ensure your virtual environment is activated:

```bash
source venv/bin/activate
```

Then run the self-healer:

```bash
python -m app.auto_healer
```

This will:

* Parse the latest logs from `logs/sample.log`
* Generate an RCA report at `reports/rca_report.html`
* Apply automated fixes for:

  * **Missing values**
  * **Known inference errors**
* Log unresolved issues for manual review

---

### 📂 Project Files Used in This Phase

| File                              | Purpose                                |
| --------------------------------- | -------------------------------------- |
| `app/auto_healer.py`              | Main controller for RCA + self-healing |
| `app/rca_engine.py`               | Log summarization and LLM-powered RCA  |
| `app/templates/rca_template.html` | HTML template for RCA report           |
| `logs/sample.log`                 | Source logs for RCA                    |
| `reports/rca_report.html`         | Output RCA report                      |

---

### 🔁 Example Output

```text
[INFO] ✅ RCA report saved at reports/rca_report.html
[INFO] ℹ️ Manual review needed for issue: ValueError: could not convert string to float: 'N/A'
```

---

### 🧩 Customizing

You can customize which types of issues are auto-healed vs. flagged in `app/auto_healer.py` by editing the rule logic inside the `auto_heal()` function.

---
