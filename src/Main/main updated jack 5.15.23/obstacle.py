from ninja import Ninja
class Obstacle(object):
    def __init__ (self, xpos, ypos, xspeed):
        self.xpos = 100
        self.ypos = 100
        self.xspeed = -5    
        
    def display(self):
        img = loadImage("rock.png")
        image(img, self.xpos, self.ypos)
    
    def move(self):
        self.xpos = self.xpos - self.xspeed;
        if self.xpos > width:
            self.xpos = width
        
    def intersect(self, ninja):
        if self.x < ninja.x + ninja.width and self.x + self.width > ninja.x and self.y < ninja.y + ninja.height and self.y + self.height > ninja.y:
            return True
        else:
            return False
