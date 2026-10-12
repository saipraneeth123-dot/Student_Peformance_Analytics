

import numpy as np


SUBJECTS = ["Python", "Mathematics", "Statistics", "Database"]


def calculate_total(marks):
   
    return int(np.sum(marks))


def calculate_average(marks):
    return round(float(np.mean(marks)), 2)


def get_pass_status(marks, attendance):
    for mark in marks:
        if mark < 35:
            return "Fail"

    if attendance < 75:
        return "Fail"

    return "Pass"


def get_grade(average, status):
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
