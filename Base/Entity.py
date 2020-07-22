class Entity():
    def __init__(self):
        self.name = None
        self.description = None
        self.attack = 0
        self.defense = 0
        self.agility = 0
        self.luck = 0
        self.hp = 0
        self.maxhp = 0
        self.mp = 0
        self.maxmp = 0
        self.maxhp = 0
        self.sprite = None

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

class NoodleHat(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Noodle Hat"
        self.defense = 3
        self.agility = 1
        self.luck = 1
        self.sprite = "Inventory/Noodle_hat.png"
        self.description = "Nothing says stay 6 feet\naway from me than this\npool noodle hat."

class H0CQ(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Hydroxychloriquine"
        self.hp = 5
        self.mp = 5
        self.description = "If Trump uses it, it must\n make COVID not so great\nagain."
