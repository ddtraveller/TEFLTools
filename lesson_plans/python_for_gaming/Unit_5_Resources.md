# ## Learning Unit 5

## Learning Unit 5: Lists and Dictionaries
- Objectives:
  * Work with lists and dictionaries to store collections of data
  * Perform operations on lists and dictionaries
- Topics:
  * Creating and accessing lists
  * List methods
  * Dictionaries
- Activities:
  * Create a list of Timor-Leste's districts and perform operations on it
  * Make a dictionary of Tetum words and their English translations

## Unit Resources

Here are detailed resources for Learning Unit 5: Lists and Dictionaries, formatted in Markdown:

# Learning Unit 5: Lists and Dictionaries - Detailed Resources

## 1. Lecture Notes

### Lists in Python

#### Introduction to Lists
- A list is an ordered collection of items in Python
- Lists are mutable (can be changed after creation)
- Lists can contain items of different data types
- Syntax: `my_list = [item1, item2, item3]`

#### Creating Lists
```python
# Empty list
empty_list = []

# List of strings
fruits = ["apple", "banana", "orange"]

# List of mixed data types
mixed_list = [1, "hello", 3.14, True]
```

#### Accessing List Elements
- List indexing starts at 0
- Negative indexing starts from the end (-1 is the last element)
```python
fruits = ["apple", "banana", "orange"]
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: orange
```

#### List Slicing
- Syntax: `list[start:end:step]`
```python
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  # Output: [1, 2, 3]
print(numbers[::2])  # Output: [0, 2, 4]
```

#### Modifying Lists
```python
fruits = ["apple", "banana", "orange"]
fruits[1] = "grape"
print(fruits)  # Output: ["apple", "grape", "orange"]
```

#### Common List Methods
- `append()`: Add an item to the end of the list
- `insert()`: Insert an item at a specific position
- `remove()`: Remove the first occurrence of an item
- `pop()`: Remove and return an item at a specific index
- `sort()`: Sort the list in-place
- `reverse()`: Reverse the list in-place
- `len()`: Return the length of the list

### Dictionaries in Python

#### Introduction to Dictionaries
- A dictionary is an unordered collection of key-value pairs
- Dictionaries are mutable
- Keys must be unique and immutable (typically strings or numbers)
- Syntax: `my_dict = {key1: value1, key2: value2}`

#### Creating Dictionaries
```python
# Empty dictionary
empty_dict = {}

# Dictionary of student scores
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Dictionary with mixed value types
person = {
    "name": "Maria",
    "age": 30,
    "is_student": False,
    "hobbies": ["reading", "hiking"]
}
```

#### Accessing Dictionary Values
```python
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(student_scores["Bob"])  # Output: 92

# Using get() method (safer if key might not exist)
print(student_scores.get("David", "Not found"))  # Output: Not found
```

#### Modifying Dictionaries
```python
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Adding a new key-value pair
student_scores["David"] = 88

# Modifying an existing value
student_scores["Alice"] = 87

# Removing a key-value pair
del student_scores["Charlie"]
```

#### Common Dictionary Methods
- `keys()`: Return a view of all keys
- `values()`: Return a view of all values
- `items()`: Return a view of all key-value pairs
- `update()`: Update the dictionary with another dictionary or iterable of key-value pairs
- `clear()`: Remove all items from the dictionary

## 2. Discussion Questions

1. How do lists and dictionaries differ in terms of how they store and access data?
2. In what situations would you choose to use a list over a dictionary, and vice versa?
3. How can lists and dictionaries be used together to represent more complex data structures?
4. What are some real-world applications of lists and dictionaries in programming?
5. How might you use lists or dictionaries to represent information about Timor-Leste's districts or languages?

## 3. Writing Exercise Instructions

Write a short essay (250-300 words) on the following topic:

"Imagine you are designing a program to manage information about traditional Timorese crafts. Describe how you would use lists and dictionaries to organize and store information about different crafts, their materials, origins, and artisans. Explain your choices and how this data structure would help in managing and accessing the information efficiently."

## 4. Assignment Details

### Assignment 1: Timor-Leste District Information System

Create a program that stores and manages information about Timor-Leste's districts. Your program should:

1. Use a list of dictionaries to store information about each district, including:
   - Name
   - Population
   - Area (in square kilometers)
   - Capital city

2. Implement functions to:
   - Add a new district
   - Remove a district
   - Update information for a district
   - Display information for all districts
   - Search for a district by name
   - Calculate and display the total population of Timor-Leste

3. Create a simple menu-driven interface for users to interact with the program

### Assignment 2: Tetum-English Dictionary

Create a Tetum-English dictionary program that allows users to look up words and manage the dictionary. Your program should:

1. Use a dictionary to store Tetum words (keys) and their English translations (values)

2. Implement functions to:
   - Add new words and translations
   - Look up translations
   - Remove words
   - Update existing translations
   - Display all words and their translations
   - Quiz the user on random words from the dictionary

3. Create a simple menu-driven interface for users to interact with the program

4. Include at least 20 initial Tetum-English word pairs in your dictionary

## 5. Additional Materials and Examples

### Example: Using Lists and Dictionaries Together

```python
# List of dictionaries representing Timor-Leste districts
timor_leste_districts = [
    {
        "name": "Dili",
        "population": 277279,
        "area": 367,
        "capital": "Dili"
    },
    {
        "name": "Baucau",
        "population": 123203,
        "area": 1506,
        "capital": "Baucau"
    },
    {
        "name": "Bobonaro",
        "population": 92049,
        "area": 1376,
        "capital": "Maliana"
    }
]

# Accessing and displaying information
for district in timor_leste_districts:
    print(f"District: {district['name']}")
    print(f"Population: {district['population']}")
    print(f"Area: {district['area']} sq km")
    print(f"Capital: {district['capital']}")
    print()

# Calculating total population
total_population = sum(district['population'] for district in timor_leste_districts)
print(f"Total population of Timor-Leste: {total_population}")
```

### Example: Nested Dictionaries

```python
# Nested dictionary representing Timorese languages
timorese_languages = {
    "Tetum": {
        "speakers": 385000,
        "family": "Austronesian",
        "writing_system": "Latin alphabet"
    },
    "Mambae": {
        "speakers": 131000,
        "family": "Austronesian",
        "writing_system": "Latin alphabet"
    },
    "Makasae": {
        "speakers": 102000,
        "family": "Trans-New Guinea",
        "writing_system": "Latin alphabet"
    }
}

# Accessing and displaying information
for language, info in timorese_languages.items():
    print(f"Language: {language}")
    print(f"Number of speakers: {info['speakers']}")
    print(f"Language family: {info['family']}")
    print(f"Writing system: {info['writing_system']}")
    print()
```

These resources provide a comprehensive set of materials for teaching and learning about lists and dictionaries in Python, with a focus on applications relevant to Timor-Leste.