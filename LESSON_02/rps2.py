import sys

import random

print("")

playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n")

print("")

player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("You must enter 1,2 or 3 'not below 1 or more than 3'")

    computerChoice = random.choice("123")