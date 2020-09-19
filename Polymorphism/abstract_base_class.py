from abc import ABCMeta, abstractmethod

class Shape(metaclass= ABCMeta):
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        print("Area of square is: {}".format(self.side*self.side))

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def area(self):
         print("Area of rectangle is: {}".format(self.width*self.height))



square1 = Square(4)
square1.area()

rectangle1 = Rectangle(10,4)
rectangle1.area()
