# pylint: disable=unused-import
from colorama import Fore, Back, Style
from music_constants import NOTE_NAMES
from midi_notes import Note

# chords from here maybe https://pypi.org/project/pychord/

DRAWING = """
---------------------------------------------------------
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  |b| |d|  |  |g| |i| |k|  |  |n| |p|  |  |s| |u| |w|  |
|  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| a | c | e | f | h | j | l | m | o | q | r | t | v | x |
|___|___|___|___|___|___|___|___|___|___|___|___|___|___|

"""

DRAWING_DIGI = """

-------- Octave 0 -------------       -------- Octave +1 ------------
[ ] [b] [d] [ ] [g] [i] [k] [ ]   |   [ ] [n] [p] [ ] [s] [u] [w] [ ]

[a] [c] [e] [f] [h] [j] [l] [m]   |   [m] [o] [q] [r] [t] [v] [x] [y]
-------------------------------       -------------------------------
"""


NOTE_MAP = {
    "C": ["a", "m", "y"],
    "C♯": ["b", "n"],
    "D": ["c", "o"],
    "D♯": ["d", "p"],
    "E": ["e", "q"],
    "F": ["f", "r"],
    "F♯": ["g", "s"],
    "G": ["h", "t"],
    "G♯": ["i", "u"],
    "A": ["j", "v"],
    "A♯": ["k", "w"],
    "B": ["l", "x"],
}


class Keyboard:
    """text representation of a keyboard"""

    def __init__(self):

        pass

    def render(self, notes, as_digi=False, hide_names=False, render_notes=False):
        if as_digi:
            d = DRAWING_DIGI.strip()
            d = d.replace("[ ]", f"{Style.DIM}{Fore.WHITE}[ ]{Style.RESET_ALL}")
        else:
            d = DRAWING.strip()

        if isinstance(notes, Note):
            print("Its a note")
            # TODO: deal with a single note
        else:
            octave = 0
            last_index = 0
            curr_note_name = "*"

            for n in notes:

                note_index = NOTE_NAMES.index(n)

                # have we wrapped around to a new octave
                if note_index < last_index:
                    octave = octave + 1
                if hide_names is False:
                    curr_note_name = n.replace("#", "")
                # natural notes
                d = d.replace(
                    f"| {NOTE_MAP[n][octave]} |",
                    f"| {Style.BRIGHT}{Fore.RED}{curr_note_name}{Style.RESET_ALL} |",
                )
                # sharps/flats
                d = d.replace(
                    f"|{NOTE_MAP[n][octave]}|",
                    f"|{Style.BRIGHT}{Fore.RED}{curr_note_name}{Style.RESET_ALL}|",
                )
                # digi render
                d = d.replace(
                    f"[{NOTE_MAP[n][octave]}]",
                    f"[{Style.BRIGHT}{Fore.RED}{curr_note_name}{Style.RESET_ALL}]",
                )

                last_index = note_index

        # clear all the unused note names from the drawing
        for n in range(ord("a"), ord("y") + 1):
            d = d.replace(f"| {chr(n)} |", "|   |")
            d = d.replace(f"|{chr(n)}|", "| |")
            d = d.replace(f"[{chr(n)}]", "[ ]")

        if render_notes:
            return f"\r\n{notes}\r\n{d}\r\n"

        return f"\r\n{d}\r\n"
