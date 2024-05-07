  # sys.exit() is a function provided by the sys module in Python that is used to exit the Python interpreter. It's typically called with an optional integer argument representing an exit status. If no argument is provided, it exits with a status code of zero, indicating successful termination.
# "
import sys
#  without the sys you cannot EXIT the program on line 15
#
# the RANDOM module
import random
 #

print("")

playerchoice = input("Enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
#\n – newline
#  you need to convert the input from STRING to Int
player = int(playerchoice)
#
# print(playerChoice)
if player < 1  | player > 3:
     # TO EXIT the program
    sys.exit("You must enter 1, 2 , or 3.")

# 🗯️ its going to randomly choose one of the characters from this string using random dot choice
computerchoice = random.choice("123")
# so after that we'll cast that to an integer
computer = int(computerchoice)

#
#
print("")
print("You choose " + playerchoice + ".")
print("Python chose " + computerchoice + ".")
print("")

#
# Define who won
# if player choose 1 which is rock and computer choose 3 which is scissors
if player == 1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 3 and computer == 2:
    print("You win!")
else:
    print("Python wins")

# BUT WHAT IF the computer and the player choose the same