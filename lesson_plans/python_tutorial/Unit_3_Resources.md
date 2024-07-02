# ## Learning Unit 3

## Learning Unit 3: Functions and Modules
- Objectives:
  * Define and use functions
  * Understand the concept of modules
- Topics:
  * Function definition and calling
  * Parameters and return values
  * Importing and using modules
- Activities:
  * Write a function to convert between US dollars and Timor-Leste's currency (USD)
  * Create a module with functions related to Timor-Leste's geography (e.g., calculate distances between cities)

## Unit Resources

Here are detailed resources for Learning Unit 3: Functions and Modules, formatted in Markdown:

# Learning Unit 3: Functions and Modules - Detailed Resources

## 1. Lecture Notes

### Functions

#### Introduction to Functions
- Functions are reusable blocks of code that perform specific tasks
- They help organize code, reduce repetition, and improve readability
- Functions can take inputs (parameters) and return outputs

#### Function Syntax
```python
def function_name(parameter1, parameter2, ...):
    # Function body
    # Code to be executed
    return result  # Optional
```

#### Calling Functions
- Functions are called by using their name followed by parentheses
- Arguments are passed inside the parentheses
```python
result = function_name(arg1, arg2)
```

#### Parameters and Arguments
- Parameters are variables listed in the function definition
- Arguments are the actual values passed to the function when it's called

#### Return Values
- Functions can return values using the `return` statement
- If no return statement is used, the function returns `None`

#### Example: Area of a Rectangle
```python
def calculate_area(length, width):
    area = length * width
    return area

rectangle_area = calculate_area(5, 3)
print(f"The area of the rectangle is {rectangle_area}")
```

### Modules

#### Introduction to Modules
- Modules are files containing Python code (definitions, functions, variables)
- They help organize and reuse code across different programs

#### Importing Modules
```python
import module_name
from module_name import function_name
from module_name import *  # Import all (use cautiously)
```

#### Using Module Functions
```python
import math
radius = 5
circumference = 2 * math.pi * radius
```

#### Creating Custom Modules
- Save Python code in a .py file
- Import it like any other module

#### Example: Timor-Leste Geography Module
```python
# tl_geography.py
def distance_between_cities(city1, city2):
    # Calculate distance logic here
    pass

def list_major_cities():
    return ["Dili", "Baucau", "Maliana", "Suai", "Lospalos"]
```

## 2. Discussion Questions

1. How do functions improve code organization and reusability?
2. What's the difference between parameters and arguments in functions?
3. When would you use a return value in a function, and when might you not need one?
4. How can modules help in developing larger Python programs?
5. What are some advantages and potential drawbacks of using modules in your code?
6. How might functions and modules be useful in solving real-world problems in Timor-Leste?

## 3. Writing Exercise Instructions

### Exercise 1: Function Documentation
Write clear and concise documentation for the following function:

```python
def calculate_coffee_yield(trees, rainfall):
    base_yield = trees * 0.5  # 0.5 kg per tree
    if rainfall < 1500:
        return base_yield * 0.8
    elif rainfall > 2500:
        return base_yield * 1.2
    else:
        return base_yield
```

Include:
- A brief description of what the function does
- Explanation of parameters
- Description of the return value
- Any assumptions or limitations

### Exercise 2: Module Design
Design a module called `tl_culture` that would contain functions related to Timor-Leste's cultural heritage. List at least five functions this module could include, with a brief description of each function's purpose.

## 4. Assignment Details

### Assignment 1: Currency Conversion Function

Create a Python function that converts between US Dollars (USD) and Timor-Leste's currency (also USD, but consider using a fictional currency for this exercise).

Requirements:
- Function should take two parameters: amount and direction of conversion
- Use a fixed exchange rate (e.g., 1 USD = 1.5 TL)
- Include error handling for invalid inputs
- Write at least three test cases to verify the function works correctly

### Assignment 2: Timor-Leste Geography Module

Create a Python module named `tl_geography` with the following functions:

1. `distance_between_cities(city1, city2)`: Calculate the distance between two cities (use simplified distance calculation)
2. `list_major_cities()`: Return a list of major cities in Timor-Leste
3. `get_city_info(city_name)`: Return a dictionary with information about the specified city (population, area, etc.)
4. `is_coastal_city(city_name)`: Return True if the city is on the coast, False otherwise

Include a main section in your module that demonstrates the use of each function when the module is run directly.

## 5. Additional Resources

### Online Resources
- [Python Official Documentation on Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Real Python - Python Modules and Packages](https://realpython.com/python-modules-packages/)

### Code Examples

#### Example 1: Simple Greeting Function
```python
def greet_person(name):
    return f"Bondia, {name}! Diak ka lae?"

# Usage
print(greet_person("Maria"))
```

#### Example 2: Using the math Module
```python
import math

def circle_area(radius):
    return math.pi * radius ** 2

# Usage
print(f"The area of a circle with radius 5 is {circle_area(5):.2f}")
```

### Timor-Leste Specific Examples

#### Example 3: Coffee Production Calculator
```python
def estimate_coffee_production(area_hectares, trees_per_hectare):
    total_trees = area_hectares * trees_per_hectare
    production_kg = total_trees * 0.5  # Assuming 0.5 kg per tree
    return production_kg

# Usage
area = 10  # hectares
density = 1000  # trees per hectare
production = estimate_coffee_production(area, density)
print(f"Estimated coffee production: {production} kg")
```

This comprehensive set of resources should provide ample material for the week's lessons on Functions and Modules, with a focus on applications relevant to Timor-Leste.