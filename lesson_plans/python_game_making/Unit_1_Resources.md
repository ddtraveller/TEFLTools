# ## Learning Unit 1

## Learning Unit 1: Introduction to Python and Game Concepts
- Objectives:
  * Understand basic Python syntax and data types
  * Grasp fundamental game development concepts
- Topics:
  * Python basics: variables, data types, and operators
  * Introduction to Pygame library
  * Game loop concept
- Activities:
  * Set up Python and Pygame environment
  * Create a simple "Hello, Timor-Leste!" program

## Unit Resources

Here are detailed resources for Learning Unit 1: Introduction to Python and Game Concepts, formatted in Markdown:

# Learning Unit 1 Resources: Introduction to Python and Game Concepts

## 1. Lecture Notes

### Introduction to Python

#### History and Importance
- Created by Guido van Rossum in 1991
- Named after Monty Python's Flying Circus
- Known for its simplicity and readability
- Widely used in various fields: web development, data science, AI, and game development

#### Basic Syntax
- Indentation is crucial for code structure
- Use '#' for single-line comments
- Print statements: `print("Hello, Timor-Leste!")`

#### Variables and Data Types
- Variables are containers for storing data values
- Naming conventions: lowercase, underscores for spaces
- Common data types:
  * Integers: `age = 25`
  * Floats: `height = 1.75`
  * Strings: `name = "Maria"`
  * Booleans: `is_student = True`

#### Basic Operators
- Arithmetic operators:
  * Addition: `+`
  * Subtraction: `-`
  * Multiplication: `*`
  * Division: `/`
  * Floor division: `//`
  * Modulus: `%`
- Comparison operators:
  * Equal to: `==`
  * Not equal to: `!=`
  * Greater than: `>`
  * Less than: `<`
  * Greater than or equal to: `>=`
  * Less than or equal to: `<=`

### Introduction to Pygame

#### What is Pygame?
- A set of Python modules designed for writing video games
- Built on top of the SDL library
- Provides functionality for graphics, sound, and input handling

#### Basic Pygame Setup
```python
import pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Pygame Window")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state here

    # Draw to the screen here
    pygame.display.flip()

pygame.quit()
```

### Game Loop Concept

- The core of most games
- Continuously runs while the game is active
- Typical structure:
  1. Process user input
  2. Update game state
  3. Render graphics
- Ensures smooth gameplay and responsiveness

## 2. Discussion Questions

1. How does Python's syntax differ from other programming languages you may have encountered?
2. Why is Python considered a good language for beginners?
3. How might the concept of variables be useful in game development?
4. What are some potential applications of arithmetic operators in games?
5. How does the game loop contribute to creating an interactive gaming experience?
6. Can you think of any traditional Timorese games that could be adapted into a computer game? How would you structure their game loop?

## 3. Writing Exercise Instructions

Write a short paragraph (100-150 words) explaining how you would use Python and Pygame to create a simple game based on a traditional Timorese activity or story. Consider what variables you might need, how you would use operators, and how the game loop would function in your concept.

## 4. Assignment Details

### "Hello, Timor-Leste!" Pygame Program

Create a Pygame window that displays "Hello, Timor-Leste!" with the following specifications:

1. Window size: 800x600 pixels
2. Background color: Light blue (RGB: 173, 216, 230)
3. Text color: Dark green (RGB: 0, 100, 0)
4. Font: Any sans-serif font, size 48
5. Text position: Centered on the screen

Bonus: Add the Timor-Leste flag colors (red, yellow, black, white) as a simple shape or border around the text.

### Python Age Calculator

Write a Python script that:
1. Prompts the user to enter their name
2. Asks for their current age
3. Calculates and prints the year when they will turn 100 years old

Example output:
```
What is your name? Maria
How old are you? 25
Maria, you will turn 100 years old in the year 2098.
```

## 5. Additional Resources

### Python Official Documentation
- [Python.org](https://www.python.org/doc/)

### Pygame Documentation
- [Pygame.org](https://www.pygame.org/docs/)

### Online Python Tutorials
- [Codecademy Python Course](https://www.codecademy.com/learn/learn-python-3)
- [Real Python Tutorials](https://realpython.com/)

### Game Development Concepts
- [Game Programming Patterns](http://gameprogrammingpatterns.com/)

### Timor-Leste Cultural Resources
- [Official Tourism Website](https://www.timorleste.tl/)
- [UNESCO Intangible Cultural Heritage in Timor-Leste](https://ich.unesco.org/en/state/timor-leste-TL)

## 6. Code Examples

### Basic Python Syntax

```python
# This is a comment
print("Hello, Timor-Leste!")

# Variables and data types
country = "Timor-Leste"
population = 1318445
area = 14874.0
is_island = True

# Using operators
average_population_density = population / area
print(f"The population density of {country} is approximately {average_population_density:.2f} people per square kilometer.")

# Simple if statement
if is_island:
    print(f"{country} is an island nation.")
else:
    print(f"{country} is not an island nation.")
```

### Simple Pygame Window

```python
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Welcome to Timor-Leste")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(WHITE)

    # Draw a simple representation of the Timor-Leste flag
    pygame.draw.rect(screen, RED, (100, 100, 600, 400))
    pygame.draw.polygon(screen, YELLOW, [(100, 100), (400, 300), (100, 500)])
    pygame.draw.polygon(screen, BLACK, [(150, 300), (200, 250), (200, 350)])

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
```

These resources provide a comprehensive foundation for the first week of the course, introducing students to Python, Pygame, and basic game development concepts within the context of Timor-Leste.