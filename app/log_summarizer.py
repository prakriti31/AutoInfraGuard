import re
import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

def extract_errors(log_path):
    with open(log_path, 'r') as f:
        lines = f.readlines()

    errors, warnings, stacktraces = [], [], []
    current_stack = []

    for line in lines:
        if "Traceback" in line or line.strip().startswith("File "):
            current_stack.append(line)
        elif current_stack:
            current_stack.append(line)
            if re.match(r'^\s*\w*Error:.*$', line):
                stacktraces.append("".join(current_stack))
                current_stack = []
        elif "error" in line.lower():
            errors.append(line)
        elif "warning" in line.lower():
            warnings.append(line)

    return errors, warnings, stacktraces


def generate_summary(log_path):
    errors, warnings, stacks = extract_errors(log_path)

    summary = {
        "filename": os.path.basename(log_path),
        "error_count": len(errors),
        "warning_count": len(warnings),
        "stacktrace_count": len(stacks),
        "errors": errors[:5],  # Top 5
        "warnings": warnings[:5],
        "stacktraces": stacks[:3],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return summary


def generate_log_summary_report(log_path, out_path="reports/log_summary.html"):
    env = Environment(loader=FileSystemLoader("app"))
    template = env.get_template("log_summary_template.html")

    summary = generate_summary(log_path)
    rendered = template.render(summary=summary)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        f.write(rendered)

    print(f"✅ Log summary report generated at {out_path}")
