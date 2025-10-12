import sys, time, random, shutil, re
from colorama import Fore, Style

Player_Name = None
Player = ""

Locations = ["Mori Forest", "watchtower", "cave", "boardwalk", "waterfall", "Mill Tunnel",
             "farmhouse", "river", "shallow bridge", "cabin", "office", "altar", "barn"]

def print_slow(text):
    for loc in Locations:
        pattern = rf"\b{re.escape(loc)}\b"
        text = re.sub(pattern, lambda m: Fore.GREEN + m.group(0) + Style.RESET_ALL, text, flags=re.IGNORECASE)

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0001)  #change always when testing to 0.0001

def glitch_text(message = "THING", flickers = 25):
    glitch_chars = ["#", "%", "!", "?", "$"]
    for _ in range(flickers):
        clear_screen()
        glitched = ""
        for text in message:
            glitched += random.choice(glitch_chars) if text != " " and random.random() < 0.35 else text
        print(Fore.RED + Style.BRIGHT + glitched + Style.RESET_ALL)
        time.sleep(random.uniform(0.05, 0.15))
    clear_screen()
    print(Fore.RED + Style.BRIGHT + message + Style.RESET_ALL)
    time.sleep(1.5)
    clear_screen()

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def print_centered_block(block: str, color=Fore.RED, bright=True):
    cols, rows = shutil.get_terminal_size((80, 24))
    lines = block.strip("\n").splitlines()
    width = max(len(line) for line in lines)
    left_pad = max((cols - width) // 2, 0)
    top_pad = max((rows - len(lines)) // 2, 0)
    sys.stdout.write("\n" * top_pad)
    style = (Style.BRIGHT if bright else "") + color
    for line in lines:
        sys.stdout.write(" " * left_pad + style + line + Style.RESET_ALL + "\n")
    sys.stdout.flush()

def maybe_whisper(name, inventory, chance=0.1):
    if random.random() >= chance:
        return
    whisper = ["\nYou feel something is watching you. ",
               "\nYou hear twigs snap.... nothing. ",
               "\nDistant sounds making you rethink what your hearing is real. ",
               "\nYou hear footsteps, perfectly in sync with yours...",
               "\nThe forest wind humming, almost like the Forest is alive. "]
    if name:
        whisper.append(f"\nThe wind brushes your ear" )
    print_slow(Fore.BLUE + random.choice(whisper) + Style.RESET_ALL)

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

def show_run_warning(duration=2.0):
    run = Fore.RED + Style.BRIGHT + r"""
░█████████  ░██     ░██ ░███    ░██ 
░██     ░██ ░██     ░██ ░████   ░██ 
░██     ░██ ░██     ░██ ░██░██  ░██ 
░█████████  ░██     ░██ ░██ ░██ ░██ 
░██   ░██   ░██     ░██ ░██  ░██░██ 
░██    ░██   ░██   ░██  ░██   ░████ 
░██     ░██   ░██████   ░██    ░███ 
    """ + Style.RESET_ALL
    clear_screen(); print_centered_block(run); time.sleep(duration); clear_screen()

def mori_loading_screen():
    mori = r"""
░███     ░███   ░██████   ░█████████  ░██████
░████   ░████  ░██   ░██  ░██     ░██   ░██  
░██░██ ░██░██ ░██     ░██ ░██     ░██   ░██  
░██ ░████ ░██ ░██     ░██ ░█████████    ░██  
░██  ░██  ░██ ░██     ░██ ░██   ░██     ░██  
░██       ░██  ░██   ░██  ░██    ░██    ░██  
░██       ░██   ░██████   ░██     ░██ ░██████                                    
    """

    for i in range (10, 101, 10):
        clear_screen()
        block = mori + f'\n"{i}%"'
        print_centered_block(block, color =Fore.RED, bright=True)
        time.sleep(0.25)
    clear_screen()

def start():
    global Player
    name = ask("What is your name? ")
    Player = name
    while True:
        age = ask("\nWhat is your age? ")
        if not age.isdigit():
            print(Fore.RED + "Invalid input. Enter a number." + Style.RESET_ALL)
            continue

        age = int(age)
        if age > 100:
            print(Fore.RED + "Don't just give a random number!" + Style.RESET_ALL)

            continue
        if age < 16:
            print_slow(name + ", you aren't old enough to play this game.")
            return

        break

    mori_loading_screen()
    print_slow("Welcome to Mori, " f"{name}" + "\n")
    print("Lets Begin\n")

    print_slow("\nYou check the time and realise it's late, you start to go back to your car, "
               "taking the path back, the darkness got darker and you start to panic which led you to take a turn into a path you've never been to. "       
               "You are now lost in the darkness of the Mori Forest.")
    print_slow(f"\n{name}, your choices now will effect if you make it back to your car.")

    inventory = set()
    inventory = left_path(name, inventory)
    return


def left_path(name, inventory):
    print_slow("\nThe path continues going deeper into the Mori forest." 
               "\nThe path seems endless leading you only to a more shallow and dark place."
               "\nWhile walking you spot something shining in the tall grass of the Mori Forest.")
    maybe_whisper(name, inventory, chance=0.3)

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

    if "Route" in inventory:
        inventory.discard("Route")
        return inventory

    inventory = left_path3(name, inventory)
    return inventory

def left_path2(name, inventory):
    print_slow(f"\n{name} you go deeper into the Mori Forest. "
               "The air grows colder, you can tell its very late. "
               "Just hoping you can make it out")
    maybe_whisper(name, inventory, chance=0.3)

    if "stenching flashlight" in inventory:
        print_slow("\nThe working flashlight cuts through the darkness of the Mori Forest. "
                   "You spot with your flashlight claw mark along the trees. Something has been here recently."
                   "\nThe trail of claw marks continue, daring you to follow...")
        maybe_whisper(name, inventory, chance=1)

        while True:
            claw = ask("\nDo you follow the claw marks or ignore them? (follow/ignore): ", inventory)
            if claw == "follow":
                print_slow("\nYou follow the claw marks and with each step the marks grow fresher. Suddenly, you hear rustling. "
                           "Your grip tightens on the flashlight. ")
                print_slow(Fore.RED + "\n...*rustle*...*snap*..." + Style.RESET_ALL)
                while True:
                    tense = ask("\nDo you shine your light at the sound or switch it off and hide? (shine/hide): ", inventory)
                    if tense == "shine":
                        print_slow("\nYou shine your flashlight in the darkness. Two pale eyes flash back-")
                        time.sleep(0.75)
                        show_run_warning(duration=2)
                        print_slow("\nIt's chasing you. "
                                   "\nYou bolt through the tress, your heart is pounding... "
                                   "\nYou hear it's feet thumping behind, chasing you. "
                                   "\nIt feel's like you've been running for hours. "
                                   "\nYou can't outrun it. "
                                   "\nGasping for air you stop next to a waterfall and boardwalk. "
                                   "\nThe waterfall drop looks deadly. "
                                   "\nThe boardwalk is stale and rocky. "
                                   "\nThe rustling from the Mori Forest is getting closer. "
                                   "\nYou have to make a choice, " + name)

                        while True:
                            creature = ask("\nDo you try to cross the boardwalk or do you jump down the waterfall hoping you survive? (cross/jump): ", inventory)
                            if creature == "cross":
                                print_slow("\nYou start trotting gently hoping you can make it to the other side of the boardwalk. "
                                           "\nSlowly..."
                                           "\nStep by step..."
                                           "\nThen..." )
                                print_slow(Fore.RED + "\n*THUD*...*THUD*...*THUD*..." + Style.RESET_ALL)
                                time.sleep(1)
                                print_slow("\nIts behind you. It crashes through the tress, it's claws scraping anything in it's way. ")
                                time.sleep(1)
                                print_slow("\nYou look back. The two pale eyes glint in the dark, closer now too close. "
                                           "\nThe boardwalk starts shaking violently ")
                                time.sleep(1)
                                show_run_warning(duration=3)
                                print_slow(Fore.RED + "\nIt's approaching you, " + Style.RESET_ALL)
                                time.sleep(1)
                                print_slow(name + " make a choice ")
                                escaping = ask("\nDo you jump or run? (jump/run): ", inventory)
                                if escaping == "jump":
                                    print_slow("\nYou jump from the boardwalk.  "
                                               "Falling...")
                                    time.sleep(3)
                                    print_slow("\nYou wake up, washed ashore. "
                                               "\nYour left hand is fractured. "
                                               "\nThe agony strikes.")
                                    time.sleep(1)
                                    glitch_text("\nAAAHHHHHHHHH" , flickers=15)
                                    print_slow("\nYou clench your wrist hoping the pain stops "
                                               "\nYour flashlight is gone, you must of lost it in the water. ")
                                    inventory.discard("stenching flashlight")
                                    inventory.add("broken left hand")

                                    inventory = cave_scene(name, inventory)
                                    inventory.add("Route")
                                    return inventory

                                elif escaping == "run":
                                    print_slow("\nYou dash forward, the planks crack beneath your feet. "
                                               "\nIt starts chasing you")
                                    print_slow("\nYou leap off the final plank as the whole boardwalk breaks down "
                                               "\nYour flashlight falls from your pocket"
                                               "\nYou tumble into the grass. "
                                               "\nYou look back.... the boardwalk is gone and so was it. "
                                               "\nDid it fall with the boardwalk? ")
                                    inventory.discard("stenching flashlight")

                                    inventory = left_path3(name, inventory)
                                    inventory.add("Route")
                                    return inventory

                                else:
                                    print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)

                            elif creature == "jump":
                                print_slow("\nYou take a deep breath and leap into the roaring waterfall. ")
                                time.sleep(1)
                                print_slow("\nCold water engulfs you, it's freezing, pulling you down violently. ")
                                print_slow(Fore.RED + "*THUMP*" + Style.RESET_ALL)
                                time.sleep(2)
                                print_slow("\nYou wake up, washed ashore you have a lump on the back of your head. "
                                           "\nIt sting's when you touch it. "
                                           "\nYour flashlight is gone, you must of lost it in the water. ")
                                inventory.discard("stenching flashlight")
                                inventory = cave_scene(name, inventory)
                                inventory.add("Route")
                                return inventory

                            else:
                                print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)

                    elif tense == "hide":
                                print_slow("\nYou click the flashlight off and crouch low next to the trees"
                                           "\nYou press your back against a tree, holding your breath ")
                    time.sleep(1)
                    maybe_whisper(name, inventory, chance=1)

                    print_slow(Fore.RED + "\n...*crack*" + Style.RESET_ALL)
                    print_slow("\nSomething heavy is stepping through the bushes.Slow. Searching. ")
                    time.sleep(1)

                    stealth=ask("\nDo you not move a muscle or throw a small pebble to distract it? (throw/dont_move): ", inventory)
                    if stealth == "throw":
                        print_slow("\nYou feel around the dirt, trying to pick up the small pebble. You flick it into the dark-far to your right. ")
                        print_slow(Fore.RED + "\n...*snap*... *scrape*" + Style.RESET_ALL)
                        time.sleep(5)

                        if random.random() < 0.6:
                            print_slow("\nIt turns. It shoves through the branches, chasing the sound."
                                       "\nYou exhale. Keeping your breathing quiet.")
                            time.sleep(3)
                            print_slow("\nYou start creeping along the treeline, keeping low, keeping quiet.")

                        else:
                            print_slow("\nIt stops. The forest is dead still ")
                            print_slow(Fore.RED + "\nYou hear it inhale. Closer." + Style.RESET_ALL)
                            maybe_whisper(name, inventory, chance=1)
                            glitch_text("DON'T MOVE", flickers=10)
                            print_slow("\nYou freeze and start trembling.Then-")
                            print_slow(Fore.RED + "\n...*THUD*..." + Style.RESET_ALL)
                            print_slow("\nIt surges the other way, shoving through the branches. Maybe it sensed something else... or lost intrest. ")

                    elif stealth == "dont_move":
                        print("Yo")

                    else:
                        print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)

                    print_slow("\nYou've waited a while now, your fear disappears "
                              "\nYou finally move on, avoiding the claw marked trees")
                    time.sleep(1)
                    print_slow("\nWhile treading through deeper into the Mori Forest you spot a tall figure. ")
                    print_slow(Fore.BLUE + "\nA watchtower" + Style.RESET_ALL)

                    inventory = left_path3(name, inventory)
                    inventory.add("Route")
                    return inventory

            elif claw == "ignore":
                print_slow("\nYou choose not to tempt your own fate, walking away from the claw marked trail "
                           "\nThe Mori Forest grows eerily quiet as you continue forward. ")

                maybe_whisper(name, inventory, chance=0.3)

            else:
                print(Fore.RED +"Invalid input. Please try again." + Style.RESET_ALL)
            return inventory

    if "flashlight" in inventory:
        inventory.add("flashlight")
        print_slow("You walk on with the non-working flashlight, clicking it again and again. "
                   "Its nothing more than just dead weight. ")
        inventory.discard("flashlight")

    print_slow("\nYou stumble blindly in the darkness of the Mori Forest. Branches claw at your arms,"
               "and with each step feeling like it could lead you to a drop. "
               "The Mori Forest whispers around you, but you can't tell if its the wind... or the voices. ")

    maybe_whisper(name, inventory, chance=0.3)

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

                maybe_whisper(name, inventory, chance=0.2)

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
        maybe_whisper(name, inventory, chance=0.2)
        print_slow("\nOne path is surrounded by crows, their dark eyes and feathers camouflage them in the darkness of the Mori Forest. "
                   "The crows make you uneasy, without thinking you take the other path. ")

