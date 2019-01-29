# SudokuGenerator

Generates a random completed sudoku board

To do this  simply run the main.py file



## How the code works


#### Class: Board

* The Board class creates the board data type which basically is just like a sudoku board.
 *It has a class attribute **contents** which is a nested list that emulates  9 rows and 9 columns with each tile having an associated value.
* It has a string representation, and methods **get_tile** and **set_tile** to get and set tile values.


#### Class: SudokuTreeNode

* This class is a tree node class which creates a tree that works with the board. Its main purpose is to get values which are acceptable for the next tile, and to be used with the class Actual.
* It has attributes  **board** (an instance of the board class), **row** and **col** to determine the node's position on the board, **children** (acceptable values for the next tile in row-major format) and **length** (used for convenience in class Actual). 
* Its methods are used to get values and create nodes for the children attribute

#### Class: Actual

* This class uses the SudokuTreeNode to create acceptable tiles for the completed sudoku board
* It has 2 class attributes. The **board** is the Board for which tiles are created. The **found** attribute is a boolean used in the get_correct method.
* It has 2 methods. The **get_correct** method  is a recursive method which finds acceptable tile values by using instances of SudokuTreeNode and simultaneously mutates the board. The **create** method basically calls the get_correct method with the correct argument.







