# Project Documentation: Student Performance Analytics System

## 1. Project title

**Student Performance Analytics System**

Student name: [Enter your name]  
Course: Python with AI  
Institute: EWB Courses  
GitHub repository: [Paste your repository URL here]  
Submission deadline: 15 October 2026

## 2. Objective

The objective of this project is to analyze student marks and attendance with Python. It turns a CSV file into a clear summary of individual and class performance, helping a user identify grades, pass/fail results, strong subjects and top-performing students.

## 3. Technologies used

- **Python:** program flow, variables, conditions, loops and functions.
- **Pandas:** loading the CSV file, organizing records in a DataFrame, grouping data and saving results.
- **NumPy:** calculating totals, averages and numerical summaries.
- **CSV:** storing the student dataset.

## 4. Dataset description

The supplied dataset contains 20 sample student records. Columns include Student ID, Name, Department, Attendance, Python, Mathematics, Statistics and Database. Subject marks and attendance are recorded on a 0–100 scale.

The dataset is included in `students.csv`. The sample data can be replaced with records approved by the trainer, as long as the column names are retained.

## 5. Implementation

1. `main.py` loads the CSV file using `pandas.read_csv()` and checks that required columns are present.
2. `functions.py` contains reusable functions to calculate total marks, average marks, pass/fail status and grade.
3. The program loops through the DataFrame rows and calculates each student's total and average.
4. The pass rule checks that all subject marks are at least 35 and attendance is at least 75%.
5. Grades are assigned using the student's average. A student who fails the pass rule receives grade F.
6. Pandas is used to calculate subject averages, department averages and pass/fail counts.
7. NumPy is used for total, average and overall class-average calculations.
8. The program prints the results in sections and saves the complete calculated table as `student_results.csv`.

## 6. Key features

- Individual student total and average
- Grade and pass/fail result
- Class average, highest average and lowest average
- Number of students passed and failed
- Pass percentage
- Subject-wise average and best-performing subject
- Top performer(s)
- Department-wise average
- Export of calculated results to CSV

## 7. Output / screenshots

When the program runs, it prints student results, class statistics, subject averages, top performers and department averages in the terminal. It also creates `student_results.csv`.

Add a screenshot of your own terminal output here if your trainer requests it.

## 8. Final outcome

The project successfully demonstrates how Python, Pandas and NumPy can be used to process a student dataset and produce understandable academic summaries. It also demonstrates functions, loops, conditions and CSV file handling.

## 9. Challenges and learning

**Use this section to describe your own experience before submitting.** Possible points to consider:

- Keeping the CSV column names consistent with the Python code.
- Applying the same pass/fail rule to every student.
- Using NumPy for numerical calculations and Pandas for table-based analysis.
- Checking the results and understanding why a student received a particular grade.

Edit this section to reflect the challenges you actually faced and what you learned while testing the project.

## 10. GitHub repository

Repository URL: [Paste your public GitHub repository URL here]

Before submission, verify that the Python files, dataset, README and this documentation file are visible in the repository. Submit the repository URL through the Google Form provided by your trainer.
