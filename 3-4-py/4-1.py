class Charmander:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getInfo(self):
        return self

a = Charmander()
a.setName("茂场晶彦")
print(a.getName())
print(a.getInfo())