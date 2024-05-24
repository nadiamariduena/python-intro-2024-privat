
import sys

import random

from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")

#-- while loop ----
#1
playagain = True
#2
while playagain:
    # respect the indentation here (otherwise the content of the loop will be placed out of the scoope and you will get errors)
    playerchoice = input("Enter... \n1 for Rock🪨,\n2 for Paper🧻, or \n3 for Scissors 🌂 :\n\n")

    player = int(playerchoice)

    if player < 1  or player > 3:

        sys.exit("You must enter 1, 2 , or 3.")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    #
    #
    print("")
    print("You choose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
    print("")


    if player == 1 and computer == 3:
        print("🎉 You win!")
    elif player == 2 and computer == 1:
        print("🎉You win!")
    elif player == 3 and computer == 2:
        print("🎉You win!")
    elif player == computer:
        print("🍿Tie game!")
    else:
        print("👾Python wins")

#3 ask the user if they want to continue or to quit
# use the \n to make a new line
    playagain = input ('\nPlay again? \nY for (yes) or \nQ to Quit \n\n')

#4 now add an if statement to handle the step 3

# but before we will check if the user will enter a lower case and if the USER enter an uppercase it will convert to lower
    if playagain.lower() == 'y':
        continue