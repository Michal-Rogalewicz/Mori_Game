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

    print_slow("\nYou check the time and realise it's late, you start to go back to the beginning of the Mori Forest, "
               "taking the path back, the darkness got darker and you start to panic which led you to take a turn into a path you've never been to. "       
               "You are now lost in the darkness of the Mori Forest.")
    print_slow(f"\n{name}, your choices now will effect if you make it out alive.")

    inventory = set()
    inventory = path1(name, inventory)
    return


def path1(name, inventory):
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

    inventory = path2(name, inventory)
    inventory = path3(name, inventory)
    inventory = path4(inventory, name)
    return inventory

def path2(name, inventory):
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
                                    inventory = cave_scene2(name, inventory)
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
                        print_slow("\nYou stay perfectly still, your body trembling but frozen in place. "
                                   "\nYou can hear your heartbeat, pounding."
                                   "\nYou feel its presence inches behind you.")
                        time.sleep(2)
                        print_slow("\nYou dare not to move a muscle."
                                   "\nEvery instinct screaming to move, but you stay frozen. ")
                        maybe_whisper(name, inventory, chance=1)
                        print_slow("\nWhatever it was, it's gone... for now. ")

                    else:
                        print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)

                    print_slow("\nYou've waited a while now, your fear disappears "
                              "\nYou finally move on, avoiding the claw marked trees")
                    time.sleep(1)
                    print_slow("\nWhile treading through deeper into the Mori Forest you spot a tall figure. ")
                    print_slow(Fore.BLUE + "\nA watchtower" + Style.RESET_ALL)

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

def path3(name, inventory):
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

