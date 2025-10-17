# ...existing code...
# Explain imports and initialization
import sys, time, random, shutil, re, textwrap  # system, timing, randomness, terminal size, regex, text wrapping
from colorama import Fore, Style, init  # colored console output helpers
init()  # initialize colorama for Windows consoles

# Locations used for highlighting in printed text (used by print_slow to color these names)
Locations = ["Mori Forest", "watchtower", "cave", "boardwalk", "waterfall", "Mill Tunnel",
             "farmhouse", "river", "shallow bridge", "cabin", "office", "altar", "barn"]

# Center a block of text in the terminal and print with color/brightness
# - Calculates padding to roughly center the block in the terminal window.
def print_centered_block(block: str, color=Fore.RED, bright=True):
    cols, rows = shutil.get_terminal_size((80, 24))
    lines = block.strip("\n").splitlines()
    width = max(len(line) for line in lines)
    left_pad = max((cols - width) // 2, 0)
    top_pad = max((rows - len(lines)) // 2, 0)
    sys.stdout.write("\n" * top_pad)
    style = (Style.BRIGHT if bright else "") + color
    for line in lines:
        # pad left and print line with color then reset style
        sys.stdout.write(" " * left_pad + style + line + Style.RESET_ALL + "\n")
    sys.stdout.flush()

# Print text slowly, highlighting known location names and optionally centering lines.
# - center: center each printed line
# - margin: used to avoid wrapping too close to terminal edges
# - delay: pause between printing each character to create a "slow text" effect
def print_slow(text, *, center=True, margin=20, delay=0.0008):
    # highlight any known location names in green (case-insensitive)
    for loc in Locations:
        pattern = rf"\b{re.escape(loc)}\b"
        text = re.sub(pattern, lambda m: Fore.GREEN + m.group(0) + Style.RESET_ALL, text, flags=re.IGNORECASE)

    cols = shutil.get_terminal_size((80, 24)).columns
    wrap_width = max(20, cols - margin)  # safe minimum width

    paragraphs = text.split("\n")

    for paragraph in paragraphs:
        if not paragraph.strip():
            # preserve blank lines
            sys.stdout.write("\n")
            continue

        # wrap long lines to terminal width
        wrapped_lines = textwrap.wrap(paragraph, width=wrap_width, replace_whitespace=False, drop_whitespace=False)
        if not wrapped_lines:
            sys.stdout.write("\n")
            continue

        for line in wrapped_lines:
            out_line = line.center(cols) if center else line
            # print each character with a short delay for dramatic effect
            for character in out_line:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(delay)
            sys.stdout.write("\n")
            sys.stdout.flush()

# Possibly print a short eerie whisper message based on chance (adds atmosphere)
# - name: used to optionally add a personal touch
# - chance: probability (0..1) the whisper appears
def maybe_whisper(name, chance=0.1):
    if random.random() >= chance:
        return
    whisper = ["\nYou feel something is watching you. ",
               "\nYou hear twigs snap.... nothing. ",
               "\nDistant sounds making you rethink what your hearing is real. ",
               "\nYou hear footsteps, perfectly in sync with yours...",
               "\nThe forest wind humming, almost like the Forest is alive. "]
    if name:
        whisper.append(f"\nThe wind brushes your ear" )
    # choose one whisper and print it slowly in blue
    print_slow(Fore.BLUE + random.choice(whisper) + Style.RESET_ALL)

# Show a flickering "glitch" animation of a message (used for dramatic events)
# - message: text to reveal after flicker
# - flickers: how many flicker frames to show
def glitch_text(message = "THING", flickers = 25):
    glitch_chars = ["#", "%", "!", "?", "$"]
    for _ in range(flickers):
        clear_screen()
        glitched = ""
        for text in message:
            # randomly replace characters with glitch chars for effect
            glitched += random.choice(glitch_chars) if text != " " and random.random() < 0.35 else text
        print(Fore.RED + Style.BRIGHT + glitched + Style.RESET_ALL)
        time.sleep(random.uniform(0.05, 0.15))
    clear_screen()
    # finally show the real message
    print(Fore.RED + Style.BRIGHT + message + Style.RESET_ALL)
    time.sleep(1.5)
    clear_screen()

# Clear the terminal screen using ANSI escape sequences
def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

# Show the player's inventory (sorted). If empty, show (empty).
def show_inventory(inventory = None):
    items = sorted(list(inventory or []))
    if items:
        print_slow("\nInventory: " + ", ".join(items) + "\n")
    else:
        print_slow("\nInventory: (empty)\n")

# Reusable input helper that supports typing 'i' or 'inventory' at any prompt to view items
# - returns the user's non-empty input in lowercase
def ask(prompt, inventory = None):
    while True:
        choice = input(prompt).strip().lower()
        # allow quick inventory check
        if choice in ('i', 'inventory'):
            show_inventory(inventory or set())
            continue
        if choice:
            return choice

# Display a large ASCII "run" warning briefly — used when the player needs to run
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

# Small loading/progress animation that shows the MORI logo and percent
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

    # simple percentage loop for the loading feel
    for i in range (10, 101, 10):
        clear_screen()
        block = mori + f"\n{i}%"
        print_centered_block(block, color =Fore.RED, bright=True)
        time.sleep(0.25)
    clear_screen()

# Unified ending display: shows frame, title, subtitle and optional color
def show_ending(title: str, subtitle: str, color=Fore.BLUE):
    clear_screen()
    glitch_text("...", flickers=10)
    time.sleep(1)
    frame = "══════════════════════════════════════"
    # show framed ending text slowly for atmosphere
    print_slow(color + "\n" + frame + Style.RESET_ALL)
    print_slow(color + f"\nENDING: {title}" + Style.RESET_ALL)
    time.sleep(1)
    print_slow("\n" + subtitle )
    print_slow(color + "\n" + frame + Style.RESET_ALL)
    time.sleep(3)

# When a game-ending condition happens, show the ending and add the ending key to inventory.
# Returns the updated inventory so the caller can keep track of endings reached.
def conclude_game(inventory: set, key: str, title: str, subtitle: str, color=Fore.BLUE):
    show_ending(title, subtitle, color=color)
    inventory.add(key)
    return inventory

# Entry point for the game: asks name and age, does basic validation and starts the story
def start():
    # ask player's name
    name = ask("What is your name? ").strip()
    while True:
        # validate age is a reasonable integer
        age = ask("\nWhat is your age? ")
        if not age.isdigit():
            print(Fore.RED + "Invalid input. Enter a number." + Style.RESET_ALL)
            continue
        age = int(age)
        if age > 100:
            print(Fore.RED + "Don't just give a random number!" + Style.RESET_ALL)
            continue
        if age < 16:
            # block very young players (game design choice)
            print_slow(name + ", you aren't old enough to play this game.")
            return
        break

    # show loading then begin
    mori_loading_screen()
    print_slow("Welcome to Mori, " f"{name}" + "\n")
    print_slow("Lets Begin\n")

    # short opening scene
    print_slow("\nYou check the time and realise it's late, you start to go back to the beginning of the Mori Forest, "
               "taking the path back, the darkness got darker and you start to panic which led you to take a turn into a path you've never been to. "       
               "You are now lost in the darkness of the Mori Forest.")
    print_slow(f"\n{name}, your choices now will effect if you make it out alive.")

    inventory = set()  # track items and endings
    path1(name, inventory)
    return


# PATH 1: initial exploration and finding flashlight / batteries
def path1(name, inventory):
    print_slow("\nThe path continues going deeper into the Mori forest." 
               "\nThe path seems endless leading you only to a more shallow and dark place."
               "\nWhile walking you spot something shining in the tall grass of the Mori Forest.")
    maybe_whisper(name, chance=0.3)

    while True:
        # prompt to stop and check the grass
        path = ask("\nDo you stop? (yes/no): ", inventory)

        if path == "yes":
            batteries = ask("\nAre you sure you want to check the long grass? (yes/no): ", inventory)
            if batteries ==  "yes":
                # add batteries to inventory if not already present
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
            # found a flashlight (initially without batteries)
            print_slow("\nYou explore under the shallow bridge and in a swamp of dirt with a grotesque smell. "
                       "\nWhile holding your nose you search the swamp finding a flashlight with missing batteries. ")

            if "flashlight" not in inventory and "stenching flashlight" not in inventory:
                inventory.add("flashlight")
                print_slow("\nYou take the stenching flashlight. ")

            # if player already found batteries, combine them to make working flashlight
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

    # continue the adventure through other path sections
    inventory = path2(name, inventory)
    inventory = path3(name, inventory)
    inventory = path4(name, inventory)
    return inventory

# PATH 2: deeper forest, possible chase sequences and consequences
def path2(name, inventory):
    print_slow(f"\n{name} you go deeper into the Mori Forest. "
               "\nThe air grows colder, you can tell its very late. "
               "\nJust hoping you can make it out")
    maybe_whisper(name, chance=0.3)

    # flashlight changes how events play out
    if "stenching flashlight" in inventory:
        print_slow("\nThe working flashlight cuts through the darkness of the Mori Forest. "
                   "\nYou spot with your flashlight claw mark along the trees. Something has been here recently."
                   "\nThe trail of claw marks continue, daring you to follow...")
        maybe_whisper(name, chance=1)

        while True:
            claw = ask("\nDo you follow the claw marks or ignore them? (follow/ignore): ", inventory)
            if claw == "follow":
                print_slow("\nYou follow the claw marks and with each step the marks grow fresher. Suddenly, you hear rustling. "
                           "\nYour grip tightens on the flashlight. ")
                print_slow(Fore.RED + "\n...*rustle*...*snap*..." + Style.RESET_ALL)
                # encounter choices: shine or hide
                while True:
                    tense = ask("\nDo you shine your light at the sound or switch it off and hide? (shine/hide): ", inventory)
                    if tense == "shine":
                        # shining leads to immediate chase and choices at boardwalk/waterfall
                        print_slow("\nYou shine your flashlight in the darkness. Two pale eyes flash back-")
                        time.sleep(0.1)
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
                                # tense sequence — multiple outcomes depend on choices and luck
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
                                print_slow(name + " make a choice.")
                                escaping = ask("\nDo you jump or run? (jump/run): ", inventory)
                                if escaping == "jump":
                                    # jumping leads to recovery but with injury and further cave sequences
                                    print_slow("\nYou jump from the boardwalk.  "
                                               "\nFalling...")
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
                                    # running may let you escape but you lose flashlight
                                    print_slow("\nYou dash forward, the planks crack beneath your feet. "
                                           "\nIt starts chasing you")
                                print_slow("\nYou leap off the final plank as the whole boardwalk breaks down "
                                           "\nYour flashlight falls from your pocket"
                                           "\nYou tumble into the grass. "
                                           "\nYou look back.... the boardwalk is gone and so was it. "
                                           "\nDid it fall with the boardwalk? ")
                                inventory.discard("stenching flashlight")
                                return inventory
                            elif creature == "jump":
                                # jumping into waterfall leads to injury and loss of flashlight
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
                        # hiding leads to stealth options with chance outcomes
                        print_slow("\nYou click the flashlight off and crouch low next to the trees"
                                   "\nYou press your back against a tree, holding your breath ")
                        time.sleep(1)
                        maybe_whisper(name, chance=1)
                        print_slow(Fore.RED + "\n...*crack*..." + Style.RESET_ALL)
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
                                maybe_whisper(name, chance=1)
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
                            maybe_whisper(name, chance=1)
                            print_slow("\nWhatever it was, it's gone... for now. ")

                        else:
                            print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)
                            continue

                        print_slow("\nYou've waited a while now, your fear disappears "
                                   "\nYou finally move on, avoiding the claw marked trees")
                        time.sleep(1)
                        print_slow("\nWhile treading through deeper into the Mori Forest you spot a tall figure. ")
                        print_slow("\nA watchtower")
                        return inventory
                    
                    else:  
                        print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)
                        continue

            elif claw == "ignore":
                # ignoring removes the chase branch
                print_slow("\nYou choose not to tempt your own fate, walking away from the claw marked trail "
                           "\nThe Mori Forest grows eerily quiet as you continue forward. ")

                maybe_whisper(name, chance=0.3)
                return inventory

            else:
                print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)
                continue

    # if only non-working flashlight present, it becomes useless and is dropped
    if "flashlight" in inventory:
        print_slow("\nYou walk on with the non-working flashlight, clicking it again and again. "
                   "\nIts nothing more than just dead weight. ")
        inventory.discard("flashlight")

    print_slow("\nYou stumble blindly in the darkness of the Mori Forest. "
               "\nBranches claw at your arms, and with each step feeling like it could lead you to a drop. "
               "\nThe Mori Forest whispers around you, but you can't tell if its the wind... or the voices. ")

    maybe_whisper(name, chance=0.3)

    # offer a simple choice to search or go forward; both give possible items
    while True:
        choice = ask("\nDo you keep moving forward or try searching around you for something that can be useful to you? (forward/search): ", inventory)
        if choice == "forward":
            print_slow("\nYou grit your teeth and press on, but each step sinks deeper into the mud. "
                       "\nYour heartbeat drowns out the silence of the Mori Forest. ")
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
                    # if lighted, the cloth reveals a code
                    print_slow("\nYou find a strange cloth with numbers written on it. ")
                    print(Fore.BLUE + "1003" + Style.RESET_ALL)
                    inventory.add("Code 1003")
                    inventory.discard("strange cloth")
                else:
                    print_slow("\nYou keep the strange cloth, though in this darkness you can't read what's on it. ")
            break

        else:
            print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)
            continue


