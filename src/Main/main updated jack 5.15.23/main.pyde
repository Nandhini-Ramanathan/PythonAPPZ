from ninja import Ninja
from bg import Bg
from obstacle import Obstacle
myNinja1 = Ninja(250, 290)
myBg1 = Bg(0, 250)
obstacles = []

def setup():
    size(1000,800)
    global img
    global screen
    img = loadImage("startscreen.png")
    screen = 1

def draw(): 
    print(screen)
    if screen == 1:
        startScreen()
    elif screen >= 2:
        playScreen()


def mouseClicked():
    global screen
    if screen == 1:
        screen = 2
    elif screen == 2:
        screen = 3

def startScreen():
    global img
    image(img, 100, 50)

def playScreen():
    global myBg1
    background(0)
    myBg1.display()
    myNinja1.display()
    
def keyPressed():
    global ninja
    if 290 <= myNinja1.ypos <= 610:
        if keyCode == UP:
            myNinja1.ypos -= 160

    if 0 <= myNinja1.ypos <= 290:
        if keyCode == DOWN:
            myNinja1.ypos += 160
