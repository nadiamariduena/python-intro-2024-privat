https://youtu.be/8ArHkS70QsQ?feature=shared

## RANDOM

### 🍭 Example 1

```python
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


# this is the choice function that will be imported at the top
    index = choice("0123")

    print(funfacts[int(index)])
# after this, import this module on the first modules1.py
    # print(kansas.capital)
    # kansas.randomfunfact()

```

<br>

### 🍭 Example 2

<br>

```python
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

    index = choice(list(funfacts.keys()))
    print(funfacts[index])

# Testing the module
if __name__ == "__main__":
    randomfunfact3()

```
