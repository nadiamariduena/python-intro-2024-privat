  # sys.exit() is a function provided by the sys module in Python that is used to exit the Python interpreter. It's typically called with an optional integer argument representing an exit status. If no argument is provided, it exits with a status code of zero, indicating successful termination.
# "
import sys
#  without the sys you cannot EXIT the program on line 15
#
# the RANDOM module
import random
#
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# #exit the program
# sys.exit()
#
#-------




print("")

playerchoice = input("Enter... \n1 for Rock🪨,\n2 for Paper🧻, or \n3 for Scissors 🌂 :\n\n")
#\n – newline
#  you need to convert the input from STRING to Int
player = int(playerchoice)
#
# print(playerChoice)
if player < 1  | player > 3:
     # TO EXIT the program
    sys.exit("You must enter 1, 2 , or 3.")
    # result: if someone types 0 or 4 or more than 4, it will exit the program with this message: You must enter 1, 2 , or 3.

# 🗯️ its going to randomly choose one of the characters from this string using random dot choice
# so this is the choice of the computer
computerchoice = random.choice("123")
# so after that we'll cast that to an integer
computer = int(computerchoice)

#
#
print("")
print("You choose " + str(RPS(player)) + ".")
print("Python chose " + str(RPS(computerchoice)) + ".")
print("")

# MESSAGE depending of the choice
# Define who won
# if player choose 1 which is rock and computer choose 3 which is scissors
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

