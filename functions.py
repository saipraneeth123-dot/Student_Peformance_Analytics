"""Helper functions for student performance calculations."""

import numpy as np


SUBJECTS = ["Python", "Mathematics", "Statistics", "Database"]


def calculate_total(marks):
    """Return the sum of a student's subject marks."""
    return int(np.sum(marks))


def calculate_average(marks):
    """Return the average mark across the subjects."""
    return round(float(np.mean(marks)), 2)


def get_pass_status(marks, attendance):
    """A student passes when every subject is at least 35 and attendance is 75% or more."""
    for mark in marks:
        if mark < 35:
            return "Fail"

    if attendance < 75:
        return "Fail"

    return "Pass"


def get_grade(average, status):
    """Assign a grade using the average; failed students receive F."""
    if status == "Fail":
        return "F"
    elif average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"
