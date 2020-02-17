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
        gridHeight = (self.height - 4*Gui.fatLine) / Gui.numGridsPerBox
        cellHeight = (gridHeight - 2*Gui.skinnyLine) / Gui.numCellsPerGrid
        gridWidth = (self.width - 4*Gui.fatLine) / Gui.numGridsPerBox
        cellWidth = (gridWidth - 2*Gui.skinnyLine) / Gui.numCellsPerGrid

        numCellsBehindCurrent = 0
        for i in range(6):
            if i % 2 == 0:
                numCellsBehindCurrent = 1
            else:
                numCellsBehindCurrent = 2
            u = i // 2
            firstGreyLineX = u*(gridWidth + Gui.fatLine) + Gui.fatLine + numCellsBehindCurrent*cellWidth + ((numCellsBehindCurrent - 1) * Gui.skinnyLine)
            firstGreyLineY = u*(gridHeight + Gui.fatLine) + Gui.fatLine + numCellsBehindCurrent*cellHeight + ((numCellsBehindCurrent - 1) * Gui.skinnyLine)
            pygame.draw.rect(window, Gui.GRAY, (0, firstGreyLineY, self.width, Gui.skinnyLine))
            pygame.draw.rect(window, Gui.GRAY, (firstGreyLineX, 0, Gui.skinnyLine, self.height))
        
    def drawVerticalBoldedLines(self, window):
        gridWidth = (self.width - 4*Gui.fatLine) / Gui.numGridsPerBox
        pygame.draw.rect(window, Gui.BLACK, (gridWidth + Gui.fatLine, 0, Gui.fatLine, self.height))
        pygame.draw.rect(window, Gui.BLACK, (2*gridWidth + 2*Gui.fatLine, 0, Gui.fatLine, self.height))
    
    def drawHorizontalBoldedLines(self, window):
        gridHeight = (self.height - 4*Gui.fatLine) / Gui.numGridsPerBox
        pygame.draw.rect(window, Gui.BLACK, (0, gridHeight + Gui.fatLine, self.width, Gui.fatLine))
        pygame.draw.rect(window, Gui.BLACK, (0, 2*gridHeight + 2*Gui.fatLine, self.width, Gui.fatLine))
    
    def drawBorder(self, window):
        pygame.draw.rect(window, Gui.BLACK, (0, 0, self.width, Gui.fatLine))
        pygame.draw.rect(window, Gui.BLACK, (0, 0, Gui.fatLine, self.height))
        pygame.draw.rect(window, Gui.BLACK, (0, self.height - Gui.fatLine, self.width, self.height))
        pygame.draw.rect(window, Gui.BLACK, (self.width - Gui.fatLine, 0, self.width, self.height))

    def populateWithNumbers(self, window, grid):
        gridHeight = (self.height - 4*Gui.fatLine) / Gui.numGridsPerBox
        cellHeight = (gridHeight - 2*Gui.skinnyLine) / Gui.numCellsPerGrid
        gridWidth = (self.width - 4*Gui.fatLine) / Gui.numGridsPerBox
        cellWidth = (gridWidth - 2*Gui.skinnyLine) / Gui.numCellsPerGrid

        fnt = pygame.font.SysFont("comicsans", 40)
        for j, y in enumerate(grid):
            for i, x in enumerate(y):
                if str(x) == "0":
                    continue
                text = fnt.render(str(x), 1, Gui.BLACK)
                u = i // 3
                v = j // 3
                x = self.windowToCellTransformWidth(u, gridWidth) + ((i % 3)*(cellWidth + Gui.skinnyLine)) + 20
                y = v*(gridHeight + Gui.fatLine) + Gui.fatLine + ((j % 3)*(cellHeight + Gui.skinnyLine)) + 20
                window.blit(text, (x, y))

    def windowToCellTransformWidth(self, u, gridWidth):
        return u*(gridWidth + Gui.fatLine) + Gui.fatLine
 

