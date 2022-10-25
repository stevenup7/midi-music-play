from enum import Enum

# midi supports 127 notes from C-1 up to G9
C_MINUS_1 = 0
G9 = 127
MIDI_NOTE_RANGE = (C_MINUS_1, G9)

NOTE_NAMES = ["C", "C♯", "D", "D♯", "E", "F", "F♯", "G", "G♯", "A", "A♯", "B"]


class SCALE_TYPES(Enum):
    """the types of scales"""

    MAJOR = 1
    MINOR = 2
    IONIAN = 3
    DORIAN = 4
    PHYGIAN = 5
    LYDIAN = 6
    MIXOLYDIAN = 7
    AEOLIAN = 8
    LOCRIAN = 9


# how many semitones per step in a scale
class SCALE_OFFSETS(Enum):
    """a clean way to express scale offests"""

    NONE = 0
    HALF = 1
    WHOLE = 2


SCALE_OFFSETS = {
    SCALE_TYPES.MAJOR: [
        SCALE_OFFSETS.NONE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.HALF,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.HALF,
    ],
    SCALE_TYPES.MINOR: [
        SCALE_OFFSETS.NONE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.HALF,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.HALF,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
    ],
    SCALE_TYPES.IONIAN: [
        SCALE_OFFSETS.NONE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.HALF,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.HALF,
    ],
    SCALE_TYPES.DORIAN: [
        SCALE_OFFSETS.NONE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.HALF,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.HALF,
        SCALE_OFFSETS.WHOLE,
    ],
    SCALE_TYPES.PHYGIAN: [
        SCALE_OFFSETS.NONE,
        SCALE_OFFSETS.HALF,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.HALF,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
    ],
    SCALE_TYPES.LYDIAN: [
        SCALE_OFFSETS.NONE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.HALF,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.HALF,
    ],
    SCALE_TYPES.MIXOLYDIAN: [
        SCALE_OFFSETS.NONE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.HALF,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.HALF,
        SCALE_OFFSETS.WHOLE,
    ],
    SCALE_TYPES.AEOLIAN: [
        SCALE_OFFSETS.NONE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.HALF,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.HALF,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
    ],
    SCALE_TYPES.LOCRIAN: [
        SCALE_OFFSETS.NONE,
        SCALE_OFFSETS.HALF,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.HALF,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
        SCALE_OFFSETS.WHOLE,
    ],
}

SCALE_TYPE_NAMES = {
    SCALE_TYPES.MAJOR: "Major",
    SCALE_TYPES.MINOR: "Minor",
    SCALE_TYPES.IONIAN: "Ionian",
    SCALE_TYPES.DORIAN: "Dorian",
    SCALE_TYPES.PHYGIAN: "Phygian",
    SCALE_TYPES.LYDIAN: "Lydian",
    SCALE_TYPES.MIXOLYDIAN: "Mixolydian",
    SCALE_TYPES.AEOLIAN: "Aeolian",
    SCALE_TYPES.LOCRIAN: "Locrian",
}

NOTE_ALIASES = {
    "D♭": "C♯",
    "E♭": "D♯",
    "G♭": "F♯",
    "A♭": "G♯",
    "B♭": "A♯",
    "C♯": "D♭",
    "D♯": "E♭",
    "F♯": "G♭",
    "G♯": "A♭",
    "A♯": "B♭",
}

SHARP_FLAT_ALIASES = {
    "#": "♯",
    "3": "♯",
    "b": "♭",
}


def fix_note_string(input_str):
    """# clean up the string (uppercase and replace # for ♯ and b with ♭)"""
    # TODO: put this funciton somewhere better
    note = input_str[0]
    note = note.upper()
    accidental = ""
    if len(input_str) == 2:
        accidental = input_str[1]
        for alias, actual in SHARP_FLAT_ALIASES.items():
            accidental = accidental.replace(alias, actual)
    return note + accidental


def is_alias_of(input_str, expected_str):
    """test if two note names are equivalent eg "D♭" == "C♯"""
    # TODO: put this funciton somewhere better

    # they are the same
    if input_str == expected_str:
        return True
    # the input_str does not have an alias
    if not input_str in NOTE_ALIASES:
        return False
    # the input_str does have a matching alias
    if NOTE_ALIASES[input_str] == expected_str:
        return True
    return False
