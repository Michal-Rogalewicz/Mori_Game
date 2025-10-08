import sys
import time
import random
from colorama import Fore, Style

def show_run_warning():

    sys.stdout.write("\033[0;31m")
    sys.stdout.flush()

    run = Fore.RED + Style.BRIGHT + r"""
    
██████  ██    ██ ███    ██ 
██   ██ ██    ██ ████   ██ 
██████  ██    ██ ██ ██  ██ 
██   ██ ██    ██ ██  ██ ██ 
██   ██  ██████  ██   ████ 

""" + Style.RESET_ALL

    print(run)
    time.sleep(1)

    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def maybe_whisper(name, inventory, chance=0.20):
    if random.random() >= chance:
        return
    whisper = ["\nYou feel something is watching you. ",
               "\nYou hear twigs snap.... nothing. ",
               "\nDistant sounds making you rethink what your hearing is real. "]
    if name:                                                                                          #remember to add this throughout the story
        whisper.append(f"\nThe wind brushes your ear" )
    msg = random.choice(whisper)
    print_slow(Fore.BLUE + msg + Style.RESET_ALL)

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

def ask(prompt, inventory = None):
    while True:
        choice = input(prompt)

        if choice in ('i', 'inventory'):
            if inventory is not None:
                show_inventory(inventory)
            else:
                print_slow("\nInventory:  (empty)\n")
            continue

        if choice:
            return choice

