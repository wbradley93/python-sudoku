"""
Sudoku Backtracking Solver
Author: Wes Bradley
Last Modified: 31 October 2016

Takes sudoku board `b` in the form of a 9x9 list array with empty spots represented
as 0 and starting place `n` in range(0,82) and modifies `b` starting at
(row, column) = (n//9, n%9) such that it's new entries represent a solved sudoku
board. To solve entire board, execute solve(b,0). Returns True if solution exists,
otherwise returns False.
"""
from helpers import validMove

def solve(b, n):
    # get the current position on board
    r = n//9
    c = n%9

    if n == 81:                             # if we've fixed the last entry
        return True
    elif b[r][c] > 0:                       # if place already holds a number
        return solve(b, n+1)
    else:
        v = 0
        while True:
            v += 1
            if v == 10:                     # if no valid entry in [1,...,9] exists
                b[r][c] = 0                 # erase the spot
                return False                # backtrack, or return False if n = 0
            elif validMove(b, r, c, v):     # if v doesn't break a rule
                b[r][c] = v                 # set v in spot n
                if solve(b, n+1):           # if we don't backtrack to n
                    return True
