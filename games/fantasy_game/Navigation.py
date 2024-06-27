import json
from math import radians, cos, sin, asin, sqrt
import random
from Combat import encounter
from game_utils import select_initial_encounter, get_location_description

# Define the path to the JSON folder
JSON_FOLDER = 'json'

def haversine(lat1, lon1, lat2, lon2, elevation1, elevation2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees) and considering elevation
    """
    # convert decimal degrees to radians 
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    distance = c * r
    # calculate elevation difference
    elevation_diff = abs(elevation1 - elevation2)
    
    # calculate distance considering elevation
    distance = sqrt(distance**2 + elevation_diff**2)
    
    return distance

def load_locations(file_path):
    """
    Load locations from a JSON file
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Check if the loaded data is a list
        if isinstance(data, list):
            return data
        # Check if the loaded data is a dictionary with a 'locations' key
        elif isinstance(data, dict) and 'locations' in data:
            return data['locations']
        else:
            print(f"Error: Unexpected data structure in {file_path}")
            print("Expected a list of locations or a dictionary with a 'locations' key.")
            return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
        return []
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while loading locations: {str(e)}")
        return []

def get_nearby_locations(locations, current_location, movement_speed):
    """
    Get nearby locations within the movement speed range, excluding the current location
    """
    nearby_locations = []
    
    for location in locations:
        if location['name'] != current_location['name']:
            distance = haversine(current_location['latitude'], current_location['longitude'],
                                 location['latitude'], location['longitude'],
                                 current_location['elevation'], location['elevation'])
            
            if distance <= movement_speed:
                nearby_locations.append(location)
    
    return nearby_locations

def find_starting_location(locations, movement_speed):
    """
    Find a starting location with at least 1 nearby location
    """
    all_connected = False
    while not all_connected:
        for location in locations:
            nearby = get_nearby_locations(locations, location, movement_speed)
            if not nearby:
                print(f"Warning: {location['name']} is not connected to any other location.")
                print(f"Increasing movement speed to connect all locations.")
                movement_speed += 10  # Increase movement speed by 10 km
                break
        else:
            all_connected = True
    
    print(f"All locations are now connected with a movement speed of {movement_speed} km.")
    return random.choice(locations), movement_speed

def navigate(locations, current_location, movement_speed):
    """
    Navigate through the locations based on movement speed
    """
    print(f"Current Location: {current_location['name']}")
    print(f"Description: {current_location['description']}")
    
    nearby_locations = get_nearby_locations(locations, current_location, movement_speed)
    
    print("\nNearby Locations:")
    for i, location in enumerate(nearby_locations, 1):
        print(f"{i}. {location['name']}")
    
    choice = input("Enter the number of the location you want to visit (or 'q' to quit): ")
    
    if choice == 'q':
        print("Exiting navigation.")
        return None
    
    if choice.isdigit() and 1 <= int(choice) <= len(nearby_locations):
        destination = nearby_locations[int(choice) - 1]
        print(f"\nNavigating to {destination['name']}...")
        return destination
    
    print("Invalid choice. Please try again.")
    return current_location

def start_navigation(file_path, movement_speed, character_data):
    """
    Start the navigation system
    """
    locations = load_locations(file_path)
    if not locations:
        print("Error: No locations loaded. Exiting navigation.")
        return
    
    current_location, adjusted_movement_speed = find_starting_location(locations, movement_speed)
    
    while True:
        current_location = navigate(locations, current_location, adjusted_movement_speed)
        
        if current_location is None:
            break
        
        # Here you might want to add a chance for an encounter
        if random.random() < 0.5:  # 50% chance for an encounter
            monster_data, _ = select_initial_encounter()
            victory = encounter(character_data, monster_data, current_location['name'], file_path, adjusted_movement_speed)
            if victory:
                print("You were victorious! You continue your exploration.")
            else:
                print("You retreat from the encounter and rest for a while.")