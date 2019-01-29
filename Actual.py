"""
class Actual is created
"""
from SudokuTreeNode import *
import random


class Actual:
    """
    This is the class that creates the tiles on the sudoku board
    """

    def __init__(self):
        """
        initiates the object with a blank board and a boolean
        """
        self.found = False
        self.board = Board()

    def get_correct(self, node: SudokuTreeNode) -> None:
        """
        Adds a suitable value to the current tile, then calls itself to do the same for possible values
        on the next tile if the board is not complete. If the board is complete it does nothing.
        """
        if not self.found:
            self.board.contents[node.row][node.col] = node.value
            node.board = self.board
            node.get_children()
            random.shuffle(node.children)
            if node.length == 80:
                self.found = True
            else:
                for x in node.children:
                    self.get_correct(x)

    def create(self) -> None:
        """
        calls get_correct with the correct values

        """
        number = random.randint(1, 9)
        node = SudokuTreeNode(number, 0, 0, self.board, 0)
        self.get_correct(node)






