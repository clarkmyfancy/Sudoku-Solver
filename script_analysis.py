def main():
    pass
    # while True:
        # call some functions/ run the backtracking algorithm
        # get how long that program took to run
        # take that data and save it to a file, or a new file
        # or whatever, but then go back later and plot that data to see imporvements



if __name__ == "__main__":
    main()



######################################
# The code below was the state of the solver before any refactorings
# and it is being kept to allow for tracking algorithm improvements by using this program
######################################

#     import numpy as np
# import pygame

# from Gui import Gui

# class Solver:

#     def __init__(self, grid, window, gui):
#         self.grid = grid
#         self.window = window
#         self.gui = gui
#         self.wasSolved = False

#     def solve(self, window):
#         if self.wasSolved == True:
#             return self.grid
#         for y in range(9):
#             for x in range(9):
#                 if self.grid[y][x] == 0:
#                     for n in range(1, 10):
#                         if self.isMovePossible(x, y, n):
#                             self.grid[y][x] = n 
#                             self.gui.renderPuzzle(window, self.grid, False)
#                             pygame.display.update()
#                             self.solve(window)
#                             if self.wasSolved:
#                                 return self.grid
#                             self.grid[y][x] = 0
#                     return
#         print()
#         print(self.grid)
#         self.wasSolved = True
#         return self.grid

#     def isMovePossible(self, x, y, n):
#         okay_in_row = self.possibleForRow(y, n)
#         okay_in_column = self.possibleForColumn(x, n)
#         okay_in_square = self.possibleForSquare(x, y, n)
#         return okay_in_row and okay_in_column and okay_in_square

#     def possibleForRow(self, y, n):
#         for i in range(9):
#             if self.grid[y][i] == n:
#                 return False
#         return True

#     def possibleForColumn(self, x, n):
#         for i in range(9):
#             if self.grid[i][x] == n:
#                 return False
#         return True

#     def possibleForSquare(self, x, y, n):
#         x0 = (x // 3) * 3
#         y0 = (y // 3) * 3
#         for j in range(3):
#             for i in range(3):
#                 if self.grid[y0 + j][x0 + i] == n:
#                     return False
#         return True