import os
import json
import random
import pygame
import requests
import io

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ultima-like Game")

# List of available icons in S3
icon_files = [
    "shaman.png", "goblin.png", "001-book.png", "001-knight.png", "001-wizard.png", "002-crown.png", "002-dragon.png",
    "002-wizard.png", "003-dwarf.png", "003-elf.png", "003-sword.png", "004-elf.png",
    "004-frog.png", "004-ufo.png", "005-potion.png", "005-robot.png", "005-witch.png",
    "006-mermaid.png", "006-ogre.png", "006-wizard.png", "007-giant.png", "007-magic wand.png",
    "007-superhero.png", "008-gnome.png", "008-magic mirror.png", "008-ninja.png", "009-chest.png",
    "009-knight.png", "009-little red riding hood.png", "010-unicorn.png", "010-wolf.png",
    "011-crystal ball.png", "011-gnome.png", "011-queen.png", "012-cauldron.png", "012-cowboy.png",
    "012-king.png", "013-dragon.png", "013-genie.png", "013-princess.png", "014-fairy.png",
    "014-prince.png", "014-shoe.png", "015-bigfoot.png", "015-frog prince.png", "016-fairy.png",
    "016-king.png", "017-goblin.png", "017-robin hood.png", "018-oni.png", "018-pirate.png",
    "019-faun.png", "019-goblin.png", "020-elf.png", "020-princess.png", "021-medusa.png",
    "021-pig.png", "022-pirate.png", "022-tin man.png", "023-scarecrow.png", "023-vampire.png",
    "024-cowardly lion.png", "024-krampus.png", "025-geisha.png", "025-pinocchio.png",
    "026-godzilla.png", "026-puss in boots.png", "027-mad hatter.png", "027-werewolf.png",
    "028-cyclops.png", "028-red-riding-hood.png", "029-haunted.png", "029-white rabbit.png",
    "030-cyclops.png", "030-mermaid.png", "031-frog.png", "031-genie.png", "032-ogre.png",
    "032-vampire.png", "033-minotaur.png", "033-unicorn.png", "034-dragon.png", "034-jackalope.png",
    "035-loch-ness-monster.png", "035-phoenix.png", "036-poison.png", "036-spartan.png",
    "037-witch.png", "038-pegasus.png", "039-princess-1.png", "040-grim-reaper.png",
    "041-kraken.png", "042-frankenstein.png", "043-cerberus.png", "044-griffin.png",
    "045-zombie.png", "046-samurai.png", "047-sphynx.png", "048-centaur.png", "049-leprechaun.png",
    "050-angel.png"
]


# Function to load a random PNG from a public S3 bucket
def load_png_from_s3(name):
    base_url = "https://tl-web.s3.us-west-2.amazonaws.com/icons/"
    filtered_icons = [icon for icon in icon_files if icon.startswith(name)]
    if filtered_icons:
        random_icon = random.choice(filtered_icons)
        png_url = base_url + random_icon
        print(f"Loading icon from URL: {png_url}")
        response = requests.get(png_url)
        print(f"Response status code: {response.status_code}")
        if response.status_code == 200:
            return pygame.image.load(io.BytesIO(response.content))
        else:
            print(f"Failed to load icon from URL: {png_url}")
            print(f"Response text: {response.text}")
    else:
        print(f"No icons found with name: {name}")
    return None
# Function to load JSON files from a directory
def load_json_files(directory):
    json_files = [file for file in os.listdir(directory) if file.endswith(".json")]
    data = []
    for file in json_files:
        file_path = os.path.join(directory, file)
        print(f"Loading JSON file: {file_path}")
        with open(file_path, "r") as f:
            data.append(json.load(f))
    return data

# Game loop
# Game loop
def game_loop():
    # Load character JSON files
    characters_data = load_json_files("characters")
    print(f"Loaded {len(characters_data)} character(s)")
    characters = []
    for character_data in characters_data:
        character_icon = load_png_from_s3(character_data["class"].lower())
        if character_icon:
            character_icon = pygame.transform.scale(character_icon, (50, 50))  # Adjust the size to about 1 inch
        character = {
            "class": character_data["class"],
            "element": character_data["element"],
            "archetype": character_data["archetype"],
            "icon": character_icon,
            "stats": character_data["attributes"]
        }
        characters.append(character)
        print(f"Loaded character: {character}")

    # Load monster JSON files
    monsters_data = load_json_files("monsters")
    print(f"Loaded {len(monsters_data)} monster(s)")
    monsters = []
    for monster_data in monsters_data:
        monster_icon = load_png_from_s3(monster_data["name"].lower())
        if monster_icon:
            monster_icon = pygame.transform.scale(monster_icon, (50, 50))  # Adjust the size to about 1 inch
        monster = {
            "name": monster_data["name"],
            "icon": monster_icon,
            "stats": {
                "level": monster_data["level"],
                "health": monster_data["health"],
                "max_health": monster_data["max_health"],
                "attack": monster_data["attack"],
                "defense": monster_data["defense"],
                "speed": monster_data["speed"],
                "experience_points": monster_data["experience_points"]
            },
            "abilities": monster_data["abilities"],
            "loot": monster_data["loot"],
            "dialogue": monster_data["dialogue"]
        }
        monsters.append(monster)
        print(f"Loaded monster: {monster}")

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the window
        window.fill((255, 255, 255))

        # Draw characters on the game screen
        for character in characters:
            if character["icon"]:
                character_x = window_width // 2 - character["icon"].get_width() // 2
                character_y = window_height - character["icon"].get_height() - 20
                window.blit(character["icon"], (character_x, character_y))

        # Draw monsters on the game screen
        for monster in monsters:
            if monster["icon"]:
                monster_x = random.randint(0, window_width - monster["icon"].get_width())
                monster_y = random.randint(0, window_height - monster["icon"].get_height() - 100)  # Adjust the vertical range
                window.blit(monster["icon"], (monster_x, monster_y))

        # Update the display
        pygame.display.update()

    # Quit the game
    pygame.quit()

# Run the game
game_loop()