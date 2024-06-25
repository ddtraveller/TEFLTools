import random
import json
import time
from Character import create_character
from Combat import combat
from Navigation import start_navigation
import anthropic

client = anthropic.Anthropic()

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

    with open("monsters.json", "r") as file:
        monsters_data = json.load(file)
    
    world_description = "In a realm where dark creatures lurk in the shadows, brave adventurers must face terrifying monsters born from ancient myths and legends. This land is home to vengeful spirits, shapeshifting demons, and nightmarish beings that prey on the unwary. From the misty forests to the treacherous swamps, danger lurks around every corner, challenging even the most valiant heroes."

    prompt = f"""As a Dungeon Master, create a compelling background origin story for a character with the following attributes:

Character Name: {character_name}
Character Gender: {character_gender}
Character Class: {character_class}
Element: {character_element}
Archetype: {character_archetype}
Main Weapon: {character_main_weapon}
Equipment: {', '.join(character_equipment)}
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

    background_story = message.content[0].text.strip()

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

    with open("character_data.json", "w") as file:
        json.dump(character_data, file, indent=4)

    print("\nUpdated character data saved to 'character_data.json'.")

    # Load monster data and select a monster of level 3 or lower for the first encounter
    with open("monsters.json", "r") as file:
        monsters_data = json.load(file)
        eligible_monsters = [monster for monster in monsters_data if monster['level'] <= 3]
        if not eligible_monsters:
            print("No suitable monsters found for the first encounter. Please check the monsters.json file.")
            return character_data
        selected_monster_data = random.choice(eligible_monsters)

    print(f"\nAs you travel further, you encounter a {selected_monster_data['name']}!")
    print(f"\nThe {selected_monster_data['name']} Description:")
    print(selected_monster_data['long_description'])

    user_input = input(f"\nWhat do you want to say to the {selected_monster_data['name']}? ")

    level_difference = selected_monster_data['level'] - character_data['level']
    if level_difference > 2:
        relative_power = "much less powerful"
    elif level_difference > 0:
        relative_power = "less powerful"
    elif level_difference < -2:
        relative_power = "much more powerful"
    elif level_difference < 0:
        relative_power = "more powerful"
    else:
        relative_power = "about the same in power"

    prompt = f"""In this fantasy role-playing game scenario, you are a {selected_monster_data['name']}.
Your description: {selected_monster_data['long_description']}
You have encountered {character_data['name']}, a level {character_data['level']} {character_data['class']}.
You feel: {random.choice(selected_monster_data['dialogue'])}
{character_data['name']} says: "{user_input}"
How do you respond? Stay in character and remember this is a fictional game interaction."""

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=300,
        temperature=0.7,
        system=f"You are role-playing as a {selected_monster_data['name']} in a fantasy game. You are interacting with {character_data['name']}, a {character_data['gender']} {character_data['class']}. They are {relative_power} compared to you. Respond in character based on your description. This is a fictional game scenario.",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print(f"\nThe {selected_monster_data['name']}'s response:")
    response = message.content[0].text.replace("\\n\\n", "\n")
    print(response)

    print(f"\nThe {selected_monster_data['name']} suddenly quits talking and charges you!")

    combat(character_data, selected_monster_data)

    print(f"\nAfter the {selected_monster_data['name']} encounter, you continue your journey.")

    return character_data

def main():
    character_data = generate_character()
    
    file_path = 'Locations.csv'
    movement_speed = 50
    start_navigation(file_path, movement_speed)

if __name__ == "__main__":
    main()