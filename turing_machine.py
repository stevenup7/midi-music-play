from midi_notes import MidiNotes, Scale
from midi_bars import MidiBar
from music_constants import NOTE_NAMES, SCALE_TYPES
import random
import time
import math
from scipy.stats import halfnorm

skewed_normal_t = halfnorm.rvs(0, 0.3, 5000)
skewed_normal = []
# there has to be a better way but this works
for i, v in enumerate(skewed_normal_t):
    if v < 1:
        skewed_normal.append(v)

#  |_
#  | |
#  | |_mylar
#  | | |
#  | | |
#  | | |_
#  | | | |_
#  | | | | |_ _
#  |_|_|_|_|_|_|____

note_choosing_functions = {}


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
        global skewed_normal
        self.bpm = random.randint(30, 300)
        self.key = random.choice(NOTE_NAMES)
        self.scale_type = random.choice(list(SCALE_TYPES))
        self.scale = Scale(self.key, self.scale_type)
        # skew towards 1 octave
        self.range = math.floor(random.choice(skewed_normal) * 3) + 1

        self.length = random.randint(1, 4) * 16
        self.notes_ordered = random.sample(self.scale.notes, len(self.scale.notes))


class MelodyMachine:
    def __init__(self):
        self.bar = MidiBar()
        self.create_genes()
        self.ppqnTime = 60 / self.genes.bpm / 24

        self.length = self.genes.length
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
            r = self.genes.scale.notes[min(round(random.gauss(4, 4 / 3)), 7)]
            self.notelist.append(r)

    def generate_gates(self):
        print("generating - list of gates")
        self.gatelist = []
        for n in range(0, self.genes.length):
            g = random.randint(0, 1)
            self.gatelist.append(g)


class MelodyMachinePlayer:
    def __init__(self, melody_machine):
        self.machine = melody_machine

    def midi_play(self):
        isOn = False
        note = None

        while True:
            for i in range(0, self.machine.length):
                if isOn:
                    self.midi_note_off(note)
                if self.machine.gatelist[i] == 1:
                    isOn = True
                    note = self.machine.notelist[i]
                    self.midi_note_on(note)
                time.sleep(self.machine.ppqnTime)

    def midi_note_on(self, note):
        print(f"note {note} on")

    def midi_note_off(self, note):
        pass
        # print(f"note {note} off")


def init():
    mm = MelodyMachine()
    mp = MelodyMachinePlayer(mm)
    mp.midi_play()


if __name__ == "__main__":
    init()
