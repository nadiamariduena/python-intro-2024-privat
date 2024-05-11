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

newlist = list(mytuple)