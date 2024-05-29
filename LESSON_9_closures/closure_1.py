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
        # 3 🟥 --- important!
        # we need the nonlocal key to tell python we will be reassigning a value
        nonlocal coins
        #The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.Use the keyword nonlocal to declare that the variable is not local.
        #-------------
        #
        # 4 defining how many coins the user has now, he has
        coins -= 1

        # 5 conditional
        # if the user has more than 1 show the first image, then if the user has equal to 1 show that he has 1 coin left, at last the user is OUT of coins
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins")

    # 6 🟥 --- important!  here below we are not calling() the function, WE ARE ONLY "returning" it
    return play_game

#7 here TOMMY = is a new function, this tommy function  is going to handle the "parent_function" , within it i will add the value as "Tommy"
tommy = parent_function("Tommy")

# 8 calling tommy function which is holdinf the data of the parent_function and all the nested functions etc
tommy()
#
# RESULT
# #Tommy has 2 coins left.
