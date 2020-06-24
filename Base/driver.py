# This is a driver for testing the combat module

import koronakombat as kk

# Agent constructor is (hp, at, df, moveList, Name)
hero = kk.Hero(10,8,6, ['Attack'], 'Hero')
enemy = kk.Enemy(6,7,4, ['Attack', 'Smile'], 'Small Child')

combat1 = kk.Kombat()
combat1.run(hero, enemy)

