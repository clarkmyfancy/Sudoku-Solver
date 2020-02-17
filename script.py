import numpy as np
import pygame

from Gui import Gui
from Solver import Solver

# grid = np.array([
#         [0,6,9,0,0,0,0,0,0],
#         [0,0,7,6,0,0,0,5,0],
#         [0,2,0,0,0,1,0,0,7],
#         [2,0,1,0,0,0,4,0,6],
#         [0,0,0,0,0,2,0,0,9],
#         [0,0,0,0,8,0,0,0,2],
#         [0,0,0,3,0,0,1,0,0],
#         [8,1,0,5,4,0,0,0,0],
#         [0,0,0,7,0,0,0,9,0]

#     ])

grid = np.array([
    [0,0,0,9,0,0,0,0,0],
    [8,3,0,0,7,0,6,0,0],
    [0,4,0,0,0,0,8,0,7],
    [0,0,0,7,5,4,0,0,8],
    [1,5,7,0,0,0,0,9,6],
    [2,8,0,1,0,0,0,0,0],
    [0,6,0,0,9,0,1,0,5],
    [4,1,0,0,8,0,0,0,0],
    [9,0,8,0,0,0,0,7,0]
])
WIDTH = 600
HEIGHT = 600

def main():
    surface = (WIDTH, HEIGHT)
    window = pygame.display.set_mode(surface)
    pygame.display.set_caption("Sudoku Solver")

    GUI = Gui(WIDTH, HEIGHT)
    solver = Solver(grid, window, GUI)

    running = True
    waiting = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        if not waiting:
            GUI.renderPuzzle(window, grid, False)
            solvedGrid = solver.solve(window)
            if solver.wasSolved:
                GUI.renderPuzzle(window, solvedGrid, True)
                pygame.display.update()
                waiting = True

if __name__ == "__main__":
    main()
    pygame.quit()


