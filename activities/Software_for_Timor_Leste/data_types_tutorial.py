import json
from datetime import datetime

# Dictionary
person = {"name": "John", "age": 25, "city": "New York"}
print("Dictionary:", person)

# List
fruits = ["apple", "banana", "orange"]
print("List:", fruits)

# List Comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print("List Comprehension:", squared_numbers)

# Class Object and __init__ Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person_obj = Person("Alice", 30)
print("Class Object:", person_obj.name, person_obj.age)

# JSON
data = {"name": "John", "age": 25, "city": "New York"}
json_string = json.dumps(data)
print("JSON:", json_string)

# String
message = "Hello, world!"
print("String:", message)

# Numbers
x = 10
y = 3.14
z = 2 + 3j
print("Integer:", x)
print("Float:", y)
print("Complex:", z)

# Dates and Time
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("Current Time:", current_time)
print("Formatted Time:", formatted_time)