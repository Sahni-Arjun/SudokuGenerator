
from SudokuTree import *
import random


class Actual:
    """
    This is the class that creates the tiles on the sudoku board
    """

    def __init__(self):
        self.found = False
        self.board = Board()

    def get_correct(self, node: SudokuTreeNode):
        """
        gives a correct value to a piece on a sudoku board
        :param node:
        :type node:
        :return:
        :rtype:
        """
        if not self.found:
            self.board.set_tile(node.row, node.col, node.value)
            node.board = self.board
            node.get_children()
            random.shuffle(node.children)
            if node.length == 80:
                self.found = True
            else:
                for x in node.children:
                    self.get_correct(x)

    def create(self):
        """
        creates a random solved sudoku board
        :return:
        :rtype:
        """
        number = random.randint(1, 9)
        node = SudokuTreeNode(number, 0, 0, self.board, 0)
        self.get_correct(node)






