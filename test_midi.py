from midi_notes import MidiNotes, Scale, SCALE_TYPES


def test_generation():
    m = MidiNotes()
    assert m.note_map["C4"].note == "C"
    assert m.note_map["C4"].midinote == 60
    assert m.note_map["C-1"].note == "C"
    assert m.note_map["C-1"].midinote == 0
    assert m.midi_map[127].name == "G9"


def test_scale():
    s = Scale("C", SCALE_TYPES.MAJOR)
    assert s.notes == ["C", "D", "E", "F", "G", "A", "B", "C"]
    s = Scale("D", SCALE_TYPES.MINOR)
    assert s.notes == ["D", "E", "F", "G", "A", "A#", "C", "D"]
