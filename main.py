# Course: CS 30
# Period: 2
# Date created: 20/11/24
# Date last modified: 20/11/30
# Name: Dora Liu
# Description: RPG Game



# dictionory for the characters
print("characters:\n")
characters = {
    # description of the player
    "player": {
        "description": "someone who have been trapped in the world",
        "health": 100,
        "damage": 5,
    },
    # description of Chaugnar Faugn
    "Chaugnar Faugn": {
        "description": "the owner of the world. Monster in the audi",
        "health": 200,
        "damage": 50,
    },
    # description of the slave girl
    "slave girl": {
        "description": "a slave girl who have a gun in her hand",
        "health": 80,
        "damage": 5,
    },
    #  description of the monster in the liburary
    "monster 2": {
        "description": "the monster from liburary",
        "health": 50,
        "damage": 50,
    },
}

# The loop
for character, traits in characters.items():
    print(f"# {character.title()}:")
    print(f"{character.title()} is {traits['description']}.")
    print(f"{character.title()}'s health is {traits['health']}.")
    print(f"{character.title()}'s damage is {traits['damage']}.")
    print("\n")

# print a line to separate
print("-----------------------------------------------")

# dictionary for locations
print("locations:")
locations = {
    #  description of the kichen
    "kichen": [
        "where have a lot of seasonings and utensils",
        "Some prepared “soup” in the pot",
    ],
    #  description of the slave room
    "slave room": [
        "where the little slave is waiting for you over here",
        "where you can get the only thing to attact the monsters",
    ],
    # description of the auditorium
    "auditorium": [
        "where Chaugnar Faugn hide",
        "place that you can find the poison you need",
    ],
    #  description of the soup room
    "soup room": [
        "where you begining from",
        "where the original soup is",
    ],
    #  description of the library
    "library": [
        "where you can find all info of this area",
        "another place that you can get the poison to escape",
        "where the second monster is",
    ],
}

# Loop the dictionary, locations and print its keps and values seperately
for location, descriptions in locations.items():
    msg = f"{location.title()} is the place "
    for i, description in enumerate(descriptions):
        msg += description
        # put a . after the last sentence
        if i == len(descriptions) - 1:
            msg += "."
        # put an and after the second last sentence
        elif i == len(descriptions) - 2:
            msg += ", and "
        # put , before every sentence that is not the last or second last
        else:
            msg += ", "
    print(msg)
    print("\n")


print("\n" )

# print a line to separate
print("-----------------------------------------------")

print("inventory:")
# dictionary of the inventory
inventory = {
    "soup": {
        "description": 'the "key" to escape',
        "amount": 1,
    },
    "note": {
        "description": "some notes about these rooms",
        "amount": 5,
    },
    "candle": {
        "description": "Use to light up your road",
        "amount": 3,
    },
    "gun": {
        "description": "You can get it from the slave, have a higher damage",
        "amount": 1,
        "damage": 50,
    },
    "map": {"description": "A paper to show you the way", "amount": 1},
}

# The loop
for inventory, traits in inventory.items():
    # Print the keys
    print(f"{inventory.title()}")
    # Loop the dictionary traits and print its items
    for info, descript in traits.items():
        print(f"*{info.title()}: {descript}")
    print()
