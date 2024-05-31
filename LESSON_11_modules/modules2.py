from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"


def randomfunfact():
    funfacts = [
        "Kansas is a considered flat, but it does have a mount.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas City",
        "Aconsiderable portion of Kansas City is actually in Missouri",
        "Most Kansans are annoyed by Wisard of Oz references from people outside of Kansas"
    ]


# this is the choice function that will be imported at the top
    index = choice("0123")

    print(funfacts[int(index)])
# after this, import this module on the first modules1

.py
    # print(kansas.capital)
    # kansas.randomfunfact()