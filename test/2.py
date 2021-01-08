import math


# l = 78.2
# a = 104.5
# b = 76.2
#
# while True:
#     L = input("lab")
#     L, A, B = L.split(" ")
#     L = float(L)
#     A = float(A)
#     B = float(B)
#
#     res = ((L - l)*(L - l) + (A - a)*(A-a) + (B - b)*(B-b))/3
#     import math
#     res = math.sqrt(res)
#     print(res)


class RuleEva:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.k = 2

    def like_li_hood_ratio(self, a1, b1):
        """
        似然比统计量
        a : +
        b : -
        """
        a2 = a1 * math.log2(a1 / (self.a / (self.a + self.b)))
        b2 = b1 * math.log2(b1 / (self.b / (self.a + self.b)))
        return 2 * (a2 + b2)

    def foil(self, a1, b1):
        """
        FOIL 信息增益
        :param a1:
        :param b1:
        :return:
        """
        a2 = math.log2(a1 / (a1 + b1))
        b2 = math.log2(self.a / (self.a + self.b))
        return a1 * (a2 - b2)

    def laplace(self, a1, b1):
        n = a1 + b1
        return (a1 + 1) / (n + self.k)

    def m(self, a1, b1, p):
        n = a1 + b1
        return (a1 + self.k * p) / (n + self.k)


d = RuleEva(100, 400)
l1 = [[4, 1], [30, 10], [100, 90]]
print("i[0], i[1]", "似然比统计量", 'foil', "laplace", "m")
for i in l1:
    res = d.like_li_hood_ratio(i[0], i[1])
    print(i[0], i[1], res, end="   ")
    res = d.foil(i[0], i[1])
    print(res, end="    ")
    res = d.laplace(i[0], i[1])
    print(res, end="   ")
    res = d.m(i[0], i[1], 0.2)
    print(res, end="\n")
