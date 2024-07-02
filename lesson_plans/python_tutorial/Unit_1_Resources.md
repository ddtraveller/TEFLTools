# ## Learning Unit 1

## Learning Unit 1: Introduction to Python and Basic Syntax
- Objectives:
  * Understand what Python is and its applications
  * Set up a Python development environment
  * Write and run simple Python programs
- Topics:
  * Overview of Python and its uses in Timor-Leste
  * Installing Python and IDLE
  * Basic syntax: variables, data types, and operators
- Activities:
  * Install Python and IDLE on personal computers
  * Write a program to calculate the cost of common goods in Timor-Leste (e.g., rice, coffee)

## Unit Resources

Here are detailed resources for Learning Unit 1: Introduction to Python and Basic Syntax, formatted in Markdown:

# Learning Unit 1 Resources: Introduction to Python and Basic Syntax

## 1. Lecture Notes

### Overview of Python and its uses in Timor-Leste

Python is a high-level, interpreted programming language created by Guido van Rossum in 1991. It's known for its simplicity and readability, making it an excellent choice for beginners.

Key points:
- Python is versatile and used in various fields: web development, data analysis, artificial intelligence, scientific computing, and more.
- In Timor-Leste, Python can be applied to:
  * Analyze agricultural data to improve crop yields
  * Develop websites to promote tourism
  * Create educational software in Tetum
  * Process and analyze health data to improve public health initiatives

### Installing Python and IDLE

Steps to install Python:
1. Visit python.org
2. Download the latest version of Python 3.x
3. Run the installer, ensuring to check "Add Python to PATH"
4. Verify installation by opening command prompt/terminal and typing `python --version`

IDLE (Integrated Development and Learning Environment) comes bundled with Python installation.

### Basic syntax: variables, data types, and operators

Variables:
- Used to store data in memory
- Created by assigning a value: `variable_name = value`
- Follow naming conventions: lowercase, underscores for spaces

Data types:
- int: Whole numbers (e.g., `age = 25`)
- float: Decimal numbers (e.g., `price = 1.50`)
- str: Text (e.g., `name = "Maria"`)
- bool: True or False (e.g., `is_student = True`)

Operators:
- Arithmetic: +, -, *, /, // (integer division), % (modulo), ** (exponent)
- Comparison: ==, !=, <, >, <=, >=
- Logical: and, or, not

## 2. Discussion Questions

1. How might Python programming skills benefit Timor-Leste's development?
2. What are some potential challenges in learning and using Python in Timor-Leste?
3. How does the concept of variables in programming relate to mathematics?
4. Why is it important to choose appropriate data types when programming?
5. How might you use Python operators to solve everyday problems in Timor-Leste?

## 3. Writing Exercise Instructions

Write a short paragraph (100-150 words) explaining how you think Python programming could be used to address a specific issue in Timor-Leste. Consider areas such as agriculture, education, healthcare, or tourism.

## 4. Assignment Details

### Assignment 1: Setting Up Python Environment

Objective: Install Python and IDLE on your personal computer.

Steps:
1. Download Python 3.x from python.org
2. Install Python, ensuring to add it to your system PATH
3. Open IDLE and create a new file
4. Write a simple program that prints "Hello, Timor-Leste!"
5. Save and run the program
6. Take a screenshot of your IDLE window showing the successful execution

Submit: The screenshot of your IDLE window

### Assignment 2: Calculating Goods Cost

Objective: Write a program to calculate the cost of common goods in Timor-Leste.

Requirements:
1. Create variables for at least 3 common goods (e.g., rice, coffee, tais) and assign prices
2. Calculate and print the total cost of buying one of each item
3. Apply a 10% discount to the total and print the discounted price
4. Use appropriate variable names and add comments to explain your code

Example output:
```
Original total: $25.50
Discounted total: $22.95
```

Submit: Your Python script (.py file)

## 5. Additional Materials and Examples

### Example: Basic Python Program

```python
# This program calculates the cost of a meal in Timor-Leste

# Define prices
rice_price = 1.50
fish_price = 3.00
vegetable_price = 0.75

# Calculate total
total = rice_price + fish_price + vegetable_price

# Print result
print(f"The total cost of the meal is ${total:.2f}")
```

### Tetum-English Mini-Dictionary

To help students relate Python concepts to their native language, here's a mini-dictionary of programming terms:

- Variable = Variavel
- Data = Dadus
- String = Liafuan
- Number = Numeru
- Boolean = Loos ka Sala
- Print = Hatudu
- Input = Hatama

### Real-world Application Example

Scenario: A local coffee cooperative wants to track their daily sales.

```python
# Timor-Leste Coffee Cooperative Daily Sales Tracker

# Input daily sales
arabica_sales = float(input("Enter Arabica coffee sales (kg): "))
robusta_sales = float(input("Enter Robusta coffee sales (kg): "))

# Set prices
arabica_price = 15.00  # USD per kg
robusta_price = 12.00  # USD per kg

# Calculate total sales
total_sales = (arabica_sales * arabica_price) + (robusta_sales * robusta_price)

# Print report
print("\nDaily Sales Report")
print(f"Arabica sales: {arabica_sales} kg")
print(f"Robusta sales: {robusta_sales} kg")
print(f"Total revenue: ${total_sales:.2f}")
```

This example demonstrates practical use of variables, input functions, calculations, and formatted output in a context relevant to Timor-Leste's coffee industry.