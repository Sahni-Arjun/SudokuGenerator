"""
Class for testing the methods in the class SudokuTreeNode
"""
from SudokuTreeNode import *
from Actual import *
import unittest
import random


class SudokuTreeNodeTests(unittest.TestCase):
    """
    unittests created for all the methods of class SudokuTreeNode
    2 setup methods are created so that the code runs faster as a solved board will not be created
    when it is not needed
    """
    def setup_empty(self):
        """
        creates an empty Board for testing
        """
        self.board = Board()
        self.number = random.randint(1, 9)

    def setup_solved(self):
        """
        creates a solved Board for testing
        """
        x = Actual()
        x.create()
        self.board = x.board
        self.number = random.randint(1, 9)

    def test_get_row_empty(self):
        """
        test for the method get_row

        """
        self.setup_empty()
        node = SudokuTreeNode(self.number, 0, 5, self.board, 0)
        checker = [0, 0, 0, 0, 0, 0]
        self.assertEqual(node.get_row(), checker)


if __name__ == '__main__':
    unittest.main()
