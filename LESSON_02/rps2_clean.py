# the clean version
import sys
import random

print("")

playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n")

print("")

player = int(playerchoice)

if player < 1  or player > 3:
    sys.exit("You must enter 1,2 or 3 'not below 1 or more than 3'")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print("You choose " + playerchoice + ".")
print("Python chose " + computerchoice + ".")
print("")

#
# Message

if player == 1 and computer == 3:
    print("You WIN")
elif player == 2 and computerchoice == 1:
    print("Ýou WIN")
elif player == 3 and computer == 2:
    print("Ýou WIN")
elif player == computer:
    print("🍿Tie game!")
else:
   print("👾Python wins")