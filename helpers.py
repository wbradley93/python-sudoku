"""
Sudoku Helper Functions
Author: Wes Bradley
Last Modified: 3 December 2016

Defines various helper functions for use throughout Sudoku project.
"""
def validMove(b, r, c, v):
    return not (v in b[r] or v in (i[c] for i in b) or \
        any(v in k for k in [j[3 * (c//3):3 * (c//3) + 3] for j in b[3 * (r//3):3 * (r//3) + 3]]))