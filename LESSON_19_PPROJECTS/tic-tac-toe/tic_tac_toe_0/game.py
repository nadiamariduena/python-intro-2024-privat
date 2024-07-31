class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # This creates a list (like a row of boxes) with 9 empty spaces. Each space will be where we put X or O. Think of it as a 3x3 grid but stored in a single line.

        self.current_winner = None # Keep track of winner

    # def print_board(self):
    #     #This part creates a list of rows from the board. Let’s break this down:
    #     #- - self.board: This is the list with all the spaces on the board.
    #     for row in [self.board[i*3:(i+1)*3] for i in range(3)]: