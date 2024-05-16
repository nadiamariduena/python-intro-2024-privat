
# ------ ** CORRECTED
print('---- example 8 ----')
#------- **
#
# LOOP over the list and check if there is a specific name

thenames = ["Dave", "Sara", "John"]

for px in thenames:
# you will notice that it will jump and continue the loop after sara
    if px == 'Sara':
      continue
    print(px)
    #🔴 the problem why i couldnt get the 2 values as a result and only one, its because of the identation, read the MD about it
# result: Dave, John
#
#
# ------ **
print('---- example 9 RANGE (again) ----')
#------- **
#
## Do something similar with the RANGE

for example9 in range(2, 4):
    print(example9)

# result
# 2
# 3
#
#
# ------ **
print('---- example 10 RANGE (again) ----')
#------- **
# Sample Spotify playlist data
spotify_playlist = [
    {"title": "Song 1", "artist": "Artist 1", "genre": "Pop", "popularity": 85},
    {"title": "Song 2", "artist": "Artist 2", "genre": "Rock", "popularity": 70},
    {"title": "Song 3", "artist": "Artist 3", "genre": "Hip-hop", "popularity": 90},
    {"title": "Song 4", "artist": "Artist 4", "genre": "Electronic", "popularity": 80},
    {"title": "Song 5", "artist": "Artist 5", "genre": "Pop", "popularity": 75}
]

# Analyzing a range of songs in the playlist
for index in range(1, 4):  # Analyze songs from index 1 to 3 (excluding 4)
    song = spotify_playlist[index]
    print("Analyzing song:", song["title"])
    # Add your analysis code here

#🖐️ result

# Analyzing song: Song 2
# Analyzing song: Song 3
# Analyzing song: Song 4

#
#
#
# ------ **
print('---- example 11 RANGE   ----')
#------- **
# IN the following example
# we will start at 0, the second value means that we will go until 100 but since the condition states 100 we will go until 95, and the third value will determine how we want to reach the 100, in this case it will be 5 by 5

for x in range(0, 100, 5):
    print(x)
    #result:
#0
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50
# 55
# 60
# 65
# 70
# 75
# 80
# 85
# 90
# 95
#