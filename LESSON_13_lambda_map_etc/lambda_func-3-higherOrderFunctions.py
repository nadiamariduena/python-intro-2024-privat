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

#
#
# ** FILTER
numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter with lambda to FILTER out even numbers

even_numbers = list(filter(lambda x: x % 2 == 0, numbers_2))

