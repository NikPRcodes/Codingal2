from abc import ABC, abstractmethod

class Shapes(ABC):
    def area(self):
        pass

    def perimeter(self):
        pass

    def display(self):
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

class Rectangle(Shapes):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

class Square(Shapes):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


rectangle = Rectangle(10, 5)
print("Rectangle:")
rectangle.display()

square = Square(7)
print("\nSquare:")
square.display()