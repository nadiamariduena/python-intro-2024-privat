# ------ **
print('---- example range 1 ----')
#------- **
#
#

for i in range(5):
    print(i)

# result
# 0
# 1
# 2
# 3
# 4
#
#

# ------ **
print('---- example range 2 ----')
#------- **
#
#

playlist = ["Shape of You", "Despacito", "Uptown Funk", "See You Again", "Closer"]

print("My Spotify Playlist:")
##
# len(playlist) returns the length of the playlist, which is the number of tracks.
#
# i iterates over each number generated by range(), representing the track number.

#
for i in range(len(playlist)):
    #
    #range(len(playlist)) generates a sequence of numbers from 0 to len(playlist) - 1. This sequence corresponds to the indices of the tracks in the playlist.
    #
    print(f"{i+1}. {playlist[i]}")
    #  playlist[i] accesses each track title using the current value of i.

    #
    #
# RESULT:
# My Spotify Playlist:
#1. Shape of You
# 2. Despacito
# 3. Uptown Funk
# 4. See You Again
# 5. Closer
#
# ------ **
print('---- example enumerate 3 ----')
#------- **
#
playlist = ["Shape of You", "Despacito", "Uptown Funk", "See You Again", "Closer"]

print("My Spotify Playlist:")
#
#
for i, track in enumerate(playlist, start=1):
    print(f"{i}. {track}")
# RESULT:
# My Spotify Playlist:
#1. Shape of You
# 2. Despacito
# 3. Uptown Funk
# 4. See You Again
# 5. Closer
#

# ------ **
print('---- example 4 ----')
#------- **
#
playlist = ["Shape of You", "Despacito", "Uptown Funk", "See You Again", "Closer"]

print("My Spotify Playlist:")
tracks_with_numbers = [f"{i+1}. {track}" for i, track in enumerate(playlist)]
for track_with_number in tracks_with_numbers:
    print(track_with_number)
# RESULT:
# My Spotify Playlist:
#1. Shape of You
# 2. Despacito
# 3. Uptown Funk
# 4. See You Again
# 5. Close

#
#
# ------ **
print('---- example range 5 ----')
#------- **
#
# ------------
#  basic examples
#
names = ['dace', 'sarah', 'john']
for x in names:
    print(x)
    #result
#     dace
# sarah
# john
#
#
# ------ **
print('---- example 6 ----')
#------- **
#

for x in 'Mississippi':
    print(x)
# RESULT

# M
# i
# s
# s
# i
# s
# s
# i
# p
# p
# i

# ------ **
print('---- example 7 ----')
#------- **
#
# LOOP over the list and check if there is a specific name

names2 = ['romeo', 'chiara', 'charles']

for xx in names2:
    if xx == 'romeo':
      break
print(xx)
# result: romeo