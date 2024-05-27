# Define a playlist with song titles
playlist = [
    "Song 1: Blinding Lights",
    "Song 2: Watermelon Sugar",
    "Song 3: Levitating",
    "Song 4: Peaches",
    "Song 5: Save Your Tears",
    "Song 6: Good 4 U",
    "Song 7: Kiss Me More"
]

# Initialize variables
value = True  # Control variable for the loop
count = 0     # Initialize count to 0

# Begin the loop to play songs
while value:
    count += 1       # Increase count by 1

    # Simulate playing the song by printing the title
    print(f"Playing {playlist[count - 1]}")

    if count == 5:   # Check if 5 songs have been played
        break        # If yes, stop the loop

