import pretty_midi
import numpy as np
import fractions
from typing import Tuple, List
import melody as md

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
def ask_melody():
    print("Type in the melody you want to search for:")
    while True:
        pitches = input("Enter the pitch (comma-separated, e.g., C4, D4, E4): ").strip().split(',')
        durations = input("Enter the durations (comma-separated, e.g., 0.5, 0.25): ").strip().split(',')
        print(pitches)
        melody = md.Melody([], [])
        for index in range(len(pitches)):
            melody.add_note(md.Note(pitches[index], durations[index]))
        return melody
def are_melodies_similar(melody1, melody2):
    difference_array = []
    for index in range(len(melody1)):
        difference_array.append(melody1[index] - melody2[index])
    standard_deviation = np.std(difference_array)
    return standard_deviation < 1


def find_melody_in_song(song, melody):
    smallest_note = md.find_smallest_note(song, melody)
    
    song_array = song.create_tqs(smallest_note)
    melody_array = melody.create_tqs(smallest_note)
    for i in range(len(song_array) - len(melody_array) + 1):
        if are_melodies_similar(song_array[i:i + len(melody_array)], melody_array):
            print("Melody found!")
            return int(i * smallest_note + 0.5)
    return -1
midi_file = "Happy-Birthday-To-You-1.mid"
song_melody = md.Melody([], [])
song_melody.song_to_melody(midi_file)
time_signature = find_time_signature(midi_file)

print(song_melody)
user_melody = ask_melody()
print(user_melody)
index = find_melody_in_song(song_melody, user_melody)
print(index)
print(song_melody[index])
#output_midi_file = "output.mid"
#tempo = 120
#create_midi_file(melody, output_midi_file, tempo)
