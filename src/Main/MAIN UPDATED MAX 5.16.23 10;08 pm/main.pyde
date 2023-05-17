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
    elif screen >= 2:
        playScreen()
    # for obstacle in obstacles:
    #     if obstalce.intersect(myNinja1) == True:
    #         println('game over')

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
        # if obstacle.intercept(myNinja1) == True:
        #     background(0)
        #     text("GAME OVER", width/2, width/2)
    
def keyPressed():
    global ninja
    if 10 <= myNinja1.ypos <= 620:
        if keyCode == UP or key == 'w':
            myNinja1.ypos -= 30
    if -10 <= myNinja1.ypos <= 600:
        if keyCode == DOWN or key == 's':
            myNinja1.ypos += 30
    if -10 <= myNinja1.xpos <= 810:
        if keyCode == RIGHT or key == 'd':
            myNinja1.xpos += 30
    if 20 <= myNinja1.xpos <= 820:
        if keyCode == LEFT or key == 'a':
            myNinja1.xpos -= 30
            
