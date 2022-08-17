import pygame
from square import Square
from grid import Grid
pygame.init()

##############################################################################################################

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

grid = Grid()
square_thickness = 1
square_size = 15

##############################################################################################################

def draw_grid():
    for i in range(0,width, square_size):
        # print(i)
        for j in range(0, height, square_size):
            # print(j)
            pygame.draw.rect(screen, BLACK, pygame.Rect(i, j, square_size, square_size),square_thickness)
            grid.add(Square(square_size,i,j))

##############################################################################################################

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((width//2,height//2))
pygame.display.set_caption('Path Finder')
screen.fill(WHITE)
draw_grid()

##############################################################################################################

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip() # Flip the display

pygame.quit()
