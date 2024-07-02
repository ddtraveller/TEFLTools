# ## Learning Unit 6

## Learning Unit 6: File I/O and Basic Data Analysis
- Objectives:
  * Read from and write to files
  * Perform basic data analysis on local datasets
- Topics:
  * Reading and writing text files
  * CSV files
  * Basic data analysis
- Activities:
  * Read a CSV file of Timor-Leste economic data and calculate averages
  * Write a program to analyze coffee production data from different regions

## Unit Resources

Here are detailed resources for Learning Unit 6: File I/O and Basic Data Analysis, formatted in Markdown:

# Resources for Learning Unit 6: File I/O and Basic Data Analysis

## 1. Sample CSV Files

### Timor-Leste Economic Data (timor_leste_economy.csv)

```
Year,GDP_Growth,Inflation,Unemployment
2015,4.0,0.6,3.8
2016,5.1,-1.3,4.1
2017,3.6,0.5,4.4
2018,3.1,2.3,4.5
2019,3.4,0.9,4.8
2020,-6.8,0.5,5.1
2021,1.5,3.8,5.3
```

### Coffee Production Data (coffee_production.csv)

```
Region,2019_Production,2020_Production,2021_Production
Ermera,1500,1450,1600
Aileu,800,750,850
Liquiça,600,580,620
Manufahi,450,400,480
Ainaro,350,330,370
```

## 2. Detailed Lecture Notes

### 2.1 Reading and Writing Text Files

#### Opening and Reading Files

```python
# Open a file for reading
file = open('example.txt', 'r')

# Read the entire file
content = file.read()

# Read line by line
for line in file:
    print(line.strip())

# Close the file
file.close()

# Using 'with' statement (recommended)
with open('example.txt', 'r') as file:
    content = file.read()
```

#### Writing to Files

```python
# Open a file for writing
with open('output.txt', 'w') as file:
    file.write("Hello, Timor-Leste!\n")
    file.write("This is a new line.")

# Appending to a file
with open('output.txt', 'a') as file:
    file.write("\nThis line is appended.")
```

### 2.2 Working with CSV Files

```python
import csv

# Reading a CSV file
with open('timor_leste_economy.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header
    for row in csv_reader:
        print(f"Year: {row[0]}, GDP Growth: {row[1]}%")

# Writing to a CSV file
data = [
    ['District', 'Population'],
    ['Dili', 277279],
    ['Baucau', 123203],
    ['Ermera', 125702]
]

with open('districts.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
```

### 2.3 Basic Data Analysis

```python
import csv

# Calculate average GDP growth
total_growth = 0
count = 0

with open('timor_leste_economy.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header
    for row in csv_reader:
        total_growth += float(row[1])
        count += 1

average_growth = total_growth / count
print(f"Average GDP growth: {average_growth:.2f}%")

# Find maximum coffee production
max_production = 0
max_region = ""

with open('coffee_production.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header
    for row in csv_reader:
        production_2021 = int(row[3])
        if production_2021 > max_production:
            max_production = production_2021
            max_region = row[0]

print(f"Region with highest 2021 production: {max_region} ({max_production} tons)")
```

## 3. Discussion Questions

1. How can file I/O be useful in real-world applications in Timor-Leste?
2. What are some advantages of using CSV files for storing data compared to plain text files?
3. How might data analysis of economic indicators help in policy-making for Timor-Leste?
4. What other types of local data could be analyzed to benefit communities in Timor-Leste?
5. How can we ensure data privacy and security when working with sensitive information in files?

## 4. Writing Exercise Instructions

Write a short essay (200-300 words) on the following topic:

"The Importance of Data Analysis in Developing Timor-Leste's Agriculture Sector"

Consider the following points:
- How can data analysis help farmers make better decisions?
- What types of data would be most useful to collect and analyze?
- What challenges might exist in implementing data-driven agriculture in Timor-Leste?

## 5. Assignment Details

### 5.1 Timor-Leste Economic Data Analysis

1. Read the 'timor_leste_economy.csv' file.
2. Calculate and print the average GDP growth rate for all years.
3. Find and print the year with the highest and lowest inflation rates.
4. Calculate the average unemployment rate for the last three years in the dataset.
5. Write a summary of your findings to a new text file called 'economic_summary.txt'.

### 5.2 Coffee Production Analysis

1. Read the 'coffee_production.csv' file.
2. For each region, calculate the average production over the three years.
3. Determine which region had the highest increase in production from 2019 to 2021.
4. Create a new CSV file called 'coffee_summary.csv' with columns: Region, Average Production, Production Increase.
5. Print a statement about which region might be the best to invest in based on the data, and why.

## 6. Additional Materials and Examples

### 6.1 Error Handling in File Operations

```python
try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("An error occurred while reading the file.")
```

### 6.2 Using Pandas for Data Analysis (Advanced)

```python
import pandas as pd

# Read CSV file
df = pd.read_csv('timor_leste_economy.csv')

# Calculate average GDP growth
average_growth = df['GDP_Growth'].mean()

# Find year with highest inflation
max_inflation_year = df.loc[df['Inflation'].idxmax(), 'Year']

print(f"Average GDP growth: {average_growth:.2f}%")
print(f"Year with highest inflation: {max_inflation_year}")
```

### 6.3 Data Visualization Example (Using matplotlib)

```python
import matplotlib.pyplot as plt
import pandas as pd

# Read CSV file
df = pd.read_csv('coffee_production.csv')

# Create bar plot
plt.figure(figsize=(10, 6))
plt.bar(df['Region'], df['2021_Production'])
plt.title('Coffee Production by Region in 2021')
plt.xlabel('Region')
plt.ylabel('Production (tons)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('coffee_production_2021.png')
plt.show()
```

This comprehensive set of resources should provide ample material for the week's lessons on File I/O and Basic Data Analysis, with a focus on applications relevant to Timor-Leste.