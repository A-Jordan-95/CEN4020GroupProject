# This file will contain all attacks written as function that takes two Agent objects
# These functions will be placed into a dictionary called mmd. To use an atack, one
# must simply call like mmd["NameOfAttack"](attackingAgent, defendingAgent)
# this call will return the damage that is dealt by the attack, leading to a suggested
# syntax: damage = mmd["NameOfAttack"](attackingAgent, defendingAgent)
#
# For reference, here is the init for the Hero class (as of 7/8/2020)
#
# def __init__(self, hp, mp, at, df, ag, lk, ml, name):
#        self.hp = hp
#        self.maxHP = hp
#        self.mp =mp
#        self.maxMP = mp
#        self.at = at
#        self.df = df
#        self.ag = ag
#        self.lk = lk
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
    dmg = int((attacker.at-(target.df/2))/2*(1+random.random()))
    msg = attacker.name + " coughs on " + target.name + "\n" + attacker.name +" did "+ str(dmg)+ " damage to " + target.name
    return msg, dmg

def sungaze(attacker, target):
    dmg = 0
    heal = int((attacker.lk)*(1+random.random())/2)
    msg = attacker.name + " gazes at the sun lovingly..." + "\n" + attacker.name +" gained "+ str(heal)+ " HP points "
    attacker.hp = attacker.hp+heal
    if(attacker.hp>attacker.maxHP):
        attacker.hp = attacker.maxHP
    attacker.mp = attacker.mp - 1
    return msg, dmg

mmd = {"Run": None, "Hide": None, "Smile": smile, "Attack": attack, "Chortle": chortle, "Cough": cough, "SunGaze": sungaze}


