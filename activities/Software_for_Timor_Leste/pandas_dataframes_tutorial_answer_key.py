import pandas as pd
import numpy as np

# Set up the mystery data
suspects = pd.DataFrame({
    'Name': ['Alice Smith', 'Bob Johnson', 'Carol Williams', 'David Brown'],
    'Age': [35, 42, 38, 45],
    'Occupation': ['Teacher', 'Accountant', 'Chef', 'Lawyer'],
    'Phone': ['555-1234', '555-5678', '555-9876', '555-4321']
})

locations = pd.DataFrame({
    'Place': ['Library', 'Park', 'Cafe', 'Office'],
    'Address': ['123 Book St', '456 Green Ave', '789 Coffee Rd', '101 Work Ln']
})

clues = pd.DataFrame({
    'Item': ['Red scarf', 'Black gloves', 'Blue pen', 'Green notebook'],
    'Location': ['Library', 'Park', 'Cafe', 'Office']
})

phone_book = pd.DataFrame({
    'Name': ['Police Station', 'Hospital', 'Fire Department'],
    'Phone': ['911', '555-7777', '555-3333']
})

print("Welcome to the Pandas Detective Mystery Solution!")

# Step 1: Find where the red scarf was last seen
print("\nStep 1: Finding where the red scarf was last seen")
scarf_location = clues[clues['Item'] == 'Red scarf']['Location'].values[0]
print(f"The red scarf was last seen at the {scarf_location}")

# Step 2: Find suspects who could be near the library
print("\nStep 2: Finding suspects who could be near the library")
potential_suspect = suspects[suspects['Occupation'] == 'Teacher']
print("Potential suspect:")
print(potential_suspect)

# Step 3: Get the suspect's name
print("\nStep 3: Getting the suspect's name")
suspect_name = suspects[suspects['Occupation'] == 'Teacher']['Name'].values[0]
print(f"The suspect's name is {suspect_name}")

# Step 4: Find the suspect's phone number
print("\nStep 4: Finding the suspect's phone number")
suspect_phone = suspects[suspects['Name'] == 'Alice Smith']['Phone'].values[0]
print(f"Alice Smith's phone number is {suspect_phone}")

# Step 5: Find the police station's number
print("\nStep 5: Finding the police station's number")
police_phone = phone_book[phone_book['Name'] == 'Police Station']['Phone'].values[0]
print(f"The police station's phone number is {police_phone}")

print("\nMystery Solved! Here's a summary of our investigation:")
print(f"1. The red scarf was found at the {scarf_location}.")
print(f"2. We identified a potential suspect who works as a Teacher.")
print(f"3. The suspect's name is {suspect_name}.")
print(f"4. We found {suspect_name}'s phone number: {suspect_phone}.")
print(f"5. We contacted the police at {police_phone}.")
print("\nGreat work, Detective! You've successfully used Pandas to solve the mystery!")