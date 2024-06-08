

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
# 🖐️ Another way
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
#-----------
# 🖐️ FUNCTION can return aother function
# -----------
# You can find the examples here: https://www.geeksforgeeks.org/higher-order-functions-in-python/
#
def create_adder(x):
    def adder(y):
        return  x + y

    return adder


# add 15
add_15 = create_adder(15)

print(add_15(10))
# result
# 25

#
#-----------
# 🖐️ pass arguments to other functions
# -----------
# 1
def shout(text):
    return text.upper()
#2
def whisper(text):
    return text.lower()
#3
def greet(func_new):
# STORING the function in a variable
    greeting = func_new("Hi, I am created by a \ passed as an argument")

    #4
    print(greeting)

#5
greet(shout)
greet(whisper)

# RESULT:
#HI, I AM CREATED BY A \ PASSED AS AN ARGUMENT
# hi, i am created by a \ passed as an argument


#-----------
#
# -----------




#--------------------------
##
# NONE (nor true or false)
# ----------
#
#
def suma(numm1, numm2):
#the first return from below is called an earlier return. it will ignore the second return
    if (type(numm1) is not int or type(numm2) is not int):
        return
# this if is checking if each of the parameters (numm1 and numm2) are integers, but as you can see i purposely added a letter to get an error
    return numm1 + numm2

total2 = suma("e", 4)
print(total2)
# result: None (because i have a letter which is not an integer but a string)

##  -------
# Another way to pass the arguments on the parameter
# ----------
#
def sumas(param1, param2 = 3):
    if (type(param1) is not int or type(param2) is not int):
        return
    return param1 + param2

totalParam = sumas(1)
print(totalParam)
#result: 4
#

