from pickle import TRUE
from settings import *
from square import Square
import sys
import tkinter as tk

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

#The heuristic that will be used for A* using manhattan distance
def heuristic(pos1,pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return (x1 - x2)**2 + (y1 - y2)**2

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
        return currentNode.get_pos() == endPos.get_pos()
def displaySearching(currentNode, startPos,endPos):
        if(currentNode != startPos and currentNode != endPos):
            currentNode.toggle_finding()
        currentNode.draw(WIN)
        pygame.display.flip()
def a_star(grid,startPos,endPos):
    print('A* is called')
    listOfNodes: list = [(startPos,heuristic(startPos.get_pos(),endPos.get_pos()))]
    tracingBack = None
    while listOfNodes:    
        currentNode = listOfNodes.pop(0)
        if hasBeenFound(currentNode[0], endPos):
            tracingBack = currentNode[0]
            break
        displaySearching(currentNode[0],startPos,endPos)
        for neighbour in currentNode[0].assignNeighbours(grid):
            if (neighbour.get_iswall() != True and not neighbour.get_is_visited()):
                neighbour.setCame_from(currentNode[0])
                neighbour.set_is_visited()
                listOfNodes.append((neighbour,heuristic(neighbour.get_pos(),endPos.get_pos())))
                listOfNodes.sort(key=lambda a: a[1])
        CLOCK.tick(FPS)
    if(listOfNodes == []):
        print("No solution found")
        return
    tracingBrack(tracingBack,startPos)
        

def djikstra(grid,startPos,endPos):
    print('Djikstr\'s is called')
    listOfNodes: list = [startPos]
    tracingBack = None
    while listOfNodes:    
        currentNode = listOfNodes.pop(0)
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
        CLOCK.tick(FPS)
    if(listOfNodes == []):
        print("No solution found")
        return
    tracingBrack(tracingBack,startPos)
def BFS(grid,startPos,endPos):
    print("BFS is called")
    listOfNodes: list = [startPos]
    tracingBack = None
    while listOfNodes:    
        currentNode = listOfNodes.pop(0)
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
        CLOCK.tick(FPS)
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
        CLOCK.tick(FPS)
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
                    grid[row][col].toggle_wall() # make this a wall that cannot be traversed

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                #print(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    startPos = None
                    endPos = None
                    grid = create_grid(ROWS,WIDTH)
                elif event.key == pygame.K_SPACE and endPos and startPos: # if the spacebar is pressed and there is a start position and end position
                    print("points and walls selected!")
                    choice = input("Which algorithm would you like to use?\nBFS\nDFS\nDjikstra's\nA*\n")
                    choice=choice.upper()
                    choice_dict={"BFS":"BFS(grid,startPos,endPos)","DFS":"DFS(grid,startPos,endPos)","DJIKSTRA":"djikstra(grid,startPos,endPos)","A*":"a_star(grid,startPos,endPos)"}
                    while choice not in choice_dict:
                        print("Invalid input")
                        choice = input("Which algorithm would you like to use?\nBFS\nDFS\nDjikstra's\nA*\n")
                        choice=choice.upper()
                    algorithm=choice_dict[choice]
                    eval(algorithm)
                    # window=tk.Tk()
                    # window.mainloop()
                    # button1 = tk.Button(
                    #     text="A*",
                    #     width=25,
                    #     height=5,
                    #     bg="blue",
                    #     fg="yellow",
                    # )
                    # button2 = tk.Button(
                    #     text="Djikstra's",
                    #     width=25,
                    #     height=5,
                    #     bg="blue",
                    #     fg="yellow",
                    # )
                    # button3 = tk.Button(
                    #     text="DFS",
                    #     width=25,
                    #     height=5,
                    #     bg="blue",
                    #     fg="yellow",
                    # )
                    # button4 = tk.Button(
                    #     text="BFS",
                    #     width=25,
                    #     height=5,
                    #     bg="blue",
                    #     fg="yellow",
                    # )
                    # button1.pack()
                    # button2.pack()
                    # button3.pack()
                    # button4.pack()
                    # window.mainloop()
        CLOCK.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
