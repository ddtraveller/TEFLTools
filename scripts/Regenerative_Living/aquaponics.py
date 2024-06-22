import json
import os

def get_input(prompt, options=None):
    while True:
        response = input(prompt).strip().lower()
        if options is None or response in options:
            return response
        print("Invalid input. Please try again.")

def load_instructions(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. Using default instructions.")
        return default_instructions()
    except json.JSONDecodeError:
        print(f"Warning: {file_path} is not valid JSON. Using default instructions.")
        return default_instructions()

def default_instructions():
    return {
        "pond_construction": {
            "small": {"instructions": ["Dig a small pond", "Line the pond", "Fill with water"]},
            "medium": {"instructions": ["Dig a medium pond", "Line the pond", "Fill with water"]},
            "large": {"instructions": ["Dig a large pond", "Line the pond", "Fill with water"]}
        },
        "filtration_system": {
            "tilapia": ["Install mechanical filter", "Install biological filter"],
            "catfish": ["Install high-capacity filter", "Ensure good aeration"],
            "carp": ["Install robust filtration system", "Add UV sterilizer"]
        },
        "grow_beds": {
            "leafy": ["Build shallow beds", "Install drainage"],
            "herbs": ["Build medium-depth beds", "Ensure good drainage"],
            "fruiting": ["Build deep beds", "Add support structures"]
        },
        "growing_medium": {
            "gravel": ["Wash gravel", "Fill beds with gravel"],
            "coconut_coir": ["Rinse coir", "Mix with some gravel", "Fill beds"],
            "clay_pebbles": ["Rinse pebbles", "Fill beds with pebbles"]
        },
        "plumbing": ["Install pipes", "Add valves for control"],
        "power_system": {
            "grid": ["Install dedicated circuit", "Use weatherproof outlets"],
            "solar": ["Install solar panels", "Set up batteries and inverter"],
            "offgrid": ["Set up independent power system", "Ensure backup power options"],
            "manual": ["Design system for manual operation", "Install hand pumps or bicycle-powered generators"],
            "wind": ["Install wind turbine", "Set up batteries and inverter"]
        },
        "fish_introduction": ["Cycle system", "Slowly introduce fish"],
        "planting": ["Start seeds", "Transplant to system"],
        "water_quality_management": ["Test regularly", "Maintain proper pH and nutrient levels"]
    }

def print_instructions(instructions, indent=0):
    if isinstance(instructions, list):
        for item in instructions:
            print("  " * indent + "- " + str(item))
    elif isinstance(instructions, dict):
        for key, value in instructions.items():
            print("  " * indent + str(key) + ":")
            print_instructions(value, indent + 1)
    else:
        print("  " * indent + str(instructions))

def aquaponics_planner():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, 'aquaponics_instructions.json')
    instructions = load_instructions(json_path)

    print("Welcome to the Aquaponics Project Planner!")
    
    # Fish pond size
    pond_size = get_input("What size fish pond do you want to build? (small/medium/large): ", 
                          ["small", "medium", "large"])
    
    # Fish species
    fish_options = {"tilapia": "Tilapia", "catfish": "Catfish", "carp": "Carp"}
    fish = get_input("Which fish species do you want to use? (tilapia/catfish/carp): ", 
                     list(fish_options.keys()))
    
    # Plant types
    plant_options = {"leafy": "Leafy greens", "herbs": "Herbs", "fruiting": "Fruiting plants"}
    plants = get_input("Which type of plants do you want to grow? (leafy/herbs/fruiting): ", 
                       list(plant_options.keys()))
    
    # Growing medium
    medium = get_input("What growing medium do you want to use? (gravel/coconut_coir/clay_pebbles): ", 
                       ["gravel", "coconut_coir", "clay_pebbles"])
    
    # Power source
    power_options = {
        "grid": "Grid electricity",
        "solar": "Solar power",
        "offgrid": "Off-grid system",
        "manual": "Manual power (e.g., hand pumps, bicycle generators)",
        "wind": "Wind power"
    }
    print("\nAvailable power sources:")
    for key, value in power_options.items():
        print(f"- {value}")
    power = get_input("What power source will you use? (grid/solar/offgrid/manual/wind): ", 
                      list(power_options.keys()))
    
    # Generate instructions
    print("\n--- Detailed Aquaponics System Instructions ---")
    print(f"Fish Pond Size: {pond_size.capitalize()}")
    print(f"Fish Species: {fish_options[fish]}")
    print(f"Plant Type: {plant_options[plants]}")
    print(f"Growing Medium: {medium.replace('_', ' ').capitalize()}")
    print(f"Power Source: {power_options[power]}")
    
    print("\n1. Pond Construction:")
    print_instructions(instructions['pond_construction'][pond_size]['instructions'])
    
    print("\n2. Filtration System:")
    print_instructions(instructions['filtration_system'][fish])
    
    print("\n3. Grow Beds:")
    print_instructions(instructions['grow_beds'][plants])
    
    print("\n4. Growing Medium:")
    print_instructions(instructions['growing_medium'][medium])
    
    print("\n5. Plumbing:")
    print_instructions(instructions['plumbing'])
    
    print("\n6. Power System:")
    print_instructions(instructions['power_system'][power])
    
    print("\n7. Fish Introduction:")
    print_instructions(instructions['fish_introduction'])
    
    print("\n8. Planting:")
    print_instructions(instructions['planting'])
    
    print("\n9. Water Quality Management:")
    print_instructions(instructions['water_quality_management'])
    
    print("\nRemember to research specific care requirements for your chosen fish and plants.")
    print("Consult local experts or experienced aquaponics practitioners for additional guidance.")

if __name__ == "__main__":
    aquaponics_planner()