import random
import time

# Unit 1: Introduction to Programming and Python
def guess_the_number():
    print("Unit 1: Guess the Number!")
    secret_number = random.randint(1, 20)
    attempts = 0

    print("I'm thinking of a number between 1 and 20.")
    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

# Unit 2: Variables and Data Types
def math_challenge():
    print("Unit 2: Lightning Math Challenge!")
    score = 0
    rounds = 5

    for _ in range(rounds):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(['+', '-', '*'])
        
        if operator == '+':
            correct_answer = num1 + num2
        elif operator == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2

        start_time = time.time()
        user_answer = int(input(f"What's {num1} {operator} {num2}? "))
        end_time = time.time()

        if user_answer == correct_answer and (end_time - start_time) < 5:
            print("Correct and fast! +2 points")
            score += 2
        elif user_answer == correct_answer:
            print("Correct! +1 point")
            score += 1
        else:
            print(f"Sorry, the correct answer was {correct_answer}")

    print(f"Game over! Your final score is {score} out of {rounds * 2} possible points.")

# Unit 3: Control Flow
def adventure_game():
    print("Unit 3: Timor-Leste Adventure Game!")
    print("You're on a journey through Timor-Leste. Make choices to navigate your adventure.")

    while True:
        print("\nYou're at a crossroads. Do you want to:")
        print("1. Climb Mount Ramelau")
        print("2. Explore the beaches of Atauro Island")
        print("3. Visit the markets in Dili")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("You climb Mount Ramelau and enjoy breathtaking views of Timor-Leste!")
            if random.random() < 0.5:
                print("You discover a rare plant species. Scientists thank you for your contribution!")
            else:
                print("The climb was tough, but worth it for the sunrise.")
        elif choice == '2':
            print("You have a wonderful time snorkeling and relaxing on Atauro Island.")
            if random.random() < 0.5:
                print("You spot a pod of dolphins! What an incredible experience!")
            else:
                print("The crystal clear waters and vibrant marine life amaze you.")
        elif choice == '3':
            print("You wander through the lively markets of Dili, taking in the sights and smells.")
            if random.random() < 0.5:
                print("You find a beautiful traditional tais. It will make a great souvenir!")
            else:
                print("You taste some delicious local fruits you've never tried before.")
        else:
            print("Invalid choice. Please try again.")
            continue

        play_again = input("Do you want to continue your adventure? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing the Timor-Leste Adventure Game!")
            break

# Unit 4: Functions
def word_scramble():
    print("Unit 4: Timorese Word Scramble!")

    words = ["Timor", "Leste", "Dili", "Atauro", "Ramelau", "Tais", "Fatuk", "Lafaek"]

    def scramble_word(word):
        return ''.join(random.sample(word, len(word)))

    def play_round():
        word = random.choice(words)
        scrambled = scramble_word(word)
        attempts = 3

        print(f"Unscramble this word: {scrambled}")
        while attempts > 0:
            guess = input("Your guess: ").capitalize()
            if guess == word:
                print("Correct! Well done!")
                return True
            else:
                attempts -= 1
                print(f"Sorry, that's not right. You have {attempts} attempts left.")
        
        print(f"Out of attempts. The word was {word}.")
        return False

    score = 0
    rounds = 5

    for _ in range(rounds):
        if play_round():
            score += 1

    print(f"Game over! You unscrambled {score} out of {rounds} words.")

# Unit 5: Lists and Dictionaries
def memory_game():
    print("Unit 5: Timorese Symbol Memory Game!")
    symbols = ['🌴', '🏔️', '🏖️', '🐊', '🐬', '🌺', '☕', '🎭']
    pairs = symbols * 2
    random.shuffle(pairs)
    board = [' '] * 16
    matched = []

    def print_board():
        for i in range(0, 16, 4):
            print(' '.join(board[i:i+4]))

    def get_move():
        while True:
            try:
                position = int(input("Enter a position (1-16): ")) - 1
                if 0 <= position < 16 and board[position] == ' ':
                    return position
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a number between 1 and 16.")

    moves = 0
    while len(matched) < len(symbols):
        print_board()
        pos1 = get_move()
        board[pos1] = pairs[pos1]
        print_board()
        
        pos2 = get_move()
        board[pos2] = pairs[pos2]
        print_board()
        
        moves += 1
        
        if pairs[pos1] == pairs[pos2]:
            print("Match found!")
            matched.append(pairs[pos1])
        else:
            print("No match. Try again!")
            time.sleep(2)
            board[pos1] = ' '
            board[pos2] = ' '

    print(f"Congratulations! You completed the game in {moves} moves.")

