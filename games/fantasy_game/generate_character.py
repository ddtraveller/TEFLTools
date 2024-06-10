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
weapons = {
    "Greatsword": {"damage": 10, "speed": 3, "strength": 15, "dexterity": 10},
    "Longsword": {"damage": 8, "speed": 5, "strength": 13, "dexterity": 12},
    "Battleaxe": {"damage": 9, "speed": 4, "strength": 14, "dexterity": 11},
    "Warhammer": {"damage": 9, "speed": 4, "strength": 14, "dexterity": 11},
    "Rapier": {"damage": 7, "speed": 7, "strength": 11, "dexterity": 14},
    "Shortsword": {"damage": 6, "speed": 6, "strength": 12, "dexterity": 13},
    "Dagger": {"damage": 4, "speed": 8, "strength": 10, "dexterity": 13},
    "Hand Crossbow": {"damage": 6, "speed": 6, "strength": 12, "dexterity": 13},
    "Staff": {"damage": 5, "speed": 5, "strength": 12, "dexterity": 12},
    "Wand": {"damage": 4, "speed": 6, "strength": 10, "dexterity": 13},
    "Sling": {"damage": 4, "speed": 6, "strength": 10, "dexterity": 13},
    "Mace": {"damage": 7, "speed": 5, "strength": 13, "dexterity": 12},
    "Flail": {"damage": 8, "speed": 4, "strength": 14, "dexterity": 11},
    "Crossbow": {"damage": 8, "speed": 4, "strength": 14, "dexterity": 11},
    "Longbow": {"damage": 8, "speed": 5, "strength": 13, "dexterity": 14},
    "Maul": {"damage": 10, "speed": 3, "strength": 15, "dexterity": 10},
    "Scimitar": {"damage": 7, "speed": 6, "strength": 12, "dexterity": 13},
    "Quarterstaff": {"damage": 6, "speed": 5, "strength": 12, "dexterity": 12},
    "Club": {"damage": 5, "speed": 5, "strength": 12, "dexterity": 12},
    "Unarmed Strike": {"damage": 3, "speed": 5, "strength": 3, "dexterity": 3},
    "Nunchaku": {"damage": 5, "speed": 9, "strength": 11, "dexterity": 15},
    "Greataxe": {"damage": 10, "speed": 3, "strength": 15, "dexterity": 10}
}
equipment = {
    "Fighter": "Heavy Armor, Shield",
    "Rogue": "Leather Armor, Thieves' Tools",
    "Wizard": "Spellbook, Component Pouch",
    "Cleric": "Holy Symbol, Chain Mail",
    "Ranger": "Studded Leather Armor, Quiver",
    "Paladin": "Plate Armor, Holy Symbol",
    "Martial Artist": "Leather Armor, Herbalism Kit",
    "Shaman": "Lute, Entertainer's Pack",
    "Monk": "Robes, Holy Symbol",
    "Barbarian": "Hide Armor, Handaxe"
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

    stories = [
        {
            "story": "You come across a group of bandits attacking a helpless merchant and his family on a lonely road. The merchant begs for your help. What do you do?",
            "options": [
                "Rush in to confront the bandits and save the merchant",
                "Sneak around to create a distraction and help the merchant escape",
                "Ignore the situation and continue on your way"
            ],
            "scores": [1, 0, -1]
        },
        {
            "story": "While exploring an ancient ruins, you find a mysterious artifact emanating an eerie glow. You sense it holds great power, but also potential danger. What do you do?",
            "options": [
                "Turn the artifact over to the local authorities for safekeeping",
                "Keep the artifact to study its power and potential uses",
                "Destroy the artifact to prevent it from falling into the wrong hands"
            ],
            "scores": [1, -1, 0]
        },
        {
            "story": "A powerful wizard offers to teach you forbidden magic, claiming it will make you invincible. However, you suspect the magic may come at a great cost. What do you do?",
            "options": [
                "Refuse the offer, believing the cost is too high",
                "Accept the offer, but vow to use the magic only for good",
                "Accept the offer eagerly, craving the power it promises"
            ],
            "scores": [1, 0, -1]
        },
        {
            "story": "While walking through a crowded marketplace, you witness a skilled pickpocket stealing from an elderly woman. The thief notices you and starts to run. What do you do?",
            "options": [
                "Call for the city guard to report the crime",
                "Chase after the thief to confront them and return the stolen goods",
                "Pretend you didn't see anything and blend into the crowd"
            ],
            "scores": [1, 0, -1]
        },
        {
            "story": "A noble approaches you with a lucrative offer to help in a political scheme against a rival house. The plan involves spreading rumors and sabotaging the rival's reputation. What do you do?",
            "options": [
                "Refuse to get involved in the political intrigue",
                "Agree to help, but try to minimize the damage to the rival house", 
                "Agree to help and follow the noble's orders without question"
            ],
            "scores": [1, 0, -1]
        },
        {
            "story": "During your travels, you uncover a secret that could expose a corrupt government official. The official has been exploiting the poor for personal gain. What do you do?",
            "options": [
                "Gather evidence and expose the truth to the public",
                "Use the information to blackmail the official for your own benefit",
                "Keep the secret to yourself, fearing the consequences of getting involved"
            ],
            "scores": [1, -1, 0]
        }
    ]

    element_score = 0

    for story in stories:
        print(story["story"])
        choice = get_user_choice(story["options"])
        element_score += story["scores"][choice]

    character_class = random.choice(classes)
    element_index = abs(element_score) % 4
    character_element = elements[element_index]
    archetype_index = abs(element_score) % 12
    character_archetype = archetypes[archetype_index]
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