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
nums = {1, True, 2, False, 3,4,0}
print(nums)
#result: {False, 1, 2, 3, 4}