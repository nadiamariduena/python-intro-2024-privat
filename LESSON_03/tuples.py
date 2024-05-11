#------ LIST
mylist = list([1, "Neil", True])
print(mylist)
#result
#[1, 'Neil', True]
#
#------ TUPLE
#
mytuple = tuple(("Dave", 42, True))
#
#
anothertuple = (1,4,2,8)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))
#result
# ('Dave', 42, True)
# <class 'tuple'>
# <class 'tuple'>


#
# #
# # Since Tuples are unchangeable 🔴(meaning that we cannot change, add or remove items after the tuple has been created.) we can create a copy of the tuple and then insert a new ITEM

newlist = list(mytuple)  # Converts mytuple to a list
newlist.append('🤚 Neil')  # Appends an element to the list
print(newlist)  # Prints the modified list
newtuple = tuple(newlist)  # Converts the modified list back to a tuple
print(newtuple)  # Prints the modified tuple

#
#
# - UNPACKING the tuple ----
#anothertuple = (1,4,2,8)

(one, *two, hey) = anothertuple

print(one)
print(two)
print(hey)
