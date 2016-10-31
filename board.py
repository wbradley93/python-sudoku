"""
Sudoku Board Class
Author: Wes Bradley
Last Modified: 31 October 2016

Defines sudoku board class and related methods
"""

from generate import generateBoard
from copy import deepcopy

class Board(object):
    def __init__(self, diff):
        self.diff = diff
        self.solution, self.initialBoard = generateBoard(self.diff)
        self.board = deepcopy(self.initialBoard)
    
    def getDiff(self):
        return self.diff
        
    def getInitialBoard(self):
        return self.initialBoard
        
    def getBoard(self):
        return self.board
        
    def getSolution(self):
        return self.solution
        
    def resetBoard(self):
        self.board = deepcopy(self.initialBoard)
        
    def __str__(self):
        hLine = "-" * 37 + "\n"
        out = hLine 
        for i in range(9):
            line = "|"
            for j in range(9):
                line += " " + (" " if self.board[i][j] is 0 else str(self.board[i][j])) + " |"
            out += line + "\n"
            out += hLine
        return out