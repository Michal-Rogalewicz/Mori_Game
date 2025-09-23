import sys
import time
from colorama import Fore, Style

def print_slow(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0001)

def left_path():

    print_slow("\n The path continues going deeper into the Mori forest." 
            "The path seems endless leading you only to a more shallow and dark place.")

    has_batteries = False

    while True:
        path = input("\nDo you stop? (yes/no): ")
        if path == "yes":
            print_slow("\nWhile walking back you spot something shining in the tall grass of the Mori Forest.")
            flashlight = input("\nDo you check the long grass? (yes/no): ")
            if flashlight == "yes":
                print_slow("\nSearching.....with your hand..... you find.......... some used batteries.")
                has_batteries = True
                print_slow("\nYou continue on which leads you to an old shallow bridge.")
                break
            elif flashlight == "no":
                print_slow("You continue on which leads you to a old shallow bridge")
                break
            else:
                print("Invalid input. Please try again.")
                continue

        elif path == "no":
            print_slow("\nYou continue on which leads you to a old shallow bridge.")
            break
        else:
            print("Invalid input. Please try again.")
            continue

    while True:
        bridge = input("\nDo you inspect the shallow bridge? (yes/no): ")
        if bridge == "yes":
            if has_batteries:
                print_slow("\nYou inspect under the shallow bridge and in a swamp of dirt with a grotesque smell, "
                        "you search finding a flashlight with missing batteries." 
                        "\nYou have the batteries, the stenching flashlight now works. This might come in handy late for you")
                break

        elif bridge == "no":
            print_slow("\nYou continue on treading through the Mori Forest.")
            break

        else:
            print_slow("Invalid input. Please try again.")
            break

        return has_batteries

def right_path():
    print_slow("\nThe loud silence of the Mori Forest makes you continue to be anxious,"
                    "by each second going deeper into the Mori Forest. You hear a river nearby,"
                    "the soothing sound of waves makes you feel at peace calming your nerves.")
    print_slow("\nYou go towards the soothing sound of the river.")

    return False

def left_path2(name, has_batteries):
    print_slow("\nWith the flashlight you go deeper into the Mori Forest. "
               "Not knowing where you are or what time it even is"
               "You continue jhk"


def start():
    name = input("\nWhat is your name? ")
    while True:
        age = input("\nWhat is your age? ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Invalid input. Enter a number.")

    if age < 16:
        print_slow(name + ", you aren't old enough to play this game.")
        return

    print("\nVERIFICATION COMPLETE.")
    print(Fore.RED + r"""
                                                    __  __   ___   ____   ___
                                                   |  \/  | / _ \ |  _ \ |_ _|
                                                   | |\/| || | | || |_) | | |
                                                   | |  | || |_| ||  _ <  | |
                                                   |_|  |_| \___/ |_| \_\|___|
    """ + Style.RESET_ALL)

    print_slow("Welcome to Mori" + name + "\n")
    print("Lets Begin\n")

    print_slow(Fore.RED + """
"10%"
"20%"
"30%"
"40%"
"50%"
"60%"
"70%"
"80%"
"90%"
"100%"
""" + Style.RESET_ALL)

    print_slow(
        "\nYou check the time and realise it's late, you start to go back to your car, "
        "taking the path back, the darkness got darker and you start to panic which led you to take a turn into a path you've never been to. "
        "You are now lost in the darkness of the Mori Forest.")

    print_slow(f"\n{name}, your choices now will effect if you make it back to your car.")

    while True:
        start1 = input("\nDo you take the left or right path? (left/right): ")
        if start1 == "left":
            has_batteries = left_path()
            break
        elif start1 == "right":
            has_batteries = right_path()
            break
        else:
            print("\nInvalid input. Please type 'left' or 'right'.")

    if __name__ == "__main__":
        start()