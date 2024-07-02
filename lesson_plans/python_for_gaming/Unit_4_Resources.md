# ## Learning Unit 4

## Learning Unit 4: Functions
- Objectives:
  * Define and call functions
  * Understand function parameters and return values
- Topics:
  * Defining functions
  * Function parameters
  * Return values
- Activities:
  * Write a function to convert between US dollars and Timorese centavos
  * Create a function that generates a random fact about Timor-Leste

## Unit Resources

Here are detailed resources for Learning Unit 4: Functions, formatted in Markdown:

# Learning Unit 4: Functions - Detailed Resources

## 1. Lecture Notes

### Defining Functions

- Functions are reusable blocks of code that perform specific tasks
- Syntax for defining a function:
  ```python
  def function_name(parameters):
      # Function body
      # Code to be executed
  ```
- Example:
  ```python
  def greet():
      print("Bondia Timor-Leste!")
  ```
- Functions should have descriptive names that indicate their purpose
- Use snake_case for function names (e.g., `calculate_area`, `convert_currency`)

### Function Parameters

- Parameters are variables listed in the function definition
- They allow functions to accept input values
- Syntax:
  ```python
  def function_name(parameter1, parameter2, ...):
      # Function body using parameters
  ```
- Example:
  ```python
  def greet_person(name):
      print(f"Bondia, {name}!")
  ```
- Multiple parameters are separated by commas
- Parameters vs. Arguments:
  - Parameters are in the function definition
  - Arguments are the actual values passed when calling the function

### Return Values

- Functions can send back a value to the caller using the `return` statement
- Syntax:
  ```python
  def function_name(parameters):
      # Function body
      return value
  ```
- Example:
  ```python
  def calculate_area(length, width):
      area = length * width
      return area
  ```
- Functions can return multiple values using tuples:
  ```python
  def get_dimensions():
      return 10, 20  # Returns a tuple (10, 20)
  ```
- If no return statement is used, the function returns `None` by default

### Calling Functions

- To use a function, you call it by its name followed by parentheses
- If the function has parameters, provide arguments in the parentheses
- Example:
  ```python
  greet()  # Calls the greet function
  greet_person("Maria")  # Calls greet_person with an argument
  ```
- You can assign the return value of a function to a variable:
  ```python
  result = calculate_area(5, 3)
  print(result)  # Outputs: 15
  ```

## 2. Discussion Questions

1. How do functions help in organizing and structuring code?
2. What are the benefits of using parameters in functions?
3. How does the use of return values make functions more versatile?
4. Can you think of real-world scenarios in Timor-Leste where functions could be useful in a program?
5. How might you use functions to simplify a program that calculates grades for a class?
6. What are some best practices for naming functions and parameters?
7. How do functions relate to the DRY (Don't Repeat Yourself) principle in programming?
8. In what situations might you choose not to use a return value in a function?

## 3. Writing Exercise Instructions

Write a short paragraph (100-150 words) explaining how you would use functions to create a simple program related to Timor-Leste. Consider topics such as:
- Calculating coffee harvest yields
- Converting between different units of measurement used in Timor-Leste
- Creating a simple language translation tool for Tetum to English
- Analyzing data about Timor-Leste's districts

In your explanation, include at least two functions you would create, what parameters they might have, and what they would return (if anything).

## 4. Assignment Details

### Assignment 1: Currency Conversion Function

Create a Python function called `usd_to_centavos` that converts US dollars to Timorese centavos. Use the following specifications:

- The function should take one parameter: the amount in US dollars (as a float)
- Use an exchange rate of 1 USD = 100 Timorese centavos (adjust if needed for current rates)
- The function should return the amount in centavos as an integer
- Include input validation to ensure the input is a positive number
- If the input is invalid, the function should return None and print an error message

Example usage:
```python
result = usd_to_centavos(5.50)
print(result)  # Should output: 550

result = usd_to_centavos(-2)
print(result)  # Should output: None (and print an error message)
```

### Assignment 2: Random Fact Generator

Create a function called `timor_leste_fact` that returns a random fact about Timor-Leste. Use the following specifications:

- The function should not take any parameters
- Create a list of at least 10 interesting facts about Timor-Leste
- Use the `random` module to select and return a random fact from the list
- Include a parameter `exclude` (default value None) that allows the caller to specify a fact to exclude from the selection

Example usage:
```python
print(timor_leste_fact())  # Outputs a random fact
print(timor_leste_fact(exclude="Timor-Leste gained independence in 2002"))  # Outputs a random fact, excluding the specified one
```

## 5. Additional Materials and Examples

### Example: Area Calculation Function

```python
def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle
    
    Returns:
    float: The area of the rectangle
    """
    if length <= 0 or width <= 0:
        print("Error: Length and width must be positive numbers.")
        return None
    
    area = length * width
    return area

# Example usage
result = calculate_rectangle_area(5, 3)
print(f"The area of the rectangle is: {result} square units")

result = calculate_rectangle_area(-2, 4)
print(result)  # Will print None and an error message
```

### Example: Greeting Function with Multiple Parameters

```python
def greet_timorese(name, district, language="Tetum"):
    """
    Generate a personalized greeting for a person from Timor-Leste.
    
    Parameters:
    name (str): The person's name
    district (str): The person's home district
    language (str): The language of greeting (default is Tetum)
    
    Returns:
    str: A personalized greeting
    """
    greetings = {
        "Tetum": "Bondia",
        "Portuguese": "Bom dia",
        "English": "Good morning"
    }
    
    if language not in greetings:
        return f"Sorry, I don't know how to greet in {language}."
    
    greeting = greetings[language]
    return f"{greeting}, {name} from {district}!"

# Example usage
print(greet_timorese("Maria", "Dili"))
print(greet_timorese("João", "Baucau", "Portuguese"))
print(greet_timorese("Sarah", "Oecusse", "French"))
```

These resources provide a comprehensive set of materials for teaching the Functions unit in the context of Timor-Leste. The lecture notes, discussion questions, writing exercise, assignments, and additional examples all work together to reinforce the learning objectives while incorporating culturally relevant content.