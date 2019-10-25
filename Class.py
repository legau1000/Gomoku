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
        self._Danger = danger

    def GetDanger(self):
        return self._Danger

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

    def AddMyMouve(self, x, y):
        self._Map[x][y].ChangePlayer('O')
        self._Map[x][y].ChangeDanger(0)

    def AddEnemyMouve(self, x, y):
        self._Map[x][y].ChangePlayer('P')
        self._Map[x][y].ChangeDanger(0)

    def PrintMap(self):
        for line in self._Map:
            for letter in line:
                print(letter.GetPlayer(), end='')
            print()

class MyGame:
    def __init__(self, size):
        self._size = size
        self._Map = MyMap(size)

    def PrintMap(self):
        self._Map.PrintMap()

    def GetSize(self):
        return self._size

    def addMyMouve(self, x, y):
        self._Map.AddMyMouve(x, y)

    def addEnemyMouve(self, x, y):
        self._Map.AddEnemyMouve(x, y)
