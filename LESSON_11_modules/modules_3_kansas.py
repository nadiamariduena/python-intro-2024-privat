from random import choice

capital = "Topeka"
bird = "Western Meadowlark"
flower = "Sunflower"
song = "Home on the Range"

def randomfunfact3():
    funfacts = {
        "0": "0Kansas is considered flat, but it does have a mount.",
        "1": "1Wichita is the largest city in the state, but many would guess that it is Kansas City.",
        "2": "2A considerable portion of Kansas City is actually in Missouri.",
        "3": "3Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas."
    }

    index = choice(list(funfacts.keys()))
    print(funfacts[index])

# Testing the module
if __name__ == "__main__":
    randomfunfact3()
