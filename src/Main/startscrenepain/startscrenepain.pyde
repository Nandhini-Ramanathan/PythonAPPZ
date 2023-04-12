# Carter Newberg and Jack Barklow - 4/5/23 - Game start not functional, start screen displays
from button import Button
global screen

def setup():
    size(800, 600)
    global img
    global img2
    img = loadImage("startscreen.png")
    img2 = loadImage("gameplaymockup.png")
    screen = 1
    
def draw():
    # image(ing, 0, 0)
    if screen == 1:
        startScreen()
    elif screen == 2:
        playScreen()

def mousePressed():
    if screen == 1:
        screen = 2
    elif screen == 2:
        screen = 3

def startScreen():
    background(0)
    global img
    image(img, 0, 0)

def playScreen():
    background(0)
    global img2
    image(img2, 0, 0)
