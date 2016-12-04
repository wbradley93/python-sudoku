"""
Sudoku Hole Digger
Author: Wes Bradley
Last Modified: 5 December 2016

Takes a solved sudoku board and 'digs out' a number of spaces by a method
corresponding to the chosen difficulty level.
TODO: implement more sophisticated digging methods for higher difficulties than
        those in generate.pdf (k-SAT solver!)
"""

from backtrack import solve
from helpers import validMove
from random import randrange
from copy import deepcopy
import difficulty as diff

def isUnique(b, r, c):
    val = b[r][c]
    for i in [j for j in range(1, 10) if j != val]:
        if validMove(b, r, c, i):
            bc = deepcopy(b)
            bc[r][c] = i
            if solve(bc, 0):
                return False
    return True

def randomDig(b, d):
    givens = 81
    pRange = [i for i in range(givens)]
    while len(pRange) > 0:
        num = pRange.pop(randrange(len(pRange)))
        if givens > randrange(diff.givenRange[d][0], diff.givenRange[d][1]+1):
            r = num//9
            c = num%9
            if (9 - b[r].count(0)) > diff.rowColBound[d] and \
                    sum(1 if i[c] != 0 else 0 for i in b) > diff.rowColBound[d] \
                    and isUnique(b, r, c):
                b[r][c] = 0
                givens -= 1
    return b

#def bruteDig(b, dif):
#    givens = 81
#    for i in range(81):
#        r = i//9
#        c = i%9
#        if givens > randrange(diff.givenRange[dif][0], diff.givenRange[dif][1]+1) \
#            and (9 - b[r].count(0)) > diff.rowColBound[dif] \
#            and sum(1 if i[c] != 0 else 0 for i in b) > diff.rowColBound[dif] \
#            and isUnique(b, r, c):
#                b[r][c] = 0
#                givens -= 1
#        print(str(b))
#    return b
#
#def sDig(b, dif):
#    return b
#
#def leftRightDig(b, dif):
#    return b
