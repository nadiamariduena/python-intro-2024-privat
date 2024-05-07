  # sys.exit() is a function provided by the sys module in Python that is used to exit the Python interpreter. It's typically called with an optional integer argument representing an exit status. If no argument is provided, it exits with a status code of zero, indicating successful termination.
# "
import sys
#  without the sys you cannot EXIT the program on line 15
#
print("")

playerChoice = input("Enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

#\n – newline
#  you need to convert the input from STRING to Int
player = int(playerChoice)
#
# print(playerChoice)
if playerChoice < 1  | playerChoice > 3:
    # sys.exit("You must enter 1, 2 , or 3")
    #
     # TO EXIT the program
    sys.exit("You must enter 1, 2 , or 3")
