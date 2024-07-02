# ## Learning Unit 2

## Learning Unit 2: Variables and Data Types  
- Objectives:
  * Understand variables and basic data types in Python
  * Perform calculations and manipulate strings
- Topics:
  * Numeric data types (int, float)
  * Strings
  * Variables
  * Basic math operations
- Activities:
  * Write a program to calculate the area of Timor-Leste in square kilometers
  * Create variables for Timor-Leste's population and GDP, then calculate GDP per capita

## Unit Resources

Here are detailed resources for Learning Unit 2: Variables and Data Types, formatted in Markdown:

# Learning Unit 2: Variables and Data Types - Detailed Resources

## 1. Lecture Notes

### Introduction to Variables

Variables are fundamental building blocks in programming. They allow us to store and manipulate data in our programs.

- A variable is a named storage location in a computer's memory
- Variables have a name, a value, and a type
- In Python, we create variables using the assignment operator (=)

Example:
```python
age = 25
name = "Maria"
height = 1.75
```

### Data Types

Python has several built-in data types. We'll focus on three basic ones:

1. Integers (int):
   - Whole numbers, positive or negative
   - Example: `age = 25`

2. Floating-point numbers (float):
   - Numbers with decimal points
   - Example: `height = 1.75`

3. Strings (str):
   - Sequences of characters (text)
   - Enclosed in single or double quotes
   - Example: `name = "Maria"`

### Basic Math Operations

Python can perform various mathematical operations:

- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Integer division: `//`
- Modulus (remainder): `%`
- Exponentiation: `**`

Examples:
```python
a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333...
print(a // b) # 3
print(a % b)  # 1
print(a ** b) # 1000
```

### String Manipulation

Strings in Python can be manipulated in various ways:

1. Concatenation:
   - Joining strings together using the `+` operator
   - Example: `full_name = first_name + " " + last_name`

2. String methods:
   - `.upper()`: Converts string to uppercase
   - `.lower()`: Converts string to lowercase
   - `.capitalize()`: Capitalizes the first letter
   - `.strip()`: Removes whitespace from beginning and end

Examples:
```python
greeting = "hello"
print(greeting.upper())  # HELLO
print(greeting.capitalize())  # Hello

name = "  Maria  "
print(name.strip())  # Maria
```

## 2. Discussion Questions

1. Why are variables important in programming? How do they make our code more flexible?
2. What are the differences between integers and floats? When might you use one over the other?
3. How can string manipulation be useful in real-world applications?
4. Why is it important to choose meaningful names for variables?
5. How might you use variables and math operations to solve problems related to Timor-Leste's economy or geography?

## 3. Writing Exercise Instructions

Write a short paragraph (5-7 sentences) explaining how you would use variables and basic math operations to solve a real-world problem in Timor-Leste. Consider issues related to agriculture, economy, education, or healthcare. Include examples of variables you would use and calculations you would perform.

## 4. Assignment Details

### Assignment 1: Area Calculation Program

Write a Python program that calculates the area of Timor-Leste in square kilometers.

Instructions:
1. Create variables for the length and width of Timor-Leste (you may need to research or estimate these values)
2. Calculate the area by multiplying length by width
3. Print the result with a descriptive message

Example output:
```
The area of Timor-Leste is approximately 14874 square kilometers.
```

### Assignment 2: GDP per Capita Calculation

Create a Python program that calculates the GDP per capita of Timor-Leste.

Instructions:
1. Create variables for Timor-Leste's population (1,318,445) and GDP ($2.7 billion)
2. Calculate the GDP per capita by dividing the GDP by the population
3. Print the result with a descriptive message

Example output:
```
The GDP per capita of Timor-Leste is approximately $2048.54.
```

## 5. Additional Resources and Examples

### Real-world Application: Coffee Production Calculator

Timor-Leste is known for its coffee production. Here's an example of how variables and math operations can be used in a real-world scenario:

```python
# Coffee production calculator

# Variables
farms = 5
trees_per_farm = 1000
yield_per_tree = 0.5  # in kilograms

# Calculations
total_trees = farms * trees_per_farm
total_yield = total_trees * yield_per_tree

# Output
print(f"With {farms} farms, each having {trees_per_farm} trees,")
print(f"the total coffee yield is {total_yield} kilograms.")
```

### Cultural Integration: Tetum Greeting Generator

This example demonstrates string manipulation with cultural relevance:

```python
# Tetum greeting generator

name = input("Enter your name: ")
time_of_day = input("Enter the time of day (morning/afternoon/evening): ")

greeting = ""
if time_of_day.lower() == "morning":
    greeting = "Bondia"
elif time_of_day.lower() == "afternoon":
    greeting = "Botarde"
else:
    greeting = "Bonoite"

print(f"{greeting}, {name.capitalize()}! Diak ka lae?")
```

These resources provide a comprehensive foundation for teaching variables and data types in Python, with a focus on applications relevant to Timor-Leste. The lecture notes, discussion questions, exercises, and examples should help students grasp these fundamental concepts while relating them to their local context.