# student_utils.py

def calculate_percentage(marks):
    total = sum(marks)
    maximum = len(marks) * 100
    return (total / maximum) * 100


def calculate_average(marks):
    return sum(marks) / len(marks)


def find_largest(marks):
    return max(marks)


def check_pass(marks):
    return all(mark >= 35 for mark in marks)


def grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"