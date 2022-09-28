from pickle import TRUE
from string import whitespace
from tokenize import Whitespace
from settings import *

class Square():
    def __init__(self,size,row,col,total_rows):
        self.size=size
        self.row = row
        self.col = col
        self.x= row * size
        self.y= col * size
        self.total_rows = total_rows
        self.searched = False
        self.colour = WHITE
        self.neighbours = []
        self.came_from = None
        self.is_wall = False
        self.is_visited = False
    def set_is_visited(self):
        self.is_visited = True
    def get_is_visited(self):
        return self.is_visited
    def assignNeighbours(self,grid):
        #print("Problem 50")
        if (self.row == 0 and self.col == 47 ):
            self.neighbours.append(grid[self.row + 1][self.col])
            self.neighbours.append(grid[self.row][self.col - 1])
        elif (self.row == 0 and self.col == 0):
            self.neighbours.append(grid[self.row + 1][self.col])
            self.neighbours.append(grid[self.row][self.col + 1])
        elif (self.row == 47 and self.col == 0):
            self.neighbours.append(grid[self.row - 1][self.col])
            self.neighbours.append(grid[self.row][self.col + 1])
        elif (self.row == 47 and self.col == 47 ):
            self.neighbours.append(grid[self.row - 1][self.col])
            self.neighbours.append(grid[self.row][self.col - 1])
        elif(self.row == 47):
            self.neighbours.append(grid[self.row][self.col + 1])
            self.neighbours.append(grid[self.row][self.col - 1])
            self.neighbours.append(grid[self.row -1 ][self.col])
        elif(self.row == 0):
            self.neighbours.append(grid[self.row][self.col + 1])
            self.neighbours.append(grid[self.row][self.col - 1])
            self.neighbours.append(grid[self.row + 1 ][self.col])
        elif (self.col == 47):
            self.neighbours.append(grid[self.row - 1][self.col])
            self.neighbours.append(grid[self.row + 1][self.col])
            self.neighbours.append(grid[self.row ][self.col - 1])
        elif (self.col == 0):
            self.neighbours.append(grid[self.row - 1][self.col])
            self.neighbours.append(grid[self.row + 1][self.col])
            self.neighbours.append(grid[self.row ][self.col + 1])
        else:
            self.neighbours.append(grid[self.row - 1][self.col])
            self.neighbours.append(grid[self.row + 1][self.col])
            self.neighbours.append(grid[self.row ][self.col + 1])
            self.neighbours.append(grid[self.row ][self.col - 1])
        return self.neighbours




            

    def get_row(self):
        return self.row
    def get_col(self):
        return self.col
    def get_size(self):
        return self.size

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_pos(self):
        return self.row, self.col

    def get_colour(self):
        return self.colour

    #the node has been searched
    def is_searched(self):
        return self.is_searched == RED

    def make_searched(self):
        self.colour = RED
        self.is_searched = True

    def get_iswall(self):
        return self.is_wall

    def make_wall(self):
        self.colour = BLACK
        self.is_wall = True

    #This will determine the start Node
    def toggle_start(self):
        self.colour = BLUE

    def toggle_end(self):
        self.colour = ORANGE
    def toggle_rightPath(self):
        self.colour = GREEN
    def toggle_finding(self):
        self.colour = RED
    def draw(self,win):
        pygame.draw.rect(win,self.colour,(self.x,self.y,self.size,self.size))

    def update_neighbours(self,grid):
        pass
    def setCame_from(self,newSquare):
        self.came_from = newSquare
    def getCame_from(self):
        return self.came_from

    #The heuristic that will be used for A* using manhattan distance
    def heuristic(pos1,pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x1 - x2) + abs(y1 - y2)
