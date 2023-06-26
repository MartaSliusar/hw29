class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __add__(self, other):
        area = self.get_area() + other.get_area()
        width = int(area / (self.height + other.height))
        height = int(area / width)
        return Rectangle(width, height)

    def __mul__(self, n):
        area = self.get_area() * n
        width = int(area / self.height)
        height = int(area / width)
        return Rectangle(width, height)

    def __str__(self):
        return f" {Rectangle({self.width}, {self.height})}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_area() == 8
assert r2.get_area() == 18

r3 = r1 + r2
assert r3.get_area() == 26

r4 = r1 * 4

assert r4.get_area() == 32
