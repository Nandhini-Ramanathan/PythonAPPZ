#Nandhini
class Bg(object):
    def __init__(self, xpos, ypos, xspeed):
        self.xpos = xpos
        self.ypos = ypos 
        self.xspeed = xspeed
        
    def display(self):
        # fill(255)
        # noStroke()
        # rect(self.xpos, self.ypos, 500, 500);
        img = loadImage("background.png")
        image(img, self.xpos, 0)

    def move(self):
        self.xpos = self.xpos - self.xspeed;
        if self.xpos > width:
            self.xpos = 0
            
            
