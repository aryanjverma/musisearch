import pretty_midi
import numpy as np
import fractions
from typing import Tuple, List

Melody = Tuple[List[int], List[float]]
def extract_pitches(midi_path):
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
    notes_and_durations = []
    i = 0
    while i < len(notes):
        new_notes = []
        new_notes.append(notes[i].pitch)
        j = i + 1
        while j < len(notes) and notes[j].start - notes[i].start < 0.01:
            new_notes.append(notes[j].pitch)
            j += 1
        duration = notes[i].get_duration()
        if j < len(notes):
            duration += notes[j].start - notes[i].end
        duration *= tempo / 60
        notes_and_durations.append((new_notes, round(duration, 3)))
        i = j
    return notes_and_durations
def find_time_signature(midi_path):
    midi_data = pretty_midi.PrettyMIDI(midi_path)
    time_signature_changes = midi_data.time_signature_changes
    if not time_signature_changes:
        raise ValueError("No time signature found in MIDI file")
    # Assuming the first time signature is the one we want
    return time_signature_changes[0].numerator, time_signature_changes[0].denominator
def create_midi_file(notes_and_durations, output_path, tempo):
    midi_data = pretty_midi.PrettyMIDI()
    melody_instrument = pretty_midi.Instrument(program=0)

    start_time = 0.0

    for pitch, duration in notes_and_durations:
        delta = duration * 60/tempo
        note = pretty_midi.Note(
            velocity=100,
            pitch=pitch,
            start=start_time,
            end=start_time + delta
        )
        melody_instrument.notes.append(note)
        start_time += delta

    midi_data.instruments.append(melody_instrument)
    midi_data.write(output_path)

def extract_melody(notes_and_durations):
    notes = []
    rhythm = []
    
    for pitches, duration in notes_and_durations:
        pitches = np.array(pitches)
        if len(pitches) > 0:
            notes.append(int(np.max(pitches)))
            rhythm.append(float(duration))
    return (notes, rhythm)


def ask_melody():
    print("Type in the melody you want to search for:")
    while True:
        notes = input("Enter the notes (comma-separated, e.g., C4, D4, E4): ").strip( ).split(',')
        
        durations = input("Enter the durations (comma-separated, e.g., 0.5, 0.25): ").strip( ).split(',')
        note_numbers = []
        for note in notes:
            note_number = note_to_number(note.strip())
            if note_number is not None:
                note_numbers.append(note_number)
            else:
                print(f"Invalid note: {note}")
        new_durations = []
        for duration in durations:
            try:
                new_durations.append(float(duration.strip()))
            except ValueError:
                print(f"Invalid duration: {duration}")
                return None
        return (note_numbers, new_durations)
def create_note_array(melody, smallest_note):
    melody_notes, melody_rhythm = melody
    note_array = []
    for index in range(len(melody_notes)):
        note =melody_notes[index]
        duration = melody_rhythm[index]
        for _ in range(int(duration / smallest_note)):
            note_array.append(int(note))
    return note_array
def are_melodies_similar(melody1, melody2):
    difference_array = []
    for index in range(len(melody1)):
        difference_array.append(melody1[index] - melody2[index])
    standard_deviation = np.std(difference_array)
    return standard_deviation < 1

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

def find_melody_in_song(song, melody):
    smallest_note = find_smallest_note(melody, song)
    
    song_array = create_note_array(song, smallest_note)
    melody_array = create_note_array(melody, smallest_note)
    for i in range(len(song_array) - len(melody_array) + 1):
        if are_melodies_similar(song_array[i:i + len(melody_array)], melody_array):
            print("Melody found!")
            return int(i * smallest_note + 0.5)
    return -1
midi_file = "Happy-Birthday-To-You-1.mid"
pattern = extract_pitches(midi_file)
time_signature = find_time_signature(midi_file)
song_melody = extract_melody(pattern)
print(song_melody)
user_melody = ask_melody()
user_melody = np.array(user_melody)
index = find_melody_in_song(song_melody, user_melody)
print(index)
print(song_melody[index])
#output_midi_file = "output.mid"
#tempo = 120
#create_midi_file(melody, output_midi_file, tempo)
