#
# Machine Problem 5
#
# Drei Luna
#
# Description: This script will use the cs1graphics module to create a graphics
# scene and then animate the scene. The inital scene has a sun , clouds and a bird.
# afterwords a plane and another bird fly on screen and off screen.
#


from cs1graphics import *
import math
import random
import time
from cloud import Cloud
from plane import Plane
from bird import Bird


root = Canvas(1000,500,'skyblue','myWorld')

grass = Rectangle(1000,300)
grass.moveTo(500,630)
grass.setFillColor('Dark Green')
grass.setBorderWidth(0)
root.add(grass)


def makeCloud(origin:list, rad:int, cRad:int, divisions:int=5):
    '''
    cRad is a irrelevent parameter to keep this algorithim from dividing itself. Please repeat your radius value for this parameter
    '''
    if divisions > 0:
        root.add(Cloud(origin, rad, int((rad/10)+1), int(cRad/2)).getCloudLayer())
        makeCloud(origin, (2*rad)/3, cRad, divisions-1,)




plane = Plane().getPlaneLayer(1000,125)
bird = Bird(500,200)
bird.changeReferencePoint(500,300)
birdLayer = bird.getBirdLayer()
root.add(birdLayer)
secondBirdLayer = birdLayer.clone()
secondBirdLayer.moveTo(-10,400)
secondBirdLayer.rotate(-35)
root.add(secondBirdLayer)
root.add(plane)


def animate(payload,secondPayload,thirdPayload):
    for i in range(1100):
        time.sleep(.001)
        payload.move(-1, 0)
        secondPayload.rotate(.49)
        thirdPayload.move(1,-1)
        





makeCloud([500,100], 50, 50)
makeCloud([200,350], 50, 50)
makeCloud([624,400], 50, 50)
makeCloud([784,233], 50, 50)
makeCloud([130,157], 50, 50)


animate(plane,birdLayer,secondBirdLayer)


