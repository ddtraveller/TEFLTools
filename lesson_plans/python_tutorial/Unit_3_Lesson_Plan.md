Here's a detailed lesson plan for Learning Unit 3: Functions and Modules, formatted in Markdown:

# Lesson Plan: Functions and Modules

## 1. Resources Needed
- Computers with Python 3.x installed
- IDLE or preferred text editor
- Projector for demonstrations
- Handouts with function syntax and module import examples
- Currency conversion rates for USD to Timor-Leste's currency (USD)
- Map of Timor-Leste with major cities and distances

## 2. Lesson Objectives
By the end of this lesson, students will be able to:
- Define and call functions in Python
- Use parameters and return values in functions
- Import and use modules in their Python programs
- Apply functions and modules to solve problems relevant to Timor-Leste

## 3. Warm-up Activity (10 minutes)
- Group discussion: Ask students to brainstorm repetitive tasks they perform daily (e.g., cooking rice, making coffee)
- Introduce the concept of functions as a way to package repetitive tasks in programming

## 4. Pre-teaching Key Vocabulary (10 minutes)
Introduce and explain the following terms:
- Function
- Parameter
- Argument
- Return value
- Module
- Import

## 5. Presentation of Main Lesson Content (30 minutes)
### 5.1 Functions
- Explain the purpose and benefits of functions
- Demonstrate function syntax:
  ```python
  def function_name(parameters):
      # function body
      return value
  ```
- Show how to call functions and pass arguments

### 5.2 Modules
- Introduce the concept of modules as collections of related functions
- Demonstrate how to import modules:
  ```python
  import module_name
  from module_name import function_name
  ```
- Show built-in modules like `math` and `random`

## 6. Practice Activities (30 minutes)
### 6.1 Function Practice
Students write simple functions:
- A greeting function that takes a name as a parameter
- A function to calculate the area of a rectangle

### 6.2 Module Practice
Students import and use functions from the `math` module:
- Calculate the circumference of a circle using `math.pi`
- Use `math.sqrt()` to find the square root of a number

## 7. Production Tasks (40 minutes)
### 7.1 Currency Conversion Function
Students create a function to convert between USD and Timor-Leste's currency:
```python
def usd_to_tl(usd_amount):
    # Conversion logic here
    return tl_amount
```

### 7.2 Timor-Leste Geography Module
Students create a module named `tl_geography` with functions:
- Calculate distance between two cities
- List major cities
- Provide information about a specific city

## 8. Wrap-up and Review (10 minutes)
- Recap key points about functions and modules
- Address any questions or misconceptions
- Preview the next lesson on data structures

## 9. Homework Assignment
- Expand the `tl_geography` module to include more functions (e.g., calculate area of districts, find the capital of a district)
- Write a program that uses functions to calculate and display statistics about Timor-Leste (e.g., population density, literacy rate)

## 10. Key Vocabulary Definitions
- **Function**: A reusable block of code that performs a specific task
- **Parameter**: A variable in the function definition that accepts input values
- **Argument**: The actual value passed to a function when it is called
- **Return value**: The output of a function, specified by the `return` statement
- **Module**: A file containing Python definitions and statements, which can be imported and used in other programs
- **Import**: The process of bringing functions or variables from a module into the current program