class Obstacle(object):
    def __init__ (self, xpos, ypos, xspeed):
        self.xpos = int(random(
        self.ypos = ypos
        self.xspeed = xspeed
    
    def display(self):
        img = loadImage("rock.png")
        image(img, self.xpos, self.ypos)
    
    def move(self):
        self.xpos = self.xpos - self.xspeed;
        if self.xpos > width:
            self.xpos = width
        
    boolean intersect(self, ninja):
        d = dist(self.x, self.y, ninja.x, ninja.y)
        if d < 50:
            return True
        else:
            return False
