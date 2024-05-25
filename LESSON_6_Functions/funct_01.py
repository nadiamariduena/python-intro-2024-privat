

def hello():
   print('Hello World 🍰')
#
#
# just like in js, you call the function like here below: name + parentheses
hello()
## you can only use underscores but not minuses, capital or  uppercase, only lowercase
# hello_world()
def sum(num1, num2):
    print(num1 + num2)

sum(4, 5)
sum(1,7)
sum(100,3)
#
# 9
# 8
# 103

##  -------
# Another way
# ----------
#
#
def sumFunction(num3, num4):
    return num3 + num4
total = sumFunction(2, 3)
print(total)
# result: 5
#
#

##  -------
# NONE (nor true or false)
# ----------
#
#
def suma(numm1, numm2):
#the first return from below is called an earlier return. it will ignore the second return
    if (type(numm1) is not int or type(numm2) is not int):
        return

    return numm1 + numm2

total2 = suma("e", 4)
print(total2)