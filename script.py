from Puzzle import Puzzle
import pygame


def main():
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    DARK_GREEN = (31, 159, 91)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    # puzzle = Puzzle()
    # puzzle.print_board()
   
    # puzzle.solve()
    # print()
    # puzzle.print_board()
    pygame.init()
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My first game")

    clock = pygame.time.Clock()
    playing = True
    while playing:

        # Main Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        # Game Logic goes here

        # Drawing code should go Here

        screen.fill(WHITE)
        pygame.draw.rect(screen, DARK_GREEN, [0, 0, 150, 500], 0)
        # pygame.draw.rect(screen, DARK_GREEN, [0, 0, 150, 500], 0)
        pygame.draw.rect(screen, DARK_GREEN, [160, 0, 150, 500], 0)
     
       

        # update the screen
        pygame.display.flip()

        # limit the game to 60 frames a second
        clock.tick(60)

    pygame.quit()

    

if __name__ == "__main__":
    main()
