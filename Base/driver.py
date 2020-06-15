# This is a driver for testing the combat module

import koronakombat as kk

hero = kk.Hero(10,8,6, ['Attack'], 'Hero')
enemy = kk.Enemy(6,7,4, ['Attack', 'Smile'], 'Small Child')

kk.Kombat(hero, enemy)

