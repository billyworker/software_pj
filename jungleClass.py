class Chess:
    def __init__(self, x, y, rank, player, aType):
        self.__x = x
        self.__y = y
        self.__rank = rank
        self.__player = player
        self.__aType = aType

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getRank(self):
        return self.__rank

    def getPlayer(self):
        return self.__player

    def getName(self):
        return self.__player + self.__aType

    def setPos(self, x, y):
        self.__x = x
        self.__y = y

    def inPos(self, x, y):
        if self.__x == x and self.__y == y:
            return True
        else:
            return False

    def isName(self, name):
        if self.getName() == name:
            return True
        else:
            return False

# Den position
class Den:
    def __init__(self):
        self.__x = 3
        self.__aY = 0
        self.__bY = 8

    def isDen(self, x, y):
        if self.__x == x:
            if self.__aY == y or self.__bY == y:
                return True
        return False

    def isDenA(self, x, y):
        if self.__x == x and self.__aY == y:
            return True
        return False

    def isDenB(self, x, y):
        if self.__x == x and self.__bY == y:
            return True
        return False

# Trap position
class Trap:
    def __init__(self):
        self.__aY1 = 0
        self.__aY2 = 1
        self.__bY1 = 8
        self.__bY2 = 7

        self.__x1 = 2
        self.__x2 = 4
        self.__x3 = 3

    def isTrap(self, x, y):
        if self.__aY1 == y:
            if self.__x1 == x or self.__x2 == x:
                return True
        elif self.__aY2 == y:
            if self.__x3 == x:
                return True
        elif self.__bY1 == y:
            if self.__x1 == x or self.__x2 == x:
                return True
        elif self.__bY2 == y:
            if self.__x3 == x:
                return True
        return False

    def isTrapA(self, x, y):
        if self.__aY1 == y:
            if self.__x1 == x or self.__x2 == x:
                return True
        elif self.__aY2 == y:
            if self.__x3 == x:
                return True
        return False

    def isTrapB(self, x, y):
        if self.__bY1 == y:
            if self.__x1 == x or self.__x2 == x:
                return True
        elif self.__bY2 == y:
            if self.__x3 == x:
                return True
        return False

# river position
class River:
    def __init__(self):
        self.__x = {1, 2, 4, 5}
        self.__y = {3, 4, 5}

    def isRiver(self, x, y):
        if x in self.__x and y in self.__y:
            return True
        return False