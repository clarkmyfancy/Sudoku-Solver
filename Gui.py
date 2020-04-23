import pygame 

pygame.font.init()

class Gui:

    BLACK = 0, 0, 0
    GRAY = 128, 128, 128
    WHITE = 255, 255, 255
    BLUE = 0, 0, 255
    RED = 255, 0, 0
    LIGHT_GREEN = 144, 238, 144

    fatLine = 10
    skinnyLine = 3

    numGridsPerBox = 3
    numCellsPerGrid = 3

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.gridHeight = (self.height - 4*Gui.fatLine) / Gui.numGridsPerBox
        self.cellHeight = (self.gridHeight - 2*Gui.skinnyLine) / Gui.numCellsPerGrid
        self.gridWidth = (self.width - 4*Gui.fatLine) / Gui.numGridsPerBox
        self.cellWidth = (self.gridWidth - 2*Gui.skinnyLine) / Gui.numCellsPerGrid

    def renderPuzzle(self, window, grid, wasSolved):
        window.fill(Gui.WHITE)
        if wasSolved:
            window.fill(Gui.LIGHT_GREEN)
        self.drawGrid(window)
        self.populateWithNumbers(window, grid)
        
    def drawGrid(self, window):
        self.drawThinGridLines(window)
        self.drawVerticalBoldedLines(window)
        self.drawHorizontalBoldedLines(window)
        self.drawBorder(window)

    def drawThinGridLines(self, window):
        numCellsBehindCurrent = 0
        for i in range(6):
            if i % 2 == 0:
                numCellsBehindCurrent = 1
            else:
                numCellsBehindCurrent = 2
            u = i // 2
            firstGreyLineX = u*(self.gridWidth + Gui.fatLine) + Gui.fatLine + numCellsBehindCurrent*self.cellWidth + ((numCellsBehindCurrent - 1) * Gui.skinnyLine)
            firstGreyLineY = u*(self.gridHeight + Gui.fatLine) + Gui.fatLine + numCellsBehindCurrent*self.cellHeight + ((numCellsBehindCurrent - 1) * Gui.skinnyLine)
            pygame.draw.rect(window, Gui.GRAY, (0, firstGreyLineY, self.width, Gui.skinnyLine))
            pygame.draw.rect(window, Gui.GRAY, (firstGreyLineX, 0, Gui.skinnyLine, self.height))
        
    def drawVerticalBoldedLines(self, window):
        pygame.draw.rect(window, Gui.BLACK, (self.gridWidth + Gui.fatLine, 0, Gui.fatLine, self.height))
        pygame.draw.rect(window, Gui.BLACK, (2*self.gridWidth + 2*Gui.fatLine, 0, Gui.fatLine, self.height))
    
    def drawHorizontalBoldedLines(self, window):
        pygame.draw.rect(window, Gui.BLACK, (0, self.gridHeight + Gui.fatLine, self.width, Gui.fatLine))
        pygame.draw.rect(window, Gui.BLACK, (0, 2*self.gridHeight + 2*Gui.fatLine, self.width, Gui.fatLine))
    
    def drawBorder(self, window):
        pygame.draw.rect(window, Gui.BLACK, (0, 0, self.width, Gui.fatLine))
        pygame.draw.rect(window, Gui.BLACK, (0, 0, Gui.fatLine, self.height))
        pygame.draw.rect(window, Gui.BLACK, (0, self.height - Gui.fatLine, self.width, self.height))
        pygame.draw.rect(window, Gui.BLACK, (self.width - Gui.fatLine, 0, self.width, self.height))

    def populateWithNumbers(self, window, grid):
        fnt = pygame.font.SysFont("comicsans", 40)
        for j, y in enumerate(grid):
            for i, x in enumerate(y):
                if str(x) == "0":
                    continue
                text = fnt.render(str(x), 1, Gui.BLACK)
                u = i // 3
                v = j // 3
                margin = 20
                x = u*(self.gridWidth + Gui.fatLine) + Gui.fatLine + ((i % 3)*(self.cellWidth + Gui.skinnyLine)) + margin
                y = v*(self.gridHeight + Gui.fatLine) + Gui.fatLine + ((j % 3)*(self.cellHeight + Gui.skinnyLine)) + margin
                window.blit(text, (x, y))

