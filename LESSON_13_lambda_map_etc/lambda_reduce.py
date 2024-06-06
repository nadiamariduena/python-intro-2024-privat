
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
# ** SPOTIFY
# ------------
# FIND THE DURATION OF A List
# ------------

playlist_durations = [180, 240, 200, 300, 210] # duration of songs in seconds

# find the total duration
total_duration = reduce(lambda x, y: x + y, playlist_durations)

print("Total duration of the playlist:", total_duration, "seconds")

# result
#Total duration of the playlist: 1130 seconds
#
#
#

# ** Shoes ESHOP
# ------------
#  find the total revenue generated from selling these shoes.add()
# -We can use reduce along with a lambda function to calculate the total revenue.
# ------------

shoe_prices = [50, 70, 90, 60] # prices of shoes in dollars

# we want to find the total revenue generated from selling these shoes. We can use "reduce" and a lambda function like this:
#
#
total_revenue = reduce(lambda x, y: x + y, shoe_prices)

print("Total revenue from selling shoes", total_revenue, "dollars")
# result
# Total revenue from selling shoes 270 dollars
#
#
#
# ** Shoes ESHOP
# ------------
# Suppose we have a list of tuples where each tuple represents a shoe sale. Each tuple contains the shoe size and its corresponding price. We want to find the total revenue generated from selling these shoes across all sizes.
# ------------

from functools import reduce

shoe_sales = [(8, 50), (9, 70), (7, 90), (8, 60), (10, 80)]  # (size, price) tuples

# Now we want to calculate the total revenue. We can still use `reduce` along with a lambda function, but this time, we need to extract the price from each tuple and accumulate it to find the total revenue

total_revenue = reduce(lambda acc, sale: acc + sale[1], shoe_sales, 0)

# In this example, the lambda function lambda acc, sale: acc + sale[1] takes two arguments: acc (the accumulated revenue so far) and sale (the current sale tuple). It extracts the price (the second element) from each sale tuple and adds it to the accumulated revenue. The reduce function applies this lambda function cumulatively to the list shoe_sales, starting with an initial value of 0 for the accumulated revenue, resulting in the total revenue generated from selling shoes.

print("Total revenue from selling shoes:", total_revenue, "dollars")

# result
# Total revenue from selling shoes: 350 dollars


#
#
# ** pizza resto
# ------------
# pizza restaurant where we have a list of orders. Each order is represented by a tuple containing the pizza size and its corresponding price. We want to find the total revenue generated from these orders.

#
# from functools import reduce
#
pizza_orders = [("medium", 12), ("large", 15), ("small",10), ("largeXl", 18), ("mediumXl", 14 )]

