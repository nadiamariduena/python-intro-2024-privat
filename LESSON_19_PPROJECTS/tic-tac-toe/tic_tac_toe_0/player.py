import math
import random


class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    def get_move(self, game):
        pass


# inherited class
# I will build a random comp player  that builds on top of this bass player object. And so in our initialization
class RandomComputerPlayer:
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

