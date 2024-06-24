# Instructions:
# Help the little python named "Py" escape a predator, find food, and a home!
# Follow the steps below to add functions and modules to the script.
# Each step will guide you through different aspects of functions and modules.
# Step 1: Call the "escape_predator" function in the main block to help Py escape from a predator.
# Step 2: Modify the "escape_predator" function to take a "predator" parameter and print the predator Py is escaping from.
# Step 3: Modify the "find_food" function to return the food that Py finds. Print the food in the main block.
# Step 4: Call the "build_home" function in the main block to help Py build a cozy home.
# Step 5: Modify the "build_home" function to take a "material" parameter and print the material Py uses to build the home.
# Step 6: Modify the "explore_surroundings" function to return the direction that Py explores. Print the direction in the main block.
# Step 7: Call the "make_friends" function in the main block to help Py make new friends.
# Step 8: Modify the "make_friends" function to take a "friend_name" parameter and print the name of Py's new friend.
# Step 9: Modify the "escape_predator" function to use the "random" module to randomly select the predator Py escapes from.
# Step 10: Modify the "explore_surroundings" function to use the "os" module to print the current working directory.

import random
import time
import math
import os
import datetime
import sys

def escape_predator(outcome='exit'):
   print("Py is being chased by a predator!")
   print("Quick, open this script in a text editor and go to Step 1 to save little Py!")
   time.sleep(1)
   if outcome == 'exit':
       sys.exit()
   print("Py quickly slithers into a narrow crevice and escapes.")
   time.sleep(1)
   print("Phew! That was close. Py is safe now.")

def find_food():
   print("Py is feeling hungry and needs to find some food.")
   time.sleep(1)
   food_options = ["mouse", "frog", "insect"]
   food = random.choice(food_options)
   time.sleep(1)
   # print('Py ate the ' + food)
   
def build_home(material):
    print("Py needs a place to rest and decides to build a home.")
    time.sleep(1)
    if material == 'stone':
       print('Py feels safe and secure in the stone home.')
    else:
        sys.exit()

def explore_surroundings():
   print("Py is curious and wants to explore the surroundings.")
   time.sleep(1)
   directions = ["north", "south", "east", "west"]
   direction = random.choice(directions)
   return direction

def make_friends():
   print("Py meets another friendly python.")
   time.sleep(1)
   print("Py and the other python become good friends and decide to travel together.")
   time.sleep(1)
   print("Having a companion makes the journey more enjoyable for Py.")

if __name__ == "__main__":
   print("Hello, World!")
   print("Meet Py, the little python who is about to embark on an exciting adventure!")
   time.sleep(2)

   # Step 1: Call the "escape_predator" function here by adding escape_predator() below. Remove the # to uncomment the line.
   # escape_predator()
   # Step 2: Change the outcome parameter to the "escape_predator" function to be 'safe' instead of 'exit'
   escape_predator(outcome='exit')
   # Step 3: Print the food that Py finds using the "find_food" function
   # uncomment the print('Py ate the ' + food) line
   find_food()
   
   # Step 4: Call the "build_home" function here
   # build_home('straw')
   
   # Step 5: Pass stone as the material parameter to the "build_home" function
   # build_home("stone")
   
   # Step 6: Print the direction that Py explores using the "explore_surroundings" function
   # direction=explore_surroundings()
   # print(direction)
   explore_surroundings()
   
   # Step 7: delete the sys.exit() line below.
   sys.exit()

   print("Congratulations! You've helped Py escape a predator, find food, build a home, explore the surroundings, and make new friends!")
   print("Py is grateful for your guidance and looks forward to more adventures together.")
   print("Keep learning and exploring the world of Python!")