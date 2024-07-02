import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.score = 0

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def mini_game_tais_weaving():
    print_slow("You encounter a master weaver who challenges you to a Tais weaving contest!")
    print_slow("You need to select the correct color sequence to complete the Tais pattern.")
    colors = ['Red', 'Black', 'Yellow', 'White']
    pattern = [random.choice(colors) for _ in range(4)]
    
    for attempt in range(3):
        print_slow(f"Attempt {attempt + 1}. Choose 4 colors from: Red, Black, Yellow, White")
        guess = [input(f"Color {i+1}: ").capitalize() for i in range(4)]
        
        if guess == pattern:
            print_slow("Congratulations! You've woven a beautiful Tais!")
            return True
        else:
            correct_positions = sum(g == p for g, p in zip(guess, pattern))
            print_slow(f"You got {correct_positions} colors in the correct position. Try again!")
    
    print_slow(f"The correct pattern was: {', '.join(pattern)}. Better luck next time!")
    return False

def mini_game_coffee_harvest():
    print_slow("You find yourself in a lush coffee plantation. Time for a coffee bean picking challenge!")
    print_slow("You need to pick the ripe coffee cherries. Red ones are ripe, green ones are not.")
    
    score = 0
    for _ in range(5):
        cherry = random.choice(['Red', 'Green'])
        print_slow(f"You see a {cherry} coffee cherry. Do you pick it? (yes/no)")
        choice = input().lower()
        
        if (cherry == 'Red' and choice == 'yes') or (cherry == 'Green' and choice == 'no'):
            print_slow("Good choice!")
            score += 1
        else:
            print_slow("Oops, that wasn't the right choice.")
    
    print_slow(f"You picked {score} out of 5 correctly!")
    return score >= 3

def mini_game_crocodile_riddle():
    print_slow("You encounter the wise crocodile of Timor-Leste. He has a riddle for you:")
    print_slow("I am the oldest, yet the youngest. I am born each morning, yet never die. What am I?")
    
    attempts = 3
    while attempts > 0:
        answer = input("Your answer: ").lower()
        if "sun" in answer:
            print_slow("The crocodile nods approvingly. You've solved the riddle!")
            return True
        else:
            attempts -= 1
            print_slow(f"That's not correct. You have {attempts} attempts left.")
    
    print_slow("The crocodile shakes his head. The answer was 'the sun'. Better luck next time!")
    return False

def explore_dili():
    print_slow("You arrive in the bustling capital city of Dili.")
    print_slow("Where would you like to go?")
    print_slow("1. Cristo Rei")
    print_slow("2. Tais Market")
    print_slow("3. Timor Plaza")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        print_slow("You climb up to the Christ the King statue and enjoy a breathtaking view of the city.")
        print_slow("You find a mysterious map piece hidden near the statue!")
        return "map_piece"
    elif choice == '2':
        print_slow("You wander through the colorful Tais Market.")
        if mini_game_tais_weaving():
            print_slow("The master weaver, impressed by your skills, gives you a beautiful Tais!")
            return "tais"
    elif choice == '3':
        print_slow("You explore Timor Plaza, the modern heart of Dili.")
        print_slow("You buy a delicious Timorese coffee at Kafe Aroma Timor.")
    
    return None

def explore_maubisse():
    print_slow("You travel to the cool, mountainous region of Maubisse, famous for its coffee.")
    print_slow("What would you like to do?")
    print_slow("1. Visit a coffee plantation")
    print_slow("2. Hike in the mountains")
    print_slow("3. Visit the local market")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        print_slow("You visit a local coffee plantation.")
        if mini_game_coffee_harvest():
            print_slow("The plantation owner, impressed by your skills, gives you a bag of premium Timorese coffee!")
            return "coffee"
    elif choice == '2':
        print_slow("You go for a hike in the beautiful mountains.")
        print_slow("At the peak, you find another piece of the mysterious map!")
        return "map_piece"
    elif choice == '3':
        print_slow("You explore the local market, filled with fresh produce and handicrafts.")
        print_slow("You buy some delicious tropical fruits.")
    
    return None

def explore_jaco_island():
    print_slow("You take a boat to the pristine Jaco Island, a protected natural area.")
    print_slow("What would you like to do?")
    print_slow("1. Snorkel in the crystal-clear waters")
    print_slow("2. Explore the beach")
    print_slow("3. Look for the wise crocodile")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        print_slow("You snorkel in the beautiful coral reefs, seeing colorful fish and marine life.")
        print_slow("You spot something shiny in the coral...")
        print_slow("It's another piece of the map!")
        return "map_piece"
    elif choice == '2':
        print_slow("You walk along the pristine white sand beach.")
        print_slow("You find a beautiful seashell to take as a souvenir.")
    elif choice == '3':
        print_slow("You search for the legendary wise crocodile of Timor-Leste.")
        if mini_game_crocodile_riddle():
            print_slow("The crocodile, impressed by your wisdom, reveals the location of the Golden Crocodile!")
            return "golden_crocodile_location"
    
    return None

def main_game():
    print_slow("Welcome to Timor-Leste Adventure: The Quest for the Golden Crocodile!")
    player_name = input("Enter your name, brave adventurer: ")
    player = Player(player_name)
    
    print_slow(f"Welcome, {player.name}! You are on a quest to find the legendary Golden Crocodile of Timor-Leste.")
    print_slow("Your journey will take you across this beautiful country. Good luck!")
    
    locations = [explore_dili, explore_maubisse, explore_jaco_island]
    random.shuffle(locations)
    
    for location in locations:
        item = location()
        if item:
            player.inventory.append(item)
            print_slow(f"You obtained: {item}")
        
        print_slow(f"Your inventory: {', '.join(player.inventory)}")
        print_slow("----------------------")
    
    if "golden_crocodile_location" in player.inventory and player.inventory.count("map_piece") == 3:
        print_slow("Congratulations! You've collected all the map pieces and found the Golden Crocodile's location!")
        print_slow("You follow the map to a hidden cave...")
        print_slow("There it is! The Golden Crocodile statue, glittering in the cave!")
        print_slow(f"Well done, {player.name}! You've completed your quest and discovered Timor-Leste's legendary treasure!")
    else:
        print_slow("Your quest has come to an end, but the Golden Crocodile remains hidden.")
        print_slow("Perhaps another adventure awaits you in the beautiful lands of Timor-Leste!")
    
    print_slow(f"Thank you for playing, {player.name}! We hope you enjoyed your adventure in Timor-Leste!")

if __name__ == "__main__":
    main_game()