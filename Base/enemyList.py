# This file will contain a all enemies in the game, and will used by
# the getEnemy function from the Kombat class

class SmallChild():
    def __init__(self):
        self.hp = 6
        self.maxHP = 6
        self.mp = 4
        self.maxMP = 4
        self.at = 7
        self.df = 4
        self.ag = 5
        self.lk = 3
        self.moveList = ['Attack', 'Smile']
        self.name = 'Small Child'

    def getDecision(self,h):
        if(self.hp == self.maxHP):
            return "Smile"
        else:
            return "Attack"

class BigChild():
    def __init__(self):
        self.hp = 12
        self.maxHP = 12
        self.mp = 0
        self.maxMP = 0
        self.at = 8
        self.df = 5
        self.ag = 2
        self.lk = 1
        self.moveList = ['Attack', 'Chortle']
        self.name = 'Big Child'

    def getDecision(self,h):
        if(self.hp == self.maxHP):
            return "Chortle"
        else:
            return "Attack"

enemyMap = {"overworld":[SmallChild(), BigChild()], "DollarStore":[SmallChild(), BigChild()], "MalMart":[SmallChild(), BigChild()], "TheSchool":[SmallChild(), BigChild()], "hobo":[BigChild()], "kovid_mantis":[BigChild()], "karen_demon_from_hell":[BigChild()]}
