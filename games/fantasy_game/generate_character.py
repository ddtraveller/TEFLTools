import random
import json
import time
from Spells import Spells

classes = ["Fighter", "Rogue", "Wizard", "Cleric", "Ranger", "Paladin", "Martial Artist", "Shaman", "Monk", "Barbarian"]
elements = ["Fire", "Air", "Earth", "Water"]
archetypes = ["Lion", "Eagle", "Bear", "Wolf", "Owl", "Snake", "Dolphin", "Elephant", "Butterfly", "Turtle", "Deer", "Fox"]
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
    "Barbarian": (0, 20)
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

    character_class = random.choice(classes)
    element_index = abs(element_score) % 4
    character_element = elements[element_index]
    archetype_index = abs(element_score) % 12
    character_archetype = archetypes[archetype_index]

    # Load weapons and equipment from items.json file
    with open("items.json", "r") as file:
        items_data = json.load(file)
        weapons = items_data["weapons"]
        equipment = items_data["equipment"]

    character_equipment = equipment[character_class]

    attributes = {
        "Strength": random.randint(9, 18),
        "Intelligence": random.randint(9, 18),
        "Wisdom": random.randint(9, 18),
        "Dexterity": random.randint(9, 18),
        "Constitution": random.randint(9, 18),
        "Charisma": random.randint(9, 18)
    }

    attribute_average = sum(attributes.values()) / len(attributes)

    while attribute_average < 13:
        attributes = {
            "Strength": random.randint(9, 18),
            "Intelligence": random.randint(9, 18),
            "Wisdom": random.randint(9, 18),
            "Dexterity": random.randint(9, 18),
            "Constitution": random.randint(9, 18),
            "Charisma": random.randint(9, 18)
        }
        attribute_average = sum(attributes.values()) / len(attributes)

    strength = attributes["Strength"]
    dexterity = attributes["Dexterity"]

    valid_weapons = [weapon for weapon, stats in weapons.items()
                     if strength >= stats["strength"] and dexterity >= stats["dexterity"]]

    if character_class == "Fighter":
        preferred_weapons = ["Greatsword", "Longsword", "Battleaxe", "Warhammer"]
    elif character_class == "Rogue":
        preferred_weapons = ["Rapier", "Shortsword", "Dagger", "Hand Crossbow"]
    elif character_class == "Wizard":
        preferred_weapons = ["Staff", "Dagger", "Wand", "Sling"]
    elif character_class == "Cleric":
        preferred_weapons = ["Mace", "Warhammer", "Flail", "Crossbow"]
    elif character_class == "Ranger":
        preferred_weapons = ["Longbow", "Shortsword", "Rapier", "Dagger"]
    elif character_class == "Paladin":
        preferred_weapons = ["Longsword", "Warhammer", "Greatsword", "Maul"]
    elif character_class == "Martial Artist":
        preferred_weapons = ["Scimitar", "Quarterstaff", "Club", "Sling"]
    elif character_class == "Shaman":
        preferred_weapons = ["Rapier", "Longsword", "Crossbow", "Dagger"]
    elif character_class == "Monk":
        preferred_weapons = ["Quarterstaff", "Unarmed Strike", "Shortsword", "Nunchaku"]
    elif character_class == "Barbarian":
        preferred_weapons = ["Greataxe", "Greatsword", "Maul", "Warhammer"]
    else:
        preferred_weapons = []

    available_weapons = [weapon for weapon in valid_weapons if weapon in preferred_weapons]

    if available_weapons:
        character_main_weapon = random.choice(available_weapons)
    else:
        character_main_weapon = random.choice(valid_weapons)

    print("\nYour Fantasy Character Avatar:")
    print("Class:", character_class)
    print("Element:", character_element)
    print("Archetype:", character_archetype)
    print("Main Weapon:", character_main_weapon)
    print("Equipment:", character_equipment)

    spells = Spells()
    character_spells = []

    if character_class == "Wizard":
        for _ in range(3):
            spell_category = random.choice(list(spells.spell_types.keys())).lower() + "_spells"
            character_spells.append(random.choice(getattr(spells, spell_category)))
    elif character_class in ["Cleric", "Shaman", "Monk"]:
        for _ in range(2):
            spell_category = random.choice(list(spells.spell_types.keys())).lower() + "_spells"
            character_spells.append(random.choice(getattr(spells, spell_category)))
    elif character_class in ["Rogue", "Ranger", "Paladin", "Martial Artist"]:
        spell_category = random.choice(list(spells.spell_types.keys())).lower() + "_spells"
        character_spells.append(random.choice(getattr(spells, spell_category)))

    if character_spells:
        print("Spells:")
        for spell in character_spells:
            print("- " + spell)

    print("\nAttributes:")
    for attribute, score in attributes.items():
        print(f"{attribute}: {score}")
    print(f"Average Attribute Score: {attribute_average:.2f}")

    # Load background stories from the JSON file
    try:
        with open("background_stories.json", "r") as file:
            background_data = json.load(file)

        # Find the matching background story based on element and archetype
        background_story = next((bg["story"] for bg in background_data["backgrounds"]
                                 if bg["element"] == character_element and bg["archetype"] == character_archetype), None)
    except FileNotFoundError:
        background_story = None
    if background_story:
        print("\nBackground Story:")
        print(background_story)
    else:
        default_story = "You are a " + character_element + " " + character_class + " with the spirit of the " + character_archetype + ". " + \
                        "From a young age, you showed an aptitude for adventure and a strong connection to the elemental forces. " + \
                        "Your choices throughout your life have shaped you into the person you are today. " + \
                        "Now, armed with your " + character_main_weapon + " and " + character_equipment + ", you set out to make your mark on the world."
        print("\nBackground Story:")
        print(default_story)

    # Generate the character data as a dictionary
    character_data = {
        "class": character_class,
        "element": character_element,
        "archetype": character_archetype,
        "main_weapon": character_main_weapon,
        "equipment": [character_equipment],  # Convert to a list
        "spells": character_spells,
        "attributes": attributes,
        "background_story": background_story if background_story else default_story
    }

    # Generate starting income based on the character's class
    min_income, max_income = starting_income[character_class]
    character_money = random.randint(min_income, max_income)

    # Load equipment from equipment.json file
    with open("equipment.json", "r") as file:
        equipment_data = json.load(file)
        
    # Save the character data to a JSON file
    with open("character_data.json", "w") as file:
        json.dump(character_data, file, indent=4)

    print("\nCharacter data saved to 'character_data.json'.")

    input("\nHit enter to continue...")

    # Merchant encounter
    print("\nAs you set out on your journey, you come across a merchant on the road.")
    print("The merchant greets you and offers an assortment of items for sale:")

    # Randomly select a dozen items from equipment_data
    merchant_items = random.sample(equipment_data, 12)

    for i, item in enumerate(merchant_items, 1):
        print(f"{i}. {item['name']} - {item['cost']}")
        print(f"   {item['description']}")

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

    # Add purchased items to the character data
    character_data["purchased_items"] = [item["name"] for item in purchased_items]
    character_data["remaining_money"] = character_money
    
    # Add purchased items to the equipment list
    character_data["equipment"].extend(character_data["purchased_items"])

    # Save the updated character data to the JSON file
    with open("character_data.json", "w") as file:
        json.dump(character_data, file, indent=4)

    print("\nUpdated character data saved to 'character_data.json'.")
    print("\nYour Fantasy Character Avatar:")
    print("Class:", character_class)
    print("Element:", character_element)
    print("Archetype:", character_archetype)
    print("Main Weapon:", character_main_weapon)
    print("Equipment:", character_data["equipment"])

# Run the character generator
generate_character()