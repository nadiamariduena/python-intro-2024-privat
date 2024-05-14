# SETS

- set is the final data collection I will talk about. Below you will see the chatgpt documentation about the topic and some exercises and also some of my questions about ít

<br>
<br>

### What are the SETS?

- A set in Python is an unordered collection of unique elements.

- This means that sets don't allow duplicate elements, and they are not indexed.

- Sets are defined by enclosing comma-separated values inside curly braces {}.

<br>
<br>

## 🟠 my question: If sets cannot be duplicated and are not indexed where can they be used? because in a real scenario I will need to change/modify or add NEW data very often

<br>

### 🟡 chatgpt answer:

<br>

🔴 You're absolutely right! In scenarios where you need to continuously add more data or modify existing data, sets might not be the best choice.

<br>

- Sets are more **suitable** for situations where you have a **fixed collection of unique elements** that you want to perform set operations on, such as finding intersections or unions.

<br>

<br>

## EXAMPLE 1)

```python
# Creating an empty set
empty_set = set()
#
# Creating a set with elements

my_set = {1, 2, 3, 4, 5}
#
# Adding elements to a set
my_set.add(6)
#
#
#  Removing elements from a set
my_set.remove(3)
```

<br>
<br>

### 🟨 Union of SETS

- The union of two sets consists of all unique elements present in either set.

<br>

#### In Python, you can use the `union()` method or the `|` operator to perform the union operation.

<br>

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # or union_set = set1 | set2
# Output: {1, 2, 3, 4, 5}

```

<br>

### 🟨 Intersection of Sets (intersection_set):

- The intersection of two sets consists of all elements that are common to both sets.

<br>

- In Python, you can use the `intersection()` method or the `&` operator to perform the intersection operation.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)  # or intersection_set = set1 & set2
# Output: {3}

```

<br>
<br>

### 🟨 Difference of Sets (difference_set):

The difference between two sets consists of all elements that are present in the first set but not in the second set.

- In Python, you can use the `difference()` method or the `-` operator to perform the difference operation.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)  # or difference_set = set1 - set2
# Output: {1, 2}

```

<br>
<br>

## 👾 my QUESTION:

- But if there is an union of the 3 that is contained within the set1 and set2, isnt this going to destroy or modify the datas contained in the 3's?

#### Chatgpt Answer:

- You're correct. Performing the union of sets will merge the elements of both sets, but duplicates will not be added.

- If there are elements common to both sets, they will be present only once in the resulting union set. Let's illustrate this with an example:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {3, 6, 7}

# Union of sets
union_set = set1.union(set2, set3)
# Output: {1, 2, 3, 4, 5, 6, 7}
```

- In this example, the union of set1, set2, and set3 results in `{1, 2, 3, 4, 5, 6, 7}.` **Notice** that the element 3 appears only once in the union set, even though it's present in both set1, set2, and set3. This is because sets only contain unique elements, and duplicates are automatically removed.

✋If you want to preserve the different data contained in all three sets separately, you should keep them separate and not perform a union operation. You can work with the individual sets as needed without merging them.

<br>

### 👾 my question:

- make a better example, lets add different data within each of the "3", and show me how it will look once the **"union"** is made. The 3 has to contain some real scenario data, lets say

```python
3: apple
3: potato
3: hammer
something like that but correctly done in set
```

#### chatgpt:

- Let's create sets with different data representing real scenarios, and then perform the union operation:

```python
set1 = {"apple", "banana", "orange"}
set2 = {"orange", "pear", "grape"}
set3 = {"banana", "grape", "pineapple"}

# Union of sets
union_set = set1.union(set2, set3)

print("Union Set:", union_set)
#
#
Union Set: {'grape', 'orange', 'banana', 'apple', 'pineapple', 'pear'}
#Union Set: {'pear', 'orange', 'apple', 'pineapple', 'grape', 'banana'}
```

### 👾 my question:

- the input is not giving me the apple as the first value and so on, why?

### chatgpt:

✋You're correct; the sets themselves do not inherently preserve any specific order of elements. **Sets in Python are unordered collections**, meaning they don't maintain the order in which elements are added.

<br>

If you want to maintain a specific order of elements, you should use a different data structure, such as a list or tuple. However, if you just want to print the elements in a specific order for display purposes, you can **sort** them before printing.

Here's how you can modify the example to print the elements in sorted order:

```python
# Define sets representing different categories of fruits
category1 = {"apple", "banana", "orange"}
category2 = {"orange", "pear", "grape"}
category3 = {"banana", "grape", "pineapple"}

# Union of sets
union_set = category1.union(category2, category3)

# Convert the union set to a sorted list for display
# 🧧 sort
sorted_fruits = sorted(union_set)


print("Union Set (Sorted):", sorted_fruits)
##
##
# output
Union Set (Sorted): ['apple', 'banana', 'grape', 'orange', 'pear', 'pineapple']

```

<br>
<br>

## Other examples

```python
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
```

<br>
<br>

## 🟡 No duplicates allowed

- In Python, 🔴 **sets are collections of unique elements, and when you create a set with mixed data types, Python will automatically convert them to the appropriate data types and eliminate duplicates**. Let's break down the behavior in your example:

```python
nums = {1,2,2,3}
print(nums)
#
#
#result
{1,2,3}
#
#
#----------
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

```

<br>
<br>

### Conversion of Boolean Values:

- In Python, True and False are boolean values, with True representing 1 and False representing 0 when used in numerical operations.

- When included in a set along with numerical values, Python treats True as 1 and False as 0.

<br>

---

<br>

## CHECK if a value is in a SET

```python

print(2 in nums)
#result: TRUE
```

<br>

#### But you cannot refer to an element in the SET with an index position or a key

<br>

### 🟡 Add a new element to a SET

```python

nums.add(8)
print(nums)
# as you can see, we have integrated the 8 to the list
#result: {False, 1, 2, 3, 4, 8}
```

<br>
<br>

## 🟡 Add more elements from one SET to another

```python
# add the new value to the morenums list and then add this new list to the already existent "nums" and use the UPDATE method to pass this values to nums
morenums = {5,6,7}
nums.update(morenums)
print(nums)
#
```

<br>
<br>

### union

- I already have examples more at the top of this file, but i wanted to repeat it

<br>

```python
# ----- UNION
# But there is another way, ou dont have to do like in the above code, you dont have to pass the "morenums"
# WHAT if i want to MERGE 2 different SETS and then create a new set from those 2?
#
#
# MERGE 2 SETS to create a new set
one = {1, 2, 3}
two = {5, 6, 7}
#
#
mynewset = one.union(two)
print(mynewset)
#result: {1, 2, 3, 5, 6, 7}
```

<br>
<br>

### KEEP DUPLICATES

- The `.intersection_update()` method in Python is used to update a set with the intersection of itself and another iterable. In simpler terms, it modifies the set on which it is called by keeping only the elements that are common to both that set and another set (or any iterable).

<br>

- You have two sets, one1 and two2, each containing some elements.

- You call one1.intersection_update(two2).

- After this operation, one1 will be modified to contain only the elements that are common between one1 and two2. Any elements present in one1 that are not in two2 will be removed from one1.

<br>

```python
one1 = {1, 2, 3}
two2 = {2, 3, 4}
#
one1.intersection_update(two2)
print(one1)
#
# result: {2, 3}
##
# In this code, after calling one1.intersection_update(two2), one1 will only contain elements that are present in both one1 and two2. So, since both sets share elements 2 and 3, one1 will be updated to {2, 3}. Any other elements in one1 that are not in two2 (like 1) will be removed.






```
