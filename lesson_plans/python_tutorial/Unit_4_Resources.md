# ## Learning Unit 4

## Learning Unit 4: Data Structures
- Objectives:
  * Understand and use lists, tuples, and dictionaries
  * Manipulate data structures effectively
- Topics:
  * Lists and list comprehensions
  * Tuples and their uses
  * Dictionaries and key-value pairs
- Activities:
  * Create a program to manage inventory for a local Tais (traditional cloth) shop
  * Develop a dictionary of Tetum words and their English translations

## Unit Resources

Here are detailed resources for Learning Unit 4: Data Structures, formatted in Markdown:

# Learning Unit 4: Data Structures - Detailed Resources

## 1. Lecture Notes

### Lists

#### Introduction to Lists
- A list is an ordered, mutable collection of items in Python
- Lists are created using square brackets []
- Items in a list can be of different data types

```python
# Creating a list
fruits = ["banana", "apple", "orange"]
mixed_list = [1, "two", 3.0, True]
```

#### Accessing List Elements
- List elements are accessed using indices, starting from 0
- Negative indices count from the end of the list

```python
fruits = ["banana", "apple", "orange"]
print(fruits[0])  # Output: banana
print(fruits[-1])  # Output: orange
```

#### Modifying Lists
- Lists are mutable, meaning they can be changed after creation
- Use the index to modify individual elements

```python
fruits = ["banana", "apple", "orange"]
fruits[1] = "mango"
print(fruits)  # Output: ["banana", "mango", "orange"]
```

#### List Methods
- append(): Adds an item to the end of the list
- remove(): Removes the first occurrence of an item
- sort(): Sorts the list in ascending order
- reverse(): Reverses the order of the list

```python
fruits = ["banana", "apple", "orange"]
fruits.append("mango")
fruits.remove("apple")
fruits.sort()
fruits.reverse()
```

#### List Comprehensions
- A concise way to create lists based on existing lists
- Syntax: [expression for item in iterable if condition]

```python
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(squared)  # Output: [1, 4, 9, 16, 25]
```

### Tuples

#### Introduction to Tuples
- A tuple is an ordered, immutable collection of items in Python
- Tuples are created using parentheses ()
- Items in a tuple can be of different data types

```python
# Creating a tuple
coordinates = (10.5, -7.2)
person = ("John", 30, "Engineer")
```

#### Accessing Tuple Elements
- Tuple elements are accessed using indices, similar to lists

```python
coordinates = (10.5, -7.2)
print(coordinates[0])  # Output: 10.5
```

#### Immutability of Tuples
- Tuples cannot be modified after creation
- Attempting to change a tuple will result in an error

```python
coordinates = (10.5, -7.2)
coordinates[0] = 11.0  # This will raise a TypeError
```

#### When to Use Tuples
- Use tuples for collections that should not be changed
- Examples: coordinates, RGB color values, database records

#### Tuple Unpacking
- Assign multiple variables at once using tuple unpacking

```python
person = ("John", 30, "Engineer")
name, age, occupation = person
print(name)  # Output: John
```

### Dictionaries

#### Introduction to Dictionaries
- A dictionary is an unordered collection of key-value pairs
- Dictionaries are created using curly braces {}
- Each key-value pair is separated by a colon :

```python
# Creating a dictionary
person = {"name": "Maria", "age": 25, "city": "Dili"}
```

#### Accessing Dictionary Elements
- Dictionary elements are accessed using keys, not indices
- Use square brackets [] or the get() method to access values

```python
person = {"name": "Maria", "age": 25, "city": "Dili"}
print(person["name"])  # Output: Maria
print(person.get("age"))  # Output: 25
```

#### Modifying Dictionaries
- Add new key-value pairs or modify existing ones using assignment
- Remove key-value pairs using the del keyword or pop() method

```python
person = {"name": "Maria", "age": 25, "city": "Dili"}
person["occupation"] = "Teacher"
person["age"] = 26
del person["city"]
```

#### Dictionary Methods
- keys(): Returns a list of all keys in the dictionary
- values(): Returns a list of all values in the dictionary
- items(): Returns a list of all key-value pairs as tuples

```python
person = {"name": "Maria", "age": 25, "city": "Dili"}
print(person.keys())
print(person.values())
print(person.items())
```

