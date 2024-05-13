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
# output
Union Set: {'grape', 'orange', 'banana', 'apple', 'pineapple', 'pear'}

```
