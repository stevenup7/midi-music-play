from colorama import Fore, Back, Style

from music_constants import NOTE_NAMES

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
    "C#": ["b", "n"],
    "D": ["c", "o"],
    "D#": ["d", "p"],
    "E": ["e", "q"],
    "F": ["f", "r"],
    "F#": ["g", "s"],
    "G": ["h", "t"],
    "G#": ["i", "u"],
    "A": ["j", "v"],
    "A#": ["k", "w"],
    "B": ["l", "x"],
}


class Keyboard:
    def __init__(self):
        pass

    def render(self, notes, asDigi=False):
        if asDigi:
            d = DRAWING_DIGI.strip()
            d = d.replace("[ ]", f"{Style.DIM}{Fore.WHITE}[ ]{Style.RESET_ALL}")
        else:
            d = DRAWING.strip()

        octave = 0
        last_index = 0
        for n in notes:
            note_index = NOTE_NAMES.index(n)
            if note_index < last_index:
                octave = octave + 1
            d = d.replace(
                f"| {NOTE_MAP[n][octave]} |",
                f"| {Style.BRIGHT}{Fore.RED}{n.replace('#', '')}{Style.RESET_ALL} |",
            )
            d = d.replace(
                f"|{NOTE_MAP[n][octave]}|",
                f"|{Style.BRIGHT}{Fore.RED}{n.replace('#', '')}{Style.RESET_ALL}|",
            )
            d = d.replace(
                f"[{NOTE_MAP[n][octave]}]",
                f"[{Style.BRIGHT}{Fore.RED}{n.replace('#', '')}{Style.RESET_ALL}]",
            )

            last_index = note_index
        for n in range(ord("a"), ord("y") + 1):
            d = d.replace(f"| {chr(n)} |", "|   |")
            d = d.replace(f"|{chr(n)}|", "| |")
            d = d.replace(f"[{chr(n)}]", "[ ]")

        return f"\r\n{notes}\r\n{d}\r\n"
