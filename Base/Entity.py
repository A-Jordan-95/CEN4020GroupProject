class Entity():
    def __init__(self):
        # Originally had None here for strings, but got some random crashes on first draw.
        # Haven't had any after this change, not sure why that would be happening
        self.name = ""
        self.description = ""
        self.attack = 0
        self.defense = 0
        self.agility = 0
        self.luck = 0
        self.hp = 0
        self.maxhp = 0
        self.mp = 0
        self.maxmp = 0
        self.sprite = ""
        
#Helmets
class NoodleHat(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Noodle Hat"
        self.defense = 5
        self.maxhp = 20
        self.agility = 1
        self.luck = 1
        self.sprite = "Inventory/Noodle_hat.png"
        self.description = "Nothing says stay 6 feet\naway from me than this\npool noodle hat."
        
class Mask(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Face Mask"
        self.defense = 2
        self.maxhp = 10
        self.sprite = "Inventory/face_mask.png"
        self.description = "I'm doing my part \n what about you?"

#Weapons
class Revolver(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Revolver"
        self.attack = 10
        self.defense = 1
        self.sprite = "Inventory/revolver.png"
        self.description = "The New Model Army was\neffective in the Civil War,\nand now effective against\nCOVID."

class Fists(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Fists"
        self.attack = 1
        self.defense = 1
        self.sprite = "Inventory/fists.png"
        self.description = "When life gives you lemons,\ngive it a sucker punch back."

class Shotgun(Entity):
    def __init__(self):
        super().__init__()
        self.name = "DB Shotgun"
        self.attack = 25
        self.defense = 1
        self.sprite = "Inventory/shotgun.png"
        self.description = "2 booms are better than one"

class MP40(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Machine Pistol"
        self.attack = 17
        self.defense = 1
        self.sprite = "Inventory/Mp40.png"
        self.description = "Like a broom, but not the cleaning type"
        
#Consumables
class H0CQ(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Hydroxychloriquine"
        self.hp = 5
        self.mp = 5
        self.description = "If Trump uses it, it must\nmake COVID not so great\nagain."

class Drink(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Energy Drink"
        self.hp = 7
        self.sprite = "Inventory/energy_drink.png"
        self.description = "Also better known by \n 'The Cardiac Arrester 3000'"
        
class MedKit(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Doober Eats Order"
        self.hp = 14
        self.sprite = "Inventory/ubereats.png"
        self.description = "Enjoying your $37 dollar\n sandwich?"

class Soup(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Bat Soup"
        self.hp = 3
        self.maxHP = 3
        self.sprite = "Inventory/batsoup_sprite.png"
        self.description = "So noxic, it's actually \n going to give you antibodies"

class Glove(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Glove"
        self.maxhp = 5
        self.defense = 2
        self.sprite = "Inventory/glove.png"
        self.description = "The first line of defense"

class Helmet(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Reinforced Helmet"
        self.maxhp = 35
        self.defense = 10
        self.sprite = "Inventory/helmet.png"
        self.description = "Even after things get better \n you still feel like your \n still in Quarantine"

class Pants(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Jeans"
        self.maxhp = 9
        self.defense = 4
        self.sprite = "Inventory/jeans.png"
        self.description = "Washing optional"

#Quest
class ToiletPaper(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Toilet Roll"
        self.hp = 0
        self.mp = 0
        self.description = "The softest ply, for the most \n sensitive of butts"
        self.sprite = "Inventory/toilet_paper.png"
