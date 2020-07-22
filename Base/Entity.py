class entity():
    def __init__(self):
        pass

    #you'll need this function for printing names out in inventory
    def __str__(self):
        return f"{self.name}"

class Revolver(entity):
    def __init__(self):
        super().__init__()
        self.name = "Revolver"
        self.value = 60
        self.mp = 0
        self.attack = 1
        self.defense = 1
        self.strength = 0
        self.intelligence = 0
        self.agility = 0
        self.immunity = 0
        self.luck = 0
        self.type = 2
        self.sprite = "Inventory/revolver.png"
        self.description = """
                        The New Model Army
                        was effective
                        in the Civil War,
                        and now effective
                        against COVID"""

class Fists(entity):
    def __init__(self):
        super().__init__()
        self.name = "Fists"
        self.value = 45
        self.mp = 0
        self.attack = 1
        self.defense = 1
        self.strength = 0
        self.intelligence = 0
        self.agility = 0
        self.immunity = 0
        self.luck = 0
        self.type = 1
        self.sprite = "Inventory/fists.png"
        self.description = """
                        When life gives
                        you lemons,
                        give it a
                        sucker punch
                        back
                        """
class noodlehat(entity):
    def __init__(self):
        super().__init__()
        self.name = "Noodle Hat"
        self.value = 10
        self.mp = 0
        self.attack = 0
        self.defense = 3
        self.strength = 0
        self.intelligence = 1
        self.agility = 0
        self.immunity = 1
        self.luck = 0
        self.type = 3
        self.sprite = "Inventory/Noodle_hat.png"
        self.description = """
                        Nothing says
                        stay 6 feet away
                        from me than
                        this pool noodle
                        hat
                        """

class H0CQ(entity):
    def __init__(self):
        super().__init__()
        self.name = "hydroxychloriquine"
        self.value = 20
        self.mp = 0
        self.attack = 0
        self.defense = 1
        self.strength = 1
        self.intelligence = 1
        self.agility = 1
        self.immunity = 6
        self.luck = 1
        self.type = 4
        self.description = """
                            If Trump uses
                            it, it must make
                            COVID not so great
                            again
                            """
