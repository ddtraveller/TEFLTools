import random
import json
import time
import os
from Character import create_character
from Combat import combat
from Navigation import start_navigation
import anthropic
import csv

ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
if ANTHROPIC_API_KEY:
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
else:
    print("Warning: ANTHROPIC_API_KEY not set. Will use fallback method for background story generation.")
    client = None

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
    "Warlock": (10, 500),
    "Druid": (10, 300)
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

def generate_background_story(character_data, world_description):
    if client:
        try:
            prompt = f"""As a Dungeon Master, create a compelling background origin story for a character with the following attributes:

Character Name: {character_data['name']}
Character Gender: {character_data['gender']}
Character Class: {character_data['class']}
Element: {character_data['element']}
Archetype: {character_data['archetype']}
Main Weapon: {character_data['main_weapon']}
Equipment: {', '.join(character_data['equipment'])}
Attributes:
{' '.join([f'{attr}: {score}' for attr, score in character_data['attributes'].items()])}

Fantasy World Description:
{world_description}

Please provide a rich and detailed background story that incorporates these elements and fits within the described fantasy world."""

            message = client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=500,
                temperature=0.7,
                system="You are a creative Dungeon Master tasked with generating compelling character backstories.",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            return message.content[0].text.strip()
        except Exception as e:
            print(f"Error generating background story using API: {e}")
            print("Using fallback method for background story generation.")

    # Fallback method if API is not available or fails
    return f"{character_data['name']} is a brave {character_data['gender']} {character_data['class']} who wields a {character_data['main_weapon']}. " \
           f"Skilled in the ways of {character_data['element']}, {character_data['name']} follows the path of the {character_data['archetype']}. " \
           f"Armed with {', '.join(character_data['equipment'])}, {character_data['name']} sets out to face the dangers of this mysterious world."

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
    
    location = random.choice(selected_monster['locations'])
    
    return selected_monster, location

