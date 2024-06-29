import sys
import math
import random
import json

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
        self.cities = ['Dili Harbor', 'Baucau Cove', 'Suai Bay', 'Oecusse Port', 'Atauro Isle', 'Com Anchorage', 'Jaco Island']
        self.current_city = 0
        self.turn = 1
        self.prices = {item['name']: item['cost'] for item in self.goods}
        self.debt = 0
        self.bank_balance = 0

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

    def update_prices(self):
        for item in self.goods:
            self.prices[item['name']] = int(item['cost'] * random.uniform(0.5, 1.5))

        if random.random() < 0.2:
            special_item = random.choice(self.goods)['name']
            if random.random() < 0.5:
                self.prices[special_item] = int(self.prices[special_item] * 0.5)
                print(f"The price of {special_item} has dropped significantly!")
            else:
                self.prices[special_item] = int(self.prices[special_item] * 2)
                print(f"The price of {special_item} has risen dramatically!")

    def display_status(self):
        print(f"\nTurn: {self.turn}")
        print(f"Current Port: {self.cities[self.current_city]}")
        print(f"Gold: {self.money}")
        print(f"Debt: {self.debt}")
        print(f"Bank Balance: {self.bank_balance}")

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
        self.update_prices()
        print(f"Sailed to {self.cities[self.current_city]}")

        if random.random() < 0.2:
            self.pirate_attack()
        elif random.random() < 0.1:
            self.offer_ship_upgrade()

    def pirate_attack(self):
        enemy_ship = random.choice(self.ships)
        print(f"You're under attack by a {enemy_ship['name']} with {enemy_ship['guns']} guns!")
        action = input("Do you want to (f)ight or (r)un? ").lower()
        if action == 'f':
            if self.guns > enemy_ship['guns']:
                damage_chance = self.maneuverability / (self.maneuverability + enemy_ship['maneuverability'])
                if random.random() < damage_chance:
                    damage = random.randint(1, self.guns)
                    enemy_ship['guns'] -= damage
                    print(f"You've damaged the enemy ship! They now have {enemy_ship['guns']} guns.")
                else:
                    print("You've missed!")
                if enemy_ship['guns'] <= 0:
                    print("You've defeated the pirates!")
                    self.money += enemy_ship['cost'] // 2
                    print(f"You've gained {enemy_ship['cost'] // 2} gold as booty!")
                else:
                    damage = random.randint(1, enemy_ship['guns'])
                    self.ship_health -= damage
                    print(f"The enemy ship has damaged your ship! Your ship health is now {self.ship_health}%.")
                    if self.ship_health <= 0:
                        print("Your ship has sunk. Game Over!")
                        exit()
            else:
                print("You're outgunned! You have no choice but to flee.")
                self.run_away(enemy_ship)
        else:
            self.run_away(enemy_ship)

    def run_away(self, enemy_ship):
        if self.speed > enemy_ship['speed']:
            print("You've managed to escape!")
        else:
            print("The enemy ship is faster than you! You can't escape.")
            damage = random.randint(1, enemy_ship['guns'])
            self.ship_health -= damage
            print(f"The enemy ship has damaged your ship! Your ship health is now {self.ship_health}%.")
            if self.ship_health <= 0:
                print("Your ship has sunk. Game Over!")
                exit()
            cargo_lost = random.randint(0, sum(self.inventory.values()) // 2)
            print(f"You lost {cargo_lost} units of random cargo.")
            while cargo_lost > 0:
                item = random.choice(list(self.inventory.keys()))
                if self.inventory[item] > 0:
                    self.inventory[item] -= 1
                    cargo_lost -= 1

    def offer_ship_upgrade(self):
        upgrade_cost = self.ships[self.ships.index(next(ship for ship in self.ships if ship['name'] == self.ship_type)) + 1]['cost'] - self.ships[self.ships.index(next(ship for ship in self.ships if ship['name'] == self.ship_type))]['cost']
        print(f"You've been offered a ship upgrade to {self.ships[self.ships.index(next(ship for ship in self.ships if ship['name'] == self.ship_type)) + 1]['name']} for {upgrade_cost} gold.")
        if input("Do you want to upgrade? (y/n) ").lower() == 'y':
            if self.money >= upgrade_cost:
                self.money -= upgrade_cost
                self.ship_type = self.ships[self.ships.index(next(ship for ship in self.ships if ship['name'] == self.ship_type)) + 1]['name']
                self.ship_capacity = self.ships[self.ships.index(next(ship for ship in self.ships if ship['name'] == self.ship_type))]['capacity']
                self.ship_health = 100
                self.guns = self.ships[self.ships.index(next(ship for ship in self.ships if ship['name'] == self.ship_type))]['guns']
                self.speed = self.ships[self.ships.index(next(ship for ship in self.ships if ship['name'] == self.ship_type))]['speed']
                self.maneuverability = self.ships[self.ships.index(next(ship for ship in self.ships if ship['name'] == self.ship_type))]['maneuverability']
                print(f"Ship upgraded to {self.ship_type}!")
            else:
                print("Not enough gold for the upgrade.")

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
    
    def play(self):
        print("Welcome to Timor-Leste Fantasy Trader!")
        self.update_prices()
        while True:
            self.display_status()
            if self.current_city == 0:  # Dili Harbor
                self.dili_harbor_options()
            action = input("\nWhat would you like to do? (buy/sell/travel/quit): ").lower()
            if action == 'quit':
                break
            elif action == 'buy':
                self.buy()
            elif action == 'sell':
                self.sell()
            elif action == 'travel':
                self.travel()
            else:
                print("Invalid action!")
    
        print(f"Game over! Final gold: {self.money}")
    
if __name__ == "__main__":
    game = TimorLesteFantasyTrader()
    game.play()