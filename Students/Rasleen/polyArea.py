class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        print("Area of rectangle: ", self.length * self.breadth)

class Square:
    def __init__(self, side):
        self.side = side 

    def area(self):
        print("Area of square: ", self.side**2)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of circle: ", 3.14*self.radius*self.radius)

class Equilateral_Triangle:
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area of Equilateral Triangle:", (3**0.5 / 4) * self.side * self.side)


square = Square(4)
rectangle = Rectangle(5, 6)
circle = Circle(3)
triangle = Equilateral_Triangle(4)

square.area()
rectangle.area()
circle.area()
triangle.area()