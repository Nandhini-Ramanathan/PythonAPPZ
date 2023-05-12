from ninja import Ninja
from bg import Bg
from button import Button

# Nandhini
myNinja1 = Ninja(250, 500)
myBg1 = Bg(500, 250, 2)

def setup():
    size(1000,800)
    
    # Carter Newberg and Jack Barklow - 4/5/23 - Game start not functional, start screen displays
    global img
    global screen
    img = loadImage("startscreen.png")
    screen = 1

def draw(): 
    print(screen)
    
    # Carter Newberg and Jack Barklow - 4/5/23 - Game start not functional, start screen displays
    if screen == 1:
        startScreen()
    elif screen == 2:
        playScreen()

def mouseClicked():
    global screen
    if screen == 1:
        screen = 2
    elif screen == 2:
        screen = 2

def startScreen():
    global img
    image(img, 100, 50)

def playScreen():
    background(0)
    myBg1.display()
    myBg1.move()
    myNinja1.display()
