from Board import *
from SudokuTree import *
import random


class Actual:

    def __init__(self):
        self.found = False
        self.board = Board()

    def get_correct(self, node: SudokuTree):
        """
        gives a correct value to a piece on a sudoku board
        :param node:
        :type node:
        :return:
        :rtype:
        """
        if not self.found:
            self.board.set(node.row, node.col, node.value)
            node.board = self.board
            node.get_children()
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
        node = SudokuTree(number, 0, 0, self.board, 0)
        self.get_correct(node)






