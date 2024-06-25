import random
import sys

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
        # Gain experience points and loot
    else:
        print("Combat ended.")

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