from turing_machine import MelodyMachineGenes, MelodyMachine
from music_constants import NOTE_NAMES, SCALE_TYPES


def test_random_generation():
    mg = MelodyMachineGenes()
    mg.generate_random()
    assert mg.key in NOTE_NAMES
    assert mg.scale_type in list(SCALE_TYPES)
    assert mg.range > 0
    assert mg.range < 4


def test_melody_generation():
    mm = MelodyMachine()
    for x in range(0, 100):
        mm = MelodyMachine()
    assert mm is not None
