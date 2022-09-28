# from turtle import width
import pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (43,43,43)
ORANGE = (218,165,32)

# SQUARE_THICKNESS = 1
SQUARE_SIZE = 15
WIDTH = ((pygame.display.Info().current_h)//3)*2
# WIDTH = pygame.display.Info().current_h
ROWS  = WIDTH//15
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Path Finding Visualiser")
CLOCK = pygame.time.Clock()
FPS = 144
