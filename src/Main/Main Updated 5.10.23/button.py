class Button(object):
    
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.xpos = ypos
        
    def display(self):
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 50, 30)