def start():
    name = input("What is your name? ")
    while True:
        age = input("\nWhat is your age? ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print(Fore.RED + "Invalid input. Enter a number." + Style.RESET_ALL)

    if age < 16:
        print_slow(name + ", you aren't old enough to play this game.")
        return

    print("\nVERIFICATION COMPLETE.")
    print(Fore.RED + r"""

                                                                                                                        ██████   ██████    ███████    ███████████   █████
                                                                                                                        ▒▒██████ ██████   ███▒▒▒▒▒███ ▒▒███▒▒▒▒▒███ ▒▒███ 
                                                                                                                        ▒███▒█████▒███  ███     ▒▒███ ▒███    ▒███  ▒███ 
                                                                                                                        ▒███▒▒███ ▒███ ▒███      ▒███ ▒██████████   ▒███ 
                                                                                                                        ▒███ ▒▒▒  ▒███ ▒███      ▒███ ▒███▒▒▒▒▒███  ▒███ 
                                                                                                                        ▒███      ▒███ ▒▒███     ███  ▒███    ▒███  ▒███ 
                                                                                                                        █████     █████ ▒▒▒███████▒   █████   █████ █████
                                                                                                                        ▒▒▒▒▒     ▒▒▒▒▒    ▒▒▒▒▒▒▒    ▒▒▒▒▒   ▒▒▒▒▒ ▒▒▒▒▒ 




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
        if start1 == "left":
            inventory_left = set()
            inventory_left = left_path(name, inventory_left)
            break

        elif start1 == "right":
            inventory_right = set()
            inventory_right = right_path(set())  # just for now have this later on change it
            break

        else:
            print(Fore.RED + "\nInvalid input. Please type 'left' or 'right'." + Style.RESET_ALL)


def left_path(name, inventory):
    print_slow("\nThe path continues going deeper into the Mori forest." 
               "\nThe path seems endless leading you only to a more shallow and dark place."
               "\nWhile walking you spot something shining in the tall grass of the Mori Forest.")

    maybe_whisper(name, inventory, chance=0.20)

    while True:
        path = ask("\nDo you stop? (yes/no): ", inventory)

        if path == "yes":
            batteries = ask("\nAre you sure you want to check the long grass? (yes/no): ", inventory)
            if batteries ==  "yes":
                if "batteries" not in inventory:
                    print_slow("\nSearching.....with your hand......you find....................some used batteries.")
                    inventory.add("batteries")
                print_slow("\nAfter finding the batteries,"
                           "\nYou continue on which leads you to an old shallow bridge.")
                break
            elif batteries == "no":
                print_slow("\nYou continue on which leads you to a old shallow bridge")
                break
            else:
                print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)
                continue

        elif path == "no":
            print_slow("\nYou continue on which leads you to a old shallow bridge.")
            break
        else:
            print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)
            continue

    while True:
        bridge = ask("\nDo you explore the shallow bridge? (yes/no): ", inventory)

        if bridge == "yes":
            print_slow("\nYou explore under the shallow bridge and in a swamp of dirt with a grotesque smell, "
                       "while holding your nose you search the swamp finding a flashlight with missing batteries. ")

            if "flashlight" not in inventory and "stenching flashlight" not in inventory:
                inventory.add("flashlight")
                print_slow("\nYou take the stenching flashlight. ")

            if "batteries" in inventory and "flashlight" in inventory and "stenching flashlight" not in inventory:
                inventory.discard("flashlight")
                inventory.discard("batteries")
                inventory.add("stenching flashlight")
                print_slow("\nYou have the batteries, the stenching flashlight now works. This might come in handy later for you. ")

            break

        elif bridge == "no":
            print_slow("\nYou continue on treading through the Mori Forest. ")
            break
        else:
            print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)
            continue

    inventory = left_path2(name, inventory)
    inventory = left_path3(name, inventory)
    return inventory

def left_path2(name, inventory):
    print_slow(f"\n{name} you go deeper into the Mori Forest. "
               "The air grows colder, you can tell its very late. "
               "Just hoping you can make it out")

    maybe_whisper(name, inventory, chance=0.20)

    if "stenching flashlight" in inventory:
        print_slow("\nThe working flashlight cuts through the darkness of the Mori Forest. "
                   "You spot with your flashlight claw mark along the trees. Something has been here recently."
                   "\nThe trail of claw marks continue, daring you to follow...")
        maybe_whisper(name, inventory, chance=1.00)
        claw = ask("\nDo you follow the claw marks or ignore them? (follow/ignore): ", inventory)
        if claw == "follow":
            print_slow("\nYou follow the claw marks and with each step the marks grow fresher. Suddenly, you hear rustling. "
                       "Your grip tightens on the flashlight. ")
            print_slow(Fore.RED + "\n...*rustle*...*snap*..." + Style.RESET_ALL)
            tense = ask("\nDo you shine your light at the sound or switch it off and hide? (shine/hide): ", inventory)
            if tense == "shine":
                print_slow("\nYou shine your flashlight in the darkness. Two pale eyes flash back-")
                time.sleep(1)
                show_run_warning()
                print_slow("\nIt's chasing you "
                           "\nYou bolt through the tress, your heart is pounding... "
                           "\nYou hear it's feet thumping behind, chasing you "
                           "\nYou can't outrun it "
                           "\nGasping for air you stop next to a bridge"
                           "\nThe "
                creature = ask("\nGasping for air you stop next to a bridge ? (yes/no): ", inventory)

        elif claw == "ignore":
            print_slow("\nYou choose not to tempt your own fate, walking away from the claw marked trail "
                       "\nThe Mori Forest grows eerily quiet as you continue forward. ")
        else:
            print(Fore.RED +"Invalid input. Please try again." + Style.RESET_ALL)
        return inventory

    if "flashlight" in inventory:
        inventory.add("flashlight")
        print_slow("You walk on with the non-working flashlight, clicking it again and again. "    
                   "Its nothing more than just dead weight. ")

    print_slow("\nYou stumble blindly in the darkness of the Mori Forest. Branches claw at your arms,"
               "and with each step feeling like it could lead you to a drop. "
               "The Mori Forest whispers around you, but you can't tell if its the wind... or the voices. ")

    while True:
        choice = ask("\nDo you keep moving forward or try searching around you for something that can be useful to you? (forward/search): ", inventory)
        if choice == "forward":
            print_slow("\nYou grit your teeth and press on, but each step sinks deeper into the mud. "
                   "Your heartbeat drowns out the silence of the Mori Forest. ")
            print_slow("\nYou keep on walking forward hoping you will spot some light. ")
            print_slow(Fore.RED +"\nYou trip"+ Style.RESET_ALL)
            print_slow(Fore.RED + "\n......." + Style.RESET_ALL)
            print_slow("\nYou look behind you" 
                   "\nTrying to view what made you trip" 
                   "\nA bag"
                   "\nYou check inside the bag"
                   "\nTo find a small pocket knife and some damp matches. ")

            if "pocket knife" not in inventory:
                inventory.add("pocket knife")
                print_slow("You now have a pocket knife. ")
                break
        elif choice == "search":
            print_slow("\nYou search around with your hands touching anything that resembles a item. "
                   "\nYou find some material it feels like it's a piece of cloth. ")

            if "strange cloth" not in inventory:
                inventory.add("strange cloth")
                if "stenching flashlight" in inventory:
                    print_slow("\nYou find a strange cloth with numbers written on it. ")
                    print(Fore.BLUE + "1003" + Style.RESET_ALL)
                    inventory.add("Code 1003")
                    inventory.discard("strange cloth")
                else:
                    print_slow("\nYou keep the strange cloth, though in this darkness you can't read what's on it. ")
            break

        else:
            print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)
            continue

    return inventory

def left_path3(name, inventory):
    print_slow("\nWhile treading through deeper into the Mori Forest you spot a tall figure. "
               "You walk towards to the tall figure that resembles a building of some sort. ")
    print_slow("\nAn abandoned watchtower. "
               "\nYou step closer, hearing the groan of old planks creaking from the wind. ")

    while True:
        watchtower = ask("\nDo you enter the watchtower or look around first? (enter/look_around): ", inventory)

        if watchtower == "look_around":
            print_slow("\nYou circle around the watchtower. "
                       "The ground is littered with broken glass, scraps and dirt. "
                       "Nothing worth your intrest. ")
            watchtower = "enter"

        if watchtower == "enter":
            print_slow("\nYou grip the splintered railing of the watchtower and start walking up. ")
            if "stenching flashlight" in inventory:
                print_slow("Your flashlight helps you get to the top safely dodging any cracks in the aged wooden stairs. "
                           "\nThe view steals your breath, all you see is an endless forest and a cold moon above you.")
                maybe_whisper(name, inventory, chance=0.20)
                print_slow("\nAn old cabin, you enter the cabin. "
                           "\nThe cabin is filled with dust. You spot a journal with your flashlight on the desk, you flip it open with one page being readable. "
                           "\nFollow the trail where the crows circle, the gate is guarded by a .... "
                           "\nA word is missing,looks like someone didn't have time to finish there journal"
                           "\nYou go down the watchtower, and continue till the end of the path. "
                           "\nThere it is"
                           "\nThe path being surrounded by crows ")
                inventory.add("Clue")
            else:
                print_slow("\nWith the darkness surrounding you every step is a mystery. "
                           "\nYou walk slowly up. "
                           "\nThe steps seem to creak more and more. "
                           "\nYou wonder what was the last time someone was up here. ")
                print_slow(Fore.RED + "\n\nCRACK" + Style.RESET_ALL)
                print_slow("\nYour foot breaks through one of the steps"
                           "\nYou grab the railings firmly ")
                creak = ask("Gasping for air do you continue to go up or do you go back down (up/down): ", inventory)
                if creak == "up":
                    print_slow("\nBrave"
                               "\nYou make it to the top safely, luck favours you. " 
                               "\nThe view steals your breath, all you see is an endless forest and a cold moon above you. "
                               "\nAn old cabin, you enter the cabin. ")

                    while True:
                        light = ask("\nThe cabin has a light switch do you turn on the light? (yes/no): ", inventory)
                        if light == "yes":
                            if "strange cloth" in inventory:
                                print_slow("\nYou take out the strange cloth, you picked up earlier, you can now read what was on it. ")
                                print_slow(Fore.BLUE + "\n1003" + Style.RESET_ALL)
                                print_slow("\nA code to something. ")
                                inventory.add("Code 1003")
                            else:
                                print_slow("\nThe dim bulb somehow turns on. You spot a journal on the desk, you flip it open with one page being readable. "
                                           "\nFollow the trail where the crows circle, the gate is guarded by a .... "
                                           "\nA word is missing like someone didn't have time to finish there journal"
                                           "\nYou go down the watchtower, and continue till the end of the path. "
                                           "\nThere it is"
                                           "\nThe path being surrounded by crows ")
                                inventory.add("Clue")
                            break
                        elif light == "no":
                            print_slow("\nYou can't make out anything in this darkness. ")
                            confirm = ask("Are you sure you don't want to turn on the light? (yes/no): ", inventory)
                            if confirm == "no":
                                continue
                            elif confirm == "yes":
                                print_slow("\nYou decide to stay in the dark, firm with your choice. "
                                           "Without any light you have no option but to go down the watchtower " 
                                           "and continue till the end of the path.")

                                break
                            else:
                                print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)
                                continue

                elif creak == "down":
                    print_slow("\nYou go down the stairs, frightened and continue till the end of the path. ")
                    break
                else:
                    print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)

    return inventory

def left_path4(inventory, name):
    if "Clue" in inventory:
        print_slow(Fore.BLUE + "\n" + name + Style.RESET_ALL + "There are two paths before you." )

    else:
        print_slow(Fore.BLUE + "\n" + name + Style.RESET_ALL + "There are two paths before you." )
        print_slow("\nOne path is surrounded by crows, their dark eyes and feathers camouflage them in the darkness of the Mori Forest. "
                   "The crows make you uneasy, without thinking you take the other path. ")

                   #Continue on


                                                        #ADD maybe_whisper(name, inventory, chance=0.20) TO THE RIGHT PATH

def right_path(inventory):
    print_slow("\nThe loud silence of the Mori Forest makes you continue to be anxious,"
               "by each second going deeper into the Mori Forest. You hear a river nearby,"
               "the soothing sound of water calms you.")
    print_slow("\nYou go towards the soothing sound of the river.")

    lantern_lit = False

    while True:
        sign = ask("\nYou see a fallen sign next to the river. Do you read it? (yes/no): ", inventory)

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
            print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)

    while True:
        print_slow("\nYou get to the end, finding a rusty farmhouse.")
        current = ask("\nDo you enter the farmhouse by the barn or the main door? (barn/main_door): ")

        if current == "barn":
            print_slow("You enter the barn, the mud swarms your feet making each step of your's heavy."
                       "\nThe mud sticks your attention")
            print(Fore.RED + "\n\n.....*creak*....." + Style.RESET_ALL)
            print("\nWhat was that?")
            print_slow("\n.....*silence*.....")
            print_slow("\n\nYou look around searching for the sound "
                           "\n\nNothing")
            print_slow("\nWhile searching you see something hidden in a pile of hay"
                       "Inside lays a small wooden box, long forgotten")

            open_box = ask("\nDo you open the small wooden box? (yes/no): ")

            if open_box == "yes":
                if "lighter" not in inventory:
                    print_slow("Inside you find a lighter, it looks well kept, "
                               "it must of been special to someone. ")
                    inventory.add("lighter")
                    print_slow("\nYou now have a lighter" )
                else:
                    print_slow("\nOnly dust remains in the box nothing else. ")

            elif open_box == "no":
                print_slow("You leave the box shut")
            else:
                print_slow(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)
            continue

        elif current == "main_door":
            print_slow("\nYou enter the pitch black farmhouse, you stand still..."
                       "\nThe farmhouse is filled with a loud silence.")
            main = ask("\nSomething is in here with you. Do you run or face the mystery? (run/face): ")

            if main == "run":
                print_slow("\nYou try to run but the mud makes your steps heavy making you trip, "
                           "making you hit the mud face first." )
                continue

            elif main == "face":
                if "lantern" not in inventory:
                    print_slow("\nYou face the the mystery,"
                               "just to see a dented lantern swaying gently from a coat rack." )
                    inventory.add("lantern")
                    print_slow("\nYou now have a lantern." )

                if not lantern_lit and "lantern" in inventory:
                    if "lighter" in inventory:
                        lighter_answer = ask("Light the lantern with the lighter? (yes/no): ", inventory)
                        if lighter_answer == "yes":
                            lantern_lit = True
                            print_slow("\nThe lamp's light pushes back the dark" )
                    else:
                        print_slow("\nYou need something to ignite the lamp" )

                print_slow("\nWith the lamp you delve deeper into the house, through the eerie hall, "
                           "which leads you to discover an old office." )

                if lantern_lit:
                    if "map" not in inventory:
                        print_slow("\nEntering the office with the luminous lantern reveals a desk. "
                                   "Inside the desk you find a odd map. "
                                   "\nThe map shows a path near the farmhouse that will lead you to the... ")
                        print_slow(Fore.RED + "Mill Tunnel" + Style.RESET_ALL)
                        inventory.add("map")
                        print_slow("\nYou now have a map")
                    else:
                        print_slow("\nNothing else to take, you already took the map.")

                else:
                    print_slow("\nWithout any light you can't seem to pick anything out. ")

                if lantern_lit and "map" in inventory:
                    print_slow("\nWith the map and your lit lantern, you go back outside. "
                               " Following the map heading towards the Mill Tunnel.")
                    return inventory
                continue
        else:
            print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    start()