def path3(name, inventory):
    print_slow("\nWhile treading through deeper into the Mori Forest you spot a tall figure. "
               "\nYou walk towards to the tall figure that resembles a building of some sort. ")
    print_slow("\nAn abandoned watchtower. "
               "\nYou step closer, hearing the groan of old planks creaking from the wind. ")

    while True:
        watchtower = ask("\nDo you enter the watchtower or look around first? (enter/look_around): ", inventory)

        if watchtower == "look_around":
            # looking around just sets you to enter after a short description
            print_slow("\nYou circle around the watchtower. "
                       "\nThe ground is littered with broken glass, scraps and dirt. "
                       "\nNothing worth your intrest. ")
            watchtower = "enter"

        if watchtower == "enter":
            print_slow("\nYou grip the splintered railing of the watchtower and start walking up. ")
            if "stenching flashlight" in inventory:
                # with a working flashlight the player finds a clue in a cabin
                print_slow("\nYour flashlight helps you get to the top safely dodging any cracks in the aged wooden stairs. "
                           "\nThe view steals your breath, all you see is an endless forest and a cold moon above you.")

                maybe_whisper(name, chance=0.2)

                print_slow("\nAn old cabin, you enter the cabin. "
                           "\nThe cabin is filled with dust. You spot a journal with your flashlight on the desk, you flip it open with one page being readable. "
                           "\nFollow the trail where the crows circle, the gate is guarded by a .... "
                           "\nA word is missing,looks like someone didn't have time to finish there journal"
                           "\nYou go down the watchtower, and continue till the end of the path. "
                           "\nThere it is"
                           "\nThe path being surrounded by crows ")
                inventory.add("Clue")
            else:
                # without light there's a risk of falling through a step
                print_slow("\nWith the darkness surrounding you every step is a mystery. "
                           "\nYou walk slowly up. "
                           "\nThe steps seem to creak more and more. "
                           "\nYou wonder what was the last time someone was up here. ")
                print_slow(Fore.RED + "\n\n*CRACK*\n\n" + Style.RESET_ALL)
                print_slow("\nYour foot breaks through one of the steps"
                           "\nYou grab the railings firmly ")
                creak = ask("Gasping for air do you continue to go up or do you go back down (up/down): ", inventory)
                if creak == "up":
                    # if you continue up in the dark, you can still find the clue if you turn on the light later
                    print_slow("\nBrave"
                               "\nYou make it to the top safely, luck favours you. " 
                               "\nThe view steals your breath, all you see is an endless forest and a cold moon above you. "
                               "\nAn old cabin, you enter the cabin. ")

                    while True:
                        light = ask("\nThe cabin has a light switch do you turn on the light? (yes/no): ", inventory)
                        if light == "yes":
                            if "strange cloth" in inventory:
                                # reveal code if player has cloth
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
                            # player can change their mind about turning on the light
                            print_slow("\nYou can't make out anything in this darkness. ")
                            confirm = ask("Are you sure you don't want to turn on the light? (yes/no): ", inventory)
                            if confirm == "no":
                                continue
                            elif confirm == "yes":
                                print_slow("\nYou decide to stay in the dark, firm with your choice. "
                                           "\nWithout any light you have no option but to go down the watchtower. " 
                                           "\nYou continue till the end of the path. ")

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

