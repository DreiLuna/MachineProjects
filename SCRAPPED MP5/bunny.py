from cs1graphics import *

class Bunny:
    def __init__(self, x_pos, y_pos):
        self.x_position = x_pos
        self.y_position = y_pos

    def getBunnyLayer(self):
        full_bunny = Layer()
        body = Circle(30, Point(self.x_position, self.y_position))
        body.setFillColor('white')
        body.setBorderWidth(0)
        head = Circle(18, Point(self.x_position, self.y_position-35))
        head.setFillColor('white')
        head.setBorderWidth(0)

        eye = Layer()
        eye_parts = []
        for i in range(0,4,2):
            if i == 0:
                mod = 1
            else:
                mod = -1
            eye_parts.append(Circle(5, Point(self.x_position-5*mod, self.y_position-40)))
            eye_parts[i].setFillColor('white')
            eye_parts.append(Circle(2, Point(self.x_position-5*mod, self.y_position-40)))
            eye_parts[i+1].setFillColor('black')
            eye_parts[i+1].setBorderWidth(0)

            eye.add(eye_parts[i])
            eye.add(eye_parts[i+1])


        ears = Layer()
        earL = []
        for i in range(2):
            if i == 0:
                mod = 1
            else:
                mod = -1
            earL.append(Circle(7, Point(self.x_position-5*mod, self.y_position-55)))
            earL[i].setFillColor('white')
            earL[i].setBorderWidth(0)
            ears.add(earL[i])
        
        feet = Layer()
        feetL =[]
        for i in range(2):
            if i == 0:
                mod = 1
            else:
                mod = -1
            feetL.append(Circle(7, Point(self.x_position-10*mod, self.y_position+30)))
            feetL[i].setFillColor('white')
            feet.add(feetL[i])
        
        nose = Polygon(Point(self.x_position-5, self.y_position-30),Point(self.x_position, self.y_position-35),Point(self.x_position+5, self.y_position-30))
        nose.setFillColor('pink')
        nose.setBorderWidth(0)

        nameTag = TextBox(20,10,Point(self.x_position, self.y_position))
        nameTag.setMessage('Bunny')
        nameTag.setFontColor('Black')
        nameTag.setBorderWidth(0)

        
        full_bunny.add(body)
        full_bunny.add(ears)
        full_bunny.add(head)
        full_bunny.add(eye)
        full_bunny.add(feet)
        full_bunny.add(nose)
        full_bunny.add(nameTag)

        

        return full_bunny