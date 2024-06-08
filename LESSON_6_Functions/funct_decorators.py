#1
# OUT (on global scope)
def hello_deco(func):


    # INSIDE (local sc) of the hello_deco()
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now, inside the wrapper function.
        func()

        print("This is AFTER 🔓 function execution")

    return inner1


# 2
# OUT (on global scope)
# DEFINING a function, to be called inside WRAPPER
def function_to_be_used():
    print("This is INSIDE 🍯 the function !!!")

# INSIDE (local sc) of the function_to_be_used
#
#passing function_to_be_used inside the decorator to control its behavior
function_to_be_used = hello_deco(function_to_be_used)

# INSIDE (local sc) of the function_to_be_used
#
# calling the function
function_to_be_used()