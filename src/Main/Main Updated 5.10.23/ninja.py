class Ninja(object):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.h = 20

    def display(self):
        # fill(0)
        # noStroke()
        # rect(self.xpos, self.ypos, 30, 50)
        img = loadImage("running.png")
        image(img, self.xpos, self.ypos)
        
        
