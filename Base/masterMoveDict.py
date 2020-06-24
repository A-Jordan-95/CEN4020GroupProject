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
    print(attacker.name," attacks!")
    return int((attacker.at-(target.df/2))/2*(1+random.random()))

def smile(attacker, target):
    print(attacker.name," stares at ", target.name)
    return 0

mmd = {"Smile": smile, "Attack": attack}