def left_path5(inventory, name):
    print("(Example")

def cave_scene(name, inventory):
    maybe_whisper(name, inventory, chance=0.5)

    print_slow("\nYou check your surroundings "
               "\nHappy that thing left you alone. "
               "\nYou approach a cave with lamps lit up with fire that dazzles your eyes. "
               "\nSomeone must of been here not long ago. "
               "\nYou take cautious steps inside, the echo of dripping water echoing throughout the cave.")
    print_slow("You steep even deeper into the cave."
               "The lamps continue on and on "
               "The walls have symbols written on them, spirals, eyes, "
               "and a crude depiction of a creature with too many limbs. "
               "The tunnels opens into a vast underground chamber. "
               "Dozens of burnt out candles circle a stone altar. "
               "Something is covered with cloth, and the smell... it's unbearable.")

    investigate = ask("\nDo you uncover what's on the altar? (yes/no): ", inventory)
    if investigate == "yes":
        print_slow("\nYour shaking hands pull back the cloth... "
                   "A mirror, cracked and blackened, stares back - your reflection twisted smiling. "
                   "A voice whispers")
        glitch_text("YOU WON'T EVER LEAVE", flickers=10)
        print_slow("\nYou kick the mirror disturbed at what you just saw. "
                   "\nThe reflection is gone, it's been replaced by your horrified face")
        inventory.add("Mirror Fragment")
    elif investigate == "no":
        print_slow("\nYou back away from the altar, refusing to see what lies beneath the cloth. ")
    else:
        print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)
    print_slow("\nYou retreat toward's the caves entrance.")
    return inventory

def cave_scene2(name, inventory):
    print_slow("\nThere is a river next to the waterfall,"
               "the soothing sound of water calms you.")
    print_slow("\nYou go towards the soothing sound of the river.")
    maybe_whisper(inventory, chance=0.2)

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
                    print_slow("\nYou now have a lighter")
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
                           "making you hit the mud face first.")
                continue
            elif main == "face":
                if "lantern" not in inventory:
                    print_slow("\nYou face the the mystery,"
                               "just to see a dented lantern swaying gently from a coat rack.")
                    inventory.add("lantern")
                    print_slow("\nYou now have a lantern.")
                if not lantern_lit and "lantern" in inventory:
                    if "lighter" in inventory:
                        lighter_answer = ask("Light the lantern with the lighter? (yes/no): ", inventory)
                        if lighter_answer == "yes":
                            lantern_lit = True
                            print_slow("\nThe lamp's light pushes back the dark")
                    else:
                        print_slow("\nYou need something to ignite the lamp")
                print_slow("\nWith the lamp you delve deeper into the house, through the eerie hall, "
                           "which leads you to discover an old office.")
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
                               "You follow the map heading towards the Mill Tunnel.")
                    return inventory
                continue
        else:
            print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    start()