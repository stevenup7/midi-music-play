# https://stackoverflow.com/questions/60182510/mido-how-to-get-midi-data-in-realtime-from-different-ports
# the following has a note chart that makes a lot of sense
# https://www.noterepeat.com/articles/how-to/213-midi-basics-common-terms-explained


def init():
    tm = new TuringMachine()

    midiListener =  new MidiListener()


if __name__ == "__main__":
    init()




class MidiListener():
    def __init__(self):
        self._chanel = 0


    def listen(self):
        if self._chanel == 0:
            print("no chanel set");
            return None
        while 1:

            break;

class TuringMachine():
    def __init__(self):
        this._tape = []
