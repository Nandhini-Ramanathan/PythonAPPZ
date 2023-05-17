from ninja import Ninja
class Obstacle(object):
    def __init__ (self, xpos, ypos, xspeed):
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        img = loadImage("rock.png")
        image(img, self.xpos, self.ypos)
    
    def move(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = -50
    
    def intersect(self, ninja):
        if self.xpos < ninja.xpos + ninja.xpos + 100 or self.xpos + 50 > ninja.xpos and self.ypos < ninja.ypos + ninja.ypos + 100 and self.ypos + 50 > ninja.ypos:
            return True
        else:
            return False
