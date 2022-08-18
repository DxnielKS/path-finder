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
        #self.traversed = False
        self.colour = WHITE
        self.neighbours = []


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
        return self.colour == RED
    
    def make_searched(self):
        self.colour = RED

    def is_wall(self):
        return self.colour == BLACK
    
    def make_wall(self):
        self.colour = BLACK
    
    #This will determine the start Node
    def toggle_start(self):
        self.colour = BLUE
    
    def toggle_end(self):
        self.colour = ORANGE


    def draw(self,win):
        pygame.draw.rect(win,self.colour,(self.x,self.y,self.size,self.size))

    def update_neighbours(self,grid):
        pass

    #The heuristic that will be used for A* using manhattan distance
    def heuristic(pos1,pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x1 - x2) + abs(y1 - y2)
