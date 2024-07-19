# Example of reading multiple files and combining data
filenames = ['tracks_spot_playlist1.txt', 'tracks_spot_playlist2.txt']

#
#
# Using context manager to manage multiple file operations
# will generate the tracks_combined_playlist.txt
with open("tracks_combined_playlist.txt", "w") as combined_file:

   # for filename in filenames: Loop through each filename within the filenames list
   for filename in filenames:
       # Open each file in read mode
       with open(filename, "r") as file:
           #Write a header indicating the filename
           combined_file.write(f"=== {filename} ===\n")
           #
           #
           # Iterate over each line in the current file