def path4(inventory, name):
    print_slow(Fore.BLUE + f"\n{name}" + Style.RESET_ALL + " There are two paths before you. One is circled with crows, the other is dark and quiet.")
    maybe_whisper(name, inventory, chance=0.3)

    if "Clue" in inventory:
        print_slow("\nYou remember the journal line: 'Follow the trail where the crows circle...'")
    else:
        print_slow("\nYou have no clear hint. You trust your gut.")

    choice = ask("\nWhich path do you take? (crows/not_crows):", inventory)
    print_slow("\nAs you step forward, the world tightens. The trees close in and something huge approaches you in the dark.")
    time.sleep(1)
    show_run_warning(2)

    if choice == "crows":
        print_slow("\nYou run through the birds they burst up in the sky like a black cloud.")
        time.sleep(1)
        print_slow("\nThe crows scattering draws attention of something. A shape surges out, it's him.")
        if "Flare Gun" in inventory and "flare" in inventory:
            if "broken left hand" in inventory:
                print_slow("\nYour injured hand trembles. Aiming is hard.")
                if random.random() < 0.45:
                    print_slow("\nYou fire the flare. It streaks wide but still erupts into a violent bloom of light.")
                else:
                    print_slow("\nYour shot sails. The flare lights the trees but misses the creature.")
                inventory.discard("flare")
            else:
                print_slow("\nYou aim and fire. The flare blossoms overhead, bathing the clearing in angry light.")
                inventory.discard("flare")
                print_slow("\nThe creature hurt and stumbles back, blinded and distraught.")
        else:
            print_slow("\nYou have nothing to light the sky.")

        if "Mirror Fragment" in inventory:
            print_slow("\nYou hold the Mirror Fragment up. Light catches the attention of the fragment and reveals a keypad by the gate.")
        else:
            print_slow("\nThere is a glint where a mirror could have reflected light.")

        if "Code 1003" in inventory:
            print_slow("\nYou dash to the keypad and punch in the numbers you memorised: 1003.")
            time.sleep(0.6)
            print_slow(Fore.GREEN + "\nThe locks inside the gate clack, it starts to open." + Style.RESET_ALL)
            print_slow("\nThe pathway clears just as the creature lunges. You wrench yourself through the gap.")
            print_slow("\nYou stagger onto a moonlit road. Headlights approach; someone has seen the flare. You're saved.")
            print_slow(Fore.BLUE + "\nENDING: " + Style.RESET_ALL + "Saved by signal and quick thinking.")
            return inventory
        else:
            print_slow("\nThe gate is stuck shut and there's no code. You need to force it.")
            if "pocket knife" in inventory:
                print_slow("\nYou jam your pocket knife into a rusty hinge and lever it like hell.")
                if random.random() < (0.7 if "broken left hand" not in inventory else 0.4):
                    print_slow("\nThe hinge gives. The gate creaks open and you tumble through as the creature slams into the metal.")
                    print_slow(Fore.BLUE + "\nENDING: " + Style.RESET_ALL + "A desperate escape — you live.")
                    return inventory
                else:
                    print_slow("\nYour injured hand fails you — the knife slips. The creature grabs at you.")
                    show_run_warning(2)
                    glitch_text("YOU CAN'T RUN", flickers=8)
                    print_slow(Fore.RED + "\nENDING: " + Style.RESET_ALL + "Caught.")
                    return inventory
            else:
                if "Flare Gun" in inventory:
                    print_slow("\nYou swing the Flare Gun like a club and manage to stagger it long enough to slip away.")
                    print_slow(Fore.BLUE + "\nENDING: " + Style.RESET_ALL + "Bruised and bleeding, you survive by sheer luck.")
                    return inventory
                print_slow("\nYou have no tool. The creature tears into your world.")
                show_run_warning(2)
                glitch_text("DARKNESS", flickers=6)
                print(Fore.RED + "\nENDING: " + Style.RESET_ALL + "Taken in the shadows.")
                return inventory

    else:
        print_slow("\nYou take the quieter path. The air grows cold and the trees press close.")
        time.sleep(0.6)
        print_slow("\nSomething moves behind you. The two pale eyes flash at you again. The chase begins.")
        stumble_penalty = 0.4 if "broken left hand" in inventory else 0.15

        print_slow("\nYou reach an old rope barrier tied across a narrow path. If you cut it you can slip through, otherwise you'll have to climb.")
        cut_choice = ask("\nDo you cut the rope or try to climb over it?, (cut/climb): ", inventory)
        if cut_choice == "cut" and "pocket knife" in inventory:
            print_slow("\nYou draw your pocket knife and saw through the rope. It snaps free and you slip through the gap.")
        else:
            if random.random() < (0.3 + stumble_penalty):
                print_slow("\nYou slip while climbing, scraping your palms and losing time.")
                show_run_warning(2)
            else:
                print_slow("\nYou climb up to the top without a problem.")

        print_slow("\nThe tunnel seperates. To the left, a rusted door with a small lock. To the right, a shaft.")
        fork = ask("\nWhich do you try? (door/shaft): ", inventory)
        if fork == "door":
            if "Code 1003" in inventory:
                print_slow("\nYou punch 1003 into the lock. It trembles and gives with a groan.")
                if "Flare Gun" in inventory and "flare" in inventory:
                    print_slow("\nYou fire the flare through a cracked window. The flare bursts into the night.")
                    inventory.discard("flare")
                    print_slow(Fore.BLUE + "\nENDING: " + Style.RESET_ALL + "The signal brings rescue, you collapse into safety.")
                    return inventory
                print_slow(Fore.BLUE + "\nENDING: " + Style.RESET_ALL + "You survive to walk another day, shaken but alive.")
                return inventory
            else:
                if "pocket knife" in inventory:
                    print_slow("\nYou pry the lock with the knife. The door opens.")
                    show_run_warning(2)
                    print_slow(Fore.BLUE + "\nENDING: " + Style.RESET_ALL + "A desperate last-minute escape — you live.")
                    return inventory
                print_slow("\nYou can't open it.It closes in.")
                glitch_text("RUN", flickers=8)
                print(Fore.RED + "\nENDING: " + Style.RESET_ALL + "Overwhelmed in the dark.")
                return inventory
        else:
            print_slow("\nYou wedge the Mirror Fragment into your palm and angle it at the shaft.")
            if "Mirror Fragment" in inventory:
                print_slow("\nThe shard sends a thin beam of reflected moonlight down the shaft, catching a hanging chain.")
                print_slow("\nYou yank the chain; it rattles and drops a rusted ladder into a hidden alcove. You climb down.")
                if "Flare Gun" not in inventory:
                    inventory.add("Flare Gun")
                    inventory.add("flare")
                    print_slow("\nIn the shed you find a Flare Gun and one flare. It might save you yet.")
            else:
                print_slow("\nYou have nothing reflective. The noise behind you grows louder.")
                show_run_warning(2)
                print_slow(Fore.RED + "\nENDING: " + Style.RESET_ALL + "Captured in the shaft of the forest.")
                return inventory

            if "flare" in inventory:
                print_slow("\nYou have one last flare. You kneel and fire it skyward.")
                inventory.discard("flare")
                print_slow(Fore.BLUE + "\nENDING: " + Style.RESET_ALL + "Rescued by chance and the flare you found. You live to tell the tale.")
                return inventory
            print_slow(Fore.BLUE + "\nENDING: " + Style.RESET_ALL + "Alive, but changed forever.")
            return inventory


