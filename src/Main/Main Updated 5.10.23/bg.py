# class Bg(object):
#     def __init__(self, xpos, ypos, w, xspeed):
#         self.xpos = xpos
#         self.ypos = ypos 
#         self.w = w
#         self.xspeed = xspeed
        
#     def display(self):
#         background(0)
#         img = loadImage("background.png")
#         image(img, self.xpos, 0)

#     def move(self):
#         self.xpos = self.xpos - self.xspeed;
    
#     def reachedEnd(self):
#         if self.xpos <= -self.w:
#             img = loadImage("background.png")
#             image(img, 0, 0)            
class Bg(object):
    def __init__(self, xpos, ypos, w, xspeed):
        self.xpos = xpos
        self.ypos = ypos 
        self.w = w
        self.xspeed = xspeed
        self.img = loadImage("background.png")

    def display(self):
        background(0)
        image(self.img, self.xpos, 0)

    def move(self):
        self.xpos = self.xpos - self.xspeed;
    
    
            
