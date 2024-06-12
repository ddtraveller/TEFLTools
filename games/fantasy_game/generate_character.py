import random
import json

class Spells:
    def __init__(self):
        self.movement_spells = [
            "Swift Wind's Blessing", "Bounding Stride", "Soaring Flight", "Nimble Retreat",
            "Dimensional Passage", "Galloping Speed", "Ascending Motion", "Brisk Pace"
        ]
        self.sorcery_spells = [
            "Mighty Bolt", "Furious Blast", "Wrathful Curse", "Scorching Ray",
            "Devouring Plague", "Heavenly Fireball", "Forceful Arrows", "Hexing Chant"
        ]
        self.elemental_spells = [
            "Burning Touch", "Tempestuous Gust", "Thunderous Clap", "Stony Grasp",
            "Elemental Attunement", "Freezing Breath", "Tremoring Earth", "Entangling Vines"
        ]
        self.healing_spells = [
            "Purifying Light", "Blessed Regeneration", "Divine Guidance", "Lifeforce Infusion",
            "Cleansing Ritual", "Circle of Protection", "Calming Influence", "Sacred Darshan",
            "Heightened Senses", "Protect the Fallen"
        ]
        self.nature_spells = [
            "Bountiful Growth", "Primal Summoning", "Verdant Barrier", "Graceful Camouflage",
            "Herbal Remedy", "Thorny Entanglement", "Swarming Insects", "Awakening Touch"
        ]
        self.internal_spells = [
            "Unbreakable Armor", "Radiant Aura", "Insightful Vision", "Unyielding Fortitude",
            "Inner Cultivation", "Resolute Stance", "Prescient Foresight", "Invulnerable Mind"
        ]
        self.mystic_spells = [
            "Third Eye Revelation", "Oracular Divination", "Nature's Wisdom", "Scholarly Insight",
            "Predictive Calculation", "Spiritual Sight", "Ancestral Knowledge", "Intuitive Perception"
        ]

spell_types = {
    "Movement": ["Rogue", "Wizard"],
    "Sorcery": ["Wizard"],
    "Elemental": ["Wizard"],
    "Healing": ["Cleric", "Paladin", "Shaman", "Monk"],
    "Nature": ["Ranger", "Shaman", "Barbarian"],
    "Internal": ["Monk", "Martial Artist"],
    "Mystic": ["Shaman", "Monk"]
}

classes = ["Fighter", "Rogue", "Wizard", "Cleric", "Ranger", "Paladin", "Martial Artist", "Shaman", "Monk", "Barbarian"]
elements = ["Fire", "Air", "Earth", "Water"]
archetypes = ["Lion", "Eagle", "Bear", "Wolf", "Owl", "Snake", "Dolphin", "Elephant", "Butterfly", "Turtle", "Deer", "Fox"]

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
            spell_category = random.choice(list(spell_types.keys())).lower() + "_spells"
            character_spells.append(random.choice(getattr(spells, spell_category)))
    elif character_class in ["Cleric", "Shaman", "Monk"]:
        for _ in range(2):
            spell_category = random.choice(list(spell_types.keys())).lower() + "_spells"
            character_spells.append(random.choice(getattr(spells, spell_category)))
    elif character_class in ["Rogue", "Ranger", "Paladin", "Martial Artist"]:
        spell_category = random.choice(list(spell_types.keys())).lower() + "_spells"
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
        "equipment": character_equipment,
        "spells": character_spells,
        "attributes": attributes,
        "background_story": background_story if background_story else default_story
    }

    # Save the character data to a JSON file
    with open("character_data.json", "w") as file:
        json.dump(character_data, file, indent=4)

    print("\nCharacter data saved to 'character_data.json'.")

# Run the character generator
generate_character()