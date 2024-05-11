# 🟠 TUPLES 01

[Python Lists & Tuples for Beginners | Python tutorial](https://youtu.be/KWKWswDfAb0?feature=shared&t=1602)

<br>
<br>

### 🌈 Python Tuples

Tuples are used to store multiple items in a single variable.

```python
mytuple = ("apple", "banana", "cherry")

```

#### Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable 🔴(meaning that we cannot change, add or remove items after the tuple has been created.

)

https://www.w3schools.com/python/python_tuples.asp

<br>
<br>

### Single Parentheses for Tuples:

- You can create a tuple in Python using single parentheses. For example:

```python
my_tuple = (1, 2, 3)

```

<br>
<br>

### Double Parentheses in Certain Cases:

- Double parentheses are sometimes used to explicitly define a tuple within a tuple, particularly when it's necessary for clarity or when working with tuples inside other data structures. For example:

```python
nested_tuple = ((1, 2), (3, 4))
```

#### 🟨 Using double parentheses for tuples can be likened to nesting objects within an array in other programming languages. It helps to maintain clarity, especially when dealing with complex data structures where you have collections of collections.

- In languages like **JavaScript**, for instance, you might have an array containing objects, and if one of those objects contains another array, you'd nest the array within the object. Similarly, in Python, you can have tuples containing other tuples, and double parentheses help signify this nesting.

Here's a comparison:

#### JavaScript:

```javascript
var arrayOfObjects = [
  { name: "John", age: 30 },
  { name: "Jane", age: 25, hobbies: ["reading", "painting"] },
];
```

#### Python

```python
list_of_tuples = [
    (1, 2),
    (3, 4, 5),
    ((1, 2), (3, 4))
]

```

- In both cases, the double parentheses or brackets denote nested structures within the main data structure.

<br>
<br>

## Exercises

```python
#------ LIST -----**
mylist = list([1, "Neil", True])
print(mylist)
#result
#[1, 'Neil', True]
# ------------------
#
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
```

### Since Tuples are unchangeable 🔴(meaning that we cannot change, add or remove items after the tuple has been created.) we can create a copy of the tuple and then insert a new ITEM
