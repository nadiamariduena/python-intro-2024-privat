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

```python
newlist = list(mytuple)  # Converts mytuple to a list
newlist.append('🤚 Neil')  # Appends an element to the list
print(newlist)  # Prints the modified list
newtuple = tuple(newlist)  # Converts the modified list back to a tuple
print(newtuple)  # Prints the modified tuple
```

<br>
<br>

# - UNPACKING the tuple ----

Tuple unpacking is a Python feature that allows you to assign the elements of a tuple to individual variables in a single line. It's a concise way to extract values from a tuple.

Here are some short examples of tuple unpacking:

#### Basic tuple unpacking:

```python

my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

```

#### Unpacking with a starred expression (for variable length tuples):

```python
my_tuple = (1, 2, 3, 4, 5)
a, b, *rest = my_tuple
print(a)    # Output: 1
print(b)    # Output: 2
print(rest) # Output: [3, 4, 5]


```

<br>
<br>

### 🌈 Now, let's see how tuple unpacking can be used in a real project:

Imagine you have a function that returns a tuple containing different pieces of information, and you want to use these pieces separately:

```python
def get_user_info():
    # Simulated data retrieval
    name = "John"
    age = 30
    email = "john@example.com"
    return name, age, email

# Using tuple unpacking to extract individual pieces of information
username, user_age, user_email = get_user_info()

print("Name:", username)
print("Age:", user_age)
print("Email:", user_email)


```

- In this example, get_user_info() returns a tuple containing user information, and tuple unpacking is used to assign each piece of information to separate variables. This makes the code more readable and eliminates the need to access elements of the tuple using indexing.

<br>

### The concept of tuple unpacking in Python is similar to array deconstruction or destructuring in JavaScript, including its usage in React.

In JavaScript, you might see something like this in React:

```javascript
const user = { name: "John", age: 30, email: "john@example.com" };

// Destructuring assignment
const { name, age, email } = user;

console.log(name); // Output: John
console.log(age); // Output: 30
console.log(email); // Output: john@example.com
```

<br>
<br>

### back to the exercises

```python
#anothertuple = (1,4,2,8)
# the values below are connected to the line 36, notice that when i add the asterisk, the value will be nested on an array
(one, *two, hey) = anothertuple

print(one)
print(two)
print(hey)

# result
#1
# [4, 2]
# 8
```

### Different methods

- with the **count** method you can figure out how many items of the same are inside a list or tuple

```python
print(anothertuple.count(2))
```
