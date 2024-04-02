from cs1graphics import *
class Bird:
    def __init__(self,x ,y):
        self.bird = Layer()
        self.body = Circle(10, Point(x,y))
        self.body.stretch(xFactor=3, yFactor=1)
        self.wing1 = Circle(10, Point(x,y))
        self.wing2 = Circle(10, Point(x,y))
        self.wing1.stretch(xFactor=1, yFactor=2)
        self.wing1.move(5,15)
        self.wing2.stretch(xFactor=1, yFactor=2)
        self.wing2.move(5,-15)

        self.wing1.setFillColor('White')
        self.wing2.setFillColor('White')
        self.wing1.setBorderWidth(0)
        self.wing2.setBorderWidth(0)
        self.body.setFillColor('White')
        self.body.setBorderWidth(0)

        self.beak = Polygon(Point((x+40)-5,y),Point((x+40)-15,y-3),Point((x+40)-15,y+3))
        self.beak.setFillColor('Yellow')
        self.beak.setBorderWidth(0)

        
        self.bird.add(self.body)
        self.bird.add(self.wing1)
        self.bird.add(self.wing2)
        self.bird.add(self.beak)

    def getBirdLayer(self):
        return self.bird
    def changeReferencePoint(self,x,y):
        self.bird.adjustReference(x,y)