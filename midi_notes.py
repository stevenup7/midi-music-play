# https://stackoverflow.com/questions/60182510/mido-how-to-get-midi-data-in-realtime-from-different-ports
# the following has a note chart that makes a lot of sense
# https://www.noterepeat.com/articles/how-to/213-midi-basics-common-terms-explained

import math
from music_constants import SCALE_TYPES, NOTE_NAMES, SCALE_OFFSETS


class Note:
    def __init__(self, midinote=None, octave=None, note=None):
        if midinote is None and octave is None and note is None:
            raise Exception("You must provide either midi note or note and octave")
        self.midinote = midinote
        self.note = note
        self.octave = octave
        self.name = f"{self.note}{self.octave}"

    def get_note(self):
        return self.note

    def set_note(self, note):
        # TODO: error checking (char A-G + sharps and flats)
        self.note = note

    def get_octave(self):
        return self.octave

    def set_octave(self, octave):
        # TODO: error checking (integer)
        self.octave = octave

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
            offset = offset + SCALE_OFFSETS[self.scale_type][n].value
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
