import random

# Define character classes, attributes, archetypes, weapons, equipment, and spells directly in the script
character_classes = {
    "Fighter": {"Strength": 2, "Constitution": 1},
    "Rogue": {"Dexterity": 2, "Charisma": 1},
    "Wizard": {"Intelligence": 2, "Wisdom": 1},
    "Cleric": {"Wisdom": 2, "Charisma": 1},
    "Ranger": {"Dexterity": 2, "Wisdom": 1},
    "Paladin": {"Strength": 1, "Charisma": 2},
    "Barbarian": {"Strength": 2, "Constitution": 1},
    "Monk": {"Dexterity": 2, "Wisdom": 1},
    "Druid": {"Wisdom": 2, "Intelligence": 1},
    "Warlock": {"Charisma": 2, "Constitution": 1}
}

character_attributes = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

character_archetypes = {
    "Fighter": ["Guardian", "Champion", "Battle Master"],
    "Rogue": ["Thief", "Assassin", "Arcane Trickster"],
    "Wizard": ["Evoker", "Diviner", "Necromancer"],
    "Cleric": ["Life Domain", "War Domain", "Trickery Domain"],
    "Ranger": ["Hunter", "Beast Master", "Gloom Stalker"],
    "Paladin": ["Oath of Devotion", "Oath of Vengeance", "Oath of the Ancients"],
    "Barbarian": ["Berserker", "Totem Warrior", "Storm Herald"],
    "Monk": ["Way of the Open Hand", "Way of Shadow", "Way of the Four Elements"],
    "Druid": ["Circle of the Land", "Circle of the Moon", "Circle of Dreams"],
    "Warlock": ["Fiend Pact", "Archfey Pact", "Great Old One Pact"]
}

weapons = {
    "Fighter": ["Longsword", "Battleaxe", "Warhammer"],
    "Rogue": ["Shortsword", "Dagger", "Rapier"],
    "Wizard": ["Quarterstaff", "Dagger", "Wand"],
    "Cleric": ["Mace", "Warhammer", "Morningstar"],
    "Ranger": ["Longbow", "Shortsword", "Twin Daggers"],
    "Paladin": ["Longsword", "Warhammer", "Greatsword"],
    "Barbarian": ["Greataxe", "Greatsword", "Maul"],
    "Monk": ["Quarterstaff", "Shortsword", "Nunchaku"],
    "Druid": ["Scimitar", "Quarterstaff", "Sickle"],
    "Warlock": ["Quarterstaff", "Dagger", "Rod"]
}

equipment = ["Backpack", "Bedroll", "Rations (1 week)", "Waterskin", "Rope (50 feet)", "Tinderbox", "Torches (10)", "Healing Potion"]

spells = [
    {"name": "Fireball", "description": "A bright streak flashes from your pointing finger to a point you choose within range and then blossoms with a low roar into an explosion of flame."},
    {"name": "Healing Word", "description": "A creature of your choice that you can see within range regains hit points equal to 1d4 + your spellcasting ability modifier."},
    {"name": "Magic Missile", "description": "You create three glowing darts of magical force. Each dart hits a creature of your choice that you can see within range."},
    {"name": "Shield", "description": "An invisible barrier of magical force appears and protects you."},
    {"name": "Detect Magic", "description": "For the duration, you sense the presence of magic within 30 feet of you."}
]

# Define the elements and their corresponding score ranges
elements = {
    "Fire": (20, 40),
    "Water": (0, 20),
    "Earth": (40, 60),
    "Air": (60, 80),
    "Spirit": (80, 100)
}

# Define spellcasting classes
spellcasting_classes = ["Wizard", "Cleric", "Warlock", "Druid"]

def create_character(element_score):
    # Determine the character's element based on the element score
    character_element = next(element for element, (min_score, max_score) in elements.items() if min_score <= element_score < max_score)

    # Select a random character class
    character_class = random.choice(list(character_classes.keys()))

    # Select a random archetype for the chosen class
    character_archetype = random.choice(character_archetypes[character_class])

    # Generate random attribute scores
    attributes = {}
    for attribute in character_attributes:
        base_score = random.randint(8, 18)
        class_bonus = character_classes[character_class].get(attribute, 0)
        attributes[attribute] = base_score + class_bonus

    # Select main weapon based on the character's class
    main_weapon = random.choice(weapons[character_class])

    # Select random equipment
    character_equipment = [main_weapon] + random.sample(equipment, 3)

    # Generate spells if the character is a spellcaster
    if character_class in spellcasting_classes:
        num_spells = random.randint(3, 5)
        character_spells = random.sample(spells, num_spells)
        # Remove duplicates while preserving order
        character_spells = list({spell['name']: spell for spell in character_spells}.values())
    else:
        character_spells = []

    # Generate a background story
    background_story = generate_background_story(character_class, character_element, character_archetype)

    # Create the character dictionary
    character = {
        "class": character_class,
        "element": character_element,
        "archetype": character_archetype,
        "attributes": attributes,
        "main_weapon": main_weapon,
        "equipment": character_equipment,
        "spells": character_spells,
        "background_story": background_story
    }

    # Add movement speed
    character["movement_speed"] = random.randint(25, 35)  # Adjust range as needed

    return character

def generate_background_story(character_class, character_element, character_archetype):
    # This is a placeholder function. In a real game, you'd want to create more complex and varied background stories.
    return f"A {character_element} attuned {character_archetype} {character_class} with a mysterious past..."

# Example usage
if __name__ == "__main__":
    element_score = random.randint(0, 100)
    character = create_character(element_score)
    print(json.dumps(character, indent=2))