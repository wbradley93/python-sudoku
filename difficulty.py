"""
Sudoku Difficulty Parameters
Author: Wes Bradley
Last Modified: 5 December 2016

Stores various parameters which decide level of difficulty of sudoku boards,
according to generator.pdf
"""
import digger as dig

# number of givens for given difficulty level, from 0: very easy to 4: evil
givenRange = [[50, 57], [36, 49], [32, 35], [28, 31], [22, 27]]

# lower bound of givens in each row/column for each difficulty level
rowColBound = [5, 4, 3, 2, 0]

# hole digging function for given difficulty level, maximizing randomness in short runtime
# NOT USED, generate.pdf's methods are incomplete, lead to skewed and not pretty boards
def getDigFunction(b, d):
    if d == 0 or d == 1:
        return dig.randomDig(b, d)
    elif d == 2:
        return dig.oneCellDig(b, d)
    elif d == 3:
        return dig.sDig(b, d)
    elif d == 4:
        return dig.leftRightDig(b, d)
    else:
        raise ValueError('invalid difficulty')