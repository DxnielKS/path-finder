from pickle import TRUE
from settings import *
from square import Square
import tkinter
import easygui
import sys
sys.setrecursionlimit(10000)
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


"""
PROGRAM FUNCTIONALITY - THIS IS WHERE ALL THE ALGORITHMS ETC SHOULD GO - A* dsijisras breadth first etc.
"""

# [i+1][j+1]
# [i+1][j-1]
# [i-1][j+1]
# [i-1][j-1]
def tracingBrack(tracingBack,startPos):
    while tracingBack != None and tracingBack != startPos:
        #print("This tracing works")
        #print(tracingBack)
        tracingBack = tracingBack.getCame_from()
        #print("New TracingBack is")
        #print(tracingBack)
        if tracingBack != startPos:
            tracingBack.toggle_rightPath()
            tracingBack.draw(WIN)
            pygame.display.flip()

def hasBeenFound(currentNode, endPos):
        if currentNode.get_pos() == endPos.get_pos():
            return True
        else:
            return False
def displaySearching(currentNode, startPos,endPos):
        if(currentNode != startPos and currentNode != endPos):
            currentNode.toggle_finding()
        currentNode.draw(WIN)
        pygame.display.flip()
def BFS(grid,startPos,endPos):
    print("BFS is called")
    listOfNodes: list = [startPos]
    tracingBack = None
    while listOfNodes:       
        currentNode = listOfNodes[0]
        listOfNodes.pop(0)
        if hasBeenFound(currentNode, endPos):
            tracingBack = currentNode
            break
        displaySearching(currentNode,startPos,endPos)
        for neighbour in currentNode.assignNeighbours(grid):
            if (neighbour.get_iswall() != True):
                if  neighbour.get_is_visited() == False:
                    neighbour.setCame_from(currentNode)
                    neighbour.set_is_visited()
                    listOfNodes.append(neighbour)
    if(listOfNodes == []):
        print("No solution found")
        return
    tracingBrack(tracingBack,startPos)
def DFS(grid,startPos,endPos):
    print("DFS is called")
    listOfNodes: list = [startPos]
    tracingBack = None
    while listOfNodes:       
        currentNode = listOfNodes[0]
        listOfNodes.pop(0)
        if hasBeenFound(currentNode, endPos):
            print("it has been found")
            tracingBack = currentNode
            break
        displaySearching(currentNode,startPos,endPos)
        for neighbour in currentNode.assignNeighbours(grid):
            if (neighbour.get_iswall() != True):
                if  neighbour.get_is_visited() == False:
                    neighbour.setCame_from(currentNode)
                    neighbour.set_is_visited()
                    listOfNodes.insert(0,neighbour)
    if(tracingBack == endPos):
        tracingBrack(tracingBack,startPos)
    else:
        print("No solution found")
        return

def get_mouse_pos(pos,rows,width):
    gap = width // rows
    y,x = pos
    row = y//gap
    col = x//gap
    return row, col

"""
Draw Function
"""

def final_draw(win,grid,rows,width):
    win.fill(WHITE)
    #print("This is being called")
    for row in grid:
        for square in row:
            square.draw(win)
            #print(square.get_colour())
    draw_grid(win,rows,width)
    pygame.display.update()


"""
Main loop of the program.
"""

def main():
    #print("Rows is ")
   #print(ROWS)
    #print("Width is ")
    #print(WIDTH)
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
                #print(node.get_colour())
                #print(node.get_pos())

                if not startPos: # if there is no start position
                    startPos = node
                    startPos.toggle_start() # make this the start position

                elif not endPos and node != startPos: # if there is no end position and the hovered node is not the start node
                    endPos = node
                    endPos.toggle_end() # make this end position

                elif node != endPos and node != startPos: # if the node is not the start or end position
                    grid[row][col].make_wall() # make this a wall that cannot be traversed

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                #print(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    startPos = None
                    endPos = None
                    grid = create_grid(ROWS,WIDTH)
                elif event.key == pygame.K_SPACE and endPos and startPos: # if the spacebar is pressed and there is a start position and end position
                    #print("points and walls selected!")
                    algorithm_choice = easygui.buttonbox('Choose an algorithm', 'Which algorithm would you like to use?', ('A*', 'Djikstras', 'Greedy','DFS','BFS'))
                    if algorithm_choice == 'A*':
                        a_star()
                    elif algorithm_choice == 'Djikstras':
                        djikstra(grid,startPos,endPos)
                    elif algorithm_choice == 'Greedy':
                        greedy()
                    elif algorithm_choice == 'DFS':
                        DFS(grid,startPos,endPos)
                    elif algorithm_choice== 'BFS':
                        # del startPos, endPos
                        BFS(grid,startPos,endPos)

        CLOCK.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()
