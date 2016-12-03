"""
Sudoku Helper Functions
Author: Wes Bradley
Last Modified: 3 December 2016

Defines various helper functions for use throughout Sudoku project.
"""
from random import randrange

def randomVal():
    return randrange(1, 10)

def randomPlace():
    return (randrange(9) for _ in range(2))

def validMove(b, r, c, v):
    return not (v in b[r] or v in (i[c] for i in b) or \
        any(v in k for k in [j[3 * (c//3):3 * (c//3) + 3] for j in b[3 * (r//3):3 * (r//3) + 3]]))