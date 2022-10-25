# learn the names of the notes
# TODO: learn chords
# TODO: learn scales

from random import choices
import os
from time import sleep

# pylint: disable=unused-import
from colorama import Fore, Back, Style
from keyboard import Keyboard
from music_constants import NOTE_NAMES, fix_note_string, is_alias_of


def cls():
    """clear the screen"""
    os.system("cls" if os.name == "nt" else "clear")


k = Keyboard()
START_WEIGHT = 10
WEIGHT_ADJUST = 5


def adjust_weights(note, is_correct, weights):
    """pass in the list of weights and the note and
    right or wrong this function will adjust the weights"""

    i = NOTE_NAMES.index(note)

    if is_correct:
        if weights[i] >= WEIGHT_ADJUST:
            weights[i] = weights[i] - WEIGHT_ADJUST
        if weights[i] < 1:
            weights[i] = 1
    else:
        if weights[i] <= START_WEIGHT * 2:
            weights[i] = weights[i] + WEIGHT_ADJUST
        if weights[i] > START_WEIGHT * 2:
            weights[i] = START_WEIGHT * 2


def learn_notes():
    """shows a keybard with a dot on it, user learns the note names ... yay"""

    is_done = False
    # list of weights for each note (if you get it wrong weight goes up, right weight goes down)
    note_weights = [START_WEIGHT] * len(NOTE_NAMES)
    result = ""

    while is_done is False:

        test_note = choices(NOTE_NAMES, weights=note_weights)[0]
        cls()

        print(k.render([test_note], hide_names=True))
        resp = input("what note is this?: ")

        if resp == "":
            # if no input then flip flag
            is_done = True
        else:
            # clean up the string (uppercase and replace # for ♯ and b with ♭)
            resp = fix_note_string(resp)

            # else check if they are correct
            if is_alias_of(resp, test_note):
                result = f"{Style.BRIGHT}{Fore.GREEN}✓ {resp}{Style.RESET_ALL}"
                adjust_weights(test_note, True, note_weights)
            else:
                print(k.render([test_note], hide_names=False))
                result = f"""{Style.BRIGHT}{Fore.RED}Wrong you guessed:{test_note}, answer is{test_note}{Style.RESET_ALL}"""
                adjust_weights(test_note, False, note_weights)
            print(result)
            sleep(0.5)
        # print(f"{sum(note_weights)} == {len(note_weights)} {note_weights}")
        if sum(note_weights) == len(note_weights):
            print(f"{Style.BRIGHT}{Fore.GREEN}## You win ##{Style.RESET_ALL}")
            is_done = True


def learn_scales():
    """teach the user the notes in a scale"""

    is_done = False
    # list of weights for each scale (if you get it wrong weight goes up, right weight goes down)
    scale_weights = [START_WEIGHT] * len(NOTE_NAMES)

    while is_done is False:
        guess = input("not done yet")
        if guess == "":
            is_done = True


def init():
    """main run shows menu
    loops until the end of user intput

    """

    menu = f"""
1) learn notes names on keyboard
2) learn scales
[all ther keys quit]
"""

    while True:
        option = input(menu)

        if option == "1":
            learn_notes()
        elif option == "2":
            learn_scales()
        else:
            break


if __name__ == "__main__":
    init()
