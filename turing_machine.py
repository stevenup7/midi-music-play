from midi_notes import MidiNotes, Scale
from music_constants import NOTE_NAMES, SCALE_TYPES
import random
import time

RANGES = {
    0: 1,
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 1,
    6: 2,
    7: 2,
    8: 2,
    9: 3,
    10: 3,
}

note_distributions = [2, 7, 3, 1, 5, 4, 6]


class MelodyMachineGenes:
    def __init__(self):
        # to make a melody you might want to have
        #   length (how many beats)
        #   key
        #   range (how many octaves)
        #   density (how many rests)
        #   bpm
        #   chordyness (how often two notes play together)
        self.generate_random()

    def generate_random(self):
        self.bpm = 120
        self.key = random.choice(NOTE_NAMES)
        self.scale_type = random.choice(list(SCALE_TYPES))
        # skew towards 1 octave
        self.range = RANGES[random.randint(1, 10)]
        self.length = random.randint(1, 4) * 16


class MelodyMachine:
    def __init__(self):
        self.tape_length = 8
        self._tape = []
        self.create_genes()
        self.note16th = 60 / self.genes.bpm / 16
        self.scale = Scale(self.genes.key, self.genes.scale_type)
        self.generate()

    def create_genes(self):
        self.genes = MelodyMachineGenes()

    def generate(self):
        self.generate_notes()
        self.generate_gates()

    def generate_notes(self):
        print("generating - list of notes")
        self.notelist = []
        for n in range(0, self.genes.length):
            r = self.scale.notes[min(round(random.gauss(4, 4 / 3)), 7)]
            self.notelist.append(r)

    def generate_gates(self):
        self.gatelist = []
        for n in range(0, self.genes.length):
            g = random.randint(0, 1)
            self.gatelist.append(g)

    def midi_play(self):
        isOn = False
        note = None

        while True:
            for i in range(0, self.genes.length):
                if isOn:
                    self.midi_note_off(note)
                if self.gatelist[i] == 1:
                    isOn = True
                    note = self.notelist[i]
                    self.midi_note_on(note)

                time.sleep(self.note16th)

    def midi_note_on(self, note):
        print(f"note {note} on")

    def midi_note_off(self, note):
        print(f"note {note} off")


def init():
    mm = MelodyMachine()
    mm.midi_play()


if __name__ == "__main__":
    init()
