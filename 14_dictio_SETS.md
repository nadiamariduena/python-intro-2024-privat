# SETS

- set is the final data collection I will talk about

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
