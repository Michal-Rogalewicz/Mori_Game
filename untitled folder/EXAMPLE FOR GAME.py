import sys
import time
from colorama import Fore, Style

def print_slow(string, delay=0.02):
    """Print text with a typing effect."""
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    if not string.endswith("\n"):
        sys.stdout.write("\n")

def handle_left():
    """
    Left path logic.
    Returns True if the player picked up batteries, otherwise False.
    """
    print_slow("\nThe path continues going deeper into the Mori forest. "
               "The path seems endless leading you to a more shallow and dark place.")

    has_batteries = False

    while True:
        path = input("\nDo you go back? (yes/no): ").strip().lower()
        if path in ("yes", "y"):
            print_slow("\nWhile walking back you spot something shining in the tall grass of the Mori Forest.")
            flashlight = input("\nDo you check the long grass? (yes/no): ").strip().lower()
            if flashlight in ("yes", "y"):
                print_slow("\nYou put your hand in the long grass... you find some used batteries.")
                has_batteries = True
                print_slow("\nYou continue on which leads you to an old shallow bridge.")
                break
            elif flashlight in ("no", "n"):
                print_slow("\nYou continue on which leads you to an old shallow bridge.")
                break
            else:
                print("Invalid input. Please try again.")
                continue

        elif path in ("no", "n"):
            print_slow("\nYou continue on which leads you to an old shallow bridge.")
            break
        else:
            print("Invalid input. Please try again.")
            continue

    # Bridge inspection
    while True:
        bridge = input("\nDo you inspect the shallow bridge? (yes/no): ").strip().lower()
        if bridge in ("yes", "y"):
            if has_batteries:
                print_slow("\nYou inspect under the shallow bridge and find a flashlight (it needs batteries). "
                           "You already have batteries — that might come in handy later.")
            else:
                print_slow("\nYou inspect under the shallow bridge and find a flashlight with missing batteries.")
            break
        elif bridge in ("no", "n"):
            print_slow("\nYou continue on treading through the Mori Forest.")
            break
        else:
            print("Invalid input. Please try again.")
            continue

    return has_batteries

def handle_right():
    """
    Right path logic.
    Returns True/False depending on whether batteries were found (False by default).
    """
    print_slow("\nThe loud silence of the Mori Forest makes you anxious. "
               "You hear a river nearby; the sound calms you.")
    print_slow("\nYou go towards the soothing sound of the river.")

    while True:
        read_sign = input("\nYou see a fallen sign. Do you read it? (yes/no): ").strip().lower()
        if read_sign in ("yes", "y"):
            print_slow("\nThe sign says 'BEWARE THE MORI'. Odd...")
            break
        elif read_sign in ("no", "n"):
            print_slow("\nYou ignore the sign and keep walking.")
            break
        else:
            print("Invalid input. Please try again.")
            continue

    # Right path currently doesn't give batteries
    return False

def next_scene(name, has_batteries):
    """
    The single entry point after either path.
    Replace the contents of this function with your next piece of code.
    """
    print_slow(f"\n{name}, you arrive at the next area of the game.")
    if has_batteries:
        print_slow("You have batteries. If you use them with the flashlight you found, you might be able to see something important.")
    else:
        print_slow("You don't have batteries right now. A flashlight would be useless without them.")
    # TODO: put your new code here
    print_slow("\n--- NEXT SCENE (paste your new scene code inside next_scene) ---")

def main():
    name = input("What is your name? ").strip()
    while True:
        age = input("How old are you? ").strip()
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Invalid input. Enter a number.")

    if age < 16:
        print_slow(name + ", you aren't old enough to play this game.")
        return

    print("\nVERIFICATION COMPLETE")
    print(Fore.RED + r"""
 __  __   ___   ____   ___ 
|  \/  | / _ \ |  _ \ |_ _|
| |\/| || | | || |_) | | |
| |  | || |_| ||  _ <  | |
|_|  |_| \___/ |_| \_\|___|
""" + Style.RESET_ALL)

    print_slow("Welcome to Mori " + name + "\n")
    print("Let's Begin\n")

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
        "You are now lost in the darkness of the Mori Forest."
    )

    print_slow(f"\n{name}, your choices now will affect whether you make it back to your car.")

    # Choose path and capture whether batteries were found
    has_batteries = False
    while True:
        start = input("\nDo you take the left or right path? (left/right): ").strip().lower()
        if start == "left":
            has_batteries = handle_left()
            break
        elif start == "right":
            has_batteries = handle_right()
            break
        else:
            print("\nInvalid input. Please type 'left' or 'right'.")

    # Continue to the single next scene
    next_scene(name, has_batteries)

if __name__ == "__main__":
    main()
