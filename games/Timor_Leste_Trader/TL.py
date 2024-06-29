import json
import random
from utils import generate_response, update_prices, pirate_attack, offer_ship_upgrade, trigger_random_event

class TimorLesteFantasyTrader:
    def __init__(self):
        with open('json/goods.json', 'r') as f:
            self.goods = json.load(f)
        with open('json/ships.json', 'r') as f:
            self.ships = json.load(f)
        self.inventory = {item['name']: 0 for item in self.goods}
        self.ship_type = 'Pinnace'
        self.ship_capacity = 100
        self.ship_health = 100
        self.guns = 1
        self.speed = 6
        self.maneuverability = 8
        self.cities = [
            'Dili Harbor', 'Baucau Cove', 'Suai Bay', 'Oecusse Port', 'Atauro Isle', 
            'Jaco Island', 'Liquica Port', 'Manatuto Bay', 'Lautem Cove'
        ]
        self.current_city = 0
        self.turn = 1
        self.prices = {item['name']: item['cost'] for item in self.goods}
        self.debt = 0
        self.bank_balance = 0
        self.morale = 100
        self.reputation = 0
        self.money = 0
        self.luxury_food_items = ['Timorese coffee beans', 'Sugar', 'Palm wine', 'Salt']
        self.basic_food_items = ['Rice', 'Corn', 'Salted fish', "Sailor's rations", "Low Quality sailor's rations"]

        print("Choose your starting condition:")
        print("1. Start with 5 guns and no money")
        print("2. Start with 1000 gold and 2000 gold debt")
        choice = input("Enter 1 or 2: ")
        if choice == '1':
            self.money = 0
            self.guns = 5
        else:
            self.money = 1000
            self.debt = 2000

    def handle_hunger(self):
        if self.turn % 3 == 0:
            food_consumed = False
            morale_change = 0

            # Check for luxury food items first
            for item in self.luxury_food_items:
                if self.inventory[item] > 0:
                    self.inventory[item] -= 1
                    food_consumed = True
                    morale_change = 5
                    print(f"Crew consumed 1 {item}. Morale increased!")
                    break
            
            # If no luxury food, check for basic food items
            if not food_consumed:
                for item in self.basic_food_items:
                    if self.inventory[item] > 0:
                        self.inventory[item] -= 1
                        food_consumed = True
                        print(f"Crew consumed 1 {item}.")
                        break
            
            # If no food at all, decrease morale
            if not food_consumed:
                morale_change = -10
                print("No food available! Crew morale decreased significantly.")

            self.update_morale(morale_change)

    def update_morale(self, change=0):
        self.morale = min(100, max(0, self.morale + change + (self.ship_health - 50) / 10 + (self.guns - 5) / 2 - self.debt / 1000))
        if sum(self.inventory.values()) / self.ship_capacity > 0.8:
            self.morale += 5
        if self.money > 10000:
            self.morale += 5
        if self.debt > 5000:
            self.morale -= 5

    def display_status(self):
        print(f"\nTurn: {self.turn}")
        print(f"Current Port: {self.cities[self.current_city]}")
        print(f"Gold: {self.money}")
        print(f"Debt: {self.debt}")
        print(f"Bank Balance: {self.bank_balance}")
        print(f"Crew Morale: {self.morale:.2f}%")
        print(f"Reputation: {self.reputation}")

        # Display food items and their quantities
        print("\nFood Supplies:")
        for item in self.luxury_food_items + self.basic_food_items:
            if self.inventory[item] > 0:
                print(f"{item}: {self.inventory[item]}")

        # Display top 3 items by price
        top_items = sorted(self.prices.items(), key=lambda x: x[1], reverse=True)[:3]
        print("\nTop 3 items by price:")
        for i, (item, price) in enumerate(top_items):
            print(f"{i+1}. {item} - {price} gold")

        # Display bottom 3 items by price
        bottom_items = sorted(self.prices.items(), key=lambda x: x[1])[:3]
        print("\nBottom 3 items by price:")
        for i, (item, price) in enumerate(bottom_items):
            print(f"{i+1}. {item} - {price} gold")

        # Display prices for items in the player's inventory
        print("\nPrices for items in your inventory:")
        for item, amount in self.inventory.items():
            if amount > 0:
                print(f"{item} - {self.prices[item]} gold")

        print(f"\nShip Type: {self.ship_type}")
        print(f"Ship Health: {self.ship_health}%")
        print(f"Guns: {self.guns}")
        print(f"Speed: {self.speed}")
        print(f"Maneuverability: {self.maneuverability}")
        print(f"Capacity: {self.ship_capacity - sum(self.inventory.values())}/{self.ship_capacity}")

    def buy(self):
        print("\nItems available for purchase:")
        for i, item in enumerate(self.goods):
            print(f"{i+1}. {item['name']} - {self.prices[item['name']]} gold")
        choice = int(input("Enter the number of the item you want to buy (0 to cancel): ")) - 1
        if choice == -1 or choice >= len(self.goods):
            return
        item = self.goods[choice]['name']
        amount = int(input(f"How many {item} would you like to buy? "))
        cost = self.prices[item] * amount
        if cost > self.money:
            print("Not enough gold!")
            return
        if amount > self.ship_capacity - sum(self.inventory.values()):
            print("Not enough capacity!")
            return
        self.money -= cost
        self.inventory[item] += amount
        print(f"Bought {amount} {item} for {cost} gold")

    def sell(self):
        print("\nItems available for sale:")
        items_to_sell = [item for item in self.inventory.items() if item[1] > 0]
        for i, (item, amount) in enumerate(items_to_sell):
            print(f"{i+1}. {item} (x{amount}) - {self.prices[item]} gold each")
        if not items_to_sell:
            print("You have nothing to sell!")
            return
        choice = int(input("Enter the number of the item you want to sell (0 to cancel): ")) - 1
        if choice == -1 or choice >= len(items_to_sell):
            return
        item = items_to_sell[choice][0]
        amount = int(input(f"How many {item} would you like to sell? "))
        if amount > self.inventory[item]:
            print("Not enough inventory!")
            return
        revenue = self.prices[item] * amount
        self.money += revenue
        self.inventory[item] -= amount
        print(f"Sold {amount} {item} for {revenue} gold")

    def travel(self):
        print("\nWhere would you like to sail?")
        for i, city in enumerate(self.cities):
            if i != self.current_city:
                print(f"{i+1}. {city}")
        choice = int(input("Enter the number of your destination: ")) - 1
        if choice == self.current_city or choice < 0 or choice >= len(self.cities):
            print("Invalid choice!")
            return
        self.current_city = choice
        self.turn += 1
        update_prices(self)
        print(f"Sailed to {self.cities[self.current_city]}")

        if random.random() < 0.2:
            pirate_attack(self)
        elif random.random() < 0.1:
            offer_ship_upgrade(self)

    def dili_harbor_options(self):
        while True:
            print("\nDili Harbor Special Options:")
            print("1. Repair ship")
            print("2. Visit money lender")
            print("3. Visit shipyard")
            print("4. Visit bank")
            print("5. Return to main menu")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.repair_ship()
            elif choice == '2':
                self.money_lender()
            elif choice == '3':
                self.shipyard()
            elif choice == '4':
                self.bank()
            elif choice == '5':
                break
            else:
                print("Invalid choice!")

    def repair_ship(self):
        repair_cost = (100 - self.ship_health) * self.ships[self.ships.index(next(ship for ship in self.ships if ship['name'] == self.ship_type))]['cost'] // 100
        print(f"Repairing your ship will cost {repair_cost} gold.")
        if input("Do you want to repair? (y/n) ").lower() == 'y':
            if self.money >= repair_cost:
                self.money -= repair_cost
                self.ship_health = 100
                print("Ship fully repaired!")
            else:
                print("Not enough gold for repairs.")

    def money_lender(self):
        print(f"Current debt: {self.debt}")
        action = input("Do you want to (b)orrow or (r)epay? ").lower()
        if action == 'b':
            max_borrow = max(0, self.money * 2 - self.debt)
            amount = int(input(f"How much do you want to borrow? (max {max_borrow}): "))
            if amount <= max_borrow:
                self.money += amount
                self.debt += int(amount * 2)
                print(f"Borrowed {amount} gold. Current gold: {self.money}, Current debt: {self.debt}")
            else:
                print("You can't borrow that much!")
        elif action == 'r':
            amount = int(input(f"How much do you want to repay? (max {min(self.money, self.debt)}): "))
            if amount <= self.money and amount <= self.debt:
                self.money -= amount
                self.debt -= amount
                print(f"Repaid {amount} gold. Current gold: {self.money}, Current debt: {self.debt}")
            else:
                print("Invalid repayment amount!")

    def shipyard(self):
        print("\nWelcome to the shipyard!")
        print("1. Upgrade/Exchange ship")
        print("2. Buy guns")
        print("3. Return to Dili Harbor")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.upgrade_ship()
        elif choice == '2':
            self.buy_guns()
        elif choice == '3':
            return
        else:
            print("Invalid choice!")

    def upgrade_ship(self):
        print("\nAvailable ships:")
        for i, ship in enumerate(self.ships):
            print(f"{i+1}. {ship['name']} - {ship['cost']} gold")
        choice = int(input("Enter the number of the ship you want to upgrade/exchange to (0 to cancel): ")) - 1
        if choice == -1:
            return
        ship = self.ships[choice]
        if self.money >= ship['cost']:
            self.money -= ship['cost']
            self.ship_type = ship['name']
            self.ship_capacity = ship['capacity']
            self.ship_health = 100
            self.guns = ship['guns']
            self.speed = ship['speed']
            self.maneuverability = ship['maneuverability']
            print(f"Congratulations! You now have a {self.ship_type}.")
        else:
            print("You don't have enough gold to purchase this ship.")

    def buy_guns(self):
        print(f"\nYou currently have {self.guns} guns.")
        gun_cost = 1000
        max_guns = min(self.money // gun_cost, self.ships[self.ships.index(next(ship for ship in self.ships if ship['name'] == self.ship_type))]['guns'] - self.guns)
        amount = int(input(f"How many guns do you want to buy? (max {max_guns}): "))
        if amount > max_guns:
            print("You can't buy that many guns!")
            return
        cost = gun_cost * amount
        self.money -= cost
        self.guns += amount    
        print(f"You bought {amount} guns for {cost} gold.")

    def bank(self):
        print(f"Current bank balance: {self.bank_balance}")
        action = input("Do you want to (d)eposit or (w)ithdraw? ").lower()
        if action == 'd':
            amount = int(input(f"How much do you want to deposit? (max {self.money}): "))
            if amount <= self.money:
                self.money -= amount
                self.bank_balance += amount
            else:
                print("You don't have that much gold!")
        elif action == 'w':
            amount = int(input(f"How much do you want to withdraw? (max {self.bank_balance}): "))
            if amount <= self.bank_balance:
                self.money += amount
                self.bank_balance -= amount
            else:
                print("You don't have that much in your account!")

    def parrot_speak(self):
        inventory_fullness = sum(self.inventory.values()) / self.ship_capacity * 100
        wealth = self.money + self.bank_balance - self.debt

        prompt = f"""The ship's condition is as follows:
        - Ship Health: {self.ship_health}%
        - Guns: {self.guns}
        - Inventory Fullness: {inventory_fullness:.2f}%
        - Wealth: {wealth} gold
        - Crew Morale: {self.morale:.2f}%

        Based on this information, give a brief assessment of the situation."""

        parrot_message = generate_response(prompt)
        return f"The ship's parrot squawks: {parrot_message}"

    def play(self):
        print("Welcome to Timor-Leste Fantasy Trader!")
        update_prices(self)
        while True:
            self.display_status()
            if self.current_city == 0:  # Dili Harbor
                self.dili_harbor_options()
            
            if self.turn % 10 == 0:
                print(self.parrot_speak())
            
            self.handle_hunger()  # Call the hunger system every turn
            
            # Trigger random event with 20% probability
            if random.random() < 0.2:
                trigger_random_event(self)
            
            print("\nWhat would you like to do?")
            print("1. Buy goods")
            print("2. Sell goods")
            print("3. Travel")
            print("4. Quit")
            
            action = input("Enter your choice (1-4): ")
            
            if action == '1':
                self.buy()
            elif action == '2':
                self.sell()
            elif action == '3':
                self.travel()
            elif action == '4':
                break
            else:
                print("Invalid action! Please choose a number between 1-4.")
            
            self.turn += 1
    
        print(f"Game over! Final gold: {self.money}")

if __name__ == "__main__":
    game = TimorLesteFantasyTrader()
    game.play()