def encounter(character_data, monster_data, location):
    print(f"\nYou find yourself in {location}.")
    description = get_location_description(location)
    if description:
        print(description)
    else:
        print("You look around, taking in the unfamiliar surroundings.")
    
    print(f"\nAs you explore this new area, you encounter a {monster_data['name']}!")
    print(f"\nThe {monster_data['name']} Description:")
    print(monster_data['long_description'])

    conversation_history = []
    encounter_ongoing = True
    interaction_count = 0

    while encounter_ongoing:
        print("\nWhat would you like to do?")
        print("1. Speak to the creature")
        print("2. Run away")
        print("3. Enter combat")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            user_input = input(f"\nWhat do you want to say to the {monster_data['name']}? ")
            conversation_history.append(f"You: {user_input}")

            prompt = f"""In this fantasy role-playing game scenario, you are a {monster_data['name']}.
Your description: {monster_data['long_description']}
You have encountered {character_data['name']}, a level {character_data['level']} {character_data['class']}.
You feel: {random.choice(monster_data['dialogue'])}

Conversation history:
{"".join(conversation_history)}

{character_data['name']} says: "{user_input}"
How do you respond? Stay in character and remember this is a fictional game interaction."""

            if client:
                try:
                    message = client.messages.create(
                        model="claude-3-5-sonnet-20240620",
                        max_tokens=300,
                        temperature=0.7,
                        system=f"You are role-playing as a {monster_data['name']} in a fantasy game. You are interacting with {character_data['name']}, a {character_data['gender']} {character_data['class']}. Respond in character based on your description. This is a fictional game scenario.",
                        messages=[
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    )
                    response = message.content[0].text.replace("\\n\\n", "\n")
                except Exception as e:
                    print(f"Error generating monster response using API: {e}")
                    response = f"The {monster_data['name']} makes a sound, but you can't quite understand it."
            else:
                response = f"The {monster_data['name']} makes a sound, but you can't quite understand it."

            print(f"\nThe {monster_data['name']}'s response:")
            print(response)
            conversation_history.append(f"{monster_data['name']}: {response}")

            interaction_count += 1
            if interaction_count >= 2:
                encounter_ongoing = False
                end_encounter(character_data, monster_data, conversation_history)

        elif choice == '2':
            print("You decide to run away from the encounter.")
            encounter_ongoing = False

        elif choice == '3':
            print(f"You prepare yourself for combat with the {monster_data['name']}.")
            combat(character_data, monster_data)
            encounter_ongoing = False

        else:
            print("Invalid choice. Please try again.")

def end_encounter(character_data, monster_data, conversation_history):
    prompt = f"""Based on the following conversation between {character_data['name']} and a {monster_data['name']}:

{"".join(conversation_history)}

Please generate a short scene, like from a movie, where the creature and character interact one last time before parting ways. The scene should reflect the tone of their conversation and provide a satisfying conclusion to their encounter."""

    if client:
        try:
            message = client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=500,
                temperature=0.7,
                system="You are a creative writer tasked with creating a cinematic scene to conclude a fantasy encounter.",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            end_scene = message.content[0].text.replace("\\n\\n", "\n")
        except Exception as e:
            print(f"Error generating end scene using API: {e}")
            end_scene = "The creature and the character part ways, each having learned something from their brief encounter."
    else:
        end_scene = "The creature and the character part ways, each having learned something from their brief encounter."

    print("\n...")
    print(end_scene)

def generate_character():
    print("Welcome to the Fantasy Character Avatar Generator!")
    print("In this interactive game, you will make choices that shape your character's personality and background.")
    print("Based on your choices, we will generate a unique Fantasy character avatar for you.")
    print("Let's begin!\n")

    character_name = input("Enter your character's name: ")
    character_gender = input("Enter your character's gender: ")

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
    character_data['name'] = character_name
    character_data['gender'] = character_gender
    base_hit_points = 10
    constitution_modifier = (character_data['attributes']['Constitution'] - 10) // 2
    hit_points = base_hit_points + constitution_modifier

    character_data['hit_points'] = hit_points
    character_data['max_hit_points'] = hit_points
    character_data['level'] = 1
    
    character_class = character_data["class"]
    
    min_income, max_income = starting_income.get(character_class, (10, 300))
    character_money = random.randint(min_income, max_income)    
    
    character_element = character_data["element"]
    character_archetype = character_data["archetype"]
    character_main_weapon = character_data["main_weapon"]
    character_equipment = character_data["equipment"]

    print("\nYour Fantasy Character Avatar:")
    print("Name:", character_name)
    print("Gender:", character_gender)
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

    world_description = "In a realm where dark creatures lurk in the shadows, brave adventurers must face terrifying monsters born from ancient myths and legends. This land is home to vengeful spirits, shapeshifting demons, and nightmarish beings that prey on the unwary. From the misty forests to the treacherous swamps, danger lurks around every corner, challenging even the most valiant heroes."

    background_story = generate_background_story(character_data, world_description)

    print("\nBackground Story:")
    print(background_story)

    character_data["background_story"] = background_story

    input("\nHit enter to continue...")

    print("\nAs you set out on your journey, you come across a merchant on the road.")
    print("The merchant greets you and offers an assortment of items for sale:")

    with open("equipment.json", "r") as file:
        equipment_data = json.load(file)

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

    character_data["purchased_items"] = [item["name"] for item in purchased_items]
    character_data["remaining_money"] = character_money

    character_data["equipment"].extend(character_data["purchased_items"])

    # Create a 'characters' folder if it doesn't exist
    if not os.path.exists('characters'):
        os.makedirs('characters')

    # Create the character's JSON file
    character_filename = f"characters/{character_name.lower()}_{character_class.lower()}.json"
    with open(character_filename, "w") as file:
        json.dump(character_data, file, indent=4)

    print(f"\nCharacter data saved to '{character_filename}'.")

    # Select initial encounter and location
    selected_monster_data, initial_location = select_initial_encounter()

    # Start the encounter
    encounter(character_data, selected_monster_data, initial_location)

    return character_data, initial_location

def main():
    character_data, starting_location = generate_character()
    
    file_path = 'Locations.csv'
    movement_speed = 50  # Adjust this value based on the character's movement speed
    start_navigation(file_path, movement_speed)  # Removed the starting_location argument

if __name__ == "__main__":
    main()