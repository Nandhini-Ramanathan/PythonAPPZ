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
    for i in range (3):
        obstacle = Obstacle(random(1000,1200), random(150, 600), random(3,10))
        obstacles.append(obstacle)

def draw():  
    global obstacle
    print(screen)
    if screen == 1:
        startScreen()
    elif screen >= 2:
        playScreen()
    elif obstacle.intersect() == True:
        background(0)
        text("GAME OVER")

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
    global ninja
    global obstacle
    background(0)
    myBg1.display()
    myNinja1.display()
    for obstacle in obstacles:
        obstacle.display()
        obstacle.move()
    
def keyPressed():
    global ninja
    if 10 <= myNinja1.ypos <= 610:
        if keyCode == UP:
            myNinja1.ypos -= 15
    if 0 <= myNinja1.ypos <= 600:
        if keyCode == DOWN:
            myNinja1.ypos += 15
    if -10 <= myNinja1.xpos <= 810:
        if keyCode == RIGHT:
            myNinja1.xpos += 15
    if 10 <= myNinja1.xpos <= 830:
        if keyCode == LEFT:
            myNinja1.xpos -= 15
