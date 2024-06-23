import random
import json
import time
from Character import create_character
from Combat import combat
from Navigation import start_navigation

starting_income = {
    "Fighter": (10, 300),
    "Rogue": (10, 250),
    "Wizard": (10, 750),
    "Cleric": (200, 1000),
    "Ranger": (10, 350),
    "Paladin": (200, 750),
    "Martial Artist": (10, 200),
    "Shaman": (10, 200),
    "Monk": (0, 20),
    "Barbarian": (0, 20),
    "Warlock": (10, 500)     
}

def get_user_choice(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        choice = input("Enter your choice (1-" + str(len(options)) + "): ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice) - 1
        else:
            print("Invalid choice. Please try again.")

def generate_character():
    print("Welcome to the Fantasy Character Avatar Generator!")
    print("In this interactive game, you will make choices that shape your character's personality and background.")
    print("Based on your choices, we will generate a unique Fantasy character avatar for you.")
    print("Let's begin!\n")

    # Load stories from stories.json file
    with open("stories.json", "r") as file:
        stories = json.load(file)

    random.shuffle(stories)
    selected_stories = stories[:6]

    element_score = 0

    for story in selected_stories:
        print(story["story"])
        choice = get_user_choice(story["options"])
        element_score += story["scores"][choice]

    character_data = create_character(element_score)
    # Calculate hit points based on Constitution
    base_hit_points = 10  # Base HP for a level 1 character
    constitution_modifier = (character_data['attributes']['Constitution'] - 10) // 2
    hit_points = base_hit_points + constitution_modifier

    # Add hit points to character data
    character_data['hit_points'] = hit_points
    character_data['max_hit_points'] = hit_points
    
    character_class = character_data["class"]
    
    # Generate starting income based on the character's class
    min_income, max_income = starting_income.get(character_class, (10, 300))  # Default to (10, 300) if class not found
    character_money = random.randint(min_income, max_income)    
    
    character_element = character_data["element"]
    character_archetype = character_data["archetype"]
    character_main_weapon = character_data["main_weapon"]
    character_equipment = character_data["equipment"]

    print("\nYour Fantasy Character Avatar:")
    print("Class:", character_class)
    print("Element:", character_element)
    print("Archetype:", character_archetype)
    print("Main Weapon:", character_main_weapon)
    print("Equipment:", character_equipment)

    if "spells" in character_data:
        print("Spells:")
        for spell in character_data["spells"]:
            print("- " + spell["name"])

    print("\nAttributes:")
    for attribute, score in character_data["attributes"].items():
        print(f"{attribute}: {score}")

    print("\nBackground Story:")
    print(character_data["background_story"])

    input("\nHit enter to continue...")

    # Merchant encounter
    print("\nAs you set out on your journey, you come across a merchant on the road.")
    print("The merchant greets you and offers an assortment of items for sale:")

    # Load equipment from equipment.json file
    with open("equipment.json", "r") as file:
        equipment_data = json.load(file)

    # Randomly select a dozen items from equipment_data
    merchant_items = random.sample(equipment_data, 12)

    for i, item in enumerate(merchant_items, 1):
        print(f"{i}. {item['name']} - {item['cost']}")
        print(f"   {item['description']}")

    # Generate starting income based on the character's class
    min_income, max_income = starting_income[character_class]
    character_money = random.randint(min_income, max_income)

    print(f"\nYou have {character_money} gold pieces to spend.")

    print(f"\nYou have {character_money // 100} gp, {(character_money % 100) // 10} sp, and {character_money % 10} cp to spend.")

    purchased_items = []

    while True:
        choice = input("Enter the number of the item you want to buy (or 'q' to quit): ")
        if choice == 'q':
            break
        if choice.isdigit() and 1 <= int(choice) <= len(merchant_items):
            item_index = int(choice) - 1
            item = merchant_items[item_index]
            cost_parts = item['cost'].split()
            cost = int(cost_parts[0])
            currency = cost_parts[1]

            if currency == 'cp':
                cost_in_cp = cost
            elif currency == 'sp':
                cost_in_cp = cost * 10
            elif currency == 'gp':
                cost_in_cp = cost * 100
            else:
                print("Unknown currency. Skipping item.")
                continue

            if character_money >= cost_in_cp:
                character_money -= cost_in_cp
                purchased_items.append(item)
                print(f"You bought {item['name']} for {item['cost']}. You have {character_money // 100} gp, {(character_money % 100) // 10} sp, and {character_money % 10} cp left.")
            else:
                print("You don't have enough money to buy that item.")
        else:
            print("Invalid choice. Please try again.")

    print(f"\nYou have {character_money // 100} gp, {(character_money % 100) // 10} sp, and {character_money % 10} cp left.")
    print("\nYou continue your journey with your newly acquired items.")

    # Add purchased items to the character data
    character_data["purchased_items"] = [item["name"] for item in purchased_items]
    character_data["remaining_money"] = character_money

    # Add purchased items to the equipment list
    character_data["equipment"].extend(character_data["purchased_items"])

    # Save the updated character data to the JSON file
    with open("character_data.json", "w") as file:
        json.dump(character_data, file, indent=4)

    print("\nUpdated character data saved to 'character_data.json'.")

    # Load goblin data from monsters/goblin.json
    with open("monsters/goblin.json", "r") as file:
        goblin_data = json.load(file)

    # Add movement_speed and armor_class to goblin data
    goblin_data['movement_speed'] = goblin_data['speed']
    goblin_data['armor_class'] = goblin_data['defense']

    # Encounter with the goblin
    print("\nAs you travel further, you encounter a goblin!")
    combat(character_data, goblin_data)

    print("\nAfter the goblin encounter, you continue your journey.")

    return character_data

def main():
    character_data = generate_character()
    
    # Start navigation after character creation
    file_path = 'Locations.csv'
    movement_speed = 50  # Adjust this value based on the character's movement speed
    start_navigation(file_path, movement_speed)

if __name__ == "__main__":
    main()