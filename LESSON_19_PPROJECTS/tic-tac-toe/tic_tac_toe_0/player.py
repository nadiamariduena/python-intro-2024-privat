import math
import random


class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    def get_move(self, game):
        pass


# inherited class
#  This is a special type of player who is a computer that makes random moves.
class RandomComputerPlayer:
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

