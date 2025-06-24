import fractions
import numpy as np
def find_smallest_note(melody, song):
    melody_rhythm = melody[1]
    song_rhythm = song[1]
    denominators = []
    for rhythm in melody_rhythm:
        
        if rhythm > 0:
            denominators.append(fractions.Fraction(rhythm).limit_denominator(16).denominator)
    for rhythm in song_rhythm:
        if rhythm > 0:
            denominators.append(fractions.Fraction(rhythm).limit_denominator(16).denominator)
    denominators.pop()
    lcm = np.lcm.reduce(denominators)
    
    return 1 / lcm
class Note:
    def __init__ (self, pitch, duration):
        if type(pitch) is str:
            self.pitch = self.note_to_number(pitch)
        else:
            self.pitch = int(pitch)
        self.duration = float(duration)
    def __repr__(self):
        return f"Note(pitch={self.pitch}, duration={self.duration})"
    def text_to_number(self,pitch):
        pitch = pitch.upper()
        if len(pitch) < 2:
            return None
        elif len(pitch) == 2:
            return int(pitch[1]) * 12 + "C#D#EF#G#A#B".index(pitch[0].upper()) + 12
        else:
            if pitch[1] == '#':
                return int(pitch[2]) * 12 + "C#D#EF#G#A#B".index(pitch[0].upper()) + 13
            elif pitch[1] == 'b':
                return int(pitch[2]) * 12 + "C#D#EF#G#A#B".index(pitch[0].upper())  + 11
class Melody:
    def __init__(self, pitches, durations, max_stdv = 0.7):
        self.notes = [Note(pitch, duration)for pitch, duration in zip(pitches, durations)] 
        self.pitches = pitches
        self.durations = durations
        self.max_stdv = max_stdv
    def __repr__(self):
        return f"Pitches(pitches={self.pitches}, durations={self.durations})"
    #tqz = time-quantized sequence
    def create_tqs(self, smallest_note):
        tqs = []
        for pitch,duration in zip(self.pitches, self.durations):
            for _ in range(int(duration / smallest_note)):
                tqs.append(int(pitch))
        return tqs
    def similarity(self, other):
        difference_array = []
        for index in range(len(self.pitches)):
            difference_array.append(self.pitches[index] - other.pitches[index])
        standard_deviation = np.std(difference_array)
        return (1 - standard_deviation/self.max_stdv) * 100
    