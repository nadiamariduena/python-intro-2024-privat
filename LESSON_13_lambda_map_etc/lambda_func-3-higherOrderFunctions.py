# Higher level functions
# its A function that takes one or more functions
# 3 x 3= 9 etc
numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

# result
# [9, 49, 144, 324, 400, 441]