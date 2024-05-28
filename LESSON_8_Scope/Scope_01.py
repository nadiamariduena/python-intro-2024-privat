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