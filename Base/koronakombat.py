# This module allows for turn based combat. Right now it is being developed
# Therefore, this is a work in progress.

# Agent will be the base class that enemies and the player will derive
# combat capabilities from
class Agent():
    def __init__(self, hp, mp, at, df, ag, lk, ml, name):
        self.hp = hp
        self.maxHP = hp
        self.mp =mp
        self.maxMP = mp
        self.at = at
        self.df = df
        self.ag = ag
        self.lk = lk
        self.moveList = ml
        self.name = name


# Enemies are Agents with added functionality to make decisions.
# Later will add more specific things like what items they have, how much
# exp they drop, and how much currency they drop
class Enemy():
    def __init__(self, e):
        self.hp = e.hp
        self.maxHP = e.hp
        self.mp = e.mp
        self.maxMP = e.mp
        self.at = e.at
        self.df = e.df
        self.ag = e.ag
        self.lk = e.lk
        self.moveList = e.moveList
        self.name = e.name

        self.getDecision = e.getDecision
# Im pretty sure that the enemy class will be removed
# there is no need for it, due to needing to overwrite
# all functions and data for each enemy type


# Right now, Hero is just an alias for Agent, but potentionally later will have
# more things like an inventory.
class Hero(Agent):
    pass

# Creating a kombat object runs the combat system. This will likely be changed in the
# future. In this state, perhaps a destructor can be written to handle the end of a combat
# encounter?
class Kombat():
    def __init__(self, loc):
        self.enem = self.getEnemy(loc)

    # pass in a string for the name of the attack, and an Agent to attack
    # returns damage but handles changing hp.
    def doDamage(self, move, attacker, target):
        from masterMoveDict import mmd

        msg, damage = mmd[move](attacker, target)
        print(str(msg))
        target.hp = target.hp - damage

        return msg

    def getEnemy(self, loc):
        from enemyList import enemyMap
        import random
        return (random.choice(enemyMap[loc])).__class__()


    # Function that runs combat
    def check_for_defeat(self,f1, f2, selection):
        if(f1.hp>0 and f2.hp >0):
            print(f1.moveList)
            print(f1.hp, "/", f1.maxHP, "HP")
            choice = selection
            player_msg = self.doDamage(f1.moveList[int(choice)],f1,f2)

            if(f2.hp<=0):
                print("You have defeated the monster! :)")
                msg = "You have defeated the monster! :)"
            else:
                enemy_msg  = self.doDamage(f2.getDecision(f1), f2, f1)
                status = "\n"+str(f1.hp) + "/" + str(f1.maxHP) + "HP"
                msg = player_msg + "\n" + enemy_msg + status
                if(f1.hp<=0):
                    print("You are dead as shit")
                    msg = "You are dead as shit"
                    exit()
            return msg

# need to write what happens when a battle ends
#    def __del__(self):
#        pass


