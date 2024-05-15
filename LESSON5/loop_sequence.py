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

for i in range(len(playlist)):
    print(f"{i+1}. {playlist[i]}")
# RESULT:
# My Spotify Playlist:
#1. Shape of You
# 2. Despacito
# 3. Uptown Funk
# 4. See You Again
# 5. Closer
#