# name = "Dave"

# def greeting(name):
#     color = "blue"
#     print(color)
#     print(name)

# greeting("John")

# # output
# # blue
# # John

name = 'Davee'

def greeting(name):
    color = "blue"
    print(color)
    print(name)

greeting("John")
## creating the new scope
print('----')

def anotherscope():
    greeting('Dave')

anotherscope()

# output:

# blue
# John
# ----
# blue
# Dave
#
#
# -----------
print('----')
#
#-------------
z_name = 'Sopgia'


# parent
def another():
    # local scope
    z_color = 'pink'

    # child function, belongs to the parent local scope
    def z_greeting(z_name):
        print(z_color)
        print(z_name)

    z_greeting('David')#z_greeting('john')

another()

# output

# pink
# David

#
#
#-------------
# what if i wanted to modify the content of a variable inside of a function, that was initially defined on the global scope (outside)
# EXAMPLE
# in this example you will notice rhat the 1 is  going to be modified in the  new count = 2
#
#
#
# -----------
print('----')
#
#-------------
name_b = 'Sully'
# 1 we cannot re assign this
count = 1

def another_b():
    color_b = 'orande'
    #2 to reasign i will need a global key
    global count
    count += 1
    # global count = 2 / dont do this
    # count = 2
    print(count)


    def greeting_b(name_b):
        print(color_b)
        print(name_b)

    greeting_b('Darius')

another_b()

#
# output
# 2
# orande
# Darius