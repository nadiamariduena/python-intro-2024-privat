class TicTacToe:
    def __init__(self):
        # This line of code: self.board = [' ' for _ in range(9)] ,  initializes the self.board
        # for _ in range(9) : This iterates 9 times, and for each iteration, it adds a space to the list.
        # Result: The list self.board will be [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']. This represents an empty Tic-Tac-Toe board with 9 positions, all initially empty.
        #
        self.board = [' ' for _ in range(9)] # This creates a list (like a row of boxes) with 9 empty spaces. Each space will be where we put X or O. Think of it as a 3x3 grid but stored in a single line.

        self.current_winner = None # Keep track of winner

    def print_board(self):
    #     #This part creates a list of rows from the board:
    #     #- - self.board: This is the list with all the spaces on the board.
         for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
             #
             #  | '.join(row) joins the elements of the row with ' | ' as the separator, so each row’s elements are separated by vertical bars.
             print('| ' +  ' | '.join(row) +  ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]

        for row in number_board:
            print('| ' + '| '.join(row) + ' |')
        #  | '.join(row) joins the elements of the row with ' | ' as the separator, so each row’s elements are separated by vertical bars.




    # The available_moves
    # - The available_moves function is designed to find out which spaces on the tic-tac-toe board are empty and can be used for a move.
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    # This line finds all the empty spaces on the board where a player can put their mark. It looks at each spot on the board and checks if it's empty. If it is, it remembers the position so the player knows where they can move.



    def empty_squares(self):
        # Check if there is at least one empty space on the board
        return ' ' in self.board # Returns True if there's at least one empty space, False otherwise





def play(game, x_player, o_player, print_game=[True]):

    # RETURNS the winner of the game! (the letter) or NONE for a TIE

    if print_game:
        game.print_board_nums()

    letter = 'X' # This **initializes the variable** `letter with 'X'`, **indicating** that **'X'** will start the game.
    # It’s used to keep track of which player's turn it is.
    # ---
    # The loop keeps running while there are still empty squares on the game board. This ensures that the game continues until there are no more moves left to be made.
    while game.empty_squares():
        #pass # wait  until we finish other stuff
    # In this context, 'pass' means the loop does not yet perform any actions.
    #  - This is a placeholder 'while' waiting to implement other parts of the game logic, such as handling player moves or checking for game end conditions.
