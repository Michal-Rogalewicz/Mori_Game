# Mori

A text-based horror adventure for the terminal, written in Python. You're lost in the Mori Forest at night, something is hunting you, and every choice you make decides whether you make it out alive.

> **Age rating:** the game asks for your age at the start and won't run for players under 16.

## Features

- **Branching story** with multiple routes through the forest, a cave, an abandoned mill tunnel and a watchtower
- **Several different endings**, from killing the creature to being taken by the shadows, plus a twist ending hidden behind a secret code
- **Inventory system**: items you find (or lose) change which options and outcomes are open to you
- **Atmosphere**: typewriter-style text, random whispers from the forest, flickering glitch text, ASCII-art warnings and a loading screen
- **Randomness**: some encounters, like distracting the creature, have chance-based outcomes, so replays can play out differently
- **Coloured terminal output** with story locations highlighted in green

## Requirements

- Python 3.8 or newer
- [colorama](https://pypi.org/project/colorama/)

## Installation and usage

```bash
git clone https://github.com/Michal-Rogalewicz/Mori_Game.git
cd Mori_Game
pip install colorama
python "MORI FILE/mori_3.py"
```

For the best experience, run it in a terminal with a dark background and make the window wide enough for the centred text and ASCII art. Text is printed slowly on purpose, so settle in.

## How to play

- Type your answer when prompted and press **Enter**. The available options are shown in brackets, for example `(yes/no)` or `(follow/ignore)`.
- Type `i` or `inventory` at any prompt to check what you're carrying.
- Explore, since items and clues from earlier in the story can unlock new options later on.
- Your injuries matter. Something like a broken hand affects how well you do in a fight.

## Project structure

```
Mori_Game/
└── MORI FILE/
    └── mori_3.py     # The whole game
```

Inside `mori_3.py`:

| Part | What it does |
| --- | --- |
| `start()` | Asks for your name and age, shows the loading screen and begins the story |
| `path1()` to `path4()` | The main story sections, from the first exploration to the final confrontation |
| `cave_scene()`, `cave_scene2()`, `mill_tunnel()` | Side routes that can lead to extra items and different endings |
| `ask()` | Input helper that handles the `inventory` command at any prompt |
| `print_slow()`, `glitch_text()`, `maybe_whisper()` | Text effects for atmosphere |
| `conclude_game()` / `show_ending()` | Displays an ending and records it |

## Adding to the story

The game is built from simple functions and an inventory `set`, so it's easy to extend: add a new scene function, give it a choice with `ask()`, and use `inventory.add(...)` / `"item" in inventory` to make choices matter.