#### Use Cases for Dictionaries
- Storing related information (e.g., a person's details)
- Creating lookup tables or mappings
- Counting occurrences of items

## 2. Discussion Questions

1. How do lists, tuples, and dictionaries differ in terms of mutability and use cases?
2. What are some real-world scenarios in Timor-Leste where you might use each of these data structures?
3. How can list comprehensions make your code more efficient and readable?
4. When would you choose to use a tuple instead of a list?
5. How might dictionaries be useful in managing data for a local business or organization?
6. What are the advantages and disadvantages of using dictionaries compared to lists?
7. How could you use nested data structures (e.g., lists within dictionaries) to represent complex information?

## 3. Writing Exercise Instructions

Write a short essay (250-300 words) on the following topic:

"The Role of Data Structures in Solving Local Challenges in Timor-Leste"

In your essay, consider the following points:
- Identify a specific challenge or problem in Timor-Leste that could be addressed using data structures
- Explain which data structure(s) would be most appropriate for this problem and why
- Describe how you would implement a solution using these data structures
- Discuss the potential impact of your solution on the local community

## 4. Assignment Details

### Assignment 1: Tais Shop Inventory Management

Create a Python program to manage the inventory of a local Tais shop. Your program should include the following features:

1. A list to store Tais items, where each item is represented by a dictionary containing:
   - Name of the Tais
   - Price
   - Quantity in stock
   - Region of origin

2. Functions to:
   - Add new Tais items to the inventory
   - Remove items from the inventory
   - Update the quantity or price of an item
   - Display the current inventory
   - Calculate the total value of the inventory

3. A main menu that allows the user to choose which operation to perform

4. Basic error handling to prevent invalid inputs

### Assignment 2: Tetum-English Dictionary

Develop a Tetum-English dictionary program with the following features:

1. A dictionary to store Tetum words as keys and their English translations as values

2. Functions to:
   - Add new words and translations
   - Look up translations for Tetum words
   - Display all words in the dictionary
   - Remove words from the dictionary
   - Update existing translations

3. A simple user interface that allows users to choose which operation to perform

4. The ability to save the dictionary to a file and load it when the program starts

5. (Bonus) Implement a reverse lookup feature to find Tetum words from English translations

## 5. Additional Materials and Examples

### Example: Using Lists for Agricultural Data

```python
# List of crops grown in Timor-Leste
crops = ["coffee", "rice", "corn", "cassava", "sweet potato"]

# List of annual production (in tons) for each crop
production = [10000, 120000, 70000, 45000, 30000]

# Displaying crop production data
for i in range(len(crops)):
    print(f"{crops[i].capitalize()}: {production[i]} tons")

# Finding the crop with the highest production
max_production = max(production)
max_index = production.index(max_production)
print(f"The crop with the highest production is {crops[max_index]} with {max_production} tons.")
```

### Example: Using Dictionaries for Municipality Data

```python
# Dictionary of Timor-Leste municipalities
municipalities = {
    "Dili": {
        "population": 277279,
        "area": 367,
        "capital": "Dili"
    },
    "Baucau": {
        "population": 123203,
        "area": 1506,
        "capital": "Baucau"
    },
    "Ermera": {
        "population": 125702,
        "area": 768,
        "capital": "Gleno"
    }
}

# Displaying municipality information
for name, info in municipalities.items():
    print(f"{name}:")
    print(f"  Population: {info['population']}")
    print(f"  Area: {info['area']} km²")
    print(f"  Capital: {info['capital']}")
    print()

# Calculating total population
total_population = sum(muni["population"] for muni in municipalities.values())
print(f"Total population of listed municipalities: {total_population}")
```

### Example: Using Tuples for Geographical Coordinates

```python
# Tuples representing coordinates of important locations in Timor-Leste
locations = [
    ("Cristo Rei", -8.5252, 125.6091),
    ("Mount Ramelau", -8.8752, 125.5683),
    ("Jaco Island", -8.4388, 127.3189)
]

# Function to calculate distance between two points (simplified)
def distance(point1, point2):
    return ((point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)**0.5

# Finding the distance between Cristo Rei and Mount Ramelau
dist = distance(locations[0], locations[1])
print(f"The distance between {locations[0][0]} and {locations[1][0]} is approximately {dist:.2f} degrees.")
```

These resources provide a comprehensive set of materials for teaching and learning about data structures in Python, with a focus on applications relevant to Timor-Leste.