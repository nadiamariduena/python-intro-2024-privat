
# ** REDUCE

from functools import reduce
# accumulator
# current
numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers)

print(total)

# result
# 16
# it s doing an addition of 1 + 2 + 3 + 4 + 5 +1