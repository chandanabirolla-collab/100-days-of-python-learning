class Shape:
    def area(self):
        print("This is a shape")


class Circle(Shape):
    def area(self):
        print("Area of Circle = πr²")


class Square(Shape):
    def area(self):
        print("Area of Square = side²")


circle = Circle()
square = Square()

circle.area()
square.area()