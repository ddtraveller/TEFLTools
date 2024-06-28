import random
import json
import os
import sys
from character_gen import generate_character
from Combat import encounter, combat
from Navigation import start_navigation
from game_utils import select_initial_encounter, get_location_description
from anthropic import Anthropic

# Define the path to the JSON folder
JSON_FOLDER = 'json'

# Assume ANTHROPIC_API_KEY is set in your environment variables
client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

encounter_weights = {
    'combat': 0.4,
    'movement': 0.2,
    'dialogue': 0.4
}

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
    
    locations_file = os.path.join(JSON_FOLDER, 'timor_leste_locations.json')
    movement_speed = 20  # Adjust this value based on the character's movement speed
    
    # Start with the movement phase
    print("You find yourself ready to explore the vast lands of Timor Leste Fantasia.")
    start_navigation(locations_file, movement_speed, character_data)

if __name__ == "__main__":
    main()