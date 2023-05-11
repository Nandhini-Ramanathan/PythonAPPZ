from ninja import Ninja
from bg import Bg

# Nandhini
myNinja1 = Ninja(250, 290)
myBg1 = Bg(500, 250, 2)

def setup():
    size(1000,800)
    global img
    global screen
    img = loadImage("startscreen.png")
    screen = 1
    imageMode(CORNER)

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
    myBg1.move()
    myNinja1.display()
    
def keyPressed():
    global ninja
    if key == CODED:
        if keyCode == UP:
            myNinja1.ypos -= 160
        if keyCode == DOWN:
            myNinja1.ypos += 160
            
def reachedEnd():
        if myBg1.xpos <= -myBg1.w:
            myBg1.xpos = 0
            image(myBg1.img, myBg1.xpos, 0)
        
