import random
import json
import csv
import os
import sys
from character_gen import generate_character
from Combat import encounter  # Remove 'combat' from this import
from Navigation import start_navigation
from anthropic import Anthropic

# Assume ANTHROPIC_API_KEY is set in your environment variables
client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

encounter_weights = {
    'combat': 0.4,
    'movement': 0.2,
    'dialogue': 0.4
}

def get_location_description(location_name):
    with open("Locations.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            if row and row[0] == location_name:
                return row[1] if len(row) > 1 else "A mysterious location in the realm."
    return "A mysterious location in the realm."

def select_initial_encounter():
    with open("monsters.json", "r") as file:
        monsters_data = json.load(file)
    
    level_1_monsters = [monster for monster in monsters_data if monster['level'] == 1]
    selected_monster = random.choice(level_1_monsters)
    
    # Ensure the monster has an 'armor_class' key
    if 'armor_class' not in selected_monster:
        selected_monster['armor_class'] = random.randint(10, 15)  # Default range, adjust as needed
    
    location = random.choice(selected_monster['locations'])
    
    return selected_monster, location

def weighted_choice(weights):
    choices = list(weights.keys())
    probabilities = list(weights.values())
    return random.choices(choices, weights=probabilities, k=1)[0]

def load_character(character_name):
    character_files = os.listdir('characters')
    for file in character_files:
        if character_name.lower() in file.lower():
            with open(f'characters/{file}', 'r') as f:
                return json.load(f)
    return None

def main():
    print("Welcome to Timor Leste Fantasia!")
    character_name = input("Enter your character's name: ")
    
    character_data = load_character(character_name)
    
    if character_data:
        print(f"\n{character_data['name']} slowly opens their eyes, the fog of a long, deep sleep gradually lifting...")
        print("As consciousness returns, memories of past adventures in Timor Leste Fantasia flood back.")
        print("The familiar sights, sounds, and scents of this magical realm surround you once more.")
        print(f"Welcome back, {character_data['name']}! Your journey continues...\n")
    else:
        print(f"No existing character found with the name {character_name}. Creating a new character...")
        character_data = generate_character(character_name)
    
    file_path = 'Locations.csv'
    movement_speed = 20  # Adjust this value based on the character's movement speed
    
    # Start with the movement phase
    print("You find yourself ready to explore the vast lands of Timor Leste Fantasia.")
    start_navigation(file_path, movement_speed, character_data)

if __name__ == "__main__":
    main()