def path4(name, inventory):
    # present two paths, one marked by crows (clue related), one darker
    print_slow(Fore.BLUE + f"\n{name}" + Style.RESET_ALL + "\n there are two paths before you. One is circled with crows, the other is dark and quiet. ")
    maybe_whisper(name, chance=0.3)

    if "Clue" in inventory:
        print_slow("\nYou remember the journal line: 'Follow the trail where the crows circle...' ")
    else:
        print_slow("\nYou have no clear hint. You trust your gut. ")

    valid = ("crows", "dark_path")
    while True:
        pick = ask("\nWhich path do you take? (crows/dark_path): ", inventory)
        if pick in valid:
            break
        print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)

    # modifiers used in combat/skill checks
    broken = "broken left hand" in inventory
    hand_penalty = 0.3 if broken else 0.0
    fear_bonus = 0.1
    close_range_burn_bonus = 0.2

    if pick == "crows":
        # staggered encounter sequence with many branching outcomes
        print_slow("\nYou step onto the path surrounded by crows. ")
        time.sleep(1)
        print_slow("\nThe cawing cuts out, the crows take flight, something else answers from the tress . ")
        print_slow(Fore.RED + "\nIt steps out..." + Style.RESET_ALL + "\nThe pale eyes glint in the dark. ")
        maybe_whisper(name, chance=1)

        if "Clue" in inventory:
            # allow the player to access a hidden hatch if they have the code
            print_slow("\nSomething feels different, it feels like you know it, memory's flash when you look around. ")
            while True:
                clue = ask("\nDo you explore the area that gives you some sort of familiarity? (yes/no): ", inventory)
                if clue in("yes", "no"):
                    break
                print(Fore.RED + "\nInvalid input. Please type 'yes' or 'no'." + Style.RESET_ALL)

            if clue == "yes":
                print_slow("\nYou explore the area, the familiarity grows stronger. "
                           "\nYou recognise the path, you've been here before. "
                           "\nAt the end a rusted maintenance hatch. A keypad blinks beside it. ")
                if "Code 1003" in inventory:
                    # success ends the game with a special tape ending
                    print_slow("\nYou punch in the code you found earlier. The hatch creaks open, revealing a dark tunnel. "
                               "\nYou follow the tunnel, until it leads you to a control room, monitors, and a tape machine that clicks on. ")
                    print_slow(Fore.YELLOW + "\nTAPE: " + Style.RESET_ALL + "\nA voice plays...")
                    print_slow("\nField Test #1003. Subject has retained partial awareness. "
                               "\nIf you are hearing this, it means you survived long enough to find the exit again. "
                               "\nYou built this place to study that creature, remember? But he learned to study you back. "
                               "\nYou are why he exists. "
                               "\nThe voice that played...")

                    return conclude_game(
                        inventory,
                        key="ENDING_TAPE",
                        title="Field Test #1003",
                        subtitle="You built the forest to watch the monster. It learned to watch you back. The voice on the tape was your's. ",
                        color=Fore.YELLOW)
                    
                else:
                    print_slow("\nYou have no idea what the code is. You decide to leave the keypad alone. ")
            else:
                print_slow("\nYou ignore the feeling of familiarity. Whatever is hidden here can stay hidden. ")

        # build action choices depending on items
        actions = []
        if "Mirror Fragment" in inventory:
            actions.append("shard")
        if "Flare Gun" in inventory and "flare" in inventory:
            actions.append("flare")
        actions.append("run")

        def pick_action():
            return ask(f"\nIts starts approaching you. What do you do" + name + "? ({'/'.join(actions)}): ", inventory)

        # choose action and run the corresponding outcome logic
        while True:
            act = pick_action()
            if act not in actions:
                print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)
                continue
            if act == "shard" and "Mirror Fragment" not in inventory:
                print_slow(Fore.RED + "\nYou reach for the shard it's not there." + Style.RESET_ALL)
                continue
            if act == "flare" and ("Flare Gun" not in inventory or "flare" not in inventory):
                print_slow(Fore.RED + "\nYou reach for a flare you don't have." + Style.RESET_ALL)
                continue

            if act == "shard":
                # detailed combat logic with random checks and multiple endings
                print_slow("\nYou raise the Mirror Fragment. It's edge bites your palm, the blood flows across the shard. "
                           "\nThe creature halts, recoiling from the sight of the bloodied glass. ")
                damage_to_creature = ask("\nDo you stab it's eye or force the shard into it's pale eyes? (stab/force): ", inventory)
                if damage_to_creature not in {"stab", "force"}:
                    print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)
                    continue

                if damage_to_creature == "stab":                                                       
                    print_slow("\nYou lunge for the eye...")
                    kill_roll = random.random()
                    kill_chance = 0.65 - hand_penalty - fear_bonus
                    if kill_roll < kill_chance:
                        glitch_text("S C R E E E E E C H", flickers=6)
                        inventory.discard("Mirror Fragment")
                        return conclude_game(
                            inventory,
                            key="ENDING_SHARD_KILL",
                            title="Shattered Reflection",
                            subtitle="The shard buries deep. Dark fluid spills out. The creature collapses, twitching. It dissolves into a dark fluid.",
                            color=Fore.CYAN)
                                                            
                    else:
                        injure_to_creature = (
                        "\nYou slice it's cheek, the gash spills dark fluid. " 
                        if not broken else    
                        "\nYour grip stutters. The shard skims the cheek.")
                        
                        print_slow(injure_to_creature)
                        drop_roll = random.random()
                        if drop_roll < (0.6 if broken else 0.3):
                            print_slow("\nThe shard slips from your bloodied hand, falling to the ground. ")
                            inventory.discard("Mirror Fragment")
                        else:
                            print_slow("\nYou rip the shard free, barely holding on. ")

                        finish_roll = random.random()
                        finish_chance = 0.5 - hand_penalty
                        if "Mirror Fragment" in inventory and finish_roll < finish_chance:
                            glitch_text("S T I L L N E S S", flickers=6)                                
                            inventory.discard("Mirror Fragment")
                            return conclude_game(
                                inventory,
                                key="ENDING_SHARD_SECOND",
                                title="Second Cut",
                                subtitle="Not clean, not kind, just final. ",
                                color=Fore.CYAN)
                            
                        else:
                            print_slow("It staggers, enraged. You have to run. ")
                            escape_roll = random.random()
                            escape_chance = 0.65 - (0.2 if broken else 0.0)
                            if escape_roll < escape_chance:
                                return conclude_game(
                                    inventory,
                                    key="ENDING_SHARD_ESCAPE",
                                    title="Bleeding Spirit",
                                    subtitle="You vanish into the trees, alive. ",
                                    color=Fore.BLUE)
                                    
                            else:
                                show_run_warning(duration=2)
                                glitch_text("N O  P A T H", flickers=10)
                                return conclude_game(
                                    inventory,
                                    key="ENDING_TAKEN",
                                    title="Taken By The Shadows",
                                    subtitle="You run. The forest chooses whose breath will continue. ",
                                    color=Fore.RED)
                                

                elif damage_to_creature == "force":
                    # forcing the shard has another set of random outcomes
                    print_slow("\nYou force it's face into the shard. ")
                    reflect_roll = random.random()
                    reflect_chance = 0.5 - hand_penalty - fear_bonus
                    if reflect_roll < reflect_chance:
                        glitch_text("S", flickers=6)
                        print_slow("\nThe shard shatters, the pieces stuck in it's face. It collapses, twitching. It dissolves into a dark fluid. ")
                        inventory.discard("Mirror Fragment")
                        return conclude_game(
                            inventory,
                            key="ENDING_SHARD_KILL",
                            title="Shattered Reflection",
                            subtitle="The shard buries deep. Dark fluid spills out. The creature collapses, twitching. It dissolves into a dark fluid.",
                            color=Fore.CYAN)
                        
                    else:
                        print_slow("\nIt thrashes free, face slashed and bleeding. ")
                        if "Flare Gun" in inventory and "flare" in inventory:
                            flare_gun = ask("\nDo you take the chance to shoot a flare at it or run? (shoot/run): ", inventory)
                            act = "flare" if flare_gun == "shoot" else "run"
                        else:
                            act = "run"
                        
                        if act == "run":
                            show_run_warning(duration=3)
                            if random.random() < (0.6 - (0.15 if broken else 0.0)):
                                return conclude_game(
                                    inventory,
                                    key="ENDING_SHARD_ESCAPE",
                                    title="Bleeding Spirit",
                                    subtitle="You vanish into the trees, alive. ",
                                    color=Fore.BLUE)

                            else:
                                glitch_text("C L O S E", flickers=5)
                                return conclude_game(
                                    inventory,
                                    key="ENDING_TAKEN",
                                    title="Taken By The Shadows",
                                    subtitle="You run. The forest chooses whose breath will continue. ",
                                    color=Fore.RED)

            elif act == "flare":
                # using a flare gun consumes the flare and has a chance to kill
                print_slow("\nYou jam the muzzle under it's ribs and fire. ")
                shot_roll = random.random()
                shot_chance = 0.55 + close_range_burn_bonus - hand_penalty - fear_bonus
                inventory.discard("flare")
                if shot_roll < shot_chance:
                    glitch_text("W H O O M P", flickers=5)
                    return conclude_game(
                        inventory,
                        key="ENDING_FLARE_KILL",
                        title="Incineration",
                        subtitle="\nThe flare hits, searing into it's flesh. It howls, collapses, twitches. It dissolves into a dark fluid. ",
                        color=Fore.RED)
                    
                else:
                    print_slow("\nThe flare skims it's shoulder, It reels, blinded")
                    if "Mirror Fragment" in inventory:
                        while True:
                            follow = ask("\nDo you try to finish it with the shard or run? (shard/run): ", inventory)
                            if follow in ["shard", "run"]:
                                break
                            print(Fore.RED + "\nInvalid input. Please type 'shard' or 'run'." + Style.RESET_ALL)

                        if follow == "shard":
                            glitch_text("S T I L L N E S S", flickers=5)
                            print_slow("\nYou cut it's throat with the shard it screams at the moon.")
                            inventory.discard("Mirror Fragment")
                            return conclude_game(
                                inventory,
                                key="ENDING_SHARD_SECOND",
                                title="Second Cut",
                                subtitle="Not clean, not kind, just final. ",
                                color=Fore.CYAN)
                        else:
                            if random.random() < (0.6 - (0.15 if broken else 0.0)):
                                return conclude_game(
                                    inventory,
                                    key="ENDING_SHARD_ESCAPE",
                                    title="Bleeding Spirit",
                                    subtitle="You sprint blindly through the forest. It never finds you.",
                                    color=Fore.BLUE)
                            else:
                                glitch_text("S H A D O W", flickers=5)
                                return conclude_game(
                                    inventory,
                                    key="ENDING_TAKEN",
                                    title="Taken By The Shadows",
                                    subtitle="You sprint blindly through the forest.",
                                    color=Fore.BLUE)
                    else:
                        if random.random() < (0.6 - (0.15 if broken else 0.0)):
                            return conclude_game(
                                inventory,
                                key="ENDING_SHARD_ESCAPE",
                                title="Bleeding Spirit",
                                subtitle="You sprint blindly through the forest. It never finds you.",
                                color=Fore.BLUE)
                        else:
                            glitch_text("S H A D O W", flickers=5)
                            return conclude_game(
                                inventory,
                                key="ENDING_TAKEN",
                                title="Taken By The Shadows",
                                subtitle="You sprint blindly through the forest.",
                                color=Fore.BLUE)

            elif act == "run":
                # running has a chance to fail based on injuries
                show_run_warning(duration=3)
                run_roll = random.random()
                run_chance = 0.3 - (0.1 if broken else 0.0)
                if run_roll < run_chance:
                    return conclude_game(
                        inventory,
                        key="ENDING_NO_PATH",
                        title="No Path",
                        subtitle="You run,it finds you in the dark.",
                        color=Fore.MAGENTA)
                    
                else:  
                    glitch_text("N O  P A T H", flickers=10)
                    print_slow(Fore.RED + "\nENDING: " + Style.RESET_ALL + "You run,it finds you in the dark. ")
                    return conclude_game(
                    inventory,
                        key="ENDING_TAKEN",
                        title="Taken in the Shadows",
                        subtitle="You run,it finds you in the dark.",
                        color=Fore.RED)
                    
        return inventory

    else:
        # dark_path branch — different obstacles and endings
        print_slow("\nYou take the quieter path. ")
        time.sleep(1)
        print_slow("\nFootsteps mirror your own. The pale eyes glint again behind you. ")
        print_slow("\nA rope is hanging from the trees. ")
        while True:
            rope_choice = ask("\nDo you cut the rope or climb it? (cut/climb): ", inventory)
            if rope_choice in ("cut", "climb"):
                break
            print(Fore.RED + "\nInvalid Input. Please type 'cut' or 'climb'." + Style.RESET_ALL)


        if rope_choice == "cut" and "pocket knife" in inventory:
            # cutting is simple if you have a pocket knife
            print_slow("\nYou cut through the rope. It snaps and coils in the dirt. ")
        else:
            # climbing may fail if injured
            if random.random() < (0.8 + hand_penalty):
                print_slow("\nYou try to climb the rope but fail and slip. ")
                show_run_warning(duration=2)
            else:
                print_slow("\nYou climb the rope and drop down the other side. ")
        
        print_slow("\nYou path descends into a cramped shaft. ")
        opts = []
        if "Mirror Fragment" in inventory: opts.append("shard")
        if "Flare Gun" in inventory and "flare" in inventory: opts.append("flare")
        opts.append("squeeze")

        while True:
            crawls_after_you = ask(f"\nIt crawls after you. What do you do {name}? ({'/'.join(opts)}): ", inventory)  
            if crawls_after_you not in opts:
                print(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)
                continue

            if crawls_after_you == "shard":
                # trap using shard in a tunnel (chance-based kill)
                print_slow("\nYou pin the shard in the tunnel so it's face must meet itself to reach you. ")
                reflect_roll = random.random()
                reflect_chance = 0.65 - hand_penalty
                if reflect_roll < reflect_chance:
                    glitch_text("S P L I N T ER ", flickers=5)
                    print_slow("\nThe shard shatters, the pieces stick in it's face. It collapses, twitching. It dissolves into a dark fluid. ")
                    inventory.discard("Mirror Fragment")
                    return conclude_game(
                        inventory,
                        key="ENDING_SHARD_KILL_2",
                        title="Shattered Reflection",
                        subtitle="Shattered Reflection, you kill it with a the shard of it's truth. ",
                        color=Fore.CYAN)

                else:
                    print_slow("\nIt smashes past the glass, ripping your arm. The shard falls with your arm. ")
                    inventory.discard("Mirror Fragment")
                    return conclude_game(
                        inventory,
                        key="ENDING_ARM_CUT_OFF",
                        title="Severance",
                        subtitle="The pain flushes. You accept your fate.",
                        color=Fore.RED)

            elif crawls_after_you == "flare":
                # flare gun again has a chance to kill at close range
                print_slow("\nYou jam the muzzle under it's ribs and fire. ")
                inventory.discard("flare")
                if random.random() < (0.70 + close_range_burn_bonus - hand_penalty):
                    glitch_text("W H O O M P", flickers=5)
                    return conclude_game(
                        inventory,
                        key="ENDING_FLARE_KILL",
                        title="Incineration",
                        subtitle="The flare hits, searing into it's flesh. It howls, collapses, twitches. It dissolves into a dark fluid.",
                        color=Fore.RED)
                    
                else:
                    return conclude_game(
                        inventory,
                        key="ENDING_TAKEN",
                        title="Taken By The Shadows",
                        subtitle="The darkness swallows you whole.",
                        color=Fore.RED)

            else:
                # squeezing through leads to a safe escape ending
                print_slow("\nYou force yourself through the tight space, ignoring the scraping and clawing behind you. ")
                print_slow("\nThe tunnel spits you out into a riverbed. Free. ")
                return conclude_game(
                    inventory,
                    key="ENDING_NEEDLE",
                    title="Thread The Needle",
                    subtitle="You live squeezing through. The night lets you pass.",
                    color=Fore.BLUE)

