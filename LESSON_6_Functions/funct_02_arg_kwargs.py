#
#
##  -------
# 🟠 ARGS
# ----------
# args will work like in javascript
# ** The *args parameter allows you to write a function that can accept a varying number of individual positional arguments in each call

def multiple_items(*args):
    # as you can see i am not adding names like in the num1 & num2, instead i grab the various values within the multiple_items("Dave"...
        print(args)
        print(type(args))

multiple_items("Dave", "John", "Noaln")
#result
#('Dave', 'John', 'Noaln')
# <class 'tuple'>
#
#
#
# EXAMPLE 2

def myFun(arg1, *argv):
    print('First argument :', arg1)
    for arg in argv:
        print('Next argument through *argv :', arg)

myFun('Hello', 'Welcome', 'to', 'Paradisse')
# RESULT:
# First argument : Hello
# Next argument through *argv : Welcome
# Next argument through *argv : to
# Next argument through *argv : Paradisse

#
#
#

#---------
# 🟠  KWARGS
# ----------

def myFune(**kwargs):
    for key, value in kwargs.items():
    #String with placeholders and format specifiers
        format_string = "%s == %s"
        #Using % operator to provide values that replace the placeholders
        print(format_string % (key, value))
#The % operator takes a tuple (key, value) and substitutes each %s with the respective elements of the tuple.




myFune(first="my", mid="beautiful", last="life")


# OUTPUT:
#first == my
# mid == beautiful
# last == life

#