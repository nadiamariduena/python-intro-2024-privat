# Closure is a function having accesss to the scope of its parent.
#
# Function after the parent function has returned

##  ----
# COINS example
# -------

#
#
def parent_function(person):
    coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins")