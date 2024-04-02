from cs1graphics import *
import math
import random
from tree import Tree
from bunny import Bunny

root = Canvas(1000,500,'blue','myWorld')

grass = Rectangle(1000,200)
grass.setFillColor((0,150,0))
grass.moveTo(500,400)
grass.setBorderWidth(0)
root.add(grass)

bunny = Bunny(200,300)
root.add(bunny.getBunnyLayer())
trees = []
locations = []

def placeRandomTree(i):
    x = random.randint(200,800)
    y = random.randint(300,400)

    
    if i == 0:
        can_run = True
    elif i == 1 and (x not in locations[0]):
        can_run = True
    elif i == 2 and (x not in locations[1]) and (x not in locations[0]):
        can_run = True
    else:
        can_run = False
        placeRandomTree(i)

    if can_run == True:
        locations.append([x+i for i in range(-150,151)])
        trees.append(Tree((x,y)))
        root.add(trees[i].getTreeLayer())

for i in range(3):
    placeRandomTree(i)




sun = Circle(30, Point(100, 50))
sun.setFillColor((188,188,188))
sun.setBorderWidth(0)
root.add(sun)

