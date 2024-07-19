filename = "tracks_exe_0_.txt"

#open file in read mode
with open(filename, "r") as file:
    for line in file:
        # will show the content of the tracks.txt in your console
        print(line.strip())

# output
#track_1: TEMPLEOFJOY 110 - IMMINENT
# track_2: Kai Pattenberg - Obvilion
#
#-----------------------------------
