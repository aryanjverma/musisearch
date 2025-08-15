import modules.notes as md

def main():
    midi_file = "Happy-Birthday-To-You-1.mid"
    song_melody = md.Melody([], [])
    song_melody.song_to_melody(midi_file)
    print(song_melody)
main()