# Python String Datatype
# Data Science with Python - Part 1


# 1. String Examples

name = "Sagar"
college = 'ABC College'
message = """Welcome to Python Programming"""

print("String Examples:")
print(name)
print(college)
print(message)


# 2. Indexing

text = "PYTHON"

print("\nIndexing:")
print(text[0])
print(text[2])
print(text[5])


# 3. Negative Indexing

print("\nNegative Indexing:")
print(text[-1])
print(text[-2])


# 4. Slicing

print("\nSlicing:")
print(text[0:3])
print(text[2:5])
print(text[:4])
print(text[3:])


# 5. Concatenation

first = "Hello"
second = "Python"

result = first + " " + second

print("\nConcatenation:")
print(result)


# 6. Repetition

text2 = "Hi "

print("\nRepetition:")
print(text2 * 3)


# 7. Sentence Analysis

sentence = input("\nEnter a sentence: ")

characters = len(sentence)
words = len(sentence.split())

vowels = 0
consonants = 0

for ch in sentence:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of characters:", characters)
print("Number of words:", words)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)


# 8. String Methods

text = "Python Programming"

print("\nString Methods:")

print("upper():", text.upper())
print("lower():", text.lower())
print("strip():", text.strip())

text_replace = "I like Java"
print("replace():", text_replace.replace("Java", "Python"))

text_split = "Python is easy"
print("split():", text_split.split())

words_list = ["Python", "is", "easy"]
print("join():", " ".join(words_list))

print("find():", text.find("Program"))

text_count = "banana"
print("count():", text_count.count("a"))

print("startswith():", text.startswith("Python"))
print("endswith():", text.endswith("Programming"))


# 9. Student Information String Processing and Validation

print("\n----- Student Information -----")

student_name = input("Enter student's name: ").strip()
email = input("Enter email: ").strip()
department = input("Enter department: ").strip()
college_name = input("Enter college name: ").strip()

# Basic processing
student_name = student_name.title()
department = department.upper()
college_name = college_name.title()
email = email.lower()

# Validation
name_valid = student_name.replace(" ", "").isalpha()
email_valid = "@" in email and "." in email
department_valid = len(department) > 0
college_valid = len(college_name) > 0

print("\n----- Student Details -----")
print("Name:", student_name)
print("Email:", email)
print("Department:", department)
print("College:", college_name)

print("\n----- Validation -----")

if name_valid:
    print("Name: Valid")
else:
    print("Name: Invalid")

if email_valid:
    print("Email: Valid")
else:
    print("Email: Invalid")

if department_valid:
    print("Department: Valid")
else:
    print("Department: Invalid")

if college_valid:
    print("College: Valid")
else:
    print("College: Invalid")