def cave_scene(name, inventory):
    maybe_whisper(name, inventory, chance=0.5)

    if "broken left hand" in inventory:
        print_slow("\nYour " + Fore.RED + "broken left hand" + Style.RESET_ALL +
                   " throbs painfully with each step.")

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
    print_slow("\nYou drag yourself along the current of the river, soaked and shivering.")
    print_slow("\nYou follow the current, hoping it might lead you out of the Mori Forest.")

    if "broken left hand" in inventory:
        print_slow("\nThe pain in your " + Fore.RED + "broken left hand" + Style.RESET_ALL +
                   " feels worse and worse, making you weaker by each second.")

    print_slow("\nYou get to the end, finding a rusty farmhouse."
               "\nYou enter the barn, the mud swarms your feet making each step of your's heavy."
               "\nThe mud sticks your attention")
    print_slow("\nWhile searching you see something hidden in a pile of hay"
               "\nInside lays a small wooden box, long forgotten")
    open_box = ask("\nDo you open the small wooden box? (yes/no): ", inventory)
    if open_box == "yes":
        if "lighter" not in inventory:
            print_slow("Inside you find a lighter, it looks well kept, "
                       " it must of been special to someone. ")
            inventory.add("lighter")
            print_slow("\nYou now have a lighter. ")
        else:
            print_slow("\nOnly dust remains in the box. ")
    elif open_box == "no":
            print_slow("You leave the box shut. ")
    else:
        print_slow(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)

    print_slow("\nYou leave the barn and enter the farmhouse,"
               "\nSomething is swaying around in the farmhouse."
               "\nYou check it out just to see a dented lantern swaying gently from a coat rack.")
    if "Lighted Lantern" not in inventory and "lantern" not in inventory:
        inventory.add("lantern")
        print_slow("\nYou now have a lantern. ")

    if "lighter" in inventory and "lantern" in inventory and "Lighted Lantern" not in inventory:
        print_slow("\nYou light the lantern with your lighter. ")
        inventory.discard("lighter")
        inventory.discard("lantern")
        inventory.add("Lighted Lantern")
        print_slow("\nYou now have a lighted lantern that glows through the darkness.")

    if "Lighted Lantern" in inventory:
        print_slow("\nWith the lamp you delve deeper into the farmhouse, through the eerie hall, "
                   " which leads you to discover an old office.")
        print_slow("\nEntering the office with the luminous lantern reveals a desk. "
                   "Inside the desk you find a odd map. ")
        if "map" not in inventory:
            inventory.add("map")
            print_slow("\nYou now have a map. ")
            print_slow("\nThe map shows a path near the farmhouse that will lead you to the... ")
            print_slow(Fore.RED + "Mill Tunnel" + Style.RESET_ALL)

        print_slow("\nWith the map and your lantern lit, you go back outside. "
                   "\nYou follow the map heading towards the Mill Tunnel.")
        return mill_tunnel(name, inventory)

    print_slow("\nYou step back outside with a lantern, it has no use to you, you throw it away. "
               "\nYou step back into the Mori Forest"
               "\nWith nothing to guide your journey, you can only wander around till you find something. "
               "\nAfter a while, you finally stumble across two paths.")

    inventory.discard("lantern")
    path4(inventory, name)
    return inventory

