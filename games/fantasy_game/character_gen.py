import random
import json
import os
from typing import List, Dict, Any
import anthropic
from Character import create_character

# Define the path to the JSON folder
JSON_FOLDER = 'json'

ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
if ANTHROPIC_API_KEY:
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
else:
    print("Warning: ANTHROPIC_API_KEY not set. Will use fallback method for background story generation.")
    client = None

STARTING_INCOME = {
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

def get_user_choice(options: List[str]) -> int:
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        choice = input(f"Enter your choice (1-{len(options)}): ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice) - 1
        print("Invalid choice. Please try again.")

def generate_background_story(character_data: Dict[str, Any], world_description: str) -> str:
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

def load_json_file(filename: str) -> Any:
    with open(os.path.join(JSON_FOLDER, filename), "r") as file:
        return json.load(file)

def save_character_data(character_data: Dict[str, Any]) -> None:
    if not os.path.exists('characters'):
        os.makedirs('characters')
    character_filename = f"characters/{character_data['name'].lower()}_{character_data['class'].lower()}.json"
    with open(character_filename, "w") as file:
        json.dump(character_data, file, indent=4)
    print(f"\nCharacter data saved to '{character_filename}'.")

def generate_character(character_name: str) -> Dict[str, Any]:
    print("Welcome to the Fantasy Character Avatar Generator!")
    print("In this interactive game, you will make choices that shape your character's personality and background.")
    print("Based on your choices, we will generate a unique Fantasy character avatar for you.")
    print("Let's begin!\n")

    character_gender = input("Enter your character's gender: ")

    stories = load_json_file('stories.json')
    random.shuffle(stories)
    selected_stories = stories[:6]

    element_score = sum(story["scores"][get_user_choice(story["options"])] for story in selected_stories)

    character_data = create_character(element_score)
    character_data['name'] = character_name
    character_data['gender'] = character_gender
    
    base_hit_points = 10
    constitution_modifier = (character_data['attributes']['Constitution'] - 10) // 2
    character_data['hit_points'] = base_hit_points + constitution_modifier
    character_data['max_hit_points'] = character_data['hit_points']
    character_data['level'] = 1
    
    character_class = character_data["class"]
    min_income, max_income = STARTING_INCOME.get(character_class, (10, 300))
    character_money = random.randint(min_income, max_income)

    print("\nYour Fantasy Character Avatar:")
    for key, value in character_data.items():
        if key != 'attributes':
            print(f"{key.capitalize()}: {value}")

    print("\nAttributes:")
    for attribute, score in character_data['attributes'].items():
        print(f"{attribute}: {score}")

    world_description = "In a realm where dark creatures lurk in the shadows, brave adventurers must face terrifying monsters born from ancient myths and legends. This land is home to vengeful spirits, shapeshifting demons, and nightmarish beings that prey on the unwary. From the misty forests to the treacherous swamps, danger lurks around every corner, challenging even the most valiant heroes."

    character_data["background_story"] = generate_background_story(character_data, world_description)

    print("\nBackground Story:")
    print(character_data["background_story"])

    input("\nHit enter to continue...")

    print("\nAs you set out on your journey, you come across a merchant on the road.")
    print("The merchant greets you and offers an assortment of items for sale:")

    equipment_data = load_json_file('equipment.json')
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
            item = merchant_items[int(choice) - 1]
            cost_parts = item['cost'].split()
            cost = int(cost_parts[0])
            currency = cost_parts[1]

            cost_in_cp = {'cp': cost, 'sp': cost * 10, 'gp': cost * 100}.get(currency)
            if cost_in_cp is None:
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

    save_character_data(character_data)

    return character_data

if __name__ == "__main__":
    character_name = input("Enter your character's name: ")
    generate_character(character_name)