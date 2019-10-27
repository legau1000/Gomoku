#!/usr/bin/env python3 

class MyDanger:
    def __init__(self):
        self._Danger = int(0)
        self._Player = '.'

    def ChangePlayer(self, player):
        self._Player = player

    def GetPlayer(self):
        return self._Player

    def ChangeDanger(self, danger):
        self._Danger += danger
        if (self._Danger < 0):
            self._Danger = 0

    def GetDanger(self):
        if (self._Player == '.'):
            return self._Danger
        else:
            return 0

class MyMap:
    def __init__(self, size):
        self.suite = 0
        self.size = size
        self.CreateMap(size)
    
    def CreateMap(self, size):
        self._Map = [[]]
        for index in range(size):
            self._Map.append([])
            for indexTwo in range(size):
                self._Map[index].append(MyDanger())

    def GetMap(self):
        return (self._Map)

    def AddMouve(self, x, y, letter):
        self._Map[x][y].ChangePlayer(letter)
        self._Map[x][y].ChangeDanger(0)

    def PrintMap(self):
        for line in self._Map:
            for letter in line:
                if (letter.GetPlayer() == '.' and letter.GetDanger() == 0):
                    print(letter.GetPlayer(), end='')
                elif (letter.GetPlayer() == '.'):
                    print(letter.GetDanger(), end='')
                else:
                    print(letter.GetPlayer(), end='')
            print()

    def cheackCase(self, x, y, value):
        if (y < 0 or y > self.size or x < 0 or x > self.size):
            return (0)
        if (self._Map[x][y].GetPlayer() == 'X'):
            return (0)
        if (self._Map[x][y].GetPlayer() == 'P'):
            self.suite = self.suite + 1
            return (value)
        self._Map[x][y].ChangeDanger(value)
        return (value - 1)

    def PutDanger(self, x, y):
        size = int(2)
        value = int(2)
        tabindex = [int(1), int(1), int(1), int(1), int(1), int(1), int(1), int(1)]
        tabValue = [int(2), int(2), int(2), int(2), int(2), int(2), int(2), int(2)]
        self.suite = 0
        while (tabValue[0] != 0):
            tabValue[0] = self.cheackCase(x, y - tabindex[0], tabValue[0])
            tabindex[0] = tabindex[0] + 1
        if (self.suite >= 2):
            #print("DANGER2 ++", self.suite * self.suite, x, y)
            self._Map[x][y + 1].ChangeDanger(self.suite * self.suite)

        self.suite = 0
        while (tabValue[1] != 0):
            tabValue[1] = self.cheackCase(x, y + tabindex[1], tabValue[1])
            tabindex[1] = tabindex[1] + 1
        if (self.suite >= 2):
            #print("DANGER ++", self.suite * self.suite, x, y)
            self._Map[x][y - 1].ChangeDanger(self.suite * self.suite)

        self.suite = 0
        while (tabValue[2] != 0):
            tabValue[2] = self.cheackCase(x - tabindex[2], y, tabValue[2])
            tabindex[2] = tabindex[2] + 1
        if (self.suite >= 2):
            #print("DANGER ++ + x", self.suite * self.suite, x, y)
            self._Map[x + 1][y].ChangeDanger(self.suite * self.suite)

        self.suite = 0
        while (tabValue[3] != 0):
            tabValue[3] = self.cheackCase(x + tabindex[3], y, tabValue[3])
            tabindex[3] = tabindex[3] + 1
        if (self.suite >= 2):
            #print("DANGER ++ - x", self.suite * self.suite, x, y)
            self._Map[x - 1][y].ChangeDanger(self.suite * self.suite)

        self.suite = 0
        while (tabValue[4] != 0):
            tabValue[4] = self.cheackCase(x - tabindex[4], y - tabindex[4], tabValue[4])
            tabindex[4] = tabindex[4] + 1
        if (self.suite >= 2):
            self._Map[x + 1][y + 1].ChangeDanger(self.suite * self.suite)

        self.suite = 0
        while (tabValue[5] != 0):
            tabValue[5] = self.cheackCase(x + tabindex[5], y + tabindex[5], tabValue[5])
            tabindex[5] = tabindex[5] + 1
        if (self.suite >= 2):
            self._Map[x - 1][y - 1].ChangeDanger(self.suite * self.suite)

        self.suite = 0
        while (tabValue[6] != 0):
            tabValue[6] = self.cheackCase(x + tabindex[6], y - tabindex[6], tabValue[6])
            tabindex[6] = tabindex[6] + 1
        if (self.suite >= 2):
            self._Map[x - 1][y + 1].ChangeDanger(self.suite * self.suite)

        self.suite = 0
        while (tabValue[7] != 0):
            tabValue[7] = self.cheackCase(x - tabindex[7], y + tabindex[7], tabValue[7])
            tabindex[7] = tabindex[7] + 1
        if (self.suite >= 2):
            self._Map[x + 1][y - 1].ChangeDanger(self.suite * self.suite)

    def GetMostDanger(self):
        #sous forme 1->dangereusité  2->x  3->y
        TabMouve = []
        bestScore = int(1)
        for index in range(len(self._Map)):
            for idx in range(len(self._Map[index])):
                if (self._Map[index][idx].GetPlayer() == '.' and int(self._Map[index][idx].GetDanger()) >= bestScore):
                    if (self._Map[index][idx].GetDanger() == bestScore):
                        TabMouve.append([self._Map[index][idx].GetDanger(), index, idx])
                    elif int(self._Map[index][idx].GetDanger()) > int(bestScore):
                        bestScore = int(self._Map[index][idx].GetDanger())
                        TabMouve.clear()
                        TabMouve.append([self._Map[index][idx].GetDanger(), index, idx])
        #print(TabMouve)
        return TabMouve

    def PutSafe(self, x, y):
        size = int(2)
        value = int(2)
        for index in range(size):
            if (y - index - 1 >= 0 and self._Map[x][y - index - 1].GetPlayer() == 'P'):
                for idx in range(size - index):
                    self._Map[x][y + idx].ChangeDanger(-(value - idx))
            if (y + index + 1 < self.size and self._Map[x][y + index + 1].GetPlayer() == 'P'):
                for idx in range(size - index):
                    self._Map[x][y - idx].ChangeDanger(-(value - idx))

            if (x - index - 1 >= 0 and self._Map[x - index - 1][y].GetPlayer() == 'P'):
                for idx in range(size - index):
                    self._Map[x + idx][y].ChangeDanger(-(value - idx))
            if (x + index + 1 < self.size and self._Map[x + index + 1][y].GetPlayer() == 'P'):
                for idx in range(size - index):
                    self._Map[x - idx][y].ChangeDanger(-(value - idx))

            if (x - index - 1 >= 0 and y +  index + 1 < self.size and
                self._Map[x - index - 1][y + index + 1].GetPlayer() == 'P'):
                for idx in range(size - index):
                    self._Map[x + idx][y - idx].ChangeDanger(-(value - idx))
            if (y - index - 1 >= 0 and x +  index + 1 < self.size and
                self._Map[x + index + 1][y - index - 1].GetPlayer() == 'P'):
                for idx in range(size - index):
                    self._Map[x - idx][y + idx].ChangeDanger(-(value - idx))

            if (x - index - 1 >= 0 and y - index - 1 >= 0 and
                self._Map[x - index - 1][y - index - 1].GetPlayer() == 'P'):
                for idx in range(size - index):
                    self._Map[x + idx][y + idx].ChangeDanger(-(value - idx))
            if (y +  index + 1 < self.size and x + index + 1 < self.size and
                self._Map[x + index + 1][y + index + 1].GetPlayer() == 'P'):
                for idx in range(size - index):
                    self._Map[x - idx][y - idx].ChangeDanger(-(value - idx))

class MyGame:
    def __init__(self, size):
        self._size = size
        self._player = 'X'
        self._Map = MyMap(size)

    def PrintMap(self):
        self._Map.PrintMap()

    def GetMoreDangerous(self):
        return self._Map.GetMostDanger()

    def GetSize(self):
        return self._size

    def addMouve(self, x, y):
        self._Map.AddMouve(x, y, self._player)
        self._Map.PutSafe(x, y)

    def addEnemyMouve(self, x, y):
        self._Map.AddMouve(x, y, 'P')
        self._Map.PutDanger(x, y)