# ## Learning Unit 5

## Learning Unit 5: File Handling and Exception Handling
- Objectives:
  * Read from and write to files
  * Handle exceptions in Python programs
- Topics:
  * Opening, reading, and writing files
  * Try-except blocks for error handling
- Activities:
  * Create a program to read and analyze data from a CSV file of Timor-Leste's agricultural production
  * Implement error handling in previous programs

## Unit Resources

Here are detailed resources for Learning Unit 5: File Handling and Exception Handling, formatted in Markdown:

# Learning Unit 5: File Handling and Exception Handling

## 1. Lecture Notes

### File Handling

#### Opening Files
```python
# Basic file opening
file = open('filename.txt', 'r')  # 'r' for read mode

# Using 'with' statement (recommended)
with open('filename.txt', 'r') as file:
    # File operations here
```

File modes:
- 'r': Read (default)
- 'w': Write (overwrites existing content)
- 'a': Append (adds to existing content)
- 'r+': Read and write

#### Reading Files
```python
# Read entire file
content = file.read()

# Read line by line
for line in file:
    print(line)

# Read specific number of characters
chunk = file.read(10)  # Reads 10 characters
```

#### Writing Files
```python
with open('output.txt', 'w') as file:
    file.write("Hello, Timor-Leste!")
    file.writelines(["Line 1\n", "Line 2\n"])
```

### Exception Handling

#### Basic Structure
```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the specific exception
    print("Cannot divide by zero!")
except Exception as e:
    # Handle any other exception
    print(f"An error occurred: {e}")
else:
    # Executed if no exception occurs
    print("Operation successful")
finally:
    # Always executed, regardless of exceptions
    print("Cleanup code")
```

#### Common Exceptions
- `FileNotFoundError`: When trying to access a file that doesn't exist
- `ValueError`: When an operation receives an argument with the right type but inappropriate value
- `TypeError`: When an operation is performed on an object of inappropriate type
- `IndexError`: When trying to access an index that is out of range

### Working with CSV Files
```python
import csv

# Reading CSV
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# Writing CSV
with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.writerow(['Ana', 25, 'Dili'])
```

## 2. Discussion Questions

1. How can file handling be useful in managing agricultural data in Timor-Leste?
2. What are some potential risks of not implementing proper exception handling in a program?
3. How might CSV files be used to track and analyze coffee production in Timor-Leste?
4. Discuss the advantages of using the `with` statement when working with files.
5. In what scenarios might you choose to use 'append' mode instead of 'write' mode when working with files?

## 3. Writing Exercise Instructions

Write a short essay (200-300 words) on the following topic:

"The Importance of Data Management in Timor-Leste's Development"

Consider the following points:
- How can effective file handling and data analysis contribute to various sectors in Timor-Leste?
- What challenges might Timor-Leste face in implementing data-driven solutions?
- Propose a specific project that could benefit from Python's file handling capabilities.

## 4. Assignment Details

### Assignment 1: Agricultural Data Analysis

Create a Python program that does the following:

1. Reads a CSV file named `timor_agriculture.csv` containing the following columns:
   - Year
   - Crop (e.g., coffee, rice, corn)
   - Production (in tons)
   - District

2. Calculates and prints:
   - The total production for each crop across all years and districts
   - The average production per year for each crop
   - The district with the highest production for each crop

3. Writes the results to a new file named `agriculture_summary.txt`

4. Implements proper exception handling for file operations and data processing

### Assignment 2: Recipe Manager

Create a Python program that manages a collection of Timorese recipes:

1. The program should read from and write to a file named `timorese_recipes.txt`

2. Implement the following features:
   - Display all recipes
   - Add a new recipe (including name, ingredients, and instructions)
   - Search for a recipe by name
   - Delete a recipe

3. Use proper exception handling for all file operations and user inputs

4. Implement a simple menu system for user interaction

## 5. Additional Materials

### Sample CSV Data (timor_agriculture.csv)

```
Year,Crop,Production,District
2018,Coffee,12000,Ermera
2018,Rice,45000,Baucau
2018,Corn,30000,Viqueque
2019,Coffee,13500,Ermera
2019,Rice,47000,Baucau
2019,Corn,32000,Viqueque
2020,Coffee,11800,Ermera
2020,Rice,46500,Baucau
2020,Corn,31500,Viqueque
```

### Example: Reading and Writing Files

```python
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of {filename}:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Successfully wrote to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# Usage
read_file('example.txt')
write_file('output.txt', "Hello, Timor-Leste!")
```

This comprehensive set of resources should provide students with a solid foundation in file handling and exception handling, with examples and exercises relevant to the Timor-Leste context.