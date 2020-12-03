class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def add(self, c):
        self.a = self.a + c.getA()
        self.b = self.b + c.getB()

    def show(self):
        if self.b > 0:
            print(str(self.a) + "+" + str(self.b) + "i")
        if self.b == 0:
            print(self.a)
        if self.b < 0:
            print(self.a + "" + self.b + "i")


c1 = Complex(2, 3)
c2 = Complex(8, -1)
c1.add(c2)
c1.show()
