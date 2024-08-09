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


        #👾 square
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

                   # If the number the player chose is not a valid empty spot, this line makes a special kind of error called ValueError. This tells the game that something went wrong and it needs to handle it.
                   raise ValueError

            # If everything is okay (the input was a number and it’s a valid empty spot), this line says that the player's move is valid. This stops the game from asking for another move.
               valid_square = True

           # if something went wrong. If there was an error (like the input wasn’t a number or wasn’t a valid spot), the game will launch the exception
           except ValueError:
               # the exception will CATCH it and launch an error procedure 'ValueError', then will print the messa below
               print(' Invalid square. Try again')
               # if there was an error, this line tells the player that their move is not allowed and asks them to try again.


    # Once a valid move is found, this line returns (gives back) the number of the chosen spot. This number will be used to put the player’s mark on the grid.
       return val