def mill_tunnel(name, inventory):
    print_slow("\nFollowing the map's trail. ")
    sign = ask("\nYou see a fallen sign. Do you read it? (yes/no): ", inventory)
    if sign == "yes":
        print_slow("\nThe sign is old and rusty barely being to read the sign you can recognise only some letters."
                   "\n\nThe sign says ")
        print_slow(Fore.RED + "B..W..RE  OF  T..E   M..LL   T..NN..L" + Style.RESET_ALL)
        print_slow("\nDisturbed you continue walking.")
    elif sign == "no":
        print_slow("\nYou ignore the sign and continue walking. ")
    else:
        print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)

    print_slow("\nYou have arrived " + name + " at the Mill Tunnel. ")
    print_slow("\nYou step inside. Water drips from the ceiling."
               "\nThe passage narrows."
               "\nA corroded warning plate on the wall."
               "\nYou read it. ")
    print_slow(Fore.RED + "DO N.T DESCEND D.WN. FL..R WE.GHT IS UN.TA..." + Style.RESET_ALL)        #UNSTABLE
    print_slow("\nYou move deeper until the floor changes from new to old rotted planks. "
               "\nSome planks look soaked and soft. ")

    while True:
        trap1 = ask("\nThere are three paths which do you take? (left,middle,right): ", inventory)

        if trap1 == "left":
            print_slow("\nYou start walking gently, you make it halfway through... ")
            print("The planks start snapping behind you. ")
            show_run_warning(3)
            print_slow("\nYou spot a small opening ahead and run for it."
                       "\nYou jump to the small opening and start to crawl out, at the end you fall out."
                       "\nYou get up and start following a path next to the opening."
                       "\nIt leads you to two paths. ")
            path4(inventory, name)
            return inventory

        elif trap1 == "middle":
            print_slow("\nYou test each board, slow and steady. "
                       "\nThe boards squeak more and more by each step. "
                       "\nThe boards hold and you cross the gap")
            break

        elif trap1 == "right":
            print_slow("\nThe right edge seems to be weak. You balance yourself and stay on the left side and make it across. ")
            break

        else:
            print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)
            continue

    print_slow("\nYou continue deeper into the tunnel... "
               "\nThe glow from your lantern makes the wire's ahead gleam faintly."
               "\nYou could try to jump over or crawl under.")

    while True:
        trap2 = ask("What do you do? (jump/crawl): ", inventory)
        if trap2 == "crawl":
                print_slow("\nYou crawl under the wire, your back scrapes it. The wire doesnt set anything off. "
                           "\nThe path ahead is clear. ")
                break
        elif trap2 == "jump":
            if "broken left hand" in inventory:
                print_slow("\nYou sway your whole body for a jump forward"
                           "\nThe pain in your hand wobbles you mid jump, making you land off balance."
                           "\nYour boots set off the wire. ")
                show_run_warning(3)
                print_slow("\nYou pounce forward.")
                print_slow(Fore.RED + "*shake*" + Style.RESET_ALL)
                print_slow("\nRock's start to fall "
                           "\nThe tunnel is starting to collapse"
                           "\nYou spot a small opening ahead and run for it."
                           "\nYou jump to the small opening and start to crawl out, at the end you fall out."
                           "\nYou get up and start following a path next to the opening."
                           "\nIt leads you to two paths.")
                path4(inventory, name)
                return inventory

            else:
                print_slow("\nYou sway your whole body for a jump forward. "
                           "\nYou land on the other side with balance, and clear the wire without touching it. "
                           "\nThe path ahead is clear. ")
                break
        else:
            print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)
            continue

    print_slow("\nA bright glow ahead struck your attention. "
               "\nThe room is blocked by a stone gate. "
               "\nThere are three stone runes set into the wall: "
               + Fore.GREEN + "SILENCE" + Style.RESET_ALL + ", "
               + Fore.BLUE + "DARKNESS" + Style.RESET_ALL + ", and"
               + Fore.YELLOW + "TIME" + Style.RESET_ALL + ".")
    print_slow("\nThe floor below you starts shifting. ")

    pattern = [["SILENCE", "TIME", "DARKNESS"],
                ["DARKNESS", "SILENCE", "TIME"],
                ["TIME", "DARKNESS", "SILENCE"]]

    print_slow(Fore.RED + f"\nThe runes glow: {pattern[0]}... {pattern[1]}...{pattern[2]}..." + Style.RESET_ALL)
    time.sleep(2)
    print_slow("Was that a code?")
    print_slow("Enter the three runes in order (example: TIME,TIME,TIME). ")
    correct_pattern = [row[0] for row in pattern]
    memory = ask("Enter the pattern: ", inventory)
    tokens = re.split(r'[\s,]+', memory.strip())
    attempt = [token.upper() for token in tokens if token]

    if attempt == correct_pattern:
        print_slow("\nThe runes all pulse at once."
                   "\nDust falls as the stone door slides open."
                   "\nYou enter the room and find an old supply room."
                   "\nThis must of been where they used to store their appliances."
                   "\nEverything looks old and rusty, how long has these been sitting here?"
                   "\nWhy was this all left behind and abandoned?"
                   "\nYou scavenge trying to find anything useful to you. ")
        print_slow("\nYou rummage through rusted lockers and crates. "
                   "\nYou find a padded case with a faded emblem.")
        time.sleep(1)

        if "Flare Gun" not in inventory:
            inventory.add("Flare Gun")
            inventory.add("flare")
            print_slow("\nYou take a Flare Gun and a single flare. "
                       "\nThe gun looks old but usable. ")
        else:
            print_slow("\nThe supply room has already been scavenged. Nothing more to take here.")

        print_slow("\nYou secure your new item and head through a passage that looks to be leading you out of the Mill Tunnel."
                   "\nYou make it out safely."
                   "\nYou start to head down a path near the exit which leads you to two paths. ")
        path4(inventory, name)
        return inventory

    else:
        show_run_warning(3)
        print_slow("\nThe runes all pulse at once in the colour red."
                   "\nThe ground rumbles, cracks forming at your feet. "
                   "\nThe tunnel is starting to collapse."
                   "\nYou spot a small opening ahead and run for it."
                   "\nYou jump to the small opening and start to crawl out, at the end you fall out."
                   "\nYou get up and start following a path next to the opening."
                   "\nIt leads you to two paths. ")
        path4(inventory, name)
        return inventory

if __name__ == "__main__":
    start()