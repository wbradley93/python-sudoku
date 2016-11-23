"""
Sudoku Hole Digger
Author: Wes Bradley
Last Modified: 31 October 2016

Takes a solved sudoku board and 'digs out' a number of spaces by a method
corresponding to the chosen difficulty level.
TODO: implement digging methods for higher difficulties
"""

from backtrack import validMove, solve
from random import randrange
from copy import deepcopy
from difficulty import givenRange, rowColBound

def isUnique(b, r, c):
    val = b[r][c]
    for i in [j for j in range(1, 10) if j != val]:
        if validMove(b, r, c, i):
            bc = deepcopy(b)
            bc[r][c] = i
            if solve(bc, 0):
                return False
    return True

def digHoles(b, dif):
    givens = 81
    pRange = [i for i in range(givens)]
    while len(pRange) > 0:
        num = pRange.pop(randrange(len(pRange)))
        if givens > randrange(givenRange[dif][0], givenRange[dif][1]+1):
            row = num//9
            col = num%9
            if (9 - b[row].count(0)) > rowColBound[dif] and \
                    sum(1 if i[col] != 0 else 0 for i in b) > rowColBound[dif] \
                    and isUnique(b, row, col):
                b[row][col] = 0
                givens -= 1
