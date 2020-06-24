# This module allows for turn based combat. Right now it is being developed
# Therefore, this is a work in progress.

# Agent will be the base class that enemies and the player will derive
# combat capabilities from
class Agent():
    def __init__(self, hp, at, df, ml, name):
        self.hp = hp
        self.maxHP = hp
        self.at = at
        self.df = df
        self.moveList = ml
        self.name = name

# Enemies are Agents with added functionality to make decisions.
# Later will add more specific things like what items they have, how much
# exp they drop, and how much currency they drop
class Enemy(Agent):
    def getDecision(self,h):
        if(self.hp == self.maxHP):
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
    # pass in a string for the name of the attack, and an Agent to attack
    # returns damage but handles changing hp.
    def getDamage(self, move, attacker, target):
        from masterMoveDict import mmd

        msg, damage = mmd[move](attacker, target)
        print(str(msg))
        target.hp = target.hp - damage

        return damage

    # Function that runs combat
    def run(self,f1, f2):
        while(f1.hp>0 and f2.hp >0):
            print(f1.moveList)
            print(f1.hp, "/", f1.maxHP, "HP")
            choice = input("What would you like to do?")
            self.getDamage(choice,f1,f2)

            if(f2.hp<=0):
                print("You have defeated the monster! :)")
            else:
                self.getDamage(f2.getDecision(f1), f2, f1)
                if(f1.hp<=0):
                    print("You are dead as shit")


#    def __del__(self):
#        pass


