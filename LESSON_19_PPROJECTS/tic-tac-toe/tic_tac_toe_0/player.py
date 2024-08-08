import math
import random


class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    def get_move(self, game):
        pass


# inherited class
#🤚 COMPUTER move
#  This is a special type of player who is a computer that makes random moves.
class RandomComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # Getting a Move: Chooses a random empty position from the board for the computer’s move.


        #
        #picks a random position from that list of available moves.
        square = random.choice(game.available_moves())
        return square
        # The method returns this random position (square), which tells the game where the computer player wants to place its mark.



#🤚 HUMAN move
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    #Human Player is asked to choose a spot to put their mark, and the game will keep
    def get_move(self, game):

       valid_square = False
       #Start with No Move: It starts with valid_square = False which means it hasn’t found a good move yet.


       val = None
       #val = None just means there’s no move chosen yet.

       while not valid_square:

           #Ask for Input: The game will ask the player to type in their move. For example, it might ask, "Where do you want to place your mark? (Pick a number from 0 to 9)."
           square = input(self.letter + '\'s turn. Input move (0-9):')


           try:

               # This line tries to turn the player's input (which is a string, like "5") into a number (an integer). For example, if the player typed "5", this line changes it into the number 5
               val = int(square)


               # Here, the game checks if the number the player chose (like 5) is one of the valid empty spots where the player can place their mark. The list game.available_moves() contains all the numbers for empty spots.
               if val not in game.available_moves():


                   raise ValueError
               valid_square = True

           except ValueError:
               print(' Invalid square. Try again')



           return val

