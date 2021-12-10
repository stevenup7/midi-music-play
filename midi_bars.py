class MidiBar:
    def __init__(self):
        beats_per_bar = 4
        self.current_pulse = 0

    def reset(self):
        self.current_pulse = 0

    def step(self):
        this.current_pulse += 1
        if self.current_pulse % 24 == 0:
            print("1/4 note")
        if self.current_pulse % 24 * 4 == 0:
            print("1 note")
