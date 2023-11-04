"""
Create a Python program that explores polymorphism using a hierarchy of shapes.
Start with a base class Shape, and then create two or more derived classes
(e.g., Circle, Rectangle, Triangle) that inherit from the Shape class.
Each shape class should have its own implementation of methods like area() and perimeter().
 These methods will calculate the area and perimeter of the respective shape.
"""
import math


class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        print("Every shape has a area!")

    def perimeter(self):
        print("Every shape has a perimetr!")


class Circle(Shape):
    def __init__(self, color, radius):
        Shape.__init__(self, color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, color, length, width):
        Shape.__init__(self, color)
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.length * self.width)


class Triangle(Shape):
    def __init__(self, color, base, height, a, c):
        Shape.__init__(self, color)
        self.base = base
        self.height = height
        self.a = a
        self.c = c

    def area(self):
        return self.base * self.height / 2

    def perimeter(self):
        return self.base * self.a * self.c


triangle1 = Triangle("green", 5, 5, 5, 5)
rectangle1 = Rectangle("red", 5, 10)
circle1 = Circle("white", 5)
shape1 = Shape("black")
print("Area of {} triangle = ".format(triangle1.color))
print(triangle1.area())
print("perimeter of {} triangle = ".format(triangle1.color))
print(triangle1.perimeter())
print("Area of {} circle = ".format(circle1.color))
print(circle1.area())
print("perimeter of {} circle = ".format(circle1.color))
print(circle1.perimeter())
print("Area of {} rectangle = ".format(rectangle1.color))
print(rectangle1.area())
print("perimeter of {} rectangle = ".format(rectangle1.color))
print(rectangle1.perimeter())
print("Area of {} shape = ".format(shape1.color))
print(shape1.area())
print("perimeter of {} shape = ".format(shape1.color))
print(shape1.perimeter())
