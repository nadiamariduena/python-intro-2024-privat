# Higher level functions
# its A function that takes one or more functions
#
# ** MAP
# 3 x 3= 9 etc
numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

# result
# [9, 49, 144, 324, 400, 441]

print("--------")
#
#
# ** FILTER
numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter with lambda to FILTER out even numbers

even_numbers = list(filter(lambda x: x % 2 == 0, numbers_2))

## remember
# The % operator returns the remainder of the division operation
# 4 % 2 equals 0 because 4 is evenly divisible by 2.
# 5 % 2 equals 1 because 5 divided by 2 leaves a remainder of 1.
print(list(even_numbers))
# result
#[2, 4, 6, 8, 10]

#
#
# SPOTIFY map example

# We want to filter out songs that are shorter than 200 seconds
# Let's assume we have a list of tuples where each tuple represents a song in the format (song_name, duration_in_seconds)
playlist = [("Song 1", 180), ("Song 2", 240), ("Song 3", 200), ("Song 4", 300), ("Song 5", 150)]


# We want to filter out songs that are shorter than 200 seconds
filtered_playlist = list(filter(lambda song: song[1] >= 200, playlist))
