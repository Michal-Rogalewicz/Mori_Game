import sys
import time
from colorama import Fore, Style

def print_slow(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0001)         #change always when testing to 0.0001

def show_inventory(inventory):
    if inventory:
        print_slow(f"\nInventory: {', '.join(sorted(inventory))}\n")
    else:
        print_slow("\nInventory:  (empty)\n")

def ask (prompt):
    """Lets player check inventory."""
    while True:
        choice = input(prompt)
        if choice in {'i',"inventory"}:
            return "_SHOWN_INVENTORY_"
        return choice

def left_path(inventory):

    print_slow("\nThe path continues going deeper into the Mori forest." 
               "\nThe path seems endless leading you only to a more shallow and dark place.")

    while True:
        print_slow("\nWhile walking you spot something shining in the tall grass of the Mori Forest.")
        path = ask("\nDo you stop? (yes/no): ")

        if path == "_SHOWN_INVENTORY_":
            show_inventory(inventory)
            continue

        if path == "yes":
            batteries = ask("\nDo you check the long grass? (yes/no): ")
            if batteries == "_SHOWN_INVENTORY_":
                show_inventory(inventory)
                continue

            if batteries ==  "yes":
                if "batteries" not in inventory:
                    print_slow("\nSearching.....with your hand......you find....................some used batteries.")
                    inventory.add("batteries")
                else:
                    print_slow("\nAfter finding the batteries,"
                               "\nYou continue on which leads you to an old shallow bridge.")
                    break
            elif batteries == "no":
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
        bridge = ask("\nDo you explore the shallow bridge? (yes/no): ")

        if bridge == "_SHOWN_INVENTORY_":
            show_inventory(inventory)
            continue

        if bridge == "yes":
            print_slow("\nYou explore under the shallow bridge and in a swamp of dirt with a grotesque smell, "
                       "while holding your nose you search the swamp finding a flashlight with missing batteries.")

            if "flashlight" not in inventory:
                inventory.add("flashlight")
                print_slow("\nYou take the stenching flashlight")

            elif "batteries" in inventory and "flashlight" not in inventory:
                inventory.discard("flashlight")
                inventory.discard("batteries")
                inventory.add("flashlight")
                print_slow("\nYou have the batteries, the stenching flashlight now works. This might come in handy later for you.")

            break

        elif bridge == "no":
            print_slow("\nYou continue on treading through the Mori Forest.")
            break
        else:
            print_slow("Invalid input. Please try again.")
            break

    return inventory

def left_path2(name,inventory):
    print_slow(f"\n{name} you go deeper into the Mori Forest. "
               "The air grows colder, you can tell its very late. "
               "Just hoping you can make it out")

    if "working flashlight" in inventory:
        print_slow("\nThe working flashlight cuts through the darkness of the Mori Forest. "
                   "You spot with your flashlight claw mark along the trees. Something has been here recently."
                   "\nThe trail of claw marks continue, daring you to follow...")
        claw = ask("\nDo you follow the claw marks or ignore them? (follow/ignore): ")
        if claw == "follow":
            print_slow("\nYou follow the claw marks and with each step the marks grow fresher. Suddenly, you hear rustling. "
                       "Your grip tightens on the flashlight. ")
        elif claw == "ignore":
            print_slow("\nYou choose not to tempt your own fate, walking away from the claw marked trail"
                       "The Mori Forest grows eerily quiet as you continue forward. ")

    elif "flashlight" in inventory:
        print_slow("You walk on with the non-working flashlight, clicking it again and again. "
                   "Its nothing more than just dead weight. ")

    else:
        print_slow("\nYou stumble blindly in the darkness of the Mori Forest. Branches claw at your arms,"
                   "and with each step feeling like it could lead you to a drop"
                   "The Mori Forest whispers around you, but you can't tell if its the wind... or the voices. ")

        choice = ask("\nDo you keep moving forward or try searching around you for something that can be useful to you? (forward/search): ")

        if choice == "_SHOWN_INVENTORY_":
            show_inventory(inventory)
            return left_path2(name, inventory)

        if choice == "forward":
            print_slow("\nYou grit your teeth and press on, but each step sinks deeper into the mud. "
                       "Your heartbeat drowns out the silence of the Mori Forest. ")

            print_slow("\nYou keep on walking forward hoping you will spot some light")
            print_slow(Fore.RED +"\nYou trip"+ Style.RESET_ALL)
            print_slow(Fore.RED + "\n......." + Style.RESET_ALL)
            print_slow("\nYou look behind you" 
                       "\nTrying to view what made you trip" )
            print_slow("\nA bag"
                       "\nYou check inside the bag"
                       "\nTo find a small pocket knife and some damp matches")
            if "pocket knife" not in inventory:
                inventory.add("pocket knife")
                print_slow("You have now a pocket knife")

        elif choice == "search":
            print_slow("\nYou search around with your hands touching anything that resembles a item"
                       "You find some material, "
                       "it looks like some cloth and there is something written on it but you can't tell what in this darkness")

            if "strange cloth" not in inventory:
                inventory.add("strange cloth")
                print_slow("\nYou keep the strange cloth, though it's meaning is unclear")

    return inventory #continue on more with your code

