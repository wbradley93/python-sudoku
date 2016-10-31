"""
Sudoku Difficulty Parameters
Author: Wes Bradley
Last Modified: 31 October 2016

Stores various parameters which decide level of difficulty of sudoku boards,
according to generator.pdf
"""

# number of givens for given difficulty level, from 0: very easy to 4: evil
givenRange = [[50, 57], [36, 49], [32, 35], [28, 31], [22, 27]]
# lower bound of givens in each row/column for each difficulty level
rowColBound = [5, 4, 3, 2, 0]
