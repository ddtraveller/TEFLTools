import random
import sys
import json
import os
from anthropic import Anthropic
from game_utils import get_location_description

# Define the path to the JSON folder
JSON_FOLDER = 'json'

# Assume ANTHROPIC_API_KEY is set in your environment variables
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
if ANTHROPIC_API_KEY:
    client = Anthropic(api_key=ANTHROPIC_API_KEY)
else:
    print("Warning: ANTHROPIC_API_KEY not set. Using fallback method for responses.")
    client = None

def get_llm_response(messages):
    if client:
        try:
            response = client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=300,
                messages=messages
            )
            return response.content[0].text
        except Exception as e:
            print(f"Error using Anthropic API: {e}")
            print("Falling back to simple response method.")
    
    # Fallback method
    return "The creature responds in a mysterious way, leaving you to interpret its intentions."

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
                    combat_result = combat(character_data, monster_data)
                    if combat_result == "victory":
                        print("You were victorious in combat!")
                        return True
                    elif combat_result == "escaped":
                        print("You managed to escape from combat.")
                        return False
                    elif combat_result == "monster_escaped":
                        print(f"The {monster_data['name']} fled from combat.")
                        return False
                    else:
                        print("The combat ended in a draw.")
                        return False
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
            combat_result = combat(character_data, monster_data)
            if combat_result == "victory":
                print("You were victorious in combat!")
                return True
            elif combat_result == "escaped":
                print("You managed to escape from combat.")
                return False
            elif combat_result == "monster_escaped":
                print(f"The {monster_data['name']} fled from combat.")
                return False
            else:
                print("The combat ended in a draw.")
                return False

        else:
            print("Invalid choice. Please try again.")

    return False

def combat(character_data, monster_data):
    print("Combat begins!")

    # Set initial positions
    character_position = 0
    enemy_position = random.randint(5, 10)  # Enemy starts 5-10 units away

    # Get movement speeds, with default values if not present
    character_movement_speed = character_data.get('movement_speed', 30)  # Default to 30 if not present
    monster_speed = monster_data.get('movement_speed', 25)  # Default to 25 if not present

    character_dexterity = character_data['attributes']['Dexterity']
    character_initiative = character_dexterity + character_movement_speed
    monster_initiative = monster_speed + monster_data['armor_class']

    character_defense = 0
    monster_defense = 0

    while character_data['hit_points'] > 0 and monster_data['health'] > 0:
        if character_initiative >= monster_initiative:
            result = player_turn(character_data, monster_data, character_defense)
            if result == "escaped":
                print("You successfully escaped!")
                return "escaped"
            character_defense = result if isinstance(result, int) else 0
            if monster_data['health'] <= 0:
                break
            result = monster_turn(character_data, monster_data, monster_defense)
            if result == "escaped":
                print(f"The {monster_data['name']} successfully escaped!")
                return "monster_escaped"
            monster_defense = result if isinstance(result, int) else 0
            if character_data['hit_points'] <= 0:
                end_game("You have been defeated!")
        else:
            result = monster_turn(character_data, monster_data, monster_defense)
            if result == "escaped":
                print(f"The {monster_data['name']} successfully escaped!")
                return "monster_escaped"
            monster_defense = result if isinstance(result, int) else 0
            if character_data['hit_points'] <= 0:
                end_game("You have been defeated!")
            result = player_turn(character_data, monster_data, character_defense)
            if result == "escaped":
                print("You successfully escaped!")
                return "escaped"
            character_defense = result if isinstance(result, int) else 0

    if monster_data['health'] <= 0:
        print(f"You have defeated the {monster_data['name']}!")
        return "victory"
    elif character_data['hit_points'] <= 0:
        end_game("You have been defeated!")
    else:
        print("Combat ended in a draw.")
        return "draw"

def player_turn(character_data, monster_data, defense):
    print("\nIt's your turn!")
    action = get_user_choice(["Attack", "Defend", "Spell", "Run"])
    if action == 0:
        # Character attacks
        damage = character_data['attributes'].get('damage', 5)  # Default damage to 5 if not present
        if random.randint(1, 100) > monster_data['armor_class'] :
            actual_damage = max(1, damage)
            monster_data['health'] -= actual_damage
            print(f"You attack the {monster_data['name']} and deal {actual_damage} damage!")
        else:
            print("Your attack missed!")
        return 0
    elif action == 1:
        # Character defends
        print("You take a defensive stance.")
        return 5  # Increase defense by 5
    elif action == 2:
        # Character casts a spell
        if 'spells' in character_data and character_data['spells']:
            print("Available Spells:")
            for i, spell in enumerate(character_data['spells'], 1):
                print(f"{i}. {spell['name']}")
            spell_choice = int(input("Enter the number of the spell you want to cast: ")) - 1
            spell = character_data['spells'][spell_choice]
            print(f"You cast {spell['name']}!")
            # Apply spell effects
        else:
            print("You don't have any spells to cast.")
        return 0
    elif action == 3:
        # Character tries to run
        print("You attempt to run away!")
        if random.randint(1, 100) <= 50:  # 50% chance to escape
            return "escaped"
        else:
            print("Your escape attempt failed!")
            return 0

def monster_turn(character_data, monster_data, defense):
    print(f"\nThe {monster_data['name']}'s turn!")
    monster_action = random.choice(["Attack", "Defend", "Run"])
    if monster_action == "Attack":
        # Monster attacks
        ability = random.choice(monster_data['abilities'])
        accuracy = ability['accuracy']
        if random.randint(1, 100) <= accuracy - character_data['attributes'].get('armor_class', 0) - defense:
            damage = ability['damage']
            actual_damage = max(1, damage - defense)
            character_data['hit_points'] -= actual_damage
            print(f"The {monster_data['name']} uses {ability['name']} and deals {actual_damage} damage!")
            print(f"You now have {character_data['hit_points']} hit points left.")
            if character_data['hit_points'] <= 0:
                end_game("You have been defeated!")
        else:
            print(f"The {monster_data['name']} misses!")
        return 0
    elif monster_action == "Defend":
        # Monster defends
        print(f"The {monster_data['name']} takes a defensive stance.")
        return 5  # Increase defense by 5
    elif monster_action == "Run":
        # Monster tries to run
        print(f"The {monster_data['name']} tries to run away!")
        if random.randint(1, 100) <= 30:  # 30% chance to escape
            return "escaped"
        else:
            print(f"The {monster_data['name']}'s escape attempt failed!")
            return 0

def get_user_choice(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        choice = input("Enter your choice (1-" + str(len(options)) + "): ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice) - 1
        else:
            print("Invalid choice. Please try again.")

def end_game(message):
    print(message)
    print("Game Over")
    sys.exit()