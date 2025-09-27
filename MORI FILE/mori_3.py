import sys
import time
from colorama import Fore, Style

def print_slow(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0001)         #change always when testing to 0.0001

def left_path():

    print_slow("\nThe path continues going deeper into the Mori forest." 
               "\nThe path seems endless leading you only to a more shallow and dark place.")

    has_batteries = False

    while True:
        print_slow("\nWhile walking you spot something shining in the tall grass of the Mori Forest.")
        path = input("\nDo you stop? (yes/no): ")
        if path == "yes":
            flashlight = input("\nDo you check the long grass? (yes/no): ")
            if flashlight == "yes":
                print_slow("\nSearching.....with your hand......you find....................some used batteries.")
                has_batteries = True
                print_slow("\nAfter finding the batteries,"
                           "\nYou continue on which leads you to an old shallow bridge.")
                break
            elif flashlight == "no":
                print_slow("\nYou continue on which leads you to a old shallow bridge")
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
        bridge = input("\nDo you explore the shallow bridge? (yes/no): ")
        if bridge == "yes":
            if has_batteries:
                print_slow("\nYou explore under the shallow bridge and in a swamp of dirt with a grotesque smell, "
                           "while holding your nose you search the swamp finding a flashlight with missing batteries." 
                           "\nYou have the batteries, the stenching flashlight now works. This might come in handy later for you.")
                break

        elif bridge == "no":
            print_slow("\nYou continue on treading through the Mori Forest.")
            break

        else:
            print_slow("Invalid input. Please try again.")
            break

        return has_batteries

 #after name, once you thought of a way to use has_batteries enter it after like this: (name, has_batteries)

def left_path2(name):
    print_slow(f"\n{name}With the flashlight you go deeper into the Mori Forest. "
               "Not knowing where you are or what time it even is"
               "You continue hoping you can make it out of the Mori Forest. ")


        #add more loops here and dialogues to continue the story


def right_path():
    print_slow("\nThe loud silence of the Mori Forest makes you continue to be anxious,"
                       "by each second going deeper into the Mori Forest. You hear a river nearby,"
                       "the soothing sound of water calms you.")
    print_slow("\nYou go towards the soothing sound of the river.")


    while True:
        sign = input("\nYou see a fallen sign next to the river. Do you read it? (yes/no): ")
        if sign == "yes":
            print_slow("\nThe sign is old and rusty barely being to read the sign you can recognise only some letters."
                       "\n\nThe sign says ")
            print_slow(Fore.RED + "B..W..RE  OF  T..E   M..RI   F..R..S..T" + Style.RESET_ALL)
            print_slow("\nDisturbed you continue walking following the current of the river.")
            break
        elif sign == "no":
            print_slow("\nYou ignore the sign and continue walking following the current of the river.")
            break
        else:
            print("Invalid input. Please try again.")

        while True:
            current = input("\nAfter following the current you get to the end, finding a rusty farmhouse."
                        "\nDo you enter the farmhouse by the barn or the main door? (barn/main_door): ")

            if current == "barn":
                    print_slow("You enter the barn, the mud swarms your feet making each step of your's heavy."
                               "\nThe mud sticks your attention")
                    print(Fore.RED + "\n\n.....*creak*....." + Style.RESET_ALL)
                    print("\nWhat was that?")
                    print_slow("\n.....*silence*.....")
                    print_slow("\n\nYou look around searching for the sound")
                    break

            elif current == "main_door":
                    print_slow("\nYou enter the pitch black farmhouse, you stand still..."
                               "\nThe farmhouse is filled with a loud silence.")
                    setting = input("Something is in here with you"
                                        "Do you run out of the farmhouse or face the mystery that awaits you: (run/face)")
                    if setting == "run":
                       print_slow("\nYou try to run but the mud slows you down, "
                                   "making you trip hitting the mud face first")
                       break
                    elif setting == "face":
                        print_slow("\n")
                        break
                    else:
                        print("Invalid input. Please try again.")
            else:
                print("Invalid input. Please try again.")




def start():
    name = input("What is your name? ")
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

    print_slow("Welcome to Mori, " f"{name}" + "\n")
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
            if has_batteries:
                left_path2(name)
            break
        elif start1 == "right":
            has_batteries = right_path()
            break
        else:
            print("\nInvalid input. Please type 'left' or 'right'.")

if __name__ == "__main__":
    start()