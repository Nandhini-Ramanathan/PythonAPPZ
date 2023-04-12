class Ninja(object):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def display(self):
        fill(0)
        noStroke()
        rect(self.xpos, self.ypos, 30, 50);
