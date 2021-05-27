import math


class Da:

    def __init__(self, zhi, c100, m100, y100, cm100, cy100, my100, cmy100):
        self.zhi = zhi if len(zhi) == 3 else [0] * 3
        self.C100 = c100 if len(c100) == 3 else [0] * 3
        self.M100 = m100 if len(m100) == 3 else [0] * 3
        self.Y100 = y100 if len(y100) == 3 else [0] * 3
        self.CM100 = cm100 if len(cm100) == 3 else [0] * 3
        self.CY100 = cy100 if len(cy100) == 3 else [0] * 3
        self.MY100 = my100 if len(my100) == 3 else [0] * 3
        self.CMY100 = my100 if len(cmy100) == 3 else [0] * 3
        self.default_lab = [1, 1, 1]

    def pri(self):
        return self.zhi, self.C100, self.M100, self.Y100, self.CM100, self.CY100, self.MY100

    def set_lab(self, lab):
        self.default_lab = lab if len(lab) == 3 else [1, 1, 1]

    def get_lab(self, x, y, z):
        return 116 * self.f(y / self.default_lab[1]) - 16, \
               500 * (self.f(x / self.default_lab[0]) - self.f(y / self.default_lab[1])), \
               200 * (self.f(y / self.default_lab[1]) - self.f(z / self.default_lab[2])),

    @staticmethod
    def f(i_):
        if i_ > 0.008856:
            return math.pow(i_, 1 / 3)
        else:
            return 7.787 * i_ + 16 / 116

    def ji_sun(self, c, m, y, x_, y_, z_):

        def get_value(index):
            sum_ = c + m + y
            p = 1
            cp = p * c / sum_
            mp = p * m / sum_
            yp = p * y / sum_

            v = cp * (1 - mp) * (1 - yp) * self.C100[index] + \
                yp * (1 - cp) * (1 - mp) * self.Y100[index] + \
                mp * (1 - yp) * (1 - cp) * self.M100[index] + \
                cp * mp * (1 - yp) * self.CM100[index] + \
                cp * yp * (1 - mp) * self.CY100[index] + \
                mp * yp * (1 - cp) * self.MY100[index] + \
                mp * yp * cp * self.CMY100[index] + \
                (1 - cp) * (1 - mp) * (1 - yp) * self.zhi[index]
            return v

        return get_value(0), get_value(1), get_value(2)


# a = Da(
#     [84.63, 87.85, 72.31],
#     [17.41, 25.95, 54.23],
#     [38.57, 21.87, 22.53],
#     [69.17, 75.10, 7.54],
#     [36.05, 21.68, 3.23],
#     [20.35, 30.05, 12.65],
#     [8.22, 6.72, 22.69],
#     [0.99, 1.06, 0.93]
# )
# a = Da(
#     [1, 87.85, 72.31],
#     [1, 25.95, 54.23],
#     [1, 21.87, 22.53],
#     [1, 75.10, 7.54],
#     [1, 21.68, 3.23],
#     [1, 30.05, 12.65],
#     [1, 6.72, 22.69],
#     [1, 1.06, 0.93]
# )
# print(a.pri())
# print(a.jisun(69.71, 74.59, 23.84))
# # print(a.jisun(29.82, 33.07, 12.23))
# # print(a.jisun(6.51, 6.75, 7.30))
# print(a.jisun(10, 70, 10))
#
# a.set_lab([96.42, 100.00, 82.51])
# # print(a.get_lab(69.71, 74.59, 23.84))
# print(a.get_lab(47.67954, 38.40258000000001, 33.84337000000001))

# print(a.f(64))


d = []
with open("data.csv") as f:
    for i in f.readlines():
        i = i[:-1]
        # print(i.split(","))
        l = []
        # print(i)
        for j in i.split(",")[1:]:
            # print(j)
            # print(float(j))
            l.append(float(j))
        d.append(l)
zhi, c100, m100, y100, cm100, cy100, my100, cmy100 = d
a = Da(zhi, c100, m100, y100, cm100, cy100, my100, cmy100)
a.set_lab([96.42, 100.00, 82.51])

# print(a.pri())

with open("testdata.csv") as f:
    f.readline()
    for i in f.readlines():
        i = i[:-1]
        l = []
        # print(i)
        for j in i.split(",")[:]:
            # print(j)
            # print(float(j))
            l.append(float(j))
        print(l)
        print(a.ji_sun(l[0], l[1], l[2], l[3], l[4], l[5]))
