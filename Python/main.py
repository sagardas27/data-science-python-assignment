# main.py

import student_utils

marks = [80, 75, 90, 85, 70]

percentage = student_utils.calculate_percentage(marks)
average = student_utils.calculate_average(marks)
largest = student_utils.find_largest(marks)
passed = student_utils.check_pass(marks)
grade = student_utils.grade(percentage)

print("Marks:", marks)
print("Percentage:", percentage)
print("Average:", average)
print("Highest Mark:", largest)
print("Passed:", passed)
print("Grade:", grade)