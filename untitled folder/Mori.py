import sys
import time

def print_slow(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

name = input("What is your name? ")

while True:
    age = input("How old are you? ")
    if age.isdigit():
        age = int(age)
        break
    else:
        print_slow("Invalid input. Enter a number.")

if age < 16:
    print_slow(name + " you aren't old enough to play this game")
else:
    print("""
  __  __   ___   ____   ___ 
|  \/  | / _ \ |  _ \ |_ _|
| |\/| || | | || |_) | | | 
| |  | || |_| ||  _ <  | | 
|_|  |_| \___/ |_| \_\|___|
""")

    print_slow("Welcome to Mori " + name + "\n")
    print("Let's Begin\n")

    print_slow("""
"10%"
"20%"
"30"
"40%"
"50%"
"60%"
"70"
"80%"
"90%"
"100%
    """)

    print_slow(
            "\nYou check the time and realise its late, you start to go back to your car, "
            "taking the path back, "
            "the darkness got darker and you start to panic which led you to take a turn into a path, "
            "you've never been to. "
            "You are now lost in the darkness of the Mori Forest.")

    print_slow(f"\n{name}, your choices now will effect if you make it back to your car.")

    print_slow("\n\nYou are lost in the forest with darkness surrounding,"
            "the silence of the Mori is engulfing you. You have a path to the left and to your right. ")

    while True:
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
                    print("Invalid input. Please try again.")
                    break

        elif start == "right":
            print_slow("\nThe loud silence of the Mori Forest makes you continue to be anxious,"
                    "by each second going deeper into the Mori Forest. You hear a river nearby,"
                    "the soothing sound of waves makes you feel at peace calming your nerves.")
            print_slow("\nYou go towards the soothing sound of the river.")
            break
        else:
            print("\nInvalid input. Please type 'left' or 'right'.")
            break

