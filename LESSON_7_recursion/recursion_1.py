# check the explanation on 17 recursion
def add_one(num):
    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)

add_one(0)

print("-----")
#1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

#
# -----
#  BUT WHAT IF i want to reach the 10?
# ------
def adds_one(num):
    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return adds_one(total)

# add_one(0)
mynewtotal = adds_one(0)
print(mynewtotal)

# -----
#
print('---')
# ------

# value = "y"
# count = 0

# while value:
#     count += 1
#     print(count)
#     if (count == 5):
#        break
#     else:
#         value = 0
#         continue
# # result:1
# SO, from the moment the loop starts, the value is no longer 0 and therefore is no longer true, but false, so iT adds 1 and the total is 1

value = True  # Start with value set to True
count = 0     # Initialize count to 0

# Begin the loop
while value:
    count += 1       # Increase count by 1
    print(count)     # Print the current count

    if count == 5:   # Check if count is 5
        break        # If count is 5, stop the loop
