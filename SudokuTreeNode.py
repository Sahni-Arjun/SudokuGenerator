"""
SudokuTreeNode is created
"""
from Board import *


class SudokuTreeNode:
    """
    a tree class to work with the sudoku board
    """
    def __init__(self, value: int, row: int, col: int, board: Board, length: int):
        """
        initializes a node for a sudoku tree
        """
        self.value = value
        self.row = row
        self.col = col
        self.board = board
        self.length = length
        self.children = []
        if (self.length + 1) % 9 == 0:
            self.nrow = self.row + 1
            self.ncol = 0
        else:
            self.nrow = self.row
            self.ncol = self.col + 1

    def get_row(self) -> list:
        """
        gives the numbers that are already in the row before the current node

        """
        row_stuff = []
        for i in range(self.ncol):
            row_stuff.append(self.board.contents[self.nrow][i])

        return row_stuff

    def get_col(self) -> list:
        """
        gives the numbers that are already in the column above the current node

        """
        col_stuff = []
        for i in range(self.nrow):
            col_stuff.append(self.board.contents[i][self.ncol])

        return col_stuff

    def get_square(self) -> list:
        """
        get the numbers already in the 3x3 subsquare that come before the node in row-major order.

        """

        square_stuff = []
        row3 = self.nrow // 3
        col3 = self.ncol // 3

        for i in range(row3 * 3, (row3 * 3) + 3):
            for j in range(col3 * 3, (col3 * 3) + 3):
                if (9*i + j) < (9 * self.nrow + self.ncol):
                    square_stuff.append(self.board.contents[i][j])

        return square_stuff

    def get_all(self) -> list:
        """
        return all the numbers the next tile tile cannot be

        """
        total = self.get_col()
        total.extend(self.get_row())
        total.extend(self.get_square())
        return total

    def get_available(self) -> list:
        """
        returns a list of integers which can occupy the next position on the sudoku board according to sudoku rules

        """

        total = self.get_all()
        available = []
        check = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for x in check:
            if total.count(x) == 0:
                available.append(x)

        return available

    def get_children(self) -> None:
        """
        fills the class attribute children with integer values that can be placed in the next tile
        """
        children = []
        for x in self.get_available():
            node = SudokuTreeNode(x, self.nrow, self.ncol, self.board, self.length + 1)
            children.append(node)

        self.children = children



