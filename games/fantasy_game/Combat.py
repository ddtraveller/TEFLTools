import random

def combat(character_data, monster_data):
    print("Combat begins!")

    # Set initial positions
    character_position = 0
    enemy_position = random.randint(5, 10)  # Enemy starts 5-10 units away

    # Get movement speeds, with default values if not present
    character_movement_speed = character_data.get('movement_speed', 30)  # Default to 30 if not present
    monster_speed = monster_data.get('speed', 25)  # Default to 25 if not present
    
    print(f"\nYou encounter a {monster_data['name']}!")
    print(random.choice(monster_data['dialogue']))

    options = [
        "Greetings, noble creature. I mean you no harm and wish to pass peacefully.",
        f"Out of my way, you filthy {monster_data['name'].lower()}!",
        "Enough talk! Prepare to meet your doom!"
    ]

    choice = get_user_choice(options)

    character_dexterity = character_data['attributes']['Dexterity']
    character_initiative = character_dexterity + character_movement_speed
    monster_initiative = monster_speed + monster_data['defense']

    while character_data['hit_points'] > 0 and monster_data['health'] > 0:
        if character_initiative >= monster_initiative:
            player_turn(character_data, monster_data)
            if monster_data['health'] <= 0:
                break
            monster_turn(character_data, monster_data)
        else:
            monster_turn(character_data, monster_data)
            if character_data['hit_points'] <= 0:
                break
            player_turn(character_data, monster_data)

    if character_data['hit_points'] <= 0:
        print("You have been defeated!")
    elif monster_data['health'] <= 0:
        print(f"You have defeated the {monster_data['name']}!")
        # Gain experience points and loot
    else:
        print("You managed to escape!")

def player_turn(character_data, monster_data):
    print("\nIt's your turn!")
    action = get_user_choice(["Attack", "Defend", "Spell", "Run"])
    if action == 0:
        # Character attacks
        damage = character_data['attributes'].get('damage', 5)  # Default damage to 5 if not present
        monster_data['health'] -= damage
        print(f"You attack the {monster_data['name']} and deal {damage} damage!")
    elif action == 1:
        # Character defends
        print("You take a defensive stance.")
    elif action == 2:
        # Character casts a spell
        if character_data['spells']:
            print("Available Spells:")
            for i, spell in enumerate(character_data['spells'], 1):
                print(f"{i}. {spell['name']}")
            spell_choice = int(input("Enter the number of the spell you want to cast: ")) - 1
            spell = character_data['spells'][spell_choice]
            print(f"You cast {spell['name']}!")
            # Apply spell effects
        else:
            print("You don't have any spells to cast.")
    elif action == 3:
        # Character tries to run
        print("You attempt to run away!")
        return "run"

def monster_turn(character_data, monster_data):
    print(f"\nThe {monster_data['name']}'s turn!")
    monster_action = random.choice(["Attack", "Defend"] + (["Spell"] if "spells" in monster_data else []) + ["Run"])
    if monster_action == "Attack":
        # Monster attacks
        ability = random.choice(monster_data['abilities'])
        accuracy = ability['accuracy']
        if random.randint(1, 100) <= accuracy:
            damage = ability['damage']
            character_data['hit_points'] -= damage
            print(f"The {monster_data['name']} uses {ability['name']} and deals {damage} damage!")
            print(f"You now have {character_data['hit_points']} hit points left.")
        else:
            print(f"The {monster_data['name']} misses!")
    elif monster_action == "Defend":
        # Monster defends
        print(f"The {monster_data['name']} takes a defensive stance.")
    elif monster_action == "Spell" and "spells" in monster_data:
        # Monster casts a spell
        spell = random.choice(monster_data['spells'])
        print(f"The {monster_data['name']} casts {spell['name']}!")
        # Apply spell effects
    elif monster_action == "Run":
        # Monster tries to run
        print(f"The {monster_data['name']} tries to run away!")
        return "run"

def get_user_choice(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        choice = input("Enter your choice (1-" + str(len(options)) + "): ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice) - 1
        else:
            print("Invalid choice. Please try again.")