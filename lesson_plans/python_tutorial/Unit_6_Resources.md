# ## Learning Unit 6

## Learning Unit 6: Introduction to Object-Oriented Programming
- Objectives:
  * Understand the basics of object-oriented programming
  * Create and use simple classes and objects
- Topics:
  * Classes and objects
  * Attributes and methods
- Activities:
  * Design a class to represent a traditional Timorese house (Uma Lulik)
  * Create a simple inventory management system for a local coffee cooperative

## Required Resources
- Python 3.x installed on computers
- IDLE or any text editor
- Access to internet for downloading Python and additional resources

## Suggested Items to Cover
- Python's role in data analysis and its potential applications in Timor-Leste's development
- Ethical considerations in programming and data handling
- Career opportunities in programming within Timor-Leste and internationally

## Practical Experience and Community Engagement
- Develop a simple website for a local business or community organization
- Create a program to assist in educational efforts (e.g., a Tetum language learning app)
- Participate in a coding workshop for local high school students

## Additional Resources
- Online Python documentation (https://docs.python.org/)
- Free online courses on platforms like Coursera or edX
- Local programming communities or meetups in Dili
- Books on Python programming translated into Tetum or Portuguese, if available

## Unit Resources

Here are detailed resources for Learning Unit 6: Introduction to Object-Oriented Programming, formatted in Markdown:

# Resources for Learning Unit 6: Introduction to Object-Oriented Programming

## 1. Lecture Notes

### Introduction to Object-Oriented Programming (OOP)

Object-Oriented Programming is a programming paradigm that organizes code into objects, which are instances of classes. This approach helps in creating modular, reusable, and easier-to-maintain code.

Key concepts:
- Classes: Blueprints for creating objects
- Objects: Instances of classes
- Attributes: Data stored inside an object
- Methods: Functions that belong to a class and define object behavior

#### Benefits of OOP:
1. Modularity: Code is organized into discrete units (objects)
2. Reusability: Objects can be reused across different parts of a program or in different programs
3. Encapsulation: Data and methods are bundled together, hiding internal details
4. Abstraction: Complex systems can be modeled as simpler, abstract representations

### Creating Classes and Objects in Python

In Python, we define a class using the `class` keyword:

```python
class UmaLulik:
    def __init__(self, size, location, materials):
        self.size = size
        self.location = location
        self.materials = materials

    def describe(self):
        return f"This Uma Lulik is {self.size} square meters, located in {self.location}, and made of {self.materials}."

    def renovate(self, new_materials):
        self.materials = new_materials
        return f"The Uma Lulik has been renovated with {new_materials}."

# Creating an object (instance) of the UmaLulik class
my_uma = UmaLulik(100, "Dili", "wood and thatch")

# Using methods
print(my_uma.describe())
print(my_uma.renovate("concrete and metal roofing"))
```

### Attributes and Methods

- Attributes are variables that belong to a class or object
- Methods are functions that belong to a class and can access or modify its attributes

In the `UmaLulik` example:
- Attributes: `size`, `location`, `materials`
- Methods: `describe()`, `renovate()`

## 2. Discussion Questions

1. How does Object-Oriented Programming relate to real-world concepts? Can you think of examples from Timorese culture that could be modeled using OOP?

2. What are the advantages of using OOP compared to procedural programming? How might these benefits apply to software development projects in Timor-Leste?

3. How can the concept of classes and objects be used to model a local coffee cooperative's inventory system? What attributes and methods would be useful?

4. Discuss the ethical considerations of using OOP to model real-world systems. How can we ensure that our abstractions are respectful and accurate when representing cultural elements?

5. How might OOP concepts be applied to solve local challenges in Timor-Leste, such as in agriculture, education, or healthcare?

## 3. Writing Exercise Instructions

Write a short essay (300-500 words) on the following topic:

"The Potential of Object-Oriented Programming in Timor-Leste's Development"

Consider the following points in your essay:
- How OOP can be applied to model and solve local problems
- Potential applications in sectors such as agriculture, education, or healthcare
- Challenges and opportunities in implementing OOP-based solutions in Timor-Leste
- The role of culturally-sensitive programming in software development

## 4. Assignment Details

### Individual Assignment: Create a Tais Shop Management System

Design and implement a `TaisShop` class to represent a traditional cloth shop in Timor-Leste. Your class should include:

1. Attributes:
   - Inventory (a dictionary of Tais items and their quantities)
   - Sales record (a list of sales transactions)
   - Shop name and location

2. Methods:
   - `add_stock(item, quantity)`: Add new items to the inventory or update existing quantities
   - `make_sale(item, quantity)`: Process a sale, update inventory, and record the transaction
   - `generate_report()`: Display current inventory and total sales

3. Implement a simple command-line interface to interact with your `TaisShop` class, allowing users to:
   - Add new stock
   - Make sales
   - View reports

Submit your Python script and a short report (200-300 words) explaining your design choices and how this system could benefit local Tais shops.

### Group Project: Coffee Cooperative Inventory System

In groups of 3-4, design and implement a simple inventory management system for a local coffee cooperative using OOP principles. Your system should include:

1. Classes:
   - `Product` (representing different types of coffee)
   - `Inventory` (managing the stock of products)
   - `Order` (representing customer orders)

2. Functionalities:
   - Add new coffee products to the inventory
   - Update stock quantities
   - Process customer orders
   - Generate reports (e.g., current stock levels, sales history)

3. Implement a basic user interface (command-line or simple GUI) to interact with the system

Submit your Python scripts, a UML diagram of your class structure, and a group report (500-750 words) discussing:
- Your design process and decisions
- How OOP principles were applied in your solution
- Potential real-world applications and benefits for coffee cooperatives in Timor-Leste
- Challenges faced and how you overcame them

## 5. Additional Materials and Examples

### UML Diagram Example: Uma Lulik Class

```
+-------------------+
|     UmaLulik      |
+-------------------+
| - size: float     |
| - location: str   |
| - materials: str  |
+-------------------+
| + describe(): str |
| + renovate(): str |
+-------------------+
```

### Real-World OOP Application Example: Agricultural Monitoring System

Consider a system to monitor and manage agricultural data for Timor-Leste's coffee farms:

```python
class CoffeeFarm:
    def __init__(self, name, location, size):
        self.name = name
        self.location = location
        self.size = size
        self.plants = []
        self.harvest_data = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def record_harvest(self, date, quantity):
        self.harvest_data.append({"date": date, "quantity": quantity})

    def get_total_harvest(self):
        return sum(data["quantity"] for data in self.harvest_data)

class CoffeePlant:
    def __init__(self, variety, age):
        self.variety = variety
        self.age = age
        self.health_status = "Good"

    def update_health(self, status):
        self.health_status = status

# Usage example
farm = CoffeeFarm("Ermera Coffee", "Ermera District", 10)
plant1 = CoffeePlant("Arabica", 3)
farm.add_plant(plant1)
farm.record_harvest("2023-05-15", 500)
```

This example demonstrates how OOP can be used to model real-world entities and their relationships in a way that's relevant to Timor-Leste's agricultural sector.