print("")

playerChoice = input("Enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

#\n – newline
#
# print(playerChoice)
if playerChoice < 1  | playerChoice > 3:
    sys.exit("You must enter 1, 2 , or 3")