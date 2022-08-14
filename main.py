import pygame
pygame.init()

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((width//2,height//2))

WHITE = (255, 255, 255)
BLACK = (0,0,0)
squares = []

def drawGrid():
    for i in range(0,width, 30):
        # print(i)
        for j in range(0, height, 30):
            # print(j)
            pygame.draw.rect(screen, BLACK, pygame.Rect(i, j, 30, 30),2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    drawGrid()
    pygame.display.flip() # Flip the display

pygame.quit()