# Unit 6: File I/O and Basic Data Analysis
def trivia_game():
    print("Unit 6: Timor-Leste Trivia Game!")
    
    # Create a sample trivia file
    trivia_data = [
        {"question": "What is the capital of Timor-Leste?", "answer": "Dili"},
        {"question": "In what year did Timor-Leste gain independence?", "answer": "2002"},
        {"question": "What is the official currency of Timor-Leste?", "answer": "US Dollar"},
        {"question": "What is the highest mountain in Timor-Leste?", "answer": "Mount Ramelau"},
        {"question": "What is the traditional cloth of Timor-Leste called?", "answer": "Tais"}
    ]

    import json
    with open('timor_leste_trivia.json', 'w') as f:
        json.dump(trivia_data, f)

    # Play the game
    score = 0
    with open('timor_leste_trivia.json', 'r') as f:
        questions = json.load(f)
        random.shuffle(questions)

    for q in questions:
        print("\n" + q["question"])
        answer = input("Your answer: ")
        if answer.lower() == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {q['answer']}.")

    print(f"\nGame over! You scored {score} out of {len(questions)}.")

    # Basic data analysis
    print("\nTrivia Game Statistics:")
    print(f"Total questions: {len(questions)}")
    print(f"Correct answers: {score}")
    print(f"Accuracy: {(score/len(questions))*100:.2f}%")

# Unit 7: Introduction to Libraries and APIs
def emoji_weather():
    print("Unit 7: Emoji Weather Forecast!")
    
    import random

    def get_weather_emoji():
        weathers = ['☀️', '🌤️', '⛅', '🌥️', '☁️', '🌦️', '🌧️', '⛈️', '🌩️', '🌨️']
        return random.choice(weathers)

    def get_temperature():
        return random.randint(20, 35)  # Typical range for Timor-Leste

    cities = ['Dili', 'Baucau', 'Maliana', 'Suai', 'Lospalos', 'Aileu']
    forecast = {}

    print("Welcome to the Timor-Leste Weather Forecast!")
    for city in cities:
        forecast[city] = {
            'weather': get_weather_emoji(),
            'temperature': get_temperature()
        }

    while True:
        print("\nChoose a city to get the weather forecast:")
        for i, city in enumerate(cities, 1):
            print(f"{i}. {city}")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == '0':
            print("Thanks for using the Emoji Weather Forecast!")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(cities):
            city = cities[int(choice)-1]
            print(f"\nWeather forecast for {city}:")
            print(f"Condition: {forecast[city]['weather']}")
            print(f"Temperature: {forecast[city]['temperature']}°C")
        else:
            print("Invalid choice. Please try again.")

# Unit 8: Final Project
def coffee_farm_simulator():
    print("Unit 8: Timor-Leste Coffee Farm Simulator!")

    class CoffeeFarm:
        def __init__(self, name):
            self.name = name
            self.trees = 100
            self.coffee = 0
            self.money = 1000

        def plant_trees(self, number):
            cost = number * 5
            if self.money >= cost:
                self.trees += number
                self.money -= cost
                print(f"Planted {number} new coffee trees!")
            else:
                print("Not enough money to plant trees.")

        def harvest_coffee(self):
            harvest = self.trees * random.uniform(0.5, 1.5)
            self.coffee += harvest
            print(f"Harvested {harvest:.2f} kg of coffee!")

        def sell_coffee(self, amount):
            if self.coffee >= amount:
                earnings = amount * random.uniform(3, 7)
                self.coffee -= amount
                self.money += earnings
                print(f"Sold {amount} kg of coffee for ${earnings:.2f}!")
            else:
                print("Not enough coffee to sell.")

    farm = CoffeeFarm(input("Enter your farm name: "))
    year = 1

    while True:
        print(f"\nYear {year} on {farm.name}")
        print(f"Trees: {farm.trees}")
        print(f"Coffee: {farm.coffee:.2f} kg")
        print(f"Money: ${farm.money:.2f}")

        action = input("What would you like to do? (plant/harvest/sell/end): ").lower()

        if action == 'plant':
            try:
                num_trees = int(input("How many trees to plant? "))
                farm.plant_trees(num_trees)
            except ValueError:
                print("Please enter a valid number.")
        elif action == 'harvest':
            farm.harvest_coffee()
        elif action == 'sell':
            try:
                amount = float(input("How much coffee to sell? "))
                farm.sell_coffee(amount)
            except ValueError:
                print("Please enter a valid number.")
        elif action == 'end':
            print(f"Game over! You ran {farm.name} for {year} years.")
            print(f"Final stats - Trees: {farm.trees}, Coffee: {farm.coffee:.2f} kg, Money: ${farm.money:.2f}")
            break
        else:
            print("Invalid action. Please choose plant, harvest, sell, or end.")

        year += 1

# Main game menu
def main_menu():
    games = [
        guess_the_number,
        math_challenge,
        adventure_game,
        word_scramble,
        memory_game,
        trivia_game,
        emoji_weather,
        coffee_farm_simulator
    ]

    while True:
        print("\nWelcome to the Timor-Leste Python Game Collection!")
        print("Choose a game to play:")
        for i, game in enumerate(games, 1):
            print(f"{i}. Unit {i}: {game.__name__.replace('_', ' ').title()}")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == '0':
            print("Thanks for playing! Goodbye!")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(games):
            games[int(choice)-1]()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()