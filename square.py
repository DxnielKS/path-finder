class Square():
    def __init__(self,size,x,y):
        self.size=size
        self.x=x
        self.y=y
        self.traversed = False
        self.wall = False
    def get_size(self):
        return self.size
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def is_taversed(self):
        return self.traversed
    def is_wall():
        return self.wall
    def toggle_traversed(self):
        self.traversed=True
    def traverse(self):
        None