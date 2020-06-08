#max size of the inventory
#default can be changed
MAXIMUM_SIZE = 20
#a master list key value pair
#the string name acts as a key
#the value is the item type and the health/damage
#ideally, all in game items would be put in the master list
masterList = {
    "Fists": [1, 40],
    "Soup": [0, 35],
    "Revolver": [1, 70],
    "McRib": [0,70]
}
#item classes (limited here to two)
#could be expanded upon later
class powerUp():
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.type = 0

    #this is analogus to ostream overload in C++, it tells how to print an object
    def __str__(self):
        return f" Obj: {self.name} \n HP: {self.health} \n Type: Powerup \n"

class weapon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        self.type = 1

    def __str__(self):
        return f" Obj: {self.name} \n DP: {self.damage} \n Type: Weapon \n"

def addItem(name, playerList):
    #will not add an item if max size is achieved
    if len(playerList) == MAXIMUM_SIZE:
        return 0
    else:
        #search by key, aka the name
        #the value is the type and damage
        index = 0
        for value in masterList:
            if value == name:
                index = masterList[value]
        #is the item a powerup?
        if (index[0] == 0):
            playerList.append(powerUp(name, index[1]))
        #is the item a weapon
        elif (index[0] == 1):
            playerList.append(weapon(name, index[1]))
        return 1


def deleteItem(name, playerList):
        i = 0
        for pos in playerList:
            if pos.name == name:
                del playerList[i]
            else:
                i+=1

def printInventory(playerList):
    for x in playerList:
        print(x)

#clears entire inventory
def Strip(playerList):
    playerList.clear()


'''
FILE FORMAT
For an entry:
    INVENTORY SIZE
    ITEM NAME
    ITEM TYPE
    ITEM VALUE (HEALTH OR DAMAGE)
'''

def writeToFile(playerList):
    filestream = open("save.dat", "w")
    filestream.write(str(len(playerList)))
    filestream.write("\n")
    for entry in playerList:
        filestream.write(entry.name)
        filestream.write("\n")
        filestream.write(str(entry.type))
        filestream.write("\n")
        #determine if its a powerup or weapon
        if entry.type:
            filestream.write(str(entry.damage))
        else:
            filestream.write(str(entry.health))
        filestream.write("\n")
    print("Saved current inventory")
    filestream.close()


#Note, any exisiting inventory will be overwritten
def readFromFile(playerList):
    filestream = open("save.dat", "r")
    MAXIMUM_SIZE = int(filestream.readline())
    for entry in playerList:
        entry.name = filestream.readline()
        type = int(filestream.readline())
        if type:
            entry.type = type
            entry.damage = int(filestream.readline())
        else:
            entry.type = type
            entry.health = int(filestream.readline())
    if !(playerList):
        print("Error, no data written in playerList")


#find an item by searching it up
#If there are duplicates, only the
#first case will be given
def findItem(name, playerList):
    for x in playerList:
        print(x)
        if x.name == name:
            return playerList.count(name)
        else:
            return 0

#simple menu function to show capabilities of these functions
def menu():
    print("Skynet Inventory Management")
    print("Select an option:")
    print("(1) Add item to list")
    print("(2) Delete item from list")
    print("(3) Print List")
    print("(4) Clear inventory")
    print("(5) Find an item")
    print("(6) Write to File")
    print("(-1) Exit")


def main():
    playerList = []
    menu()
    x = 0
    while (x != -1):
        x = int(input(""))
        if x == 1:
            str = input("Enter item to be added: ")
            if (addItem(str, playerList) == 0):
                print("Item could not be added")
            menu()
        elif x == 2:
            str = input("Enter item to be deleted: ")
            deleteItem(str, playerList)
            menu()
        elif x == 3:
            printInventory(playerList)
            menu()
        elif x == 4:
            Strip(playerList)
            menu()
        elif x == 5:
            str = input("Search inventory for what item: ")
            result = findItem(str, playerList)
            if (result == 0):
                print("No cases found")
            else:
                print(f"Item '{str}' was found in position {result}")
            menu()
        elif x == 6:
            writeToFile(playerList)
            menu()
if __name__ == "__main__": main()
