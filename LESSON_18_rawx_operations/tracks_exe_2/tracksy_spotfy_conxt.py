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
           #
           #
           #Write a header indicating the filename
           # filename carries the list name
           combined_file.write('___ 🟡 ____\n')
           combined_file.write(f"=== {filename} ===\n")
           # The f before a string literal in Python, such as f"=== {filename} ===\n", denotes an f-string (formatted string literal). F-strings provide a way to embed expressions inside string literals, using curly braces {}.

           #
           # it will add a line after each track( i added the invader so to see it)
           # Iterate over each line in the current file
           for line in file:
               #Write each line to the combined file (space)
               combined_file.write(line)

            # add a new
               combined_file.write('👾 \n')


