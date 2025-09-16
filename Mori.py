name = input("What is your name? ")
age = input("How old are you? ")
if age >= str(16):
    print("Welcome to MORI", name)
else:
    print("You aren't old enough to play this game", name)
    quit()

print("Lets Begin\n")

import time
import sys

def print_slow(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

print_slow(
    "You check the time and realise its late, you start to go back to your car, "
    "taking the path back, "
    "the darkness got darker and you start to panic which led you to take a turn into a path, "
    "you've never been to. "
    "You are now lost in the darkness of the Mori Forest.")

print_slow(f"\n{name}, your choices now will effect if you make it back to your car.")

print_slow("\n\nYou are lost in the forest with darkness surrounding,"
           "the silence of the Mori is engulfing you. You have a path to the left and to your right. ")

start = input("\nDo you take the left or right path? ")
if start == "left":
    print_slow("\nThe path continues going deeper into the Mori forest." 
    "The path seems endless leading you only to a more shallow and dark place.")
while True:
    path = input("\nDo you go back? (yes/no): ")
    if path == "yes":
        print_slow("\nYou return to the first two paths fatigued by the Mori Forest.")
        break
    elif path == "no":
        print_slow("\nYou continue on which leads you to a old shallow bridge.")
        break
    else:
        print_slow("Invalid input. Please try again.")
