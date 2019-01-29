"""
class for the sudoku board
"""


class Board:

    """
    An object to work as a sudoku board
    """

    def __init__(self):
        """
        creates a board with 9 rows and 9 columns with all values set to 0
        """
        self.contents = []
        for i in range(9):
            self.contents.append([])
            for x in range(9):
                self.contents[len(self.contents) - 1].append(0)

    def __str__(self):
        """
        returns the string representation of the board
        :return:
        :rtype:
        """

        string = ""
        for row in self.contents:
            z = 0
            for i in row:
                if z != 8:
                    string = string + " " + str(i)
                else:
                    string = string + " " + str(i) + "\n"

                z += 1

        return string



