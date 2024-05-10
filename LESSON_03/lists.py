users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptyList = []

print("Dave" in data)

# get an element from a list

print(users[0])
print(users[-1]) # will get the last item
print(users[-2]) # will get the penultimo/second-last
print(users.index('Sara')) # result: position 2
print(users[0:2]) #here we will get the first 2 items of the list
print(users[1:]) # it will pick up the item at position 1 and all after that, the reason for that is because arent specifing a second value after the:colons
#
#
print(users[-3:-1])
print(len(users))

#
# APPEND
# append a new item to the list (similar to push in js)

users.append('Elsa')
print(users) # result ['Dave', 'John', 'Sara', 'Elsa']

#
#
users += ['Jason']
# result: ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n']
users += 'Jason'
print(users)
# result: 'J', 'a', 's', 'o', 'n'
print(users)

# ---------
# EXTEND 1
users.extend(['Robert', 'Jimmy'])
print(users)

# ----------
# EXTEND 2
# here i m inserting the data list within the user list
# users.extend(data)
# print(users)
# result
# ['Dave', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n', 'Robert', 'Jimmy', 'Dave', 42, True]

#🟡 insert item to a certain position, here below i want to insert "Bob" at position 0 which is the beginning
users.insert(0, "Bob")
print(users)
#['Bob', 'Dave', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n', 'Robert', 'Jimmy']

#
#

# I will add 2 new names to the second position

users[2:2] = ["Eddie", "Alex"]
print(users)
#result
# ['Bob', 'Dave', 'Eddie', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n', 'Robert', 'Jimmy']

# this is similar to slice in JS
#it will replace the position 1 which is the second and then it will stop at pos 3 which is alex
users[1:3] = ['robert', 'JPJ']
print(users)
#RESULT
['Bob', 'robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n', 'Robert', 'Jimmy']

#
#
#--------
# REMOVE
users.remove("Bob")
print(users)

#
#---------
#POP
#just like in JS **pop** will remove the last of the list
print(users.pop())
# result
#['robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n', 'Robert', 'Jimmy']
# Jimmy # as you can see jimmy has been removed from the list and is now out
# print(users)