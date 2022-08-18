from turtle import width
import pygame

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Path Finding Algorithm")

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (43,43,43)
ORANGE = (218,165,32)

square_thickness = 1
square_size = 15