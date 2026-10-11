"""Student Performance Analytics System."""

from pathlib import Path

import numpy as np
import pandas as pd

from functions import SUBJECTS, calculate_average, calculate_total, get_grade, get_pass_status


DATA_FILE = Path(__file__).parent / "students.csv"


def load_data(file_path):
    """Read student records from the CSV file."""
    data = pd.read_csv(file_path)

    required_columns = [
        "Student_ID", "Name", "Department", "Attendance",
        "Python", "Mathematics", "Statistics", "Database"
    ]
    missing_columns = [column for column in required_columns if column not in data.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    if data.empty:
        raise ValueError("The student dataset is empty.")

    return data


def add_results(data):
    """Add total, average, grade and pass/fail columns."""
    result = data.copy()
    totals = []
    averages = []
    statuses = []
    grades = []

    for _, student in result.iterrows():
        marks = [student[subject] for subject in SUBJECTS]
        total = calculate_total(marks)
        average = calculate_average(marks)
        status = get_pass_status(marks, student["Attendance"])
        grade = get_grade(average, status)

        totals.append(total)
        averages.append(average)
        statuses.append(status)
        grades.append(grade)

    result["Total"] = totals
    result["Average"] = averages
    result["Grade"] = grades
    result["Result"] = statuses
    return result


def show_student_results(data):
    """Print each student's calculated result."""
    columns = [
        "Student_ID", "Name", "Department", "Attendance",
        *SUBJECTS, "Total", "Average", "Grade", "Result"
    ]
    print("\n1. STUDENT RESULTS")
    print("-" * 110)
    print(data[columns].to_string(index=False))


def show_class_summary(data):
    """Print the main class statistics."""
    class_average = round(float(np.mean(data["Average"].to_numpy())), 2)
    pass_count = int((data["Result"] == "Pass").sum())
    fail_count = int((data["Result"] == "Fail").sum())

    print("\n2. CLASS SUMMARY")
    print("-" * 40)
    print(f"Number of students : {len(data)}")
    print(f"Class average      : {class_average}")
    print(f"Highest average    : {data['Average'].max():.2f}")
    print(f"Lowest average     : {data['Average'].min():.2f}")
    print(f"Students passed    : {pass_count}")
    print(f"Students failed    : {fail_count}")
    print(f"Pass percentage    : {pass_count / len(data) * 100:.2f}%")


def show_subject_summary(data):
    """Print the average mark for each subject."""
    subject_averages = data[SUBJECTS].mean().round(2)
    print("\n3. SUBJECT-WISE AVERAGE")
    print("-" * 40)
    for subject, average in subject_averages.items():
        print(f"{subject:<15}: {average:.2f}")

    best_subject = subject_averages.idxmax()
    print(f"Best-performing subject: {best_subject} ({subject_averages[best_subject]:.2f})")


def show_top_students(data):
    """Print all students who share the highest average."""
    highest_average = data["Average"].max()
    top_students = data[data["Average"] == highest_average]

    print("\n4. TOP PERFORMER(S)")
    print("-" * 40)
    print(top_students[["Student_ID", "Name", "Department", "Average", "Grade"]].to_string(index=False))


def show_department_summary(data):
    """Print average performance for each department."""
    print("\n5. DEPARTMENT-WISE AVERAGE")
    print("-" * 40)
    department_averages = data.groupby("Department")["Average"].mean().round(2)
    for department, average in department_averages.items():
        print(f"{department:<25}: {average:.2f}")


def main():
    try:
        students = load_data(DATA_FILE)
        results = add_results(students)

        print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
        print("=" * 40)
        show_student_results(results)
        show_class_summary(results)
        show_subject_summary(results)
        show_top_students(results)
        show_department_summary(results)

        output_file = DATA_FILE.parent / "student_results.csv"
        results.to_csv(output_file, index=False)
        print(f"\nCalculated results saved to: {output_file.name}")

    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        print(f"Could not run the analysis: {error}")


if __name__ == "__main__":
    main()
