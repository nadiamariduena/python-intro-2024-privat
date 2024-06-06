
# ** REDUCE
# ** 1)--- sum up the list
from functools import reduce
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
