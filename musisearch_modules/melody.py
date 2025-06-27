import pretty_midi
import fractions
import numpy as np
def find_smallest_note(melody, song):
    melody_rhythm = melody.durations
    song_rhythm = song.durations
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
def similarity(tqz1,tqz2, max_stdv = 0.7):
        difference_array = []
        for index in range(len(tqz1)):
            difference_array.append(tqz1[index] - tqz2[index])
        standard_deviation = np.std(difference_array)
        return (1 - standard_deviation/max_stdv) * 100    
class Note:
    def __init__ (self, pitch, duration):
        if type(pitch) is str:
            self.pitch = self.text_to_number(pitch)
        else:
            self.pitch = int(pitch)
        self.duration = float(duration)
    def __repr__(self):
        return f"Note(pitch={self.pitch}, duration={self.duration})"
    def text_to_number(self,pitch):
        print(pitch)
        pitch = pitch.upper().strip()
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
    def __init__(self, pitches, durations, notes=None):
        if notes is None:
            self.notes = [Note(pitch, duration)for pitch, duration in zip(pitches, durations)] 
            self.pitches = pitches
            self.durations = durations
        else:
            self.notes = notes
            self.pitches = [note.pitch for note in notes]
            self.durations = [note.duration for note in notes]
    def __repr__(self):
        return f"Pitches(pitches={self.pitches}, durations={self.durations})"
    #tqz = time-quantized sequence
    def create_tqs(self, smallest_note):
        tqs = []
        for pitch,duration in zip(self.pitches, self.durations):
            for _ in range(int(duration / smallest_note)):
                tqs.append(int(pitch))
        return tqs
    def add_note(self, note):
        if type(note) is pretty_midi.Note:
            self.notes.append(Note(note.pitch, note.end - note.start))
            self.pitches.append(note.pitch)
            self.durations.append(note.end - note.start)
        elif type(note) is Note:
            self.notes.append(note)
            self.pitches.append(note.pitch)
            self.durations.append(note.duration)
        else:
            raise TypeError("Note must be a pretty_midi.Note or Note object")
    def song_to_melody(self, midi_path):
        midi_data = pretty_midi.PrettyMIDI(midi_path)
        melody_instrument = None
        for instrument in midi_data.instruments:
            if not instrument.is_drum and len(instrument.notes) > 0:
                melody_instrument = instrument
                break
        if melody_instrument is None:
            raise ValueError("No melodic instrument found")
        notes = sorted(melody_instrument.notes, key=lambda note: note.start)
        tempo = midi_data.get_tempo_changes()[1][0]
        i = 0
        while i < len(notes):
            new_pitches = []
            new_pitches.append(notes[i].pitch)
            j = i + 1
            while j < len(notes) and notes[j].start - notes[i].start < 0.01:
                new_pitches.append(notes[j].pitch)
                j += 1
            duration = notes[i].get_duration()
            if j < len(notes):
                duration += notes[j].start - notes[i].end
            duration *= tempo / 60
            i = j
            self.add_note(Note(max(new_pitches), round(duration, 3)))
        return
    def __getitem__(self, key):
        if isinstance(key, slice):
            return Melody([],[],self.notes[key.start:key.stop])
        elif isinstance(key, int):
            return self.notes[key]
        else:
            raise TypeError("Index must be an integer or a slice")