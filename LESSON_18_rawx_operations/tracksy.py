# Example of writing Spotify tracks to a file
# the "tracks list below is going to be added to the "spotify_tracks.txt"  from the moment you run the code"
tracks = [
    "Track 1: Song Name 1",
    "Track 2: Song Name 2",
    "Track 3: Song Name 3"
]

filename = 'spotify_tracks.txt'

# Open file in write mode
# --- will generate with "open" the spotify_tracks.txt
with open(filename, 'w') as file:
    for track in tracks:
        # the "w" will add the tracks to the "file", remember: tracks is track
        file.write(track + '\n')  # Write each track followed by a newline
