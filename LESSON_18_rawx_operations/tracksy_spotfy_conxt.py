# Example of reading multiple files and combining data
filenames = ['tracks_spot_playlist1.txt', 'tracks_spot_playlist2.txt']

#
#
# Using context manager to manage multiple file operations
# will generate the tracks_combined_playlist.txt
with open("tracks_combined_playlist.txt", "w") as combined_file:
