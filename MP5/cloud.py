from cs1graphics import *
import math
import random

class Cloud:
    def __init__(self, initalOrigin:list, initalCloudRadius, initalCircles, initalCRad):
        self.origin = initalOrigin
        self.cloud_radius = initalCloudRadius
        self.circles = initalCircles
        self.cRad = initalCRad

    def getCloudLayer(self):
        cloud = Layer()
        change_in_degrees = 180/self.circles
        for i in range(self.circles+1):
            cloud.add(self.placeCircle(self.cRad, (math.cos(math.radians(change_in_degrees*i))*self.cloud_radius)+ self.origin[0], self.origin[1]-(math.sin(math.radians(change_in_degrees*i))*self.cloud_radius)))
        return cloud
    
    def placeCircle(self, cRad, x, y):
        temp = Circle(cRad,Point(x+random.randint(10,20),y+random.randint(10,20)))
        temp.setFillColor('white')
        temp.setBorderWidth(0)
        return temp