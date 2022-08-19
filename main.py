from settings import *
from square import Square
pygame.init()

##############################################################################################################
"""

Grid Functions

"""

def create_grid(rows,width):
    grid = []
    grid_size = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            square = Square(grid_size,i,j,rows)
            grid[i].append(square)
    return grid

def draw_grid(win,rows,width):
    gap = width//rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0,i*gap), (width, i*gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j*gap, 0), (j*gap, width))

##############################################################################################################

"""
PROGRAM FUNCTIONALITY - THIS IS WHERE ALL THE ALGORITHMS ETC SHOULD GO - A* dsijisras breadth first etc.
"""

def get_mouse_pos(pos,rows,width):
    gap = width // rows
    y,x = pos
    row = y//gap
    col = x//gap
    return row, col

##############################################################################################################

"""
Draw Function
"""

def final_draw(win,grid,rows,width):
    win.fill(WHITE)
    print("This is being called")
    for row in grid:
        for square in row:
            square.draw(win)
            #print(square.get_colour())
    draw_grid(win,rows,width)
    pygame.display.update()

##############################################################################################################

"""
Main loop of the program.
"""

def main():
    running = True
    startPos = None
    endPos = None
    grid = create_grid(ROWS,WIDTH)
    while running:
        #print(startPos)
        final_draw(WIN, grid, ROWS, WIDTH)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_pos(pos, ROWS, WIDTH)
                node = grid[row][col]
                print(node.get_colour())

                if not startPos: # if there is no start position
                    startPos = node
                    startPos.toggle_start() # make this the start position

                elif not endPos and node != startPos: # if there is no end position and the hovered node is not the start node
                    endPos = node
                    endPos.toggle_end() # make this end position

                elif node != endPos and node != startPos: # if the node is not the start or end position
                    node.make_wall() # make this a wall that cannot be traversed

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                print(pos)
        CLOCK.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()
