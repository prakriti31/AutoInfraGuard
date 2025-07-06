import re
import os
import openai
from dotenv import load_dotenv
from app.logger import get_logger
from jinja2 import Environment, FileSystemLoader

load_dotenv()
logger = get_logger("rca_engine")

# Configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Root cause classifier
def classify_root_cause(error_message: str) -> str:
    if "No such file or directory" in error_message or "FileNotFoundError" in error_message:
        return "Config Issue"
    elif "KeyError" in error_message or "missing" in error_message.lower():
        return "Data Issue"
    elif "ModuleNotFoundError" in error_message or "ImportError" in error_message:
        return "Code Issue"
    elif "MemoryError" in error_message or "CUDA" in error_message:
        return "Infrastructure Issue"
    return "Unknown"

# LLM-powered suggestion
def suggest_fix(error_message: str) -> str:
    try:
        prompt = f"Explain this error and suggest a fix:\n{error_message}"
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"❌ LLM suggestion failed: {e}")
        return "No suggestion available."

# Main RCA report generator
def generate_rca_report(log_path, output_path="reports/rca_report.html"):
    with open(log_path, "r") as f:
        lines = f.readlines()

    errors = [line.strip() for line in lines if "Error" in line or "Exception" in line]
    rca_results = []

    for err in errors:
        category = classify_root_cause(err)
        suggestion = suggest_fix(err)
        rca_results.append({
            "error": err,
            "category": category,
            "suggestion": suggestion
        })

    # Jinja2 template loading
    template_path = os.path.join(os.path.dirname(__file__), "rca_template.html")
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
    template = env.get_template("rca_template.html")

    html = template.render(errors=rca_results, log_file=log_path)
    os.makedirs("reports", exist_ok=True)
    with open(output_path, "w") as f:
        f.write(html)

    logger.info(f"✅ RCA report saved at {output_path}")
    return rca_results  # 🔁 RETURN the parsed issues

# Exposed callable
def run_rca(log_path: str = "logs/sample.log", output_path: str = "reports/rca_report.html") -> list:
    return generate_rca_report(log_path, output_path)
