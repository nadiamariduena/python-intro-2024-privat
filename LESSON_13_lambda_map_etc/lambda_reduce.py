
# ** REDUCE
#reduce: reduce() is a function from the functools module in Python. It applies a function of two arguments cumulatively to the items of an iterable (such as a list), from left to right, so as to reduce the iterable to a single value.
#
#
#

# ** 1)--- sum up the list
#---------------------------
from functools import reduce
#----------------------------
# accumulator
# current
numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers)

print(total)

# result
# 16
# it s doing an addition of 1 + 2 + 3 + 4 + 5 +1
# THE BELOW is the equivalent but without the rreduce
def sum_total(a,b): return  a + b
print(sum_total(10,19))
#result
#29
#
#
numbers_0 = [2, 4,6, 6]

# Using lambda function to sum up the values of the list

sum_0 = reduce(lambda x, y: x + y, numbers_0)

print("Sum of numbers", sum_0)

# result
#Sum of numbers 18
#
#
# ** 2)--- Finding the maximum number in a list using reduce and a lambda function:

numbers_2 = [10, 20, 5]

# Using lambda function to find the maximum number
#lambda x, y: x if x > y else y: This is a lambda function that takes two arguments, x and y, representing two elements from the list numbers. It compares these two elements and returns the greater one.
max_number = reduce(lambda x, y: x if x > y else y, numbers_2)
#If x is greater than y, it returns x.
# Otherwise, it returns y.

print("Maximum number:", max_number)

# result
#Maximum number: 20

#
# SPOTIFY
# ------------
# FIND THE DURATION OF A List
# ------------

playlist_durations = [180, 240, 200, 300, 210] # duration of songs in seconds

# find the total duration
total_duration = reduce(lambda x, y: x + y, playlist_durations)

print("Total duration of the playlist:", total_duration, "seconds")