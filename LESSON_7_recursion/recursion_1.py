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
