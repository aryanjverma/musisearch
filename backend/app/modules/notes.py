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
        self.accepted_denominators= [1,2,3,4,6,8,12,16,18,24,32]
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
    def __eq__(self, other):
        if not isinstance(other, Melody):
            return False
        return (self.pitches == other.pitches and 
                self.durations == other.durations and 
                self.notes == other.notes)
    def __getitem__(self, key):
        if isinstance(key, slice):
            return Melody([],[],self.notes[key.start:key.stop])
        elif isinstance(key, int):
            return self.notes[key]
        else:
            raise TypeError("Index must be an integer or a slice")
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
        timestamps = midi_data.get_tempo_changes()[0]
        tempos = midi_data.get_tempo_changes()[1]
        i = 0
        s = 0
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
            if timestamps[s] < notes[i].start:
                while s < len(timestamps) - 1 and timestamps[s + 1] < notes[i]. start:
                    s += 1
            duration *= tempos[s] / 60
            i = j
            self.add_note(Note(max(new_pitches), self.round_rhythm(duration)))
        return
    def round_rhythm(self, rhythm):
        for den in self.accepted_denominators:            
            remainder = rhythm % (1/den)
            if remainder < 0.03 or (remainder > 1/den - 0.03):
                return round(rhythm * den) / den
class Part:
    def __init__(self, instrument_name, notes,timestamps,tempos):
        self.accepted_denominators = [1,2,3,4,6,8,12,16,18,24,32]
        self.instrument_name= instrument_name
        self.raw_notes = notes
        self.timestamps = timestamps
        self.tempos = tempos
        self.part_pitches = []
        self.part_durations = []
        self.create_part()
    def create_part(self):
        timestamps = self.timestamps
        tempos = self.tempos
        i = 0
        s = 0
        while i < len(self.raw_notes):
            new_pitches = []
            new_pitches.append(self.raw_notes[i].pitch)
            j = i + 1
            while j < len(self.raw_notes) and self.raw_notes[j].start - self.raw_notes[i].start < 0.01:
                new_pitches.append(self.raw_notes[j].pitch)
                j += 1
            duration = self.raw_notes[i].get_duration()
            if j < len(self.raw_notes):
                duration += self.raw_notes[j].start - self.raw_notes[i].end
            if timestamps[s] < self.raw_notes[i].start:
                while s < len(timestamps) - 1 and timestamps[s + 1] < self.raw_notes[i].start:
                    s += 1
            duration *= tempos[s] / 60
            i = j
            self.add_note((new_pitches), self.round_rhythm(duration))
        return
    def part_to_melody(self):
        melody = Melody([],[])
        for pitches, duration in zip(self.part_pitches, self.part_durations):
            melody.add_note(Note(max(pitches), duration))
        return melody
    def add_note(self, pitches, duration):
        self.part_pitches.append(pitches)
        self.part_durations.append(duration)
        return
    def round_rhythm(self, rhythm):
        for den in self.accepted_denominators:            
            remainder = rhythm % (1/den)
            if remainder < 0.03 or (remainder > 1/den - 0.03):
                return round(rhythm * den) / den
class Score:
    def __init__(self, midi_path):
        self.midi = pretty_midi.PrettyMIDI(midi_path)
        self.score = self.create_score()
    def create_score(self):
        self.score = {}
        for instrument in self.midi.instruments:
            if not instrument.is_drum and len(instrument.notes) > 0:
                melody_instrument = instrument
                self.score[melody_instrument] = Melody(melody_instrument.notes)
        return self.score