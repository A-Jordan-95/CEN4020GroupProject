# This module allows for turn based combat. Right now it is being developed
# Therefore, this is a work in progress.

# Agent will be the base class that enemies and the player will derive
# combat capabilities from
class Agent():
    def __init__(self, hp, at, df, ml, name):
        self.hp = hp
        self.MaxHP = hp
        self.at = at
        self.df = df
        self.moveList = ml
        self.name = name

    # pass in a string for the name of the attack, and an Agent to attack
    # returns damage but handles changing hp.
    # this is just a protoype and wil be reworked
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

# Enemies are Agents withh added functionality to make decisions.
# Later will add more specific things like what items they have, how much 
# exp they drop, and how much currency they drop
class Enemy(Agent):
    def getDecision(self,h):
        if(self.hp == self.MaxHP):
            return "Smile"
        else:
            return "Attack"

# Right now, Hero is just an alias for Agent, but potentionally later will have
# more things like an inventory.
class Hero(Agent):
    pass


# Creating a kombat object runs the combat system. This will likely be changed in the
# future. In this state, perhaps a destructor can be written to handle the end of a combat
# encounter?
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






