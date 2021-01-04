import math


def signs(percent):
    digit = percent % 10
    if digit < 3:
        return "-"
    elif digit < 7:
        return ""
    else:
        return "+"


def percent_to_grade(percent, *, suffix=False, round=False):
    if round:
        if percent % 1 < 0.5:
            percent = math.floor(percent)
        else:
            percent = math.ceil(percent)
    if percent < 60:
        grade = "F"
    elif percent < 70:
        grade = "D"
    elif percent < 80:
        grade = "C"
    elif percent < 90:
        grade = "B"
    else:
        grade = "A"

    if suffix:
        if percent < 60:
            sign = ""
        elif percent < 100:
            sign = signs(percent)
        else:
            sign = "+"
        return grade + sign
    else:
        return grade


def calculate_gpa(grades):
    grade_to_point = {
        "A+": 4.33,
        "A": 4.00,
        "A-": 3.67,
        "B+": 3.33,
        "B": 3.00,
        "B-": 2.67,
        "C+": 2.33,
        "C": 2.00,
        "C-": 1.67,
        "D+": 1.33,
        "D": 1.00,
        "D-": 0.67,
        "F": 0.00,
    }

    total = 0
    for grade in grades:
        total += grade_to_point.get(grade)
    prom = total / len(grades)
    return prom

