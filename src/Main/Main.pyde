from ninja import Ninja
from background import Background
# Nandhini

myNinja1 = Ninja(250, 500)
myBackground1 = Background(500, 250,2)

def setup():
    size(1000,800)

def draw(): 
  myBackground1.move()
  myBackground1.display()
  myNinja1.display()
