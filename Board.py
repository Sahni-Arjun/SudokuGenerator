class Board:
    """
    An object to work as a sudoku board
    """

    def __init__(self):
        self.contents = []
        for i in range(9):
            self.contents.append([])
            for x in range(9):
                self.contents[len(self.contents) - 1].append(0)

    def __str__(self):
        string = ""
        for x in self.contents:
            z = 0
            for i in x:
                if z != 8:
                    string = string + " " + str(i)
                else:
                    string = string + " " + str(i) + "\n"

                z += 1

        return string


    def tile(self, row, col):
        """
        return the number at a certain position
        :param row:
        :type row:
        :param col:
        :type col:
        :return:
        :rtype:
        """
        return self.contents[row][col]

    def set(self, row, col, value):
        """
        sets the vale of a tile
        :param row:
        :type row:
        :param col:
        :type col:
        :param value:
        :type value:
        :return:
        :rtype:
        """
        self.contents[row][col] = value



