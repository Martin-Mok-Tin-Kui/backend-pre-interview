class Solver:

    def __init__(self, BOARD_SIZE = 9, EMPTY_VALUE = 0, MAX_VALUE = 9, SUB_GRID_SIZE = 3):
        self.BOARD_SIZE = BOARD_SIZE
        self.EMPTY_VALUE = EMPTY_VALUE
        self.MAX_VALUE = MAX_VALUE
        self.SUB_GRID_SIZE = SUB_GRID_SIZE


    def solve(self, board):
        """Method iterating each empty cell and test for valid value
        Args:
            board (List<List<int>>): the current board representation
        Returns:
            bool: True if successful, False otherwise.
        """
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                if board[i][j] == self.EMPTY_VALUE:
                    for num in range(1, 10):
                        if self._is_valid(board,num,i,j):
                            board[i][j] = num
                            if(self.solve(board)):
                                return True
                            board[i][j] = self.EMPTY_VALUE
                    return False
        return True


    def _is_valid(self, board, num, row, col):
        """Method to check if filling in value num into the position (row,col) 
        will invaliding the sudoku constraint
        Args:
            board (List<List<int>>): the current board representation
            num (int): the value being check
            row (int): the row number
            col (int): the column number
        Returns:
            bool: True if is valid, False otherwise.
        """
        return self._row_constraint(board, num, row) and \
        self._col_constraint(board, num, col) and \
        self._box_constraint(board, num, row, col)


    def _row_constraint(self, board, num, row):
        """Method to check if the value num is already in the row
        Returns:
            bool: True if num does not exist in the current row, False otherwise.
        """
        if num in board[row]:
            return False
        else:
            return True


    def _col_constraint(self, board, num, col):
        """Method to check if the value num is already in the column
        Returns:
            bool: True if num does not exist in the current column, False otherwise.
        """
        for i in range(self.BOARD_SIZE):
            if board[i][col] == num:
                return False
        return True


    def _box_constraint(self,board, num, row, col):
        """Method to check if the value num is already in the 3x3 sub-grid
        Returns:
            bool: True if num does not exist in the current 3x3 sub-grid, False otherwise.
        """
        box_start_row = row - row % self.SUB_GRID_SIZE
        box_start_col = col - col % self.SUB_GRID_SIZE

        for i in range(self.SUB_GRID_SIZE):
            for j in range(self.SUB_GRID_SIZE):
                if board[box_start_row+i][box_start_col+j] == num:
                    return False
        return True
