import sys
import random
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3


    playerchoice = input(
        "\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
#
#
    # 1 if the user is not in
    if playerchoice not in [1,2,3]:
    # 2 if the user is not in, lets execute some code
       print("You must enter 1, 2, or 3.")
       # 3 use recursive function
       return play_rps() # once i add this, it will go again back to the top, and it will ask again the input of 1,2or3
#
#

    player = int(playerchoice)

    # if player < 1 or player > 3:
    #     sys.exit("You must enter 1, 2, or 3.")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '').title() + ".\n")

    if player == 1 and computer == 3:
        print("🎉 You win!")
    elif player == 2 and computer == 1:
        print("🎉 You win!")
    elif player == 3 and computer == 2:
        print("🎉 You win!")
    elif player == computer:
        print("😲 Tie game!")
    else:
        print("🐍 Python wins!")
# since we are no longer evaluating playagain on the loop at the top
    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")


    if playagain.lower() == "y":
        continue
    print("\n🎉🎉🎉🎉")
    print("Thank you for playing!\n")
    playagain = False

sys.exit("Bye! 👋")

play_rps()