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

    def PutDanger(self, x, y):
        size = int(3)
        value = int(3)
        for index in range(size):
            if (y - index - 1 >= 0 and self._Map[x][y - index - 1].GetPlayer() == '.'):
                self._Map[x][y - index - 1].ChangeDanger(value - index)
            else:
                break
        for index in range(size):
            if (y + index + 1 < self.size and self._Map[x][y + index + 1].GetPlayer() == '.'):
                self._Map[x][y + index + 1].ChangeDanger(value - index)
            else:
                break
        for index in range(size):
            if (x - index - 1 >= 0 and self._Map[x - index - 1][y].GetPlayer() == '.'):
                self._Map[x - index - 1][y].ChangeDanger(value - index)
            else:
                break
        for index in range(size):
            if (x + index + 1 < self.size and self._Map[x + index + 1][y].GetPlayer() == '.'):
                self._Map[x + index + 1][y].ChangeDanger(value - index)
            else:
                break
        for index in range(size):
            if (x - index - 1 >= 0 and y - index - 1 >= 0 and self._Map[x - index - 1][y - index - 1].GetPlayer() == '.'):
                self._Map[x - index - 1][y - index - 1].ChangeDanger(value - index)
            else:
                break
        for index in range(size):
            if (x + index + 1 < self.size and y + index + 1 < self.size and self._Map[x + index + 1][y + index + 1].GetPlayer() == '.'):
                self._Map[x + index + 1][y + index + 1].ChangeDanger(value - index)
            else:
                break
        for index in range(size):
            if (x + index + 1 < self.size and y - index - 1 >= 0 and self._Map[x + index + 1][y - index - 1].GetPlayer() == '.'):
                self._Map[x + index + 1][y - index - 1].ChangeDanger(value - index)
            else:
                break
        for index in range(size):
            if (y + index + 1 < self.size and x - index - 1 >= 0 and self._Map[x - index - 1][y + index + 1].GetPlayer() == '.'):
                self._Map[x - index - 1][y + index + 1].ChangeDanger(value - index)
            else:
                break

    def GetMostDanger(self):
        #sous forme 1->dangereusité  2->x  3->y
        TabMouve = []
        bestScore = int(1)
        for index in range(len(self._Map)):
            for idx in range(len(self._Map[index])):
                if (self._Map[index][idx].GetPlayer() == '.' and int(self._Map[index][idx].GetDanger()) >= bestScore):
                    if (self._Map[index][idx].GetDanger() == bestScore):
                        TabMouve.append([self._Map[index][idx].GetDanger(), index + 1, idx + 1])
                    elif int(self._Map[index][idx].GetDanger()) > int(bestScore):
                        bestScore = int(self._Map[index][idx].GetDanger())
                        TabMouve.clear()
                        TabMouve.append([self._Map[index][idx].GetDanger(), index + 1, idx + 1])
        #print(TabMouve)
        return TabMouve

    def PutSafe(self, x, y):
        size = int(3)
        value = int(3)
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
        self._player = 'O'
        self._Map = MyMap(size)

    def PrintMap(self):
        self._Map.PrintMap()

    def GetMoreDangerous(self):
        return self._Map.GetMostDanger()

    def GetSize(self):
        return self._size

    def addMouve(self, x, y):
        self._Map.AddMouve(x - 1, y - 1, self._player)
        self._Map.PutSafe(x - 1, y - 1)

    def addEnemyMouve(self, x, y):
        self._Map.AddMouve(x - 1, y - 1, 'P')
        self._Map.PutDanger(x - 1, y - 1)