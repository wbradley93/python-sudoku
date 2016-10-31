"""
Sudoku Board Class
Author: Wes Bradley
Last Modified: 31 October 2016

Defines sudoku board class and related methods
"""

from generate import generateBoard
from copy import deepcopy

class Board:
    def __init__(self, diff):
        self.diff = diff
        self.solution, self.initialBoard = generateBoard(self.diff)
        self.board = deepcopy(self.initialBoard)
    
    def getDiff(self):
        return self.diff
        
    def getSolution(self):
        return self.__str__(self.solution)
        
    def __str__(self, b = None):
        if b is None: b = self.board
        hLine = "-" * 37 + "\n"
        out = hLine 
        for i in range(9):
            line = "|"
            for j in range(9):
                line += " " + str(b[i][j]) + " |"
            out += line + "\n"
            out += hLine
        return out