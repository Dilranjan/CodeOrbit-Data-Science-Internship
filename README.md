# CodeOrbit Tech – Data Science Internship (Tasks 1 and 2)

This beginner-friendly project completes the two tasks selected from the CodeOrbit Tech Data Science Internship PDF.

## Files
- `students_sample.csv` – sample student dataset. It intentionally contains missing values, one duplicate row and invalid numeric text so the cleaning task has something to process.
- `task1_data_cleaning.py` – cleans the CSV using pandas, calculates mean/median and value counts, and creates a short report.
- `task2_eda.py` – performs EDA on the cleaned dataset and creates a histogram, bar chart and scatter plot.
- `requirements.txt` – required Python libraries.

## Setup (VS Code terminal)
Open this folder in VS Code, then run:

```bash
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt**
```bat
.venv\Scripts\activate.bat
```

Install libraries:
```bash
python -m pip install -r requirements.txt
```

## Run in this order
```bash
python task1_data_cleaning.py
python task2_eda.py
```

Both scripts create an `output` folder automatically. Task 1 creates the cleaned CSV and report. Task 2 creates three PNG charts and its report.

## Before submission
1. Run both scripts and check that the `output` folder contains all generated files.
2. Read the reports and make sure you can explain each cleaning step and chart.
3. Keep the scripts, original CSV, cleaned CSV, reports and charts in your project folder.
4. Upload the project to GitHub or Google Drive using the folder naming format specified by your internship instructions: `CodeOrbit_ProjectName`.
5. The internship PDF also asks for a short LinkedIn video explanation for at least one project and submission through the form shared in the WhatsApp group.

Note: This is a sample learning dataset, not real student data. Review the generated findings after running the scripts before submitting.
