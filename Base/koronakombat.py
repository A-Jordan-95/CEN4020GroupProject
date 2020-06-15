
class Agent():
    def __init__(self, hp, at, df, ml, name):
        self.hp = hp
        self.MaxHP = hp
        self.at = at
        self.df = df
        self.moveList = ml
        self.name = name

    # pass in a string for the name of the attack, and an Agent to attack
    # returns damage
    def getDamage(self, move, target):
        import random
        masterMoveList = {"Smile": 0, "Attack": 1}
        if (masterMoveList[move]==0):
            print(self.name," stares at ", target.name)
            damage = 0;
        elif(masterMoveList[move]==1):
            print(self.name," attacks!")
            damage = int((self.at-(target.df/2))/2*(1+random.random()))

        print(self.name, " did ", damage, " damage to ", target.name)
        target.hp = target.hp - damage

        return damage

class Enemy(Agent):
    def getDecision(self,h):
        if(self.hp == self.MaxHP):
            return "Smile"
        else:
            return "Attack"

class Hero(Agent):
    pass

class Kombat():
    def __init__(self, f1, f2):
        while(f1.hp>0 and f2.hp >0):
            print(f1.moveList)
            print(f1.hp, "/", f1.MaxHP, "HP")
            choice = input("What would you like to do?")
            f1.getDamage(choice,f2)

            if(f2.hp<=0):
                print("You have defeated the monster! :)")
            else:
                f2.getDamage(f2.getDecision(f1), f1)
                if(f1.hp<=0):
                    print("You are dead as shit")






