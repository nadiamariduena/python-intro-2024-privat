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