def right_path():
    print_slow("\nThe loud silence of the Mori Forest makes you continue to be anxious,"
               "by each second going deeper into the Mori Forest. You hear a river nearby,"
               "the soothing sound of water calms you.")
    print_slow("\nYou go towards the soothing sound of the river.")

    while True:
        sign = ask("\nYou see a fallen sign next to the river. Do you read it? (yes/no): ")

        if sign == "_SHOWN_INVENTORY_":
            show_inventory(inventory)
            continue

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
            current = ask("\nAfter following the current you get to the end, finding a rusty farmhouse."
                          "\nDo you enter the farmhouse by the barn or the main door? (barn/main_door): ")

            if current == "_SHOWN_INVENTORY_":
                show_inventory(inventory)
                continue

            if current == "barn":
                    print_slow("You enter the barn, the mud swarms your feet making each step of your's heavy."
                               "\nThe mud sticks your attention")
                    print(Fore.RED + "\n\n.....*creak*....." + Style.RESET_ALL)
                    print("\nWhat was that?")
                    print_slow("\n.....*silence*.....")
                    print_slow("\n\nYou look around searching for the sound"
                               "Nothing")
                    print_slow("\nWhile searching you see something hidden in a pile of hay"
                               "Inside lays a small wooden box, long forgotten")

                    open_box = ask("\nDo you open the small wooden box? (yes/no): ")
                    if open_box == "_SHOWN_INVENTORY_":
                        show_inventory(inventory)
                        continue

                    if open_box == "yes":
                        if "lighter" not in inventory:
                            print_slow("Inside you find a lighter, it looks well kept, "
                                       "it must of been special to someone. ")
                            inventory.add("lighter")
                            print_slow("\nYou have now a lighter" )
                            break
                    elif open_box == "no":
                        print_slow("You leave the box shut")
                        break
                    else:
                        print_slow("\nInvalid input. Please try again.")
                    continue

            elif current == "main_door":
                    print_slow("\nYou enter the pitch black farmhouse, you stand still..."
                               "\nThe farmhouse is filled with a loud silence.")
                    setting = ask("Something is making a noise"
                                  "Do you run out of the farmhouse or face the mystery that awaits you: (run/face)")

                    if setting == "_SHOWN_INVENTORY_":
                        show_inventory(inventory)
                        continue

                    if setting == "run":
                       print_slow("\nYou run out of the farmhouse")  #change this bit cause it don't really make sense
                       break
                    elif setting == "face":
                        if "lantern" not in inventory:
                            print_slow("\nYou face the sound creeping towards it ")
                            print_slow("\nA oil lantern dangling from a coat rack, being swayed gently by the wind. "
                                       "You take it with you. ")
                            inventory.add("lantern")
                            print_slow("\nYou now have a lantern")
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
        start1 = ask("\nDo you take the left or right path? (left/right): ")
        if start1 == "_SHOWN_INVENTORY_":
            print_slow("\nInventory: (empty)\n")
            continue

        if start1 == "left":
            inventory_left = set()
            inventory_left = left_path(inventory_left)
            if "working flashlight" in inventory_left:
                left_path2(name, inventory_left)
            break

        elif start1 == "right":
            inventory_right = set()
            inventory_right = right_path(inventory_right)
            break

        else:
            print("\nInvalid input. Please type 'left' or 'right'.")

if __name__ == "__main__":
    start()