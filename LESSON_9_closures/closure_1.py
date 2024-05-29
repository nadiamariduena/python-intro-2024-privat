# Closure is a function having accesss to the scope of its parent.
#
# Function after the parent function has returned

##  ----
# COINS example
# -------

#
# 0
def parent_function(person):
    #1 by default the user has 3 coins
    coins = 3
    #2
    def play_game():
        # 🟥 --- important!
        nonlocal coins
        #-------------
        #
        # defining how many coins the user has now, he has
        coins -= 1

        # conditional
        # if the user has more than 1 show the first image, then if the user has equal to 1 show that he has 1 coin left, at last the user is OUT of coins
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins")

    #  🟥 --- important!  here below we are not calling() the func
    return play_game