
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
#--------------

# ------ **
print('---- example 12 RANGE   ----')
#------- **
# Assuming you have a list of songs and their durations in seconds
songs = [("Song 1", 180),  # Song name and duration in seconds
         ("Song 2", 240),
         ("Song 3", 200)]

# Iterate over each song
for song_name, duration in songs:
    print(f"Song: {song_name}")
    print("Timestamps:")
    # Generate timestamps at 5-second intervals for the duration of the song
    for timestamp in range(0, duration, 5):
        print(f"{timestamp} seconds")
    print()


#
#
# -------------
# ------ **
print('---- example 13 RANGE   ----')
#------- **

# Sample timestamps representing user actions (in seconds)
timestamps = [10, 25, 45, 60, 70, 90, 110, 120, 140]

# Calculate engagement metrics
total_watch_time = timestamps[-1]  # Last timestamp represents total watch time
average_watch_time = total_watch_time / len(timestamps)
retention_rate = (len(timestamps) / total_watch_time) * 100  # Percentage of total watch time covered by timestamps

# Analyze engagement by segmenting timestamps
segments = []
#
#
current_segment_start = 0
# for timestamp in timestamps:
#     segment_duration = timestamp - current_segment_start
#     segments.append((current_segment_start, segment_duration))
#     current_segment_start = timestamp

for timestamp in timestamps:
    # Calculate the duration of the current segment by subtracting the start time of the current segment
    # from the timestamp of the next segment
    segment_duration = timestamp - current_segment_start

    # Append a tuple containing the start time of the current segment and its duration to the list of segments
    segments.append((current_segment_start, segment_duration))

    # Update the start time of the next segment to be the current timestamp for the next iteration
    current_segment_start = timestamp



# Display results
print("Engagement Metrics:")
print(f"Total Watch Time: {total_watch_time} seconds")
print(f"Average Watch Time: {average_watch_time} seconds")
# Print the retention rate with 2 decimal places and a percentage sign
print(f"Retention Rate: {retention_rate:.2f}%")

# Print a new line followed by a heading for segment analysis
print("\nSegment Analysis:")

# Iterate over the segments list using enumerate to get both the index and the segment tuple
for i, (start, duration) in enumerate(segments, 1):
    # Print the segment number (index + 1), start time, and duration of each segment
    print(f"Segment {i}: Start Time = {start} seconds, Duration = {duration} seconds")
    #
    # RESULT:
#Engagement Metrics:
# Total Watch Time: 140 seconds
# Average Watch Time: 15.555555555555555 seconds
# Retention Rate: 6.43%

# Segment Analysis:
# Segment 1: Start Time = 0 seconds, Duration = 10 seconds
# Segment 2: Start Time = 10 seconds, Duration = 15 seconds
# Segment 3: Start Time = 25 seconds, Duration = 20 seconds
# Segment 4: Start Time = 45 seconds, Duration = 15 seconds
# Segment 5: Start Time = 60 seconds, Duration = 10 seconds
# Segment 6: Start Time = 70 seconds, Duration = 20 seconds
# Segment 7: Start Time = 90 seconds, Duration = 20 seconds
# Segment 8: Start Time = 110 seconds, Duration = 10 seconds
#
#---
# Segment 9: Start Time = 120 seconds, Duration = 20 seconds
# -------------
# ------ **
print('---- example 14 for loop & else statement   ----')
#------- **

for xmore in range(5, 101, 5):
    print(xmore)
else:
    print('Glad that\'s over!')

    # result:

#     5
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
# 100
# Glad that's over!

# ------ **
print('---- example 15  NESTED loops----')
#------- **

#looping through 2 different lists

names2 = ['Daria', 'Esze', 'Somal']
actions = ['codes',  'eats', 'sleeps']

#
#for each name we are going to do something
for name in names2:
    for action in actions:
        print(name + ' ' + action + '.')
#result
# Daria codes.
# Daria eats.
# Daria sleeps.
# Esze codes.
# Esze eats.
# Esze sleeps.
# Somal codes.
# Somal eats.
# Somal sleeps.
#
# --------- **
print('------ nested loop 2')
## Now get the opposite
#
names3 = ['Daria', 'Esze', 'Somal']
actions3 = ['codes',  'eats', 'sleeps']
#
#
for action3 in actions3:
    for name3 in names3:
        print(name3 + ' ' + action3 + '.')
# result:
#🖐️ notice the difference, here we inserted the name inside the loop 1, compare the result with the result of the 1 nested loop
#
#Daria codes.
# Esze codes.
# Somal codes.
# Daria eats.
# Esze eats.
# Somal eats.
# Daria sleeps.
# Esze sleeps.
# Somal sleeps.
#🖐️ its also possible to add more for loops within, but check first how this can affect the performance

# --------- **
print('------ nested loop 3')
print('------ nested loop 3')
## more loops, in this one i will have 4 lists to include in 4 loops

names4 = ["Alice", "Bob", "Charlie"]
activities = ["running", "swimming", "cycling"]
foods = ["pizza", "sushi", "burgers"]
cities = ["New York", "Los Angeles", "Chicago"]

for name4 in names4:
    for activity in activities:
        for food in foods:
            for city in cities:
                print(f"{name4} likes {activity}, enjoys eating {food}, and lives in {city}")