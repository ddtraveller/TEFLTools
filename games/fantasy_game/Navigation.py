import pandas as pd
from math import radians, cos, sin, asin, sqrt
import random
import csv

def get_location_description(location_name):
    with open("Locations.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            if row and row[0] == location_name:
                return row[1] if len(row) > 1 else "A mysterious location in the realm."
    return "A mysterious location in the realm."

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
    Load locations from a CSV file
    """
    locations = pd.read_csv(file_path)
    return locations

def get_nearby_locations(locations, current_location, movement_speed):
    """
    Get nearby locations within the movement speed range, excluding the current location
    """
    nearby_locations = []
    
    for _, location in locations.iterrows():
        if location['name'] != current_location['name']:
            distance = haversine(current_location['latitude'], current_location['longitude'],
                                 location['latitude'], location['longitude'],
                                 current_location['elevation'], location['elevation'])
            
            if distance <= movement_speed:
                nearby_locations.append(location)
    
    return nearby_locations

def find_starting_location(locations, movement_speed):
    """
    Find a starting location with at least 3 nearby locations
    """
    while True:
        current_location = locations.sample().iloc[0]
        nearby_locations = get_nearby_locations(locations, current_location, movement_speed)
        if len(nearby_locations) >= 3:
            return current_location

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
    current_location = find_starting_location(locations, movement_speed)
    
    while True:
        current_location = navigate(locations, current_location, movement_speed)
        
        if current_location is None:
            break
        
        # Here you might want to add a chance for an encounter
        if random.random() < 0.5:  # 50% chance for an encounter
            from begin_game import encounter, select_initial_encounter  # Import here to avoid circular import
            monster_data, _ = select_initial_encounter()
            victory = encounter(character_data, monster_data, current_location['name'], file_path, movement_speed)
            if victory:
                print("You were victorious! You continue your exploration.")
            else:
                print("You retreat from the encounter and rest for a while.")