import math


class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_sides(self):
        print("Sides:", self.sides)


class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__([a, b, c])

    def area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


# Example usage:
triangle = Triangle(3, 4, 5)
triangle.display_sides()
print("Area:", triangle.area())
