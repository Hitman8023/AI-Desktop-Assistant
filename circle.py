import math

class Circle:
    def __init__(self, radius):
        self.radius = float(radius) 

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


value = float(input("Pass the radius: "))
circle = Circle(value)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
