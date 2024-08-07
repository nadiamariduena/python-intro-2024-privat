# 🟠 MODULES or methods

<br>
<br>

🔸   **ENUMERATE()**   [Go to section](#enumerate)



<br>
<br>
<br>

- i say methods because they are a bit similar to js methods

```python

import sys
#  without the sys you cannot EXIT the program on line 15
#
# the RANDOM module
import random
#
# serves to enumerate, but doesnt have an index to iterate, for that use enumerate()
from enum import Enum
```

<br>
<br>

### 🟡 SYS

- `sys.exit()` **is a function provided by the sys module in Python that is used to exit the Python interpreter.** It's typically called with an optional integer argument representing an exit status. If no argument is provided, it exits with a status code of zero, indicating successful termination.

##### example

- **sys** the program if the user types less than on or more than 3

<br>

- check the game [rps2](./LESSON_02//rps2_clean.py)

```python

if player < 1  | player > 3:
    # ✋ TO EXIT the program
    sys.exit("You must enter 1, 2 , or 3.")
    # result: if someone types 0 or 4 or more than 4, it will exit the program with this message: You must enter 1, 2 , or 3.
```

<br>
<br>

### 🟡 RANDOM

- The purpose of import **random** in Python is to **provide access to functions and methods** for generating random numbers, selecting random elements from sequences, shuffling sequences randomly, and more. <br> It's part of Python's standard library and is commonly used in applications that require randomness, such as simulations, games, cryptography, and statistical sampling.

<br>
<br>

## LIST of the stuff you can use with random

#### Here are some common functions and methods available after importing random in Python:

<br>

**random()**: Returns a random floating-point number between 0 and 1.

**randint(a, b)**: Returns a random integer between a and b, inclusive.

**choice(seq)**: Returns a random element from a non-empty sequence.

**shuffle(seq)**: Randomly shuffles the elements of a sequence in place.

**sample(population, k)**: Returns a list of k unique elements chosen randomly from a population sequence without replacement.

**randrange(start, stop[, step])**: Returns a randomly chosen element from the specified range.
uniform(a, b): Returns a random floating-point number between a and b, inclusive.

**seed(seed=None)**: Initializes the random number generator with a seed value (or system time if None).

#### These functions provide various ways to generate randomness or select random elements from sequences based on different requirements.

<br>

##### example:

- check the game [rps2](./LESSON_02//rps2_clean.py)

```python
# this is the choice of the computer
computerchoice = random.choice("123")
computer = int(computerchoice)

#
#
print("")
print("You choose " + playerchoice + ".")
print("Python chose " + computerchoice + ".")
print("")
```

<br>
<br>

---

<br>

# 🟡 enum & enumerate()

- In Python, if you want to enumerate a list, you typically use the built-in enumerate() function rather than the Enum class. ( if its something that requires an id or using an index , i use **enumerate()**, and for banal stuff like colors that don't require id then i use enum)

<br>
<br>

### 🍨 enum

https://docs.python.org/3/library/enum.html

<br>

- In Python, **enum** stands for "enumeration" and it's a module that provides a way to create and use enumeration types. Enumerations are sets of symbolic names (members) bound to unique, constant values. They're helpful for creating more readable and maintainable code by providing a way to represent a fixed set of constants.

#### example

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
# 🤚 In this example, Color is an enumeration type, and RED, GREEN, and BLUE are its members. Each member has an associated value (1, 2, and 3, respectively). You can access these values by using the member name, for example: Color.RED.value would return 1.
# 🤚 Enums can be used in various scenarios such as representing choices, flags, or states in your code. They can help improve readability and maintainability by providing a clear and self-documenting way to represent these concepts.
#
```

##### example:

```python
# 1) example
from enum import Enum

class Direction(Enum):
    NORTH = 'north'
    SOUTH = 'south'
    EAST = 'east'
    WEST = 'west'

def move(direction):
    print(f"Moving {direction.value}")

move(Direction.NORTH)  # Output: Moving north
move(Direction.EAST)   # Output: Moving east
#
#
# 2) example
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

```


<br>
<br>
<br>

<a name="enumerate"></a>

<br>

## 🍨 Enumerate()

In Python, if you want to enumerate a list, you typically use the built-in enumerate() function rather than the Enum class.


<br>


### 🟣: enumerate(): will help you to loop through items that don't have an assigned id, like `"id": 0, "id": 1, its for values such as [ apple, fruits, etc,]`

<br>

#### ✅ chatgpt:

- - Yes, that's a good way to think about it. The enumerate() function helps you handle cases where items in a list or iterable don't have an explicit identifier, such as an index or ID, by automatically providing one.


<br>


### The `enumerate()` function generates an enumeration of elements in an iterable along with their index. Here's how you can use it:





<br>
<br>


### 🟤 Without enumerate()

- If you have a list of items without explicit IDs, you only get the items themselves:

```python
items = ['apple', 'banana', 'cherry']
for item in items:
    print(item)

```
#### output

```python
apple
banana
cherry

```