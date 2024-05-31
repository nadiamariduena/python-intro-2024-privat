https://youtu.be/8ArHkS70QsQ?feature=shared

<br>
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

- in other words this code, will check if i am importing it in another component, or if i am running the code from the same component, in this case will be the **modules_3_kansas.py**

```python

if __name__ == "__main__":
    randomfunfact3()
```

### chapgpt

- The if `__name__ == "__main__"`: block at the end of a Python script is a common idiom used to control whether the script should be executed when it's run directly or when it's imported as a module into another script.
