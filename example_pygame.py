import pygame

WIDTH = 600
HEIGHT = 600

black = (0,0,0)
white = (255,255,255)

def main():
    
    pygame.init()

    surface = (WIDTH, HEIGHT)
    window = pygame.display.set_mode(surface)
    pygame.display.set_caption("Sudoku Solver")

    carImg = pygame.image.load('racecar.png')

    x =  (WIDTH * 0.45)
    y = (HEIGHT * 0.8)

    def blitCar(x,y):
        window.blit(carImg, (x,y))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            print(event)
        window.fill(white)
        blitCar(x,y)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()