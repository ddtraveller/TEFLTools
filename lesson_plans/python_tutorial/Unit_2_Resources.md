# ## Learning Unit 2

## Learning Unit 2: Control Flow
- Objectives:
  * Understand and use conditional statements
  * Implement loops for repetitive tasks
- Topics:
  * If, elif, and else statements
  * For and while loops
- Activities:
  * Create a program to determine if a year is a leap year in the Gregorian calendar
  * Develop a quiz about Timor-Leste's history using conditional statements

## Unit Resources

Here are detailed resources for Learning Unit 2: Control Flow, formatted in Markdown:

# Learning Unit 2: Control Flow - Detailed Resources

## 1. Lecture Notes

### Conditional Statements

#### Introduction to Conditional Statements
Conditional statements allow programs to make decisions based on certain conditions. In Python, we use `if`, `elif` (else if), and `else` statements for this purpose.

#### Basic Syntax
```python
if condition:
    # code to execute if condition is True
elif another_condition:
    # code to execute if another_condition is True
else:
    # code to execute if all conditions are False
```

#### Example
```python
age = 18
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")
```

#### Boolean Expressions
Conditional statements rely on boolean expressions, which evaluate to either `True` or `False`. Common comparison operators include:
- `==` (equal to)
- `!=` (not equal to)
- `<` (less than)
- `>` (greater than)
- `<=` (less than or equal to)
- `>=` (greater than or equal to)

### Loops

#### Introduction to Loops
Loops allow us to repeat a block of code multiple times. Python has two main types of loops: `for` loops and `while` loops.

#### For Loops
For loops are used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.

Syntax:
```python
for item in sequence:
    # code to execute for each item
```

Example:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

#### While Loops
While loops repeat a block of code as long as a condition is True.

Syntax:
```python
while condition:
    # code to execute while condition is True
```

Example:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## 2. Discussion Questions

1. How do conditional statements help in making programs more flexible?
2. Can you think of real-life scenarios where you use if-else decision making?
3. What are the differences between `for` loops and `while` loops? When would you use one over the other?
4. How can loops be used to solve problems in everyday life in Timor-Leste?
5. What potential issues might arise if a condition in a while loop never becomes False?

## 3. Writing Exercise Instructions

Write a short paragraph explaining how you would use conditional statements and loops to create a simple program that could be useful in Timor-Leste. Consider local needs such as agriculture, education, or small businesses.

## 4. Assignment Details

### Assignment 1: Leap Year Calculator

Create a Python program that determines whether a given year is a leap year in the Gregorian calendar. 

Requirements:
- The program should prompt the user to enter a year.
- It should then calculate and print whether the year is a leap year or not.
- Use conditional statements to implement the leap year rule:
  - A year is a leap year if it is divisible by 4, except for century years.
  - Century years are leap years only if they are divisible by 400.

Example output:
```
Enter a year: 2000
2000 is a leap year.

Enter a year: 2100
2100 is not a leap year.
```

### Assignment 2: Timor-Leste History Quiz

Develop a quiz program about Timor-Leste's history using conditional statements.

Requirements:
- Create at least 5 multiple-choice questions about Timor-Leste's history.
- Use conditional statements to check if the user's answer is correct.
- Keep track of the user's score and display it at the end of the quiz.
- Use a loop to present all questions to the user.

Example structure:
```python
score = 0
total_questions = 5

# Question 1
print("In which year did Timor-Leste gain independence?")
print("a) 1999")
print("b) 2002")
print("c) 2005")
answer = input("Your answer: ")

if answer.lower() == 'b':
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is b) 2002.")

# Repeat for other questions...

print(f"You scored {score} out of {total_questions}.")
```

## 5. Additional Materials and Examples

### Example: Using loops to calculate coffee harvest

```python
# Simulating coffee harvest calculation for different regions in Timor-Leste

regions = ["Ermera", "Aileu", "Liquiçá", "Manufahi"]
total_harvest = 0

for region in regions:
    harvest = float(input(f"Enter the coffee harvest (in kg) for {region}: "))
    total_harvest += harvest

print(f"Total coffee harvest across all regions: {total_harvest} kg")
average_harvest = total_harvest / len(regions)
print(f"Average harvest per region: {average_harvest:.2f} kg")
```

### Example: Conditional statements for a simple weather advisory

```python
temperature = float(input("Enter the temperature in Celsius: "))

if temperature < 20:
    print("It's cool today. Consider wearing a jacket.")
elif 20 <= temperature < 30:
    print("The weather is pleasant. Enjoy your day!")
else:
    print("It's hot today. Stay hydrated and seek shade.")

if temperature > 35:
    print("Heat advisory: Take extra precautions in extreme heat.")
```

These resources provide a comprehensive set of materials for teaching the Control Flow unit, with a focus on conditional statements and loops, while incorporating relevant examples for students in Timor-Leste.