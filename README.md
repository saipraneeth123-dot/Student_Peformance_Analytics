# Student Performance Analytics System

A beginner-friendly Python project that reads student marks from a CSV file and summarizes academic performance using Pandas and NumPy.

## Features

- Reads student records from `students.csv` into a Pandas DataFrame.
- Calculates total and average marks for each student.
- Assigns grades and a pass/fail result.
- Shows the class average, highest and lowest averages, pass count and fail count.
- Compares average marks by subject and department.
- Lists the top-performing student or students.
- Saves the calculated results to `student_results.csv`.

## Tools used

- Python
- Pandas
- NumPy

## Dataset

The included dataset has 20 sample students. Each record includes student ID, name, department, attendance, and marks in Python, Mathematics, Statistics and Database. The sample names and scores are for demonstration; replace them with your own data if required.

## Rules used

### Pass or fail

A student passes only when:
1. Every subject mark is at least 35 out of 100.
2. Attendance is at least 75%.

Otherwise, the student is marked as `Fail`.

### Grades

Grades are based on the average mark, but a failed student receives `F`.

| Average | Grade |
| --- | --- |
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

## Project structure

```text
student-performance-analytics/
├── main.py
├── functions.py
├── students.csv
├── requirements.txt
├── README.md
├── Project_Documentation.md
└── .gitignore
```

`student_results.csv` is created automatically when the program runs.

## How to run

### 1. Install Python

Install Python 3.10 or newer from https://www.python.org/downloads/. On Windows, select **Add Python to PATH** during installation.

### 2. Open the project folder

Open a terminal in this folder.

### 3. Create and activate a virtual environment (recommended)

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bat
py -m venv .venv
.venv\Scripts\activate.bat
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

Windows:

```powershell
py -m pip install -r requirements.txt
```

macOS/Linux:

```bash
python3 -m pip install -r requirements.txt
```

### 5. Run the program

Windows:

```powershell
py main.py
```

macOS/Linux:

```bash
python3 main.py
```

The analysis is printed in the terminal, and the calculated student table is saved to `student_results.csv`.

## Concepts demonstrated

Variables and data types, lists, loops, conditional statements, functions, NumPy calculations, Pandas DataFrames, filtering, grouping and CSV file handling.

## GitHub submission

1. Create a public repository named `student-performance-analytics` (or use the visibility required by your trainer).
2. Upload `main.py`, `functions.py`, `students.csv`, `requirements.txt`, `README.md`, `Project_Documentation.md`, and `.gitignore`.
3. Commit and push your files.
4. Open the repository page and check that the files are visible.
5. Copy the repository URL into the EWB Courses Google Form. Use the actual form link provided by your trainer; it is not included here.

## Before submitting

- Run the program on your own computer.
- Read through the code and make sure you can explain the pass rule, grade rule, functions, loop and subject analysis.
- Replace the sample records or personalize the project if your trainer expects your own dataset.
- Add your name, course details and actual GitHub URL to the documentation.
- Add screenshots of your own program output if requested.
