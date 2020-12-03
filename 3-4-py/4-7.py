class animal:
    def __init__(self, age):
        self.__age = age

    def print2(self):
        print(self.__age)


class dog(animal):
    def __init__(self, age):
        animal.__init__(self, age)

    def print2(self):
        print(self.__age)


a_animal = animal(10)
a_animal.print2()
# result: 10
a_dog = dog(10)
a_dog.print2()
# 程序报错，AttributeError: dog instance has no attribute '_dog__age'
