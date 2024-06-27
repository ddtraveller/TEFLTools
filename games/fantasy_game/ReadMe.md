# Timor Leste Fantasia: A Text-Based Adventure Game

## Table of Contents
1. Introduction
2. Vocabulary
3. Setup
4. File Structure
5. Key Components
6. Anthropic API and Language Model Integration
7. Modifying the Code
8. Extending the Game

## Introduction

Timor Leste Fantasia is a text-based adventure game set in a fantastical version of Timor-Leste. The game combines traditional RPG elements with dynamic storytelling powered by the Anthropic language model. Players can explore various locations, encounter creatures, engage in dialogue, and participate in combat.

This README provides a comprehensive guide to the game's structure, focusing on how the Anthropic API is used for dynamic content generation and how Python students can modify and extend the code.

## Vocabulary

Before diving into the code, let's familiarize ourselves with some key terms used in the game:

- NPC: Non-Player Character, controlled by the game rather than the player.
- Encounter: An interaction between the player and an NPC or monster.
- Combat: A turn-based battle system where the player fights against monsters.
- Attribute: A numerical value representing a character's capabilities (e.g., Strength, Dexterity).
- Skill: A specific ability that a character can use, often in combat or for problem-solving.
- Prompt: In the context of the Anthropic API, a text input that guides the AI in generating responses.
- JSON: JavaScript Object Notation, a lightweight data interchange format used to store game data.
- API: Application Programming Interface, used here to interact with the Anthropic language model.
- Language Model: An AI system trained to understand and generate human-like text, used in this game for dynamic content generation.

## Setup

1. Ensure you have Python 3.7+ installed on your system.
2. Install required packages:
   ```
   pip install anthropic
   ```
3. Set up your Anthropic API key:
   - Sign up for an Anthropic API key at https://www.anthropic.com
   - Set the API key as an environment variable:
     ```
     export ANTHROPIC_API_KEY=your_api_key_here
     ```
4. Clone the repository and navigate to the project directory.

## File Structure

The game is organized into several Python files, each handling different aspects of the game:

- begin_game.py: Main game loop and initialization
- Navigation.py: Handles player movement between locations
- Combat.py: Manages combat encounters and dialogue interactions
- Character.py: Defines character creation and attributes
- character_gen.py: Handles character generation process
- game_utils.py: Contains utility functions used across the game

JSON files store game data:
- timor_leste_locations.json: Contains location data
- monsters.json: Defines monster attributes and behaviors
- equipment.json: Lists available equipment for characters

## Key Components

### Character Generation (character_gen.py)
- Allows players to create and customize their character
- Uses a series of questions to determine character attributes and background

### Navigation (Navigation.py)
- Manages player movement between locations
- Calculates distances and nearby locations
- Triggers random encounters

### Combat and Encounters (Combat.py)
- Handles both combat and non-combat encounters
- Uses the Anthropic API for dynamic dialogue generation
- Manages turn-based combat system

### Game Initialization (begin_game.py)
- Sets up the game environment
- Loads or creates character data
- Starts the main game loop

## Anthropic API and Language Model Integration

The game uses the Anthropic API to generate dynamic content, primarily in the Combat.py file. Key areas of integration include:

1. Dialogue Generation: 
   In the get_llm_response function, the API is used to generate NPC responses during encounters.

   ```python
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
   ```

2. Decision Making:
   The get_llm_decision function uses the API to determine the outcome of an encounter based on the conversation history.

   ```python
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

       return get_llm_response(messages)
   ```

3. Fallback Mechanism:
   The code includes a fallback mechanism for when the API is unavailable, ensuring the game can still function without dynamic content generation.

## Modifying the Code

Here are detailed explanations and code samples for modifying different aspects of the game:

1. Adding New Locations:
   Expanding the game world by adding new locations enhances the exploration aspect of the game. Each location should have a unique name, description, and coordinates.

   Edit the timor_leste_locations.json file to include new locations:

   ```json
   [
     {
       "name": "Mystic Grove of Whispers",
       "description": "An ancient forest where the trees seem to whisper secrets of the past. The air is thick with magic, and glowing fireflies dance between the gnarled branches.",
       "latitude": -8.7514,
       "longitude": 125.4889,
       "elevation": 1050
     },
     // ... existing locations ...
   ]
   ```

   Explanation: This adds a new location called "Mystic Grove of Whispers" to the game world. The description provides atmospheric details that can be used in the game narrative. The coordinates (latitude, longitude, elevation) are used by the navigation system to determine distances and nearby locations.

2. Creating New Monsters:
   Adding new monsters increases the variety of encounters and challenges for the player. Each monster should have unique attributes, abilities, and dialogue options.

   Add new monster definitions to the monsters.json file:

   ```json
   [
     {
       "name": "Shadow Stalker",
       "level": 3,
       "health": 45,
       "armor_class": 14,
       "abilities": [
         {"name": "Shadow Strike", "damage": 8, "accuracy": 75},
         {"name": "Vanish", "damage": 0, "accuracy": 100}
       ],
       "dialogue": [
         "You cannot hide from the shadows...",
         "Your light will soon be extinguished...",
         "Embrace the darkness, mortal..."
       ],
       "long_description": "A sinister creature born of darkness and fear. Its form shifts and wavers like smoke, making it difficult to pin down.",
       "locations": ["Misty Marshes of Covalima", "Echoing Caverns of Lautém"]
     },
     // ... existing monsters ...
   ]
   ```

   Explanation: This creates a new monster called "Shadow Stalker". It has basic stats like level, health, and armor class. The abilities array defines its attack options, while the dialogue array provides potential responses during encounters. The long_description is used when the player first encounters the monster, and the locations array determines where this monster can be found.

3. Expanding Character Classes:
   Adding new character classes or modifying existing ones can provide players with more diverse gameplay options. This involves updating the character creation process and potentially adding new skills or attributes.

   Modify the Character.py file to include new character classes:

   ```python
   character_classes = {
       # ... existing classes ...
       "Alchemist": {"Intelligence": 2, "Dexterity": 1},
       "Beastmaster": {"Wisdom": 2, "Strength": 1}
   }

   character_archetypes = {
       # ... existing archetypes ...
       "Alchemist": ["Potion Master", "Bomb Specialist", "Transmuter"],
       "Beastmaster": ["Wolf Companion", "Bird of Prey", "Swarm Keeper"]
   }

   def create_character(element_score):
       # ... existing code ...
       if character_class == "Alchemist":
           character["special_ability"] = "Brew Potion"
       elif character_class == "Beastmaster":
           character["companion"] = random.choice(["Wolf", "Eagle", "Swarm of Insects"])
       # ... rest of the function ...
   ```

   Explanation: This adds two new character classes: Alchemist and Beastmaster. Each class has its primary attributes defined in character_classes and potential specializations in character_archetypes. The create_character function is updated to assign special abilities or companions to these new classes.

4. Enhancing Combat System:
   Improving the combat system can make battles more engaging and strategic. This could involve adding new actions, status effects, or modifying how damage is calculated.

   In Combat.py, you can add new combat actions:

   ```python
   def player_turn(character_data, monster_data, defense):
       print("\nIt's your turn!")
       actions = ["Attack", "Defend", "Spell", "Use Item", "Analyze"]
       action = get_user_choice(actions)
       if action == 0:
           return perform_attack(character_data, monster_data)
       elif action == 1:
           return defend(character_data)
       elif action == 2:
           return cast_spell(character_data, monster_data)
       elif action == 3:
           return use_item(character_data)
       elif action == 4:
           return analyze_enemy(monster_data)

   def analyze_enemy(monster_data):
       print(f"You carefully observe the {monster_data['name']}.")
       print(f"Health: {monster_data['health']}")
       print(f"Armor Class: {monster_data['armor_class']}")
       print("Abilities:")
       for ability in monster_data['abilities']:
           print(f"- {ability['name']}")
       return 0  # Analyzing doesn't change defense
   ```

   Explanation: This adds a new "Analyze" action to combat, allowing players to gain information about their enemies. The player_turn function is expanded to include this new option, and a new analyze_enemy function is created to handle the action.

5. Improving Dialogue Generation:
   Enhancing the dialogue system can lead to more varied and interesting interactions with NPCs and monsters. This involves modifying the prompts sent to the Anthropic API.

   Adjust the prompts in get_llm_response and get_llm_decision functions in Combat.py:

   ```python
   def get_llm_response(messages, character_data, monster_data):
       prompt = f"""
   You are role-playing as a {monster_data['name']} in a fantasy world. 
   You are interacting with {character_data['name']}, a level {character_data['level']} {character_data['class']}.
   Your personality is: {monster_data.get('personality', 'mysterious and unpredictable')}.
   The current situation is: {messages[-1]['content']}

   Respond to the player's last statement or question in character, in 1-2 sentences.
   Be creative, but stay true to your character's nature and the fantasy setting.
   """
       messages.append({"role": "user", "content": prompt})
       
       # ... rest of the function remains the same
   ```

   Explanation: This modified prompt provides more context to the AI, including the monster's personality and the current situation. This can lead to more varied and contextually appropriate responses.

6. Adding New Game Mechanics:
   Introducing new gameplay elements can add depth and variety to the game. This often involves creating new Python files and integrating them into the main game loop.

   Create a new file weather.py to implement a weather system:

   ```python
   import random

   class WeatherSystem:
       def __init__(self):
           self.conditions = ["Clear", "Cloudy", "Rainy", "Stormy", "Foggy"]
           self.current_weather = "Clear"

       def update_weather(self):
           chance = random.random()
           if chance < 0.7:
               return  # 70% chance weather stays the same
           self.current_weather = random.choice(self.conditions)

       def get_weather_effect(self):
           if self.current_weather == "Rainy":
               return {"movement_speed": -5, "perception": -2}
           elif self.current_weather == "Foggy":
               return {"movement_speed": -2, "perception": -5}
           elif self.current_weather == "Stormy":
               return {"movement_speed": -10, "combat_bonus": 2}
           else:
               return {}

   # In begin_game.py
   from weather import WeatherSystem

   def main():
       # ... existing code ...
       weather_system = WeatherSystem()
       
       while True:
           weather_system.update_weather()
           weather_effects = weather_system.get_weather_effect()
           print(f"Current Weather: {weather_system.current_weather}")
           
           # Apply weather effects to character
           for stat, effect in weather_effects.items():
               character_data[stat] = character_data.get(stat, 0) + effect
           
           # ... rest of the game loop ...
   ```

   Explanation: This introduces a new weather system to the game. The WeatherSystem class manages changing weather conditions and their effects on gameplay. In the main game loop, the weather is updated periodically and its effects are applied to the character's stats.

These modifications demonstrate various ways to expand and enhance the game. Each change adds new elements to the gameplay, whether it's new locations to explore, monsters to encounter, character options to choose from, or mechanics that affect the game world. By understanding these examples, you can start to envision and implement your own unique additions to the game.

## Extending the Game

Here are some ideas for extending the game:

1. Quest System: Implement a quest system with objectives and rewards.
2. Inventory Management: Create a more complex inventory system with weight limits and item degradation.
3. NPC Interactions: Add non-combat NPCs with their own dialogue trees and quest-giving abilities.
4. Skill System: Implement a skill system that allows characters to learn and improve various abilities.
5. Weather and Time: Add a dynamic weather and time system that affects gameplay.
6. Multiplayer: Implement basic multiplayer functionality for cooperative play.

When extending the game, remember to maintain the structure of using separate files for different functionalities and update the main game loop in begin_game.py to incorporate new features.

---

This README provides a comprehensive guide to understanding, modifying, and extending the Timor Leste Fantasia game. By following these examples and explanations, you can begin to create your own unique version of the game, adding new features and content as you see fit. Happy coding and game designing!