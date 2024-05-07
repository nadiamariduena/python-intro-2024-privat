# 🟠 MODULES or methods

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
