from Puzzle import Puzzle
from Board import Board
import pygame
pygame.font.init()

def main():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    
    CUSTOM_FONT = pygame.font.SysFont('Times New Roman', 30)
    


    size = (500, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("SudoKu")

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
        width = 500
        cell_size = (width / 9) - 1
        for i in range(10):
            # this is for the bold lines
            if i % 3 == 0:
                pygame.draw.rect(screen, BLACK, [i*cell_size, 0, 10, 500], 0)
                pygame.draw.rect(screen, BLACK, [0, i*cell_size, 500, 10], 0)

            else:
                pygame.draw.rect(screen, BLACK, [i*cell_size, 0, 2, 500], 0)
                pygame.draw.rect(screen, BLACK, [0, i*cell_size, 500, 2], 0)

        demo_number_a = CUSTOM_FONT.render("1", False, (0, 0, 0))
        demo_number_b = CUSTOM_FONT.render("3", False, (0, 0, 0))
        demo_number_c = CUSTOM_FONT.render("2", False, (0, 0, 0))
        demo_number_d = CUSTOM_FONT.render("8", False, (0, 0, 0))
        demo_number_e = CUSTOM_FONT.render("5", False, (0, 0, 0))
        demo_number_f = CUSTOM_FONT.render("3", False, (0, 0, 0))

        number_placement = (cell_size / 2) - 2
        screen.blit(demo_number_a, (number_placement*2, number_placement*2))
        screen.blit(demo_number_b, (number_placement*2*2, number_placement*2*2))
        screen.blit(demo_number_c, (number_placement*2*2*2, number_placement*2*2*2))
        screen.blit(demo_number_d, (number_placement, number_placement))
        screen.blit(demo_number_e, (number_placement, number_placement))
        screen.blit(demo_number_f, (number_placement, number_placement))
       

        # update the screen
        pygame.display.flip()

        # limit the game to 60 frames a second
        clock.tick(60)

    pygame.quit()

    

if __name__ == "__main__":
    main()
