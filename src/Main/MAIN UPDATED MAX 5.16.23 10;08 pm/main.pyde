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
    img = loadImage("startscreen2.png")
    screen = 1
    for i in range (3):
        obstacle = Obstacle(random(1000,1200), random(150, 600), random(3,10))
        obstacles.append(obstacle)

def draw():  
    global obstacle
    print(screen)
    if screen == 1:
        startScreen()
    elif screen == 2 or 4:
        playScreen()
    elif obstacle.intersect() == True:
        gameOver()

def mouseClicked():
    global screen
    if screen == 1:
        screen = 2
    elif screen == 2:
        screen = 3

def startScreen():
    global img
    image(img, 0, 0)

def playScreen():
    noCursor()
    global myBg1
    global ninja
    global obstacle
    background(0)
    myBg1.display()
    myNinja1.display()
    for obstacle in obstacles:
        obstacle.display()
        obstacle.move()
        if obstacle.intersect(myNinja1) == True:
            gameOver()
            
def gameOver():
    textMode(CENTER)
    background(0)
    textSize(50)
    text("GAME OVER", 360, height/2)
    noLoop()
    
def keyPressed():
    global ninja
    if 10 <= myNinja1.ypos <= 610:
        if keyCode == UP or key == 'w':
            myNinja1.ypos -= 15
    if 0 <= myNinja1.ypos <= 600:
        if keyCode == DOWN or key == 's':
            myNinja1.ypos += 15
    if -10 <= myNinja1.xpos <= 810:
        if keyCode == RIGHT or key == 'd':
            myNinja1.xpos += 15
    if 10 <= myNinja1.xpos <= 830:
        if keyCode == LEFT or key == 'a':
            myNinja1.xpos -= 15
            
