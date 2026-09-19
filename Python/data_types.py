# Python Data Types
# Data Science with Python - Part 1


# 1. Integer
age = 22
marks = 85
temperature = -5

print("Integer:", age, marks, temperature)
print("Integer is immutable")


# 2. Float
percentage = 85.5
price = 99.99

print("\nFloat:", percentage, price)
print("Float is immutable")


# 3. Complex
number = 3 + 4j

print("\nComplex:", number)
print("Complex is immutable")


# 4. String
name = "Sagar"

print("\nString:", name)
print("String is immutable")


# 5. List
subjects = ["Python", "DBMS", "Java"]

print("\nList:", subjects)
print("List is mutable")

subjects.append("DSA")
print("After adding DSA:", subjects)


# 6. Tuple
coordinates = (10, 20, 30)

print("\nTuple:", coordinates)
print("Tuple is immutable")


# 7. Set
numbers = {1, 2, 3, 4}

print("\nSet:", numbers)
print("Set is mutable")

numbers.add(5)
print("After adding 5:", numbers)


# 8. Dictionary
student = {
    "name": "Sagar",
    "age": 22,
    "department": "Computer Science"
}

print("\nDictionary:", student)
print("Dictionary is mutable")

student["age"] = 23
print("After changing age:", student)


# 9. Boolean
is_student = True

print("\nBoolean:", is_student)
print("Boolean is immutable")