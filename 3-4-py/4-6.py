class pokemon:
    def __init__(self, name, gender, level, type, status):
        self.__type = type
        self.__gender = gender
        self.__name = name
        self.__level = level
        self.__status = status
        self.__info = [self.__name, self.__type, self.__gender, self.__level,
                       self.__status]
        self.__index = -1

    def getName(self):
        return self.__name

    def getGender(self):
        return self.__gender

    def getType(self):
        return self.__type

    def getStatus(self):
        return self.__status

    def level_up(self):
        self.__status = [s + 1 for s in self.__status]
        self.__status[0] += 1  # HP每级增加2点，其余1点

    def __iter__(self):
        print('名字属性性别等级能力')
        return self

    def next(self):
        if self.__index == len(self.__info) - 1:
            raise StopIteration
        self.__index += 1
        return self.__info[self.__index]

a = pokemon("茂场晶彦", "男", 12,1,12)

print(a.getName())
print(a.getGender())
print(a.getType())
print(a.getStatus())