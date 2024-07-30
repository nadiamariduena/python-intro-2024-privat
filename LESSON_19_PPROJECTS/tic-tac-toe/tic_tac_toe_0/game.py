class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # This creates a list (like a row of boxes) with 9 empty spaces. Each space will be where we put X or O. Think of it as a 3x3 grid but stored in a single line.

        self.current_winner = None # Keep track of winner