def cave_scene(name, inventory):
    maybe_whisper(name, chance=0.5)

    if "broken left hand" in inventory:
        # mention injury to remind player
        print_slow("\nYour " + Fore.RED + "broken left hand" + Style.RESET_ALL +
                   " throbs painfully with each step.")

    print_slow("\nYou check your surroundings "
               "\nHappy that thing left you alone. "
               "\nYou approach a cave with lamps lit up with fire that dazzles your eyes. "
               "\nSomeone must of been here not long ago. "
               "\nYou take cautious steps inside, the echo of dripping water echoing throughout the cave.")
    print_slow("\nYou steep even deeper into the cave."
               "\nThe lamps continue on and on "
               "\nThe walls have symbols written on them, spirals, eyes, "
               "\nand a crude depiction of a creature with too many limbs. "
               "\nThe tunnels opens into a vast underground chamber. "
               "\nDozens of burnt out candles circle a stone altar. "
               "\nSomething is covered with cloth, and the smell... it's unbearable.")

    investigate = ask("\nDo you uncover what's on the altar? (yes/no): ", inventory)
    if investigate == "yes":
        # finding the mirror fragment is an important plot item
        print_slow("\nYour shaking hands pull back the cloth... "
                   "\nA mirror, cracked and blackened, stares back - your reflection twisted smiling. "
                   "\nA voice whispers")
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
            print_slow("\nInside you find a lighter, it looks well kept, it must of been special to someone. ")
            inventory.add("lighter")
            print_slow("\nYou now have a lighter. ")
        else:
            print_slow("\nOnly dust remains in the box. ")
    elif open_box == "no":
            print_slow("\nYou leave the box shut. ")
    else:
        print_slow(Fore.RED + "\nInvalid input. Please try again." + Style.RESET_ALL)

    print_slow("\nYou leave the barn and enter the farmhouse,"
               "\nSomething is swaying around in the farmhouse."
               "\nYou check it out just to see a dented lantern swaying gently from a coat rack.")
    if "Lighted Lantern" not in inventory and "lantern" not in inventory:
        inventory.add("lantern")
        print_slow("\nYou now have a lantern. ")

    # if player has both lighter and lantern, combine into a lighted lantern
    if "lighter" in inventory and "lantern" in inventory and "Lighted Lantern" not in inventory:
        print_slow("\nYou light the lantern with your lighter. ")
        inventory.discard("lighter")
        inventory.discard("lantern")
        inventory.add("Lighted Lantern")
        print_slow("\nYou now have a lighted lantern that glows through the darkness.")

    if "Lighted Lantern" in inventory:
        # lighted lantern reveals a map that points to Mill Tunnel
        print_slow("\nWith the lamp you delve deeper into the farmhouse, through the eerie hall, which leads you to discover an old office.")
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

    # if lantern not useful, discard it and go back to path choices
    print_slow("\nYou step back outside with a lantern, it has no use to you, you throw it away. "
               "\nYou step back into the Mori Forest"
               "\nWith nothing to guide your journey, you can only wander around till you find something. "
               "\nAfter a while, you finally stumble across two paths.")

    inventory.discard("lantern")
    inventory = path4(name, inventory)
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
            inventory = path4(name,inventory)
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
                # injured players are more likely to trigger collapse
                print_slow("\nYou sway your whole body for a jump forward"
                           "\nThe pain in your hand wobbles you mid jump, making you land off balance."
                           "\nYour boots set off the wire. ")
                show_run_warning(3)
                print_slow("\nYou pounce forward.")
                print_slow(Fore.RED + "\n*shake*" + Style.RESET_ALL)
                print_slow("\nRock's start to fall "
                           "\nThe tunnel is starting to collapse"
                           "\nYou spot a small opening ahead and run for it."
                           "\nYou jump to the small opening and start to crawl out, at the end you fall out."
                           "\nYou get up and start following a path next to the opening."
                           "\nIt leads you to two paths.")
                inventory = path4(name,inventory)
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

    # pattern hints printed to the player; correct pattern is the first column of rows
    pattern = [["SILENCE", "TIME", "DARKNESS"],
                ["DARKNESS", "SILENCE", "TIME"],
                ["TIME", "DARKNESS", "SILENCE"]]

    print_slow(Fore.RED + f"\nThe runes glow: {pattern[0]}... {pattern[1]}...{pattern[2]}..." + Style.RESET_ALL)
    time.sleep(2)
    print_slow("\nWas that a code?")
    print_slow("\nEnter the three runes in order (example: TIME,TIME,TIME). ")
    correct_pattern = [row[0] for row in pattern]
    memory = ask("Enter the pattern: ", inventory)
    tokens = re.split(r'[\s,]+', memory.strip())
    attempt = [token.upper() for token in tokens if token]

    if attempt == correct_pattern:
        # success gives access to a supply room with a flare gun
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
        inventory = path4(name,inventory)
        return inventory

    else:
        # wrong code causes a collapse sequence and forces the player out
        show_run_warning(3)
        print_slow("\nThe runes all pulse at once in the colour red."
                   "\nThe ground rumbles, cracks forming at your feet. "
                   "\nThe tunnel is starting to collapse."
                   "\nYou spot a small opening ahead and run for it."
                   "\nYou jump to the small opening and start to crawl out, at the end you fall out."
                   "\nYou get up and start following a path next to the opening."
                   "\nIt leads you to two paths. ")
        inventory = path4(name,inventory)
        return inventory

if __name__ == "__main__":
    # run the game when this file is executed directly
    start()