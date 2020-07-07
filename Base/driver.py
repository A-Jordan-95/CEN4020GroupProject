# This is a driver for testing the combat module

import koronakombat as kk

f = open("playerData.txt", 'r')
stats = f.readline().split()
moveList = f.readline().split()
name = f.readline().strip('\n')

hero = kk.Hero(int(stats[0]),int(stats[1]),int(stats[2]),int(stats[3]),int(stats[4]),int(stats[5]), moveList, name)

f.close()

combat1 = kk.Kombat("Overworld", hero)

