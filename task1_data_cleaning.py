"""
Task 1: Data Cleaning & Exploration with Pandas
Run: python task1_data_cleaning.py
Input: students_sample.csv (included in this folder)
Outputs: output/cleaned_data.csv and output/task1_report.txt
"""
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "students_sample.csv"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {INPUT_FILE}")

    data = pd.read_csv(INPUT_FILE)
    original_rows = len(data)

    # Remove exact duplicate rows.
    duplicate_count = int(data.duplicated().sum())
    data = data.drop_duplicates().copy()

    # Convert numeric columns. Invalid text (for example, 'twenty') becomes missing.
    numeric_columns = ["Age", "Study_Hours", "Attendance", "Exam_Score"]
    for column in numeric_columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    missing_before = data.isna().sum()

    # Fill numeric missing values with each column's median.
    for column in numeric_columns:
        median_value = data[column].median()
        data[column] = data[column].fillna(median_value)

    # Fill missing categorical/text values with the most frequent value.
    for column in ["Name", "Department"]:
        if data[column].isna().any():
            mode_values = data[column].mode()
            fill_value = mode_values.iloc[0] if not mode_values.empty else "Unknown"
            data[column] = data[column].fillna(fill_value)

    # Save the cleaned dataset.
    cleaned_file = OUTPUT_DIR / "cleaned_data.csv"
    data.to_csv(cleaned_file, index=False)

    # Basic statistics and value counts.
    numeric_summary = data[numeric_columns].agg(["mean", "median"]).T
    department_counts = data["Department"].value_counts()

    report_lines = [
        "TASK 1: DATA CLEANING & EXPLORATION REPORT",
        "=" * 48,
        f"Original rows: {original_rows}",
        f"Duplicate rows removed: {duplicate_count}",
        f"Rows after duplicate removal: {len(data)}",
        "",
        "Missing/invalid values detected before filling:",
        missing_before.to_string(),
        "",
        "Cleaning steps applied:",
        "1. Loaded the CSV dataset using pandas.",
        "2. Removed exact duplicate rows.",
        "3. Converted Age, Study_Hours, Attendance and Exam_Score to numeric data types.",
        "4. Replaced invalid numeric text with missing values.",
        "5. Filled missing numeric values with the column median.",
        "6. Filled missing text values with the most frequent value.",
        "7. Saved the cleaned dataset as output/cleaned_data.csv.",
        "",
        "Mean and median:",
        numeric_summary.round(2).to_string(),
        "",
        "Department value counts:",
        department_counts.to_string(),
        "",
        f"Final row count: {len(data)}",
        f"Remaining missing values: {int(data.isna().sum().sum())}",
    ]

    report_file = OUTPUT_DIR / "task1_report.txt"
    report_file.write_text("\n".join(report_lines), encoding="utf-8")

    print("Task 1 completed successfully!")
    print(f"Cleaned dataset: {cleaned_file}")
    print(f"Report: {report_file}")
    print("\nMean and median:\n", numeric_summary.round(2))
    print("\nDepartment counts:\n", department_counts)

if __name__ == "__main__":
    main()
