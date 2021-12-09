# https://stackoverflow.com/questions/60182510/mido-how-to-get-midi-data-in-realtime-from-different-ports
# the following has a note chart that makes a lot of sense
# https://www.noterepeat.com/articles/how-to/213-midi-basics-common-terms-explained

import math
from keyboard import Keyboard
from music_constants import SCALE_TYPES, NOTE_NAMES, OFFSETS


class Note:
    def __init__(self, midinote=None, octave=None, note=None):
        if midinote is None and octave is None and note is None:
            raise Exception("You must provide either midi note or note and octave")
        self.midinote = midinote
        self.note = note
        self.octave = octave
        self.name = f"{self.note}{self.octave}"

    def __repr__(self):
        return (
            f"{self.name}, note: {self.note}, oct: {self.octave}, midi: {self.midinote}"
        )


class Scale:
    def __init__(self, root="C", scale_type=SCALE_TYPES.MAJOR):
        self.root = root
        self.scale_type = scale_type
        self.notes = []
        self.get_notes()

    def get_notes(self):
        offset = NOTE_NAMES.index(self.root)
        for n in range(0, 8):
            offset = offset + OFFSETS[self.scale_type][n]
            self.notes.append(NOTE_NAMES[offset % 12])

    def __repr__(self):
        return f"{self.root} {SCALE_TYPE_NAMES[self.scale_type]} {self.notes}"


class MidiNotes:
    def __init__(self):
        # note name as key
        self.note_map = {}
        # midi number as key
        self.midi_map = {}
        self.all_notes = []
        self.generateAll()

    def generateAll(self):
        for midinote in range(0, 128):
            notename = NOTE_NAMES[midinote % 12]
            octave = math.floor(midinote / 12) - 1
            n = Note(midinote=midinote, octave=octave, note=notename)
            self.midi_map[midinote] = n
            self.note_map[n.name] = n


def init():
    m = MidiNotes()

    print(" \r\n ")
    print("G MINOR ON DIGI")
    s = Scale("G", SCALE_TYPES.MINOR)
    k = Keyboard()
    print(k.render(s.notes))

    print("G MAJOR ON KEYBOARD")
    s2 = Scale("G", SCALE_TYPES.MAJOR)
    k = Keyboard()
    print(k.render(s2.notes))
    print(" \r\n ")


if __name__ == "__main__":
    init()
