set1 = {"apple", "banana", "orange"}
set2 = {"orange", "pear", "grape"}
set3 = {"banana", "grape", "pineapple"}

# Union of sets
union_set = set1.union(set2, set3)

print("Union Set:", union_set)

print('----other examples ------')

#----------
nums = {1,2,3,4}

nums2 = set((1,2,3,4))
#
#
print(nums)
print(nums2)
print(type(nums))
print(len(nums))
##result
# {1, 2, 3, 4}
# {1, 2, 3, 4}
# <class 'set'>
# 4

#
#--------
## No duplicates allowed


nums = {1,2,2,3}
print(nums)
#
#
#result
# as you can see, it ignored the duplicate
# {1,2,3}

#
#--------
## True is a dupe of 1, False is a dupe of zero
nums = {True, 1, 2, 0, 3,4,False}
print(nums)
#result:{0, True, 2, 3, 4}
#so if i position the True in the first Value the 1 is going to be removed, and if a position the 0 istead of the False (after the 2)and then at the end i add the False, it will out put something like this:
# {0, True, 2, 3, 4}
#
#----
# or
nums = {1, True, 2, False, 3,4,0}
print(nums)
#result: {False, 1, 2, 3, 4}
#

#
#--------
# CHECK if a value is in a SET

print(2 in nums)
#result: TRUE

#
#---------
#Add a new element to a SET

nums.add(8)
print(nums)
# as you can see, we have integrated the 8 to the list
#result: {False, 1, 2, 3, 4, 8}