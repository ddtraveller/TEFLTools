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

# Load the list of available icons from the JSON file
with open("icons/icon_files.json", "r") as f:
    icon_files = json.load(f)

# Load the list of available terrain icons from the JSON file
with open("icons/terrain/terrain.json", "r") as f:
    terrain_files = json.load(f)

# Grid settings
grid_size = 50  # Size of each grid cell
grid_rows = window_height // grid_size
grid_cols = window_width // grid_size

# Function to load a random PNG from a public S3 bucket
def load_png_from_s3(name, folder="icons"):
    base_url = f"https://tl-web.s3.us-west-2.amazonaws.com/{folder}/"
    if folder == "icons/terrain":
        filtered_icons = [icon for icon in terrain_files if name in icon.split("-", 1)[1].lower()]
    else:
        filtered_icons = [icon for icon in icon_files if icon == f"{name}.png"]
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
def game_loop():
    # Load character JSON files
    characters_data = load_json_files("characters")
    print(f"Loaded {len(characters_data)} character(s)")
    characters = []
    for character_data in characters_data:
        character_icon = load_png_from_s3(character_data["class"].lower(), folder="icons")
        if character_icon:
            character_icon = pygame.transform.scale(character_icon, (grid_size, grid_size))
        character = {
            "class": character_data["class"],
            "element": character_data["element"],
            "archetype": character_data["archetype"],
            "icon": character_icon,
            "stats": character_data["attributes"],
            "position": (grid_cols // 2, grid_rows - 1)  # Start position for the character
        }
        characters.append(character)
        print(f"Loaded character: {character}")

    # Load monster JSON files
    monsters_data = load_json_files("monsters")
    print(f"Loaded {len(monsters_data)} monster(s)")
    monsters = []
    for monster_data in monsters_data:
        monster_icon = load_png_from_s3(monster_data["name"].lower(), folder="icons")
        if monster_icon:
            monster_icon = pygame.transform.scale(monster_icon, (grid_size, grid_size))
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
            "dialogue": monster_data["dialogue"],
            "position": (random.randint(0, grid_cols - 1), 0)  # Start position for the monster
        }
        monsters.append(monster)
        print(f"Loaded monster: {monster}")

    # Load a handful of terrain icons from S3
    terrain_icons = []
    terrain_positions = []
    for i in range(5):  # Load 5 random terrain icons
        terrain_icon = load_png_from_s3(random.choice(["tree", "rain", "vines", "volcano", "bridge"]), folder="icons/terrain")
        if terrain_icon:
            terrain_icon = pygame.transform.scale(terrain_icon, (grid_size, grid_size))
            terrain_icons.append(terrain_icon)
            terrain_x = random.randint(0, grid_cols - 1)
            terrain_y = random.randint(1, grid_rows - 2)  # Avoid the first and last row
            terrain_positions.append((terrain_x, terrain_y))

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Handle character movement
                if event.key == pygame.K_UP:
                    new_position = (characters[0]["position"][0], characters[0]["position"][1] - 1)
                    if new_position[1] >= 0 and not is_position_occupied(new_position, terrain_positions):
                        characters[0]["position"] = new_position
                elif event.key == pygame.K_DOWN:
                    new_position = (characters[0]["position"][0], characters[0]["position"][1] + 1)
                    if new_position[1] < grid_rows - 1 and not is_position_occupied(new_position, terrain_positions):
                        characters[0]["position"] = new_position
                elif event.key == pygame.K_LEFT:
                    new_position = (characters[0]["position"][0] - 1, characters[0]["position"][1])
                    if new_position[0] >= 0 and not is_position_occupied(new_position, terrain_positions):
                        characters[0]["position"] = new_position
                elif event.key == pygame.K_RIGHT:
                    new_position = (characters[0]["position"][0] + 1, characters[0]["position"][1])
                    if new_position[0] < grid_cols and not is_position_occupied(new_position, terrain_positions):
                        characters[0]["position"] = new_position

        # Clear the window
        window.fill((255, 255, 255))

        # Draw the grid
        for row in range(grid_rows):
            for col in range(grid_cols):
                rect = (col * grid_size, row * grid_size, grid_size, grid_size)
                pygame.draw.rect(window, (200, 200, 200), rect, 1)

        # Draw characters on the game screen
        for character in characters:
            if character["icon"]:
                character_pos = (character["position"][0] * grid_size, character["position"][1] * grid_size)
                window.blit(character["icon"], character_pos)

        # Draw monsters on the game screen
        for monster in monsters:
            if monster["icon"]:
                monster_pos = (monster["position"][0] * grid_size, monster["position"][1] * grid_size)
                window.blit(monster["icon"], monster_pos)

        # Draw terrain icons on the game screen
        for i, terrain_icon in enumerate(terrain_icons):
            terrain_pos = (terrain_positions[i][0] * grid_size, terrain_positions[i][1] * grid_size)
            window.blit(terrain_icon, terrain_pos)

        # Update the display
        pygame.display.update()

# Helper function to check if a position is occupied by a terrain icon
def is_position_occupied(position, terrain_positions):
    for terrain_pos in terrain_positions:
        if position == terrain_pos:
            return True
    return False

# Run the game
game_loop()