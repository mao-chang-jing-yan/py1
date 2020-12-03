class Shape:
    pass


class Reactangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getCircumference(self):
        return 2 * (self.a + self.b)

    def getArea(self):
        return self.a * self.b


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def getCircumference(self):
        import math
        return 2 * math.pi * self.r

    def getArea(self):
        import math
        return math.pi * self.r * self.r


class Square(Reactangle):
    pass


a = Square(1, 2)
print(a.getArea())
print(a.getCircumference())
