from midi_notes import MidiNotes, Scale
from midi_bars import MidiBar
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

# we will select from this list using a normal distribution
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
        self.bpm = random.randint(30, 300)
        self.key = random.choice(NOTE_NAMES)
        self.scale_type = random.choice(list(SCALE_TYPES))
        # skew towards 1 octave
        self.range = RANGES[random.randint(1, 10)]
        self.length = random.randint(1, 4) * 16
        self.note_distribution = []
        for i in range(0, random.randint(self.range * 8)):
            print(i)


class MelodyMachine:
    def __init__(self):
        self.bar = MidiBar()
        self.create_genes()
        self.ppqnTime = 60 / self.genes.bpm / 24
        self.scale = Scale(self.genes.key, self.genes.scale_type)
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
            r = self.scale.notes[min(round(random.gauss(4, 4 / 3)), 7)]
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

            time.sleep(self.machine.ppqnTime)

            for i in range(0, self.machine.length):
                if isOn:
                    self.midi_note_off(note)
                if self.machine.gatelist[i] == 1:
                    isOn = True
                    note = self.machine.notelist[i]
                    self.midi_note_on(note)

    def get_midi_player(self):
        for p in mido.get_output_names():
            return print(p)

    def midi_note_on(self, note):
        print(f"note {note} on")

    def midi_note_off(self, note):
        print(f"note {note} off")


def init():
    mm = MelodyMachine()
    mp = MelodyMachinePlayer(mm)
    mp.get_midi_player()
    mp.midi_play()


if __name__ == "__main__":
    init()
