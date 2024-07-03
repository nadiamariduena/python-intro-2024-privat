https://youtu.be/8ArHkS70QsQ?feature=shared

<br>
<br>

## intro

```python
# different way of how to import modules
import math
import sys
import random
#
from enum import Enum

print(math.pi)
#result: 3.141592653589793
#
#--------
# another way
from math import pi
print(pi)
# result:   3.141592653589793

#
#--------
# another way

import random as rdm
print(dir(rdm))

# result

# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_fabs', '_floor', '_index', '_inst', '_isfinite', '_lgamma', '_log', '_log2', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

print('---------')
#
#--------
# another way
# make it more readable
# dir: directory

for item in dir(rdm):
    print(item)
    # result
#     BPF
# LOG4
# NV_MAGICCONST
# RECIP_BPF
# Random
# SG_MAGICCONST
# SystemRandom
# TWOPI
# _ONE
# _Sequence ✋ _Sequence: This isn't a module but a placeholder for any sequence type like lists, tuples, or strings.
#
#
# __all__
# __builtins__
# __cached__
# __doc__
# __file__
# __loader__
# __name__
# __package__
# __spec__
# _accumulate
# _acos
# _bisect
# _ceil
# _cos
# _e
# _exp
# _fabs
# _floor
# _index
# _inst
# _isfinite
# _lgamma
# _log
# _log2
# _os
# _pi
# _random ✋ you will see the examples with the RANDOM more at the bottom
# _repeat
# _sha512
# _sin
# _sqrt
# _test
# _test_generator
# _urandom
# _warn
# betavariate
# binomialvariate
# choice
# choices
# expovariate
# gammavariate
# gauss
# getrandbits
# getstate
# lognormvariate
# normalvariate
# paretovariate
# randbytes
# randint
# random
# randrange
# sample
# seed
# setstate
# shuffle
# triangular
# uniform
# vonmisesvariate
# weibullvariate

# check the purpose of the  modules
#https://docs.python.org/3/py-modindex.html
##
#
#
```

<br>

#### example of what you will see in each package

```python
# _Sequence
my_sequence = [1, 2, 3, 4, 5]

# __all__
__all__ = ['module1', 'module2']

# __builtins__
print(__builtins__.str(10))  # Output: '10'

# __cached__
print(__cached__)  # Output: <path_to_cached_bytecode_file>

# __doc__
print(__doc__)  # Output: Docstring of the module, if any

# __file__
print(__file__)  # Output: <path_to_current_module_file>

# __loader__
print(__loader__)  # Output: Loader object for the module

# __name__
print(__name__)  # Output: __main__ or name of the current module

# __package__
print(__package__)  # Output: Name of the package of the current module

# __spec__
print(__spec__)  # Output: Module spec, including information about loader and location

# _accumulate
import itertools
print(list(itertools.accumulate([1, 2, 3, 4, 5])))  # Output: [1, 3, 6, 10, 15]

```

<br>

### MORE modules here:

- [READ MORE: python.org/3/py-modindex.html](https://docs.python.org/3/py-modindex.html)

<br>

---

<br>

## 🍭 RANDOM

<br>

- The `choice()` method returns a randomly selected element from the specified sequence.

```python
#  example a)
import random

shopping_list = ["milk", "eggs", "bread", "apples"]
to_buy = random.choice(shopping_list)

print(to_buy)
#
#
# example b)
import random

to_learn = ("Python",
            "Matplotlib",
            "NumPy",
            "Pandas",
            "Beautiful Soup",
            "SQL")

print(random.choice(to_learn))

```

<br>
<br>

### 🍭 Example 1

```python
# CHOICE
# ✋
from random import choice

capital = "Topeka"
bird = "Western Meadowlark"
flower = "Sunflower"
song = "Home on the Range"


def randomfunfact():
    funfacts = [
        "Kansas is a considered flat, but it does have a mount.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas City",
        "A considerable portion of Kansas City is actually in Missouri",
        "Most Kansans are annoyed by Wisard of Oz references from people outside of Kansas"
    ]


# CHOICE
# ✋ this is the choice function that will be imported at the top
    index = choice("0123")

    print(funfacts[int(index)])
# after this, import this module on the first modules1.py
    # print(kansas.capital)
    # kansas.randomfunfact()

```

### 🍊 Importing it within another component

- there you will import it like here below:

```python
# On the modules1.copy(), import the content of the modules_2_kansas.py
#
#
#  import the module kansas from the modules_2_kansas.py
# if the name of the file is modules_2_kansas and you import it here below as only kansas or modules2 etc, it will not work.
# the name of the file is the one you will be using to import it here, like sere below
import modules_2_kansas
#
#
print(modules_2_kansas.capital)
modules_2_kansas.randomfunfact()
```

<br>
<br>

### 🍭 Example 2

<br>

```python
# CHOICE
# ✋
from random import choice

capital = "Topeka"
bird = "Western Meadowlark"
flower = "Sunflower"
song = "Home on the Range"

def randomfunfact3():
    funfacts = {
        "0": "Kansas is considered flat, but it does have a mount.",
        "1": "Wichita is the largest city in the state, but many would guess that it is Kansas City.",
        "2": "A considerable portion of Kansas City is actually in Missouri.",
        "3": "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas."
    }

#
#
# CHOICE
# ✋
    index = choice(list(funfacts.keys()))
    print(funfacts[index])

#
#

# Testing the module
if __name__ == "__main__":
    randomfunfact3()

```

<br>
<br>

### 🍭 `__name__ == "__main__"`

<br>

- [READ MORE: python.org/3/py-modindex.html](https://docs.python.org/3/py-modindex.html)

<br>

- in other words this code, will check if i am importing it in another component, or if i am running the code from the same component, in this case will be the **modules_3_kansas.py**

```python

if __name__ == "__main__":
    randomfunfact3()
```

#### chatgpt

- The if `__name__ == "__main__"`: block at the end of a Python script is a common idiom used to control whether the script should be executed when it's run directly or when it's imported as a module into another script.

#### 🔴 Here's what it does:

`__name__` is a special variable in Python that holds the name of the current module. If the script is being run directly (i.e., it's the main program), Python sets `__name__` to "`__main__`".
When the script is imported as a module into another script, `__name__` is set to the name of the script.

<br>

In the example you provided, the randomfunfact3() function is defined, and then the script checks if it's being run directly (**name** == "**main**"). If so, it calls the randomfunfact3() function, printing a random fun fact about Kansas. If the script were imported into another Python script, the randomfunfact3() function would still be available for use, but the code inside the if **name** == "**main**": block would not be executed unless explicitly called.
