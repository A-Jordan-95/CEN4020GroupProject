# Abstract Class (not meant to be used by itself)
class Entity:
    def __init__(self):
        # Each entity's properties
        # Write "0" here so we don't have to write all the time in inherited classes. Just have to make sure if it is
        # set to "None" you have to override in an inherited class.
        self.name = None
        self.attack = 0
        self.defense = 0
        self.sprite = None
        # All the other properties too(Immunity/Max HP/Max MP ect. from list)


# Object: Weapon
class Revolver(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Revolver"
        self.attack = 60
        self.sprite = "Inventory/revolver.png"
