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
        self.img = "Images/EnemySprites/CORONAPILLAR.png"

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
        self.img = "Images/EnemySprites/fatkid.png"

    def getDecision(self,h):
        if(self.hp == self.maxHP):
            return "Chortle"
        else:
            return "Attack"

class hobo():
    def __init__(self):
        self.hp = 30
        self.maxHP = 30
        self.mp = 0
        self.maxMP = 0
        self.at = 8
        self.df = 8
        self.ag = 9
        self.lk = 1
        self.moveList = ['Pee', 'Hug']
        self.name = 'Homeless Man'
        self.img = "Images/EnemySprites/homeless man.png"

    def getDecision(self,h):
        if(h.last == "Smile"):
            return "Hug"
        else:
            return "Pee"

class MalMartDemon():
    def __init__(self):
        self.hp = 30
        self.maxHP = 30
        self.mp = 0
        self.maxMP = 0
        self.at = 15
        self.df = 8
        self.ag = 6
        self.lk = 4
        self.moveList = ['Attack', 'Chortle']
        self.name = "MalMart Demon"
        self.img = "Images/EnemySprites/hell_worker.png"

    def getDecision(self,h):
        if(self.hp == self.maxHP):
            return "Chortle"
        else:
            return "Attack"

class DamnedSoul():
    def __init__(self):
        self.hp = 10
        self.maxHP = 10
        self.mp = 0
        self.maxMP = 0
        self.at = 5
        self.df = 3
        self.ag = 6
        self.lk = 1
        self.moveList = ['Attack', 'Chortle']
        self.name = "Damned Soul"
        self.img = "Images/EnemySprites/skull_enemy.png"

    def getDecision(self,h):
        if(self.hp == self.maxHP):
            return "Chortle"
        else:
            return "Attack"


class CovidMantis():
    def __init__(self):
        self.hp = 60
        self.maxHP = 60
        self.mp = 0
        self.maxMP = 0
        self.at = 8
        self.df = 5
        self.ag = 2
        self.lk = 1
        self.moveList = ['Attack', 'Chortle']
        self.name = 'Covid Mantis'
        self.img = "Images/EnemySprites/COVID_MANTIS_battle.png"

    def getDecision(self,h):
        if(self.hp == self.maxHP):
            return "Chortle"
        else:
            return "Attack"

class karenDemon():
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
        self.name = 'Karen Demon from Hell'
        self.img = "Images/EnemySprites/karen_combat.png"

    def getDecision(self,h):
        if(self.hp == self.maxHP):
            return "Chortle"
        else:
            return "Attack"

enemyMap = {"overworld":[KoronaPillar(), BigChild()], "DollarStore":[SmallChild(), BigChild()], "MalMart":[DamnedSoul(), MalMartDemon()], "TheSchool":[SmallChild(), BigChild()], "hobo":[hobo()], "covid_mantis":[CovidMantis()], "karen_demon_from_hell":[karenDemon()]}
