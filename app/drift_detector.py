import pandas as pd
import os
import base64
import io
from scipy.stats import ks_2samp, chi2_contingency
import seaborn as sns
import matplotlib.pyplot as plt
from jinja2 import Environment, FileSystemLoader
import pdfkit

def generate_combined_drift_report(train_path, live_path, output_html_path):
    df_train = pd.read_csv(train_path)
    df_live = pd.read_csv(live_path)

    report_data = []
    image_data = []

    for col in df_train.columns:
        # Drift Detection
        if df_train[col].dtype == 'object':
            contingency = pd.crosstab(df_train[col], df_live[col])
            try:
                chi2, p, _, _ = chi2_contingency(contingency)
            except:
                p = 1.0
            test_type = "Chi-Square"
        else:
            stat, p = ks_2samp(df_train[col], df_live[col])
            test_type = "Kolmogorov-Smirnov"

        drifted = p < 0.05
        report_data.append({
            "feature": col,
            "test": test_type,
            "p_value": round(p, 4),
            "drifted": "Yes" if drifted else "No"
        })

        # Plot Generation (Base64)
        fig, ax = plt.subplots(figsize=(6, 4))

        if df_train[col].dtype == 'object':
            train_counts = df_train[col].value_counts(normalize=True)
            live_counts = df_live[col].value_counts(normalize=True)
            all_categories = sorted(set(train_counts.index).union(live_counts.index))
            train_vals = [train_counts.get(cat, 0) for cat in all_categories]
            live_vals = [live_counts.get(cat, 0) for cat in all_categories]
            x = range(len(all_categories))

            ax.bar(x, train_vals, width=0.4, label='Train', align='center')
            ax.bar([i + 0.4 for i in x], live_vals, width=0.4, label='Live', align='center')
            ax.set_xticks([i + 0.2 for i in x])
            ax.set_xticklabels(all_categories, rotation=45)
            ax.set_ylabel("Proportion")
        else:
            sns.kdeplot(df_train[col], label='Train', fill=True, ax=ax, alpha=0.5)
            sns.kdeplot(df_live[col], label='Live', fill=True, ax=ax, alpha=0.5)
            ax.set_xlabel(col)
            ax.set_ylabel("Density")

        ax.set_title(f"Distribution: {col}")
        ax.legend()
        plt.tight_layout()

        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode("utf-8")
        buffer.close()
        plt.close()

        image_data.append({
            "feature": col,
            "image": image_base64
        })

    # Render HTML
    env = Environment(loader=FileSystemLoader("app"))
    template = env.get_template("template.html")
    rendered = template.render(features=report_data, images=image_data)

    os.makedirs(os.path.dirname(output_html_path), exist_ok=True)
    with open(output_html_path, "w") as f:
        f.write(rendered)

    print(f"✅ Combined drift report saved at {output_html_path}")
