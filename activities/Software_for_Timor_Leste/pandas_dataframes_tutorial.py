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

print("Welcome, Detective! A valuable painting has been stolen from the city museum.")
print("Your task is to solve the mystery using your data analysis skills.")

# Step 1: Find the suspect's occupation
print("\nStep 1: We found a red scarf at the crime scene. Find where it was last seen.")
print("Use: clues[clues['Item'] == 'Red scarf']['Location']")

location = input("Enter the location where the red scarf was last seen: ")

if location.lower() == 'library':
    print("Correct! The suspect might work near the library.")
    
    # Step 2: Find suspects who could be near the library
    print("\nStep 2: Find suspects whose occupation might bring them near a library.")
    print("Use: suspects[suspects['Occupation'] == 'Teacher']")
    
    suspect_occupation = input("Enter the occupation of the potential suspect: ")
    
    if suspect_occupation.lower() == 'teacher':
        print("Good work! We're looking for a teacher.")
        
        # Step 3: Get the suspect's name
        print("\nStep 3: Find the name of the teacher in our suspects list.")
        print("Use: suspects[(suspects['Occupation'] == 'Teacher')]['Name']")
        
        suspect_name = input("Enter the name of the suspect: ")
        
        if suspect_name.lower() == 'alice smith':
            print("Excellent! Alice Smith is our primary suspect.")
            
            # Step 4: Find the suspect's phone number
            print("\nStep 4: We need to call Alice Smith for questioning. Find her phone number.")
            print("Use: suspects[suspects['Name'] == 'Alice Smith']['Phone']")
            
            suspect_phone = input("Enter Alice Smith's phone number: ")
            
            if suspect_phone == '555-1234':
                print("Great! We'll call her right away.")
                
                # Step 5: Find the police station's number
                print("\nStep 5: We need to inform the police. Find the police station's number.")
                print("Use: phone_book[phone_book['Name'] == 'Police Station']['Phone']")
                
                police_phone = input("Enter the police station's phone number: ")
                
                if police_phone == '911':
                    print("Perfect! We've informed the police.")
                    
                    # Final Step: Solve the case
                    print("\nFinal Step: We found the painting in Alice's possession.")
                    print("Congratulations, Detective! You've solved the case using your Pandas skills.")
                else:
                    print("That's not the correct police number. The case remains unsolved.")
            else:
                print("That's not Alice's number. The trail has gone cold.")
        else:
            print("That's not the correct suspect. The investigation has hit a dead end.")
    else:
        print("That's not the correct occupation. The thief remains at large.")
else:
    print("That's not where the scarf was found. The investigation cannot proceed.")

print("\nThank you for using your Pandas skills to solve this mystery!")