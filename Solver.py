import numpy as np
import pygame

from Gui import Gui

class Solver:

    def __init__(self, grid, window, gui):
        self.grid = grid
        self.window = window
        self.gui = gui
        self.wasSolved = False
        # self.EXPECTED_GROUP_SUM = 45 # sum(x) from 1..9 = 45

    def solve(self, window):
        if self.wasSolved == True:
            return self.grid
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    # if self.onlyOneEmptyCellLeftInGroup():
                    #     pass
                    for n in range(1, 10):
                        if self.isMovePossible(x, y, n):
                            self.grid[y][x] = n 
                            self.gui.renderPuzzle(window, self.grid, False)
                            pygame.display.update()
                            self.solve(window)
                            if self.wasSolved:
                                return self.grid
                            self.grid[y][x] = 0
                    return
        print()
        print(self.grid)
        self.wasSolved = True
        return self.grid
    
    # def onlyOneEmptyCellLeftInGroup(self):
    #     if self.isLastEmptyCellInRow():
    #         pass
    #     pass
        # if isNotLastEmptyCellInColumn(n):
        #     return False
        
        

    # def isLastEmptyCellInRow(self):
    #     currentGroupSum = ____something
    #     missingNumber = self.EXPECTED_GROUP_SUM - currentGroupSum

    # def isNotLastEmptyCellInColumn(self):
    #     pass

    # def isNotLastEmptyCellInSquare(self):
    #     pass

    def isMovePossible(self, x, y, n):
        okay_in_row = self.possibleForRow(y, n)
        okay_in_column = self.possibleForColumn(x, n)
        okay_in_square = self.possibleForSquare(x, y, n)
        return okay_in_row and okay_in_column and okay_in_square

    def possibleForRow(self, y, n):
        for i in range(9):
            if self.grid[y][i] == n:
                return False
        return True

    def possibleForColumn(self, x, n):
        for i in range(9):
            if self.grid[i][x] == n:
                return False
        return True

    def possibleForSquare(self, x, y, n):
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for j in range(3):
            for i in range(3):
                if self.grid[y0 + j][x0 + i] == n:
                    return False
        return True