"""
the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
means the player has 1 rope, 6 torches, 42 gold coins, and so on.
Write a function named displayInventory() that would take any possible “inventory” and display it
"""

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory: dict):
    total_items = 0

    print ("Iventory:")
    for k,v in inventory.items():
        print(f"{v} {k}")
        total_items += v

    print(f"Total items in inventory: {total_items} ")

displayInventory(stuff)


print("\n**** PART TWO: UPDATING INVENTORY ****\n")
"""
Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player’s inventory 
(like in the previous project) and the addedItems parameter is a list like dragonLoot. 
The addToInventory() function should return a dictionary that represents the updated inventory. 
Note that the addedItems list can contain multiples of the same item.
""" 

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory:dict, addedItems:list):
    for item in addedItems:
        inventory[item] = inventory.get(item,0) + 1

    return inventory

updated_stuff = addToInventory(stuff,dragonLoot)
displayInventory(updated_stuff)

