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
# users += 'Jason'
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
print(users)
#['robert', 'JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n', 'Robert']
#
#-------
# DEL
# i will delete the first item of the list
del users[0]
print(users)
#result: robert has been deleted from the list ['JPJ', 'Alex', 'John', 'Sara', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n', 'Robert']

#
#
# --- del a lst
# del data
print(data)
# it will tell you the following because the list no longer exists
# line 102, in <module>
#     print(data)
#           ^^^^
# NameError: name 'data' is not defined

#
#
#---
# CLEAR the list
#clear the content of the list

# --- del a lst
# del data
data.clear()
print(data)



#
# --- SORT
# just like in javascript The **sort()** method sorts an array alphabetically:
users[1:2]=['dave', 'zardoz']

users.sort()
print(users)
# result
#['Alex', 'Elsa', 'J', 'JPJ', 'Jason', 'John', 'Robert', 'Sara', 'a', 'n', 'o', 's']

#
# -----
# LOWERCASE

users.sort(key=str.lower)
print(users)
#result
# you can see the that it sorted the list alphabetically
#['dave', 'Elsa', 'Jason', 'John', 'JPJ', 'Robert', 'Sara', 'zardoz']

#
# -- numbers
# nums = [4, 42, 78, 1, 5]
# nums.reverse()
# print(nums)
# result: [5, 1, 78, 42, 4]
#
#------
# reverse it again
#
# nums.sort(reverse=True)
# print(nums)
# result: as you can noticem the its the biggest showing first and so on [78, 42, 5, 4, 1]
#
#
#
nums = [4, 42, 78, 1,5]
#
print(sorted(nums, reverse=True))
print(nums)
#result
#[78, 42, 5, 4, 1]
# [4, 42, 78, 1, 5]
print(".----.")
#
# --- list copies

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy)
print(nums)
# result  --
#[78, 42, 5, 4, 1]
# [4, 42, 78, 1, 5]
# .----.
# [4, 42, 78, 1, 5]
# [4, 42, 78, 1, 5]
# [4, 42, 78, 1, 5]
# [4, 42, 78, 1, 5]
# ----

## Sort the nums list

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)
# [78, 42, 5, 4, 1]
# [4, 42, 78, 1, 5]
# .----.
# [4, 42, 78, 1, 5]
# [4, 42, 78, 1, 5]
# [4, 42, 78, 1, 5]
# [4, 42, 78, 1, 5]
# [4, 42, 78, 1, 5]
# [4, 42, 78, 1, 5]
# [1, 4, 5, 42, 78] ✋
# [4, 42, 78, 1, 5]


#
#----- type of the list

print(type(nums))
#result
#<class 'list'>

#
#
# creating a new list

mylist =  list([1, "Neil",  True])
print(mylist)
#rwsult
#[1, 'Neil', True]

