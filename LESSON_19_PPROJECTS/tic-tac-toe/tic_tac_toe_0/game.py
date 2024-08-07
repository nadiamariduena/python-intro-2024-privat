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




#The available_moves function is designed to find out which spaces on the tic-tac-toe board are empty and can be used for a move.
    def available_moves(self):
        # - 1 Creating a List for Moves:
        moves = []
        # Here, you create an empty list called moves. This list will store the positions on the board where a move can be made.


        # - 2 Looping Through the Board:
        # enumerate(): will help you to loop through items that dont have an assigned id, like "id": 0, "id": 1, its for values such as [ apple, fruits, etc,]
        for (i, spot) in enumerate(self.board):


            # - 3 Checking if the Spot is Empty
            if spot == ' ':

