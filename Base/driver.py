# This is a driver for testing the combat module

import koronakombat as kk

# Agent constructor is (hp, at, df, moveList, Name)
hero = kk.Hero(10, 10, 8, 6, 5, 5, ['Attack', 'Smile'], 'Hero')

combat1 = kk.Kombat("Overworld", hero)

