from cs1graphics import *
class Plane:
    def __init__(self):
        pass

    def getPlaneLayer(self, x ,y):
        plane = Layer()
        
        self.body = Circle(20, Point(x,y))

        self.body.stretch(xFactor=3, yFactor=1)
        wing1 = Polygon(Point(x+25,y), Point(x+50, y+75), Point(x-50, y))
        wing2 = wing1.clone()
        wing2.flip(angle=90)
        wing2.setFillColor('black')
        wing1.setFillColor('black')
        self.body.setFillColor('black')



        plane.add(self.body)
        plane.add(wing1)
        plane.add(wing2)
        
        return plane
    
    def getPos(self):
        return self.body.getReferencePoint()