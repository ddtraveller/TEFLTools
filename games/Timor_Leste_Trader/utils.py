import random
import anthropic
import time
import json
import os
import re

def save_game(game):
    game_state = {
        'pirate_name': game.pirate_name,
        'inventory': game.inventory,
        'ship_type': game.ship_type,
        'ship_capacity': game.ship_capacity,
        'ship_health': game.ship_health,
        'guns': game.guns,
        'speed': game.speed,
        'maneuverability': game.maneuverability,
        'current_city': game.current_city,
        'turn': game.turn,
        'prices': game.prices,
        'debt': game.debt,
        'bank_balance': game.bank_balance,
        'morale': game.morale,
        'reputation': game.reputation,
        'money': game.money
    }
    
    filename = re.sub(r'[^\w]', '_', game.pirate_name.lower()) + '.json'
    with open(filename, 'w') as f:
        json.dump(game_state, f)

def load_game(pirate_name):
    filename = re.sub(r'[^\w]', '_', pirate_name.lower()) + '.json'
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return None
    
def load_random_events():
    with open('json/random_events.json', 'r') as f:
        return json.load(f)

def trigger_random_event(game):
    events = load_random_events()
    event = random.choice(events)
    print(event['description'])
    for key, value in event['effect'].items():
        if key == 'morale':
            game.morale = max(0, min(100, game.morale + value))
        elif key == 'ship_health':
            game.ship_health = max(0, min(100, game.ship_health + value))
        elif key == 'money':
            game.money += value
    print(f"Effect applied: {event['effect']}")

def log_captain_response(response, is_victorious):
    filename = 'json/enemy_captain_victorious.json' if is_victorious else 'json/enemy_captain_defeated.json'
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            responses = json.load(f)
    else:
        responses = []
    
    responses.append(response)
    
    with open(filename, 'w') as f:
        json.dump(responses, f, indent=2)
        
client = anthropic.Anthropic()

with open('json/pirates_and_merchants.json', 'r') as f:
    pirates_and_merchants = json.load(f)

def generate_response(prompt, role="parrot", captain_name=None):
    system_message = {
        "parrot": "You are a pirate's parrot on a trading ship in Timor-Leste. Respond in a parrot's voice, using pirate slang and bird-like interjections.",
        "enemy_captain": f"You are a pirate captain{' named ' + captain_name if captain_name else ''}. You have just been defeated or emerged victorious in a sea battle. Respond with a mix of disappointment or triumph, seasoned with CREATIVE UNIQUE colorful pirate language. If you don't have a specific name, don't refer to yourself by name."
    }

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=1.0,
        system=system_message[role],
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )
    return message.content[0].text.strip()

def update_prices(game):
    for item in game.goods:
        game.prices[item['name']] = int(item['cost'] * random.uniform(0.5, 1.5))

    if random.random() < 0.2:
        special_item = random.choice(game.goods)['name']
        if random.random() < 0.5:
            game.prices[special_item] = int(game.prices[special_item] * 0.5)
            print(f"The price of {special_item} has dropped significantly!")
        else:
            game.prices[special_item] = int(game.prices[special_item] * 2)
            print(f"The price of {special_item} has risen dramatically!")
            
