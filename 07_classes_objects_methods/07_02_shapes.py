'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class Circle:

    def __init__(self, radius):
        self.radius = float(radius)
        self.diameter = self.radius * 2

    def __circumference__(self, radius):
        self.radius = float(radius)
        import math
        self.circumference = 2 * math.pi * self.radius
        return self.circumference

    def __circle_area__(self, radius):
        self.radius = float(radius)
        import math
        self.area = math.pi ** 2 * self.radius
        return self.area

    def __str__(self):
        return f"Your circle has a radius of {self.radius}, a diameter of {self.diameter}, a circumference of {my_circle.__circumference__(my_circle.radius)}, and an area of {my_circle.__circle_area__(my_circle.radius)}."

class Rectangle:

    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def __perimeter__(self):
        self.perimeter = 2 * (self.length + self.width)
        return self.perimeter

    def __rectangle_area__(self):
        self.area = self.length * self.width
        return self.area

    def __str__(self):
        return f"Your rectangle has a length of {self.length}, a width of {self.width}, a perimeter of {my_rectangle.__perimeter__()}, and an area of {my_rectangle.__rectangle_area__()}."

my_circle = Circle(5.3)
print(my_circle.__str__())

my_rectangle = Rectangle(5.5, 10.7)
print(my_rectangle.__str__())
