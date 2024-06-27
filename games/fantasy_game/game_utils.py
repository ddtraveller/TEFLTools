import random
import json
import os

# Define the path to the JSON folder
JSON_FOLDER = 'json'

def select_initial_encounter():
    monsters_file = os.path.join(JSON_FOLDER, 'monsters.json')
    with open(monsters_file, "r") as file:
        monsters_data = json.load(file)
    
    level_1_monsters = [monster for monster in monsters_data if monster['level'] == 1]
    selected_monster = random.choice(level_1_monsters)
    
    # Ensure the monster has an 'armor_class' key
    if 'armor_class' not in selected_monster:
        selected_monster['armor_class'] = random.randint(10, 15)  # Default range, adjust as needed
    
    location = random.choice(selected_monster['locations'])
    
    return selected_monster, location

def get_location_description(location_name):
    locations_file = os.path.join(JSON_FOLDER, 'timor_leste_locations.json')
    with open(locations_file, "r") as file:
        locations = json.load(file)
    for location in locations:
        if location['name'] == location_name:
            return location['description']
    return "A mysterious location in the realm."