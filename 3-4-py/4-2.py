class Charmander:
    def __init__(self, name, gender, level):
        self.type = ('fire', None)
        self.gender = gender
        self.name = name
        self.level = level
        self.status = [10 + 2 * level, 5 + 1 * level, 5 + 1 * level, 5 + 1 * level, 5 + 1 * level, 5 + 1 *
                       level]
        # 最大HP，攻击，防御，特攻，特防，速度

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getType(self):
        return self.type

    def getStatus(self):
        return self.status

a = Charmander("茂场晶彦", "男", 12)

print(a.getName())
print(a.getGender())
print(a.getType())
print(a.getStatus())
