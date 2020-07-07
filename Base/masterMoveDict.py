# This file will contain all attacks written as function that takes two Agent objects
# These functions will be placed into a dictionary called mmd. To use an atack, one
# must simply call like mmd["NameOfAttack"](attackingAgent, defendingAgent)
# this call will return the damage that is dealt by the attack, leading to a suggested
# syntax: damage = mmd["NameOfAttack"](attackingAgent, defendingAgent)
#
# For reference, here is the init for the Agent class (as of 6/23/2020)
#
#    def __init__(self, hp, at, df, ml, name):
#        self.hp = hp
#        self.maxHP = hp
#        self.at = at
#        self.df = df
#        self.moveList = ml
#        self.name = name

import random

def attack(attacker, target):
    dmg =  int((attacker.at-(target.df/2))/2*(1+random.random()))
    msg = attacker.name + " attacks!" + '\n'+ attacker.name +" did "+ str(dmg)+ " damage to " + target.name
    return msg, dmg

def smile(attacker, target):
    dmg = 0
    msg = attacker.name + " stares at " + target.name + '\n'+ attacker.name +" did "+ str(dmg)+ " damage to " + target.name
    return msg, dmg

def chortle(attacker, target):
    dmg = 0
    msg = attacker.name + " goes \"HOHOHO\"\n"+ attacker.name +" did "+ str(dmg)+ " damage to " + target.name
    return msg, dmg

def cough(attacker, target):
    dmg = 0
    msg = attacker.name + " coughs at " + target.name + "\n" + attacker.name +" did "+ str(dmg)+ " damage to " + target.name
    return msg, dmg

mmd = {"Run": None, "Hide": None, "Smile": smile, "Attack": attack, "Chortle": chortle, "Cough on": cough}


