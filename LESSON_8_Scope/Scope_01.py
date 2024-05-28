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