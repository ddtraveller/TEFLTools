import random
import json
import csv
import os
import sys
from character_gen import generate_character
from Combat import combat
from Navigation import start_navigation
from anthropic import Anthropic

# Assume ANTHROPIC_API_KEY is set in your environment variables
client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

encounter_weights = {
    'combat': 0.4,
    'movement': 0.2,
    'dialogue': 0.4
}

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
    
    # Ensure the monster has an 'armor_class' key
    if 'armor_class' not in selected_monster:
        selected_monster['armor_class'] = random.randint(10, 15)  # Default range, adjust as needed
    
    location = random.choice(selected_monster['locations'])
    
    return selected_monster, location

def weighted_choice(weights):
    choices = list(weights.keys())
    probabilities = list(weights.values())
    return random.choices(choices, weights=probabilities, k=1)[0]

def get_llm_response(messages):
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=300,
        messages=messages
    )
    return response.content[0].text

def get_llm_decision(character_data, monster_data, conversation_history):
    prompt = f"""As a Dungeon Master, you are overseeing an encounter between {character_data['name']}, 
a level {character_data['level']} {character_data['class']}, and a {monster_data['name']}.

The conversation so far:
{''.join(conversation_history)}

Based on this interaction, decide whether to:
1. Enter combat mode if the player has been hostile, aggressive, or antagonistic.
2. Generate a [scary, funny, deep, interesting, spiritual, or competitive] end scenario and move to exploration mode only if the player has been neutral or friendly.

Your decision should be heavily influenced by the player's language and attitude. If the player has used any aggressive, threatening, or insulting language, combat should be the most likely outcome.

Respond with your decision and a brief explanation in the following format:
Decision: [Combat/End Scenario]
Scenario Type (if applicable): [scary/funny/deep/interesting/spiritual/competitive]
Explanation: [Your reasoning, with specific reference to player's words or attitude]
Next Action: [A sentence describing what happens next]"""

    messages = [
        {"role": "user", "content": prompt}
    ]

    response = get_llm_response(messages)
    
    # Additional logic to force combat for extremely hostile language
    force_combat_triggers = ["die", "kill", "attack", "fight", "destroy"]
    
    if conversation_history:
        last_player_message = conversation_history[-2].lower()  # The player's last message
        if any(trigger in last_player_message for trigger in force_combat_triggers):
            return """Decision: Combat
Explanation: The player used explicitly hostile language, immediately triggering combat.
Next Action: The creature, provoked by the aggressive words, launches into an attack!"""
    
    return response

def encounter(character_data, monster_data, location, file_path, movement_speed):
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
            conversation_history.append(f"You: {user_input}\n")

            prompt = f"In this fantasy role-playing game scenario, you are a {monster_data['name']}.\n" \
                     f"Your description: {monster_data['long_description']}\n" \
                     f"You have encountered {character_data['name']}, a level {character_data['level']} {character_data['class']}.\n" \
                     f"You feel: {random.choice(monster_data['dialogue'])}\n\n" \
                     f"Conversation history:\n{''.join(conversation_history)}\n" \
                     f"{character_data['name']} says: \"{user_input}\"\n" \
                     f"How do you respond? Stay in character and remember this is a fictional game interaction."

            messages = [
                {"role": "user", "content": prompt}
            ]

            response = get_llm_response(messages)

            print(f"\nThe {monster_data['name']}'s response:")
            print(response)
            conversation_history.append(f"{monster_data['name']}: {response}\n")

            interaction_count += 1
            if interaction_count >= 2 or any(trigger in user_input.lower() for trigger in ["die", "kill", "attack", "fight", "destroy"]):
                encounter_ongoing = False
                llm_decision = get_llm_decision(character_data, monster_data, conversation_history)
                decision_lines = llm_decision.split('\n')
                decision = next((line.split(': ')[1] for line in decision_lines if line.startswith('Decision:')), None)
                next_action = next((line.split(': ')[1] for line in decision_lines if line.startswith('Next Action:')), None)

                print("\n...some time later.\n")
                if next_action:
                    print(next_action)

                if decision == 'Combat':
                    print(f"The encounter with the {monster_data['name']} turns hostile!")
                    return combat(character_data, monster_data)
                elif decision == 'End Scenario':
                    print("The encounter comes to a peaceful end.")
                    return True
                else:
                    print("The encounter comes to an unexpected end.")
                    return False

        elif choice == '2':
            print("You decide to run away from the encounter.")
            encounter_ongoing = False
            return False

        elif choice == '3':
            print(f"You prepare yourself for combat with the {monster_data['name']}.")
            return combat(character_data, monster_data)

        else:
            print("Invalid choice. Please try again.")

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
        character_data = generate_character()
    
    file_path = 'Locations.csv'
    movement_speed = 20  # Adjust this value based on the character's movement speed
    
    # Start with the movement phase
    print("You find yourself ready to explore the vast lands of Timor Leste Fantasia.")
    start_navigation(file_path, movement_speed, character_data)

if __name__ == "__main__":
    main()