def pirate_attack(game):
    enemy_ship = random.choice(game.ships)
    if enemy_ship['guns'] > 15:
        enemy_captain = random.choice([p for p in pirates_and_merchants if p['reputation'] < 0])
        captain_name = enemy_captain['name']
    else:
        captain_name = None
    
    if captain_name:
        print(f"You're under attack by a {enemy_ship['name']} captained by {captain_name} with {enemy_ship['guns']} guns!")
    else:
        print(f"You're under attack by a {enemy_ship['name']} with {enemy_ship['guns']} guns!")
    
    while True:
        if game.ship_health <= 0 or game.guns <= 0:
            print("Your ship has been defeated. Game Over!")
            enemy_captain_remark = generate_response("You've just won a sea battle. What do you say to the defeated captain?", role="enemy_captain", captain_name=captain_name)
            if captain_name:
                print(f"The victorious pirate captain, {captain_name}, sneers: {enemy_captain_remark}")
            else:
                print(f"The victorious pirate captain sneers: {enemy_captain_remark}")
            log_captain_response(enemy_captain_remark, True)
            game.reputation -= 1
            wait_for_space()
            exit()

        action = input("Do you want to (f)ight or (r)un? ").lower()
        if action == 'f':
            battle_result = combat_round(game, enemy_ship)
            if battle_result == "player_win":
                print("You've defeated the pirates!")
                game.money += enemy_ship['cost'] // 2
                print(f"You've gained {enemy_ship['cost'] // 2} gold as booty!")
                
                # New code for pirate defeat options
                defeat_choice = input("Do you want to make the pirate (w)alk the plank or (s)pare him and his officers? ").lower()
                if defeat_choice == 'w':
                    print("The pirate captain walks the plank. Your crew cheers!")
                    enemy_captain_remark = generate_response("You've just been defeated in a sea battle and are about to walk the plank. What are your last words?", role="enemy_captain", captain_name=captain_name)
                elif defeat_choice == 's':
                    print("You spare the pirate captain and his officers, letting them go aboard a life raft.")
                    game.reputation += 1
                    enemy_captain_remark = generate_response("You've just been defeated in a sea battle, but the victorious captain has spared your life. Express your gratitude.", role="enemy_captain", captain_name=captain_name)
                else:
                    print("Invalid choice. The pirate captain escapes in the confusion.")
                    enemy_captain_remark = generate_response("You've just been defeated in a sea battle, but managed to escape. What do you say?", role="enemy_captain", captain_name=captain_name)
                
                if captain_name:
                    print(f"The {defeat_choice == 's' and 'grateful' or 'defeated'} pirate captain, {captain_name}, says: {enemy_captain_remark}")
                else:
                    print(f"The {defeat_choice == 's' and 'grateful' or 'defeated'} pirate captain says: {enemy_captain_remark}")
                
                log_captain_response(enemy_captain_remark, False)
                wait_for_space()
                break
            elif battle_result == "player_lose":
                print("Your ship has been defeated. Game Over!")
                enemy_captain_remark = generate_response("You've just won a sea battle. What do you say to the defeated captain?", role="enemy_captain", captain_name=captain_name)
                if captain_name:
                    print(f"The victorious pirate captain, {captain_name}, sneers: {enemy_captain_remark}")
                else:
                    print(f"The victorious pirate captain sneers: {enemy_captain_remark}")
                log_captain_response(enemy_captain_remark, True)
                game.reputation -= 1
                wait_for_space()
                exit()
            else:
                print("The battle continues!")
        elif action == 'r':
            if run_away(game, enemy_ship):
                wait_for_space()
                break
        else:
            print("Invalid action! Please choose 'f' to fight or 'r' to run.")
            
def combat_round(game, enemy_ship):
    player_damage_chance = game.maneuverability / (game.maneuverability + enemy_ship['maneuverability'])
    enemy_damage_chance = 1 - player_damage_chance

    if random.random() < player_damage_chance and game.guns > 0:
        damage = random.randint(1, max(1, game.guns))
        enemy_ship['guns'] -= damage
        print(f"You've damaged the enemy ship! They now have {enemy_ship['guns']} guns.")
        if enemy_ship['guns'] <= 0:
            return "player_win"
    elif game.guns == 0:
        print("You have no guns left to fight with!")
    else:
        print("You missed the enemy ship!")
    
    if random.random() < enemy_damage_chance:
        damage = random.randint(1, enemy_ship['guns'])
        apply_damage(game, damage)
        if game.ship_health <= 0 or game.guns <= 0:
            return "player_lose"
    else:
        print("The enemy ship missed you!")
    
    return "continue"

def apply_damage(game, damage):
    affected_items = random.sample(['guns', 'ship_health', 'goods'], min(3, max(1, damage)))
    
    for item in affected_items:
        if item == 'guns':
            guns_lost = min(game.guns, random.randint(1, damage))
            game.guns = max(0, game.guns - guns_lost)
            print(f"You lost {guns_lost} guns in the attack!")
        elif item == 'ship_health':
            health_lost = min(game.ship_health, random.randint(1, damage * 10))
            game.ship_health = max(0, game.ship_health - health_lost)
            print(f"Your ship took {health_lost}% damage!")
        else:  # goods
            if sum(game.inventory.values()) > 0:
                goods_lost = min(sum(game.inventory.values()), random.randint(1, damage * 5))
                print(f"You lost {goods_lost} units of random cargo!")
                while goods_lost > 0:
                    item = random.choice(list(game.inventory.keys()))
                    if game.inventory[item] > 0:
                        game.inventory[item] -= 1
                        goods_lost -= 1

    print(f"After the attack: Ship Health: {game.ship_health}%, Guns: {game.guns}")

def run_away(game, enemy_ship):
    if game.speed > enemy_ship['speed']:
        print("You've managed to escape!")
        return True
    else:
        print("The enemy ship is faster than you! You can't escape.")
        damage = random.randint(1, enemy_ship['guns'])
        apply_damage(game, damage)
        if game.ship_health <= 0 or game.guns <= 0:
            print("Your ship has been defeated while trying to escape. Game Over!")
            wait_for_space()
            exit()
        return False
        
def offer_ship_upgrade(game):
    current_ship_index = game.ships.index(next(ship for ship in game.ships if ship['name'] == game.ship_type))
    if current_ship_index < len(game.ships) - 1:
        upgrade_cost = game.ships[current_ship_index + 1]['cost'] - game.ships[current_ship_index]['cost']
        merchant = random.choice([m for m in pirates_and_merchants if m['reputation'] > 0])
        print(f"You've been offered a ship upgrade to {game.ships[current_ship_index + 1]['name']} for {upgrade_cost} gold by {merchant['name']}.")
        if input("Do you want to upgrade? (y/n) ").lower() == 'y':
            if game.money >= upgrade_cost:
                game.money -= upgrade_cost
                game.ship_type = game.ships[current_ship_index + 1]['name']
                game.ship_capacity = game.ships[current_ship_index + 1]['capacity']
                game.ship_health = 100
                game.guns = game.ships[current_ship_index + 1]['guns']
                game.speed = game.ships[current_ship_index + 1]['speed']
                game.maneuverability = game.ships[current_ship_index + 1]['maneuverability']
                print(f"Ship upgraded to {game.ship_type}!")
            else:
                print("Not enough gold for the upgrade.")
    else:
        print("You already have the best ship available!")

def wait_for_space():
    print("\nPress Enter to Continue...")
    while True:
        if input() != "xxxxxx":
            break

def handle_hunger(game):
    if game.turn % 3 == 0:
        food_consumed = False
        morale_change = 0
        # Check for luxury food items first
        for item in game.luxury_food_items:
            if game.inventory[item] > 0:
                game.inventory[item] -= 1
                food_consumed = True
                morale_change = 5
                print(f"Crew consumed 1 {item}. Morale increased!")
                break
        
        # If no luxury food, check for basic food items
        if not food_consumed:
            for item in game.basic_food_items:
                if game.inventory[item] > 0:
                    game.inventory[item] -= 1
                    food_consumed = True
                    print(f"Crew consumed 1 {item}.")
                    break
        
        # If no food at all, decrease morale
        if not food_consumed:
            morale_change = -10
            print("No food available! Crew morale decreased significantly.")
        update_morale(game, morale_change)

def update_morale(game, change=0):
    game.morale = min(100, max(0, game.morale + change + (game.ship_health - 50) / 10 + (game.guns - 5) / 2 - game.debt / 1000))
    if sum(game.inventory.values()) / game.ship_capacity > 0.8:
        game.morale += 5
    if game.money > 10000:
        game.morale += 5
    if game.debt > 5000:
        game.morale -= 5

def display_status(game):
    print(f"\nTurn: {game.turn}")
    print(f"Current Port: {game.cities[game.current_city]}")
    print(f"Gold: {game.money}")
    print(f"Debt: {game.debt}")
    print(f"Bank Balance: {game.bank_balance}")
    print(f"Crew Morale: {game.morale:.2f}%")
    print(f"Reputation: {game.reputation}")
    # Display food items and their quantities
    print("\nFood Supplies:")
    for item in game.luxury_food_items + game.basic_food_items:
        if game.inventory[item] > 0:
            print(f"{item}: {game.inventory[item]}")
    # Display top 3 items by price
    top_items = sorted(game.prices.items(), key=lambda x: x[1], reverse=True)[:3]
    print("\nTop 3 items by price:")
    for i, (item, price) in enumerate(top_items):
        print(f"{i+1}. {item} - {price} gold")
    # Display bottom 3 items by price
    bottom_items = sorted(game.prices.items(), key=lambda x: x[1])[:3]
    print("\nBottom 3 items by price:")
    for i, (item, price) in enumerate(bottom_items):
        print(f"{i+1}. {item} - {price} gold")
    # Display prices for items in the player's inventory
    print("\nPrices for items in your inventory:")
    for item, amount in game.inventory.items():
        if amount > 0:
            print(f"{item} - {game.prices[item]} gold")
    print(f"\nShip Type: {game.ship_type}")
    print(f"Ship Health: {game.ship_health}%")
    print(f"Guns: {game.guns}")
    print(f"Speed: {game.speed}")
    print(f"Maneuverability: {game.maneuverability}")
    print(f"Capacity: {game.ship_capacity - sum(game.inventory.values())}/{game.ship_capacity}")