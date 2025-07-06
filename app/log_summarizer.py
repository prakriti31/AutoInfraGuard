import re
import os
import openai
from jinja2 import Environment, FileSystemLoader
from utils_llms import suggest_fix_for_error

# Basic categorization by pattern
def classify_error_type(message):
    if 'ImportError' in message:
        return 'ImportError'
    if 'ModuleNotFoundError' in message:
        return 'DependencyError'
    if 'FileNotFoundError' in message:
        return 'IOError'
    if 'ValueError' in message:
        return 'ValueError'
    if 'TypeError' in message:
        return 'TypeError'
    if 'ConnectionError' in message:
        return 'ConnectionError'
    if 'TimeoutError' in message:
        return 'Timeout'
    return 'Unknown'


def extract_errors(log_path):
    errors = []
    warnings = []
    tracebacks = []
    current_trace = []
    in_traceback = False

    with open(log_path, 'r') as f:
        for line in f:
            if 'Traceback' in line:
                in_traceback = True
                current_trace = [line]
            elif in_traceback and (line.startswith(" ") or line.startswith("    ")):
                current_trace.append(line)
            elif in_traceback:
                current_trace.append(line)
                tracebacks.append("".join(current_trace))
                in_traceback = False

            if 'ERROR' in line:
                errors.append(line)
            if 'WARNING' in line:
                warnings.append(line)

    return errors, warnings, tracebacks


def generate_summary(log_path):
    errors, warnings, tracebacks = extract_errors(log_path)

    classified_errors = []
    for error in errors:
        error_type = classify_error_type(error)
        suggestion = suggest_fix_for_error(error)
        classified_errors.append({
            "message": error,
            "type": error_type,
            "suggestion": suggestion
        })

    return {
        "errors": classified_errors,
        "warnings": warnings,
        "tracebacks": tracebacks,
        "log_file": os.path.basename(log_path)
    }


def generate_log_summary_report(log_path):
    env = Environment(loader=FileSystemLoader("app"))
    template = env.get_template("log_summary_template.html")
    summary = generate_summary(log_path)

    report_html = template.render(summary=summary)

    os.makedirs("reports", exist_ok=True)
    report_path = os.path.join("reports", "log_summary.html")
    with open(report_path, "w") as f:
        f.write(report_html)

    print(f"✅ Log summary report saved at {report_path}")
