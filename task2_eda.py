"""
Task 2: Exploratory Data Analysis (EDA)
Run this after Task 1: python task2_eda.py
Input: output/cleaned_data.csv
Outputs: output/eda_*.png and output/task2_eda_report.txt
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "output" / "cleaned_data.csv"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            "Cleaned dataset not found. Run 'python task1_data_cleaning.py' first."
        )

    data = pd.read_csv(INPUT_FILE)

    # 1. Histogram: distribution of exam scores.
    plt.figure(figsize=(8, 5))
    plt.hist(data["Exam_Score"], bins=8, edgecolor="black")
    plt.title("Distribution of Exam Scores")
    plt.xlabel("Exam Score")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "eda_exam_score_histogram.png", dpi=150)
    plt.close()

    # 2. Bar chart: average exam score by department.
    department_means = data.groupby("Department")["Exam_Score"].mean().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    department_means.plot(kind="bar", edgecolor="black")
    plt.title("Average Exam Score by Department")
    plt.xlabel("Department")
    plt.ylabel("Average Exam Score")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "eda_department_average_bar.png", dpi=150)
    plt.close()

    # 3. Scatter plot: study hours compared with exam score.
    plt.figure(figsize=(8, 5))
    plt.scatter(data["Study_Hours"], data["Exam_Score"])
    plt.title("Study Hours vs Exam Score")
    plt.xlabel("Study Hours")
    plt.ylabel("Exam Score")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "eda_study_hours_scatter.png", dpi=150)
    plt.close()

    # Identify potential outliers in exam scores using the IQR method.
    q1 = data["Exam_Score"].quantile(0.25)
    q3 = data["Exam_Score"].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = data[(data["Exam_Score"] < lower_bound) | (data["Exam_Score"] > upper_bound)]

    correlation = data["Study_Hours"].corr(data["Exam_Score"])
    average_score = data["Exam_Score"].mean()
    highest_department = department_means.index[0]

    report = [
        "TASK 2: EXPLORATORY DATA ANALYSIS (EDA) REPORT",
        "=" * 52,
        f"Number of student records analysed: {len(data)}",
        f"Average exam score: {average_score:.2f}",
        f"Lowest exam score: {data['Exam_Score'].min():.2f}",
        f"Highest exam score: {data['Exam_Score'].max():.2f}",
        f"Department with the highest average exam score: {highest_department} ({department_means.iloc[0]:.2f})",
        f"Correlation between study hours and exam score: {correlation:.2f}",
        "Interpretation: correlation close to +1 indicates a positive relationship; "
        "close to -1 indicates a negative relationship; near 0 indicates a weak linear relationship.",
        f"Potential exam-score outliers using IQR: {len(outliers)}",
        "",
        "Department average exam scores:",
        department_means.round(2).to_string(),
        "",
        "Charts created:",
        "1. eda_exam_score_histogram.png",
        "2. eda_department_average_bar.png",
        "3. eda_study_hours_scatter.png",
        "",
        "Key findings:",
        "- The histogram shows how exam scores are distributed.",
        "- The bar chart compares average exam scores across departments.",
        "- The scatter plot helps inspect the relationship between study hours and exam scores.",
        "- The correlation value gives a numerical summary of the linear relationship.",
        "- IQR is used to flag possible outliers; an outlier should be investigated, not automatically deleted.",
    ]

    report_file = OUTPUT_DIR / "task2_eda_report.txt"
    report_file.write_text("\n".join(report), encoding="utf-8")

    print("Task 2 completed successfully!")
    print(f"EDA report: {report_file}")
    print("Charts saved in:", OUTPUT_DIR)
    print(f"Study-hours/exam-score correlation: {correlation:.2f}")

if __name__ == "__main__":
    main()
