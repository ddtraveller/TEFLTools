import sys
import math
import random

def buy(self):
    item = self.action_item
    volume = self.volume
    cost = int(self.prices[item]) * int(volume)
    if self.boat["money"] < self.prices[item]:
        self.TKresponse.set("You don't have enough money to buy that\nWhat would you like to buy?")
        self.action_item = ""
        self.entry.bind("<Return>", self.value_in)
        return
    elif item in self.wares:
        if self.volume == -1:
            upTo = afford(self, item)
            text = f"How many {item} would you like to buy?\nYou can buy up to {upTo}."
            self.TKresponse.set(text)
            self.entry.bind("<Return>", self.get_user_number)
        elif self.volume == 0:
            self.reset_input()
        elif self.boat["money"] < cost:
            budget = int(self.boat["money"]/self.prices[item])
            self.TKresponse.set("You don't have that much money.\nHow many would you like to buy?")
            self.volume = -1
            self.entry.bind("<Return>", self.get_user_number)
            return
        elif volume > self.boat['capacity'] - self.boat_fill():
            self.TKresponse.set("You don't have that much room left.\nHow many would you like to buy?")
            self.volume = -1
            self.entry.bind("<Return>", self.get_user_number)
        else:
            self.transaction("buy", self.action_item, self.volume)
            return
    else:
        text = f"I'm not sure about {item}, trader.\nWhat would you like to buy?"
        self.TKresponse.set(text)
        self.action_item = ""
        self.entry.bind("<Return>", self.value_in)

def afford(self, item):
    funds = self.boat["money"] / self.prices[item]
    funds = math.floor(funds)
    funds = int(funds)
    space = self.boat["capacity"] - self.boat_fill()
    if space < funds:
        return space
    return funds        	