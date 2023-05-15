class Bg(object):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos 
        
    def display(self):
        # fill(255)
        # noStroke()
        # rect(self.xpos, self.ypos, 500, 500);
        img = loadImage("background.png")
        image(img, self.xpos, 0)


            
            
    
    
            
