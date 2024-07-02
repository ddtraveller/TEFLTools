# ## Learning Unit 3

## Learning Unit 3: Control Flow
- Objectives:
  * Use if/else statements for decision making
  * Implement loops to repeat code
- Topics:
  * if, elif, else statements  
  * for loops
  * while loops
- Activities:
  * Write a program to determine if a year is a leap year in the Gregorian calendar
  * Create a quiz about Timor-Leste history using if/else statements

## Unit Resources

Here are detailed resources for Learning Unit 3: Control Flow, formatted in Markdown:

# Learning Unit 3: Control Flow - Detailed Resources

## 1. Lecture Notes

### If/Else Statements

#### Introduction
- Control flow determines the order in which program instructions are executed
- Conditional statements allow programs to make decisions based on certain conditions
- In Python, we use if, elif, and else statements for decision-making

#### Syntax
```python
if condition:
    # code to execute if condition is True
elif another_condition:
    # code to execute if another_condition is True
else:
    # code to execute if all conditions are False
```

#### Examples
```python
# Example 1: Checking voting eligibility in Timor-Leste
age = 17
if age >= 17:
    print("You are eligible to vote in Timor-Leste.")
else:
    print("You are not yet eligible to vote in Timor-Leste.")

# Example 2: Categorizing Timor-Leste districts by population
district_population = 234000  # Dili's population
if district_population > 200000:
    print("Large district")
elif district_population > 100000:
    print("Medium district")
else:
    print("Small district")
```

### For Loops

#### Introduction
- Loops allow us to repeat a block of code multiple times
- For loops are used when we know in advance how many times we want to repeat the code

#### Syntax
```python
for variable in sequence:
    # code to be repeated
```

#### Examples
```python
# Example 1: Printing numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Example 2: Iterating over a list of Timor-Leste's national heroes
heroes = ["Xanana Gusmão", "José Ramos-Horta", "Nicolau Lobato"]
for hero in heroes:
    print(hero + " is a national hero of Timor-Leste.")
```

### While Loops

#### Introduction
- While loops repeat a block of code as long as a condition is True
- Useful when we don't know in advance how many times we need to repeat the code

#### Syntax
```python
while condition:
    # code to be repeated
```

#### Examples
```python
# Example 1: Counting down from 5
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Liftoff!")

# Example 2: Simulating coffee bean harvesting
beans_harvested = 0
while beans_harvested < 100:
    beans_harvested += 10
    print(f"Harvested {beans_harvested} coffee beans")
print("Harvest complete!")
```

## 2. Discussion Questions

1. How do conditional statements help us create more dynamic and responsive programs?
2. Can you think of any real-world scenarios in Timor-Leste where if/else statements could be useful in a program?
3. What are the key differences between for loops and while loops? When would you choose one over the other?
4. How might loops be useful in processing data about Timor-Leste's agriculture or economy?
5. Can you think of any potential issues that might arise if a while loop's condition is never met?

## 3. Writing Exercise Instructions

### Exercise 1: Timor-Leste Climate Program
Write a Python program that asks the user to input a temperature in Celsius. The program should then use if/else statements to categorize the weather and provide appropriate advice:

- If the temperature is above 30°C: "It's hot! Stay hydrated and seek shade."
- If the temperature is between 20°C and 30°C: "The weather is pleasant. Enjoy outdoor activities!"
- If the temperature is below 20°C: "It's a bit cool. Consider wearing a light jacket."

### Exercise 2: Timor-Leste Coffee Production Simulator
Create a program that simulates coffee production in Timor-Leste using a while loop. Start with 0 kg of coffee and randomly add between 10-50 kg each "day" (loop iteration) until you reach or exceed 1000 kg. Print the total after each day and the number of days it took to reach the goal.

## 4. Assignment Details

### Assignment 1: Leap Year Calculator
Write a Python program that determines whether a given year is a leap year in the Gregorian calendar. The rules for leap years are:

- A year is a leap year if it is divisible by 4
- However, if the year is divisible by 100, it is not a leap year, unless...
- The year is also divisible by 400. Then it is a leap year.

Your program should:
1. Prompt the user to enter a year
2. Use if/else statements to apply the leap year rules
3. Print whether the year is a leap year or not

### Assignment 2: Timor-Leste History Quiz
Create a multiple-choice quiz about Timor-Leste history using if/else statements. Your quiz should:

1. Have at least 5 questions
2. Present multiple-choice options for each question
3. Use if/else statements to check if the answer is correct
4. Provide feedback for correct and incorrect answers
5. Keep track of the user's score and display it at the end

Example question:
```python
print("In which year did Timor-Leste gain independence?")
print("a) 1975")
print("b) 1999")
print("c) 2002")
answer = input("Your answer: ")

if answer.lower() == "c":
    print("Correct! Timor-Leste became independent in 2002.")
    score += 1
else:
    print("Incorrect. Timor-Leste became independent in 2002.")
```

## 5. Additional Materials and Examples

### Example: Using nested if/else statements

```python
# Determining the official language to use based on region and context
region = input("Enter the region (urban/rural): ")
context = input("Enter the context (government/local): ")

if region.lower() == "urban":
    if context.lower() == "government":
        print("Use Portuguese or Tetum")
    else:
        print("Use Tetum")
else:
    if context.lower() == "government":
        print("Use Tetum")
    else:
        print("Use the local language or Tetum")
```

### Example: Using a for loop with the enumerate() function

```python
# Printing the list of Timor-Leste's districts with their index
districts = ["Aileu", "Ainaro", "Baucau", "Bobonaro", "Cova Lima", "Dili", "Ermera", "Lautém", "Liquiçá", "Manatuto", "Manufahi", "Oecusse", "Viqueque"]

for index, district in enumerate(districts, start=1):
    print(f"{index}. {district}")
```

### Example: Using a while loop with user input

```python
# Simulating a simple savings calculator for Timorese coffee farmers
savings = 0
target = 1000

while savings < target:
    amount = float(input("Enter the amount you want to save (or 0 to exit): "))
    if amount == 0:
        break
    savings += amount
    print(f"Current savings: ${savings}")

if savings >= target:
    print(f"Congratulations! You've reached your savings goal of ${target}")
else:
    print(f"You've ended your savings plan with ${savings}")
```

These resources provide a comprehensive set of materials for teaching control flow concepts in Python, with examples and exercises tailored to the Timor-Leste context.