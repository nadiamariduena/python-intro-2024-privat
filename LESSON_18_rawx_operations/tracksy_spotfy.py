# Example of writing Spotify tracks to a file
# the "tracks list below is going to be added to the "spotify_tracks.txt"  from the moment you run the code"
tracks = [
    "Track 1: James Blake - Limit To Your Love 💛",
    "Track 2: Feist - The Limit to your love🩷",
    "Track 3: Feist - 1234 🌈"
    "Track 4: Feist - Mushaboom 🎠"
]

filename = 'spotify_tracks.txt'

# Open file in write mode
# --- will generate with "open" the spotify_tracks.txt
with open(filename, 'w') as file:
    for track in tracks:
        # the "w" will add the tracks to the "file", remember: tracks is track
        file.write(track + '\n')  # Write each track followed by a newline
