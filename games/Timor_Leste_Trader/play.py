import sys
import math
import random
import tkinter as tk
import tkinter.messagebox as tkm
from buy import *
from sell import *

def proper_name(item):
    first = item[0].upper()
    output = first + item[1:len(item)]
    return output

def play(self):
    if self.volume == -999:
        self.initialize()
    else:
        self.TKupdate()
        self.TKresponse.set('What do you want to do?')
        self.entry.bind("<Return>", self.value_in)

def move(self):
    action = self.action
    action_item = self.action_item
    self.TKupdate()
    if self.boat_fill() == 0 and self.boat['money'] == 0:
        self.TKresponse.set("You have no money and no goods, you lose!")
    elif action == "":
        self.entry.bind("<Return>", self.value_in)
    elif action == "sail":
        self.TKresponse.set("Time to travel!\nWhere to, trader?")
        self.entry.bind("<Return>", self.get_user_number)
    elif action[0] == "s":
        self.action = "sell"
        action = "sell"
        if action_item == "":
            self.TKresponse.set("What would you like to sell?")
            self.entry.bind("<Return>", self.value_in)
        else:
            self.entry.bind("<Return>", sell(self))
            self.entry.delete(0, tk.END)
    elif action[0] == "b":
        self.action = "buy"
        action = "buy"
        if action_item == "":
            self.TKresponse.set("What would you like to buy?")
            self.entry.bind("<Return>", self.value_in)
        else:
            self.entry.bind("<Return>", buy(self))
            self.entry.delete(0, tk.END)
    elif action == 'quit' or action == 'q':
        text = f"I knew you weren't cut out for trading in Timor-Leste, {self.player_name}!"
        self.TKresponse.set(text)
    else:
        self.TKresponse.set("That's not a valid action here.\nIf you need help, just ask!")
        self.action = ""
        self.action_item = ""
        self.entry.bind("<Return>", self.value_in)
    return

def bigger_boat(self):
    new_capacity = int(self.boat["capacity"] * 2)
    cost = new_capacity * 25
    if self.boat["money"] > cost:
        text = f"Would you like to increase your transport capacity by {new_capacity} for {cost} money?"
        if tkm.askyesno("Upgrade Transport", text):
            self.boat["money"] -= cost
            self.boat["capacity"] += new_capacity
            self.TKupdate()
    return