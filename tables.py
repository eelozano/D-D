# This will be the library for roll tables to be used throughout other programs.
# All roll tables will accept a variable to allow for the return of multiple
# items at once.  The returns are currently strings, but in the future (depending
# on how the programs play out) it will probably start returning lists to allow
# individual programs to decide how to manipulate the returns.

# Importing libraries
import random
# Importing the d100 dice roller
from dice_roller import d100

# Ten GP gem list.  Variable number used to determine how gems to return.
def ten_gp_gem(number):
    # Initializing variable
    return_string = ""
    items = ["Azurite", "Banded agate", "Blue quartz", "Eyeagate", "Hematite", "Lapis lazuli", "Malachite", "Moss agate", "Obsidian", "Tiger eye", "Turquoise"]
    # begin loop to create list of gems to return
    while number > 0:
        # First round does not require 'and' as it would place it before the first item
        if return_string == "":
            # randomly picks an item in the list
            return_string = random.choice(items)
            number = number - 1
        else:
            return_string = return_string + " and " + random.choice(items)
            number = number - 1
    return return_string

def fifty_gp_gem(number):
    return_string = ""
    items = ["Bloodstone","Carnelian","Chalcedony","Chrysoprase","Citrine","Jasper","Moonstone","Onyx","Quartz","Sardonyx","Star rose quartz","Zircon"]
    # begin loop to create list of gems to return
    while number > 0:
        # First round does not require 'and' as it would place it before the first item
        if return_string == "":
            # randomly picks an item in the list
            return_string = random.choice(items)
            number = number - 1
        else:
            return_string = return_string + " and " + random.choice(items)
            number = number - 1
    return return_string


def one_hundred_gp_gem(number):
    return_string = ""
    items = ["Amber","Amethyst","Chrysoberyl","Coral","Garnet","Jade","Jet","Pearl","Spinel","Tourmaline"]
    # begin loop to create list of gems to return
    while number > 0:
        # First round does not require 'and' as it would place it before the first item
        if return_string == "":
            # randomly picks an item in the list
            return_string = random.choice(items)
            number = number - 1
        else:
            return_string = return_string + " and " + random.choice(items)
            number = number - 1
    return return_string

def five_hundred_gp_gem(number):
    return_string = ""
    items = ["Alexandrite","Aquamarine","Black pearl","Blue spinel","Peridot","Topaz"]
    # begin loop to create list of gems to return
    while number > 0:
        # First round does not require 'and' as it would place it before the first item
        if return_string == "":
            # randomly picks an item in the list
            return_string = random.choice(items)
            number = number - 1
        else:
            return_string = return_string + " and " + random.choice(items)
            number = number - 1
    return return_string

def one_thousand_gp_gem(number):
    return_string = ""
    items = ["Black opal","Blue sapphire","Emerald","Fire opal","Opal","Star ruby","Star sapphire","Yellow sapphire"]
    # begin loop to create list of gems to return
    while number > 0:
        # First round does not require 'and' as it would place it before the first item
        if return_string == "":
            # randomly picks an item in the list
            return_string = random.choice(items)
            number = number - 1
        else:
            return_string = return_string + " and " + random.choice(items)
            number = number - 1
    return return_string

def five_thousand_gem(number):
    return_string = ""
    items = ["Black sapphire","Diamond","Jacinth","Ruby"]
    # begin loop to create list of gems to return
    while number > 0:
        # First round does not require 'and' as it would place it before the first item
        if return_string == "":
            # randomly picks an item in the list
            return_string = random.choice(items)
            number = number - 1
        else:
            return_string = return_string + " and " + random.choice(items)
            number = number - 1
    return return_string

def twenty_five_gp_art(number):
    return_string = ""
    items = ["Silver ewer","Carved bone statuette","Small gold bracelet","Cloth-of-gold vestments","Black velvet mask stitched with silver thread","Copper chalice with silver filigree","Pair of engraved bone dice","Small mirror set in a painted wooden frame","Embroidered silk handkerchief","Gold locket with a painted portrait inside"]
    # begin loop to create list of gems to return
    while number > 0:
        # First round does not require 'and' as it would place it before the first item
        if return_string == "":
            # randomly picks an item in the list
            return_string = random.choice(items)
            number = number - 1
        else:
            return_string = return_string + " and " + random.choice(items)
            number = number - 1
    return return_string

def two_hundred_fifty_gp_art(number):
    return_string = ""
    items = ["Gold ring set with bloodstones","Carved ivory statuette","Large gold bracelet","Silver necklace with a gemstone pendant","Bronze crown","Silk robe with gold embroidery","Large well-made tapestry","Brass mug with jade inlay","Box of turquoise animal figurines","Gold bird cage with electrum filigree"]
    # begin loop to create list of gems to return
    while number > 0:
        # First round does not require 'and' as it would place it before the first item
        if return_string == "":
            # randomly picks an item in the list
            return_string = random.choice(items)
            number = number - 1
        else:
            return_string = return_string + " and " + random.choice(items)
            number = number - 1
    return return_string

def seven_hundred_fifty_gp_art(number):
    return_string = ""
    items = ["Silver chalice set with moonstones","Silver-plated steellongsword with jet set in hilt","Carved harp of exotic wood with ivory inlay and zircon gems","Small gold idol","Gold dragon comb set with red garnets as eyes","Bottle stopper cork embossed with gold leaf and set with amethysts","Ceremonial electrum dagger with a black pearl in the pommel","Silver and gold brooch","Obsidian statuette with gold fittings and inlay","Painted gold war mask"]
    # begin loop to create list of gems to return
    while number > 0:
        # First round does not require 'and' as it would place it before the first item
        if return_string == "":
            # randomly picks an item in the list
            return_string = random.choice(items)
            number = number - 1
        else:
            return_string = return_string + " and " + random.choice(items)
            number = number - 1
    return return_string

def two_thousand_five_hundred_gp_art(number):
    return_string = ""
    items = ["Fine gold chain set with a fire opal","Old masterpiece painting","Embroidered silk and velvet mantle set with numerous moonstones","Platinum bracelet set with a sapphire","Embroidered glove set with jewel chips","Jeweled anklet","Gold music box","Gold circlet set with four aquamarines","Eye patch with a mock eye set in blue sapphire and moonstone","Eye patch with a mock eye set in blue sapphire and moonstone"]
    # begin loop to create list of gems to return
    while number > 0:
        # First round does not require 'and' as it would place it before the first item
        if return_string == "":
            # randomly picks an item in the list
            return_string = random.choice(items)
            number = number - 1
        else:
            return_string = return_string + " and " + random.choice(items)
            number = number - 1
    return return_string

def seven_thousand_five_hundred_gp_art(number):
    return_string = ""
    items = ["Jeweled gold crown","Jeweled platinum ring","Small gold statuette set with rubies","Gold cup set with emeralds","Gold jewelry box with platinum filigree","Painted gold child's sarcophagus","jade game board with solid gold playing pieces","Bejeweled ivory drinking horn with gold filigree"]
    # begin loop to create list of gems to return
    while number > 0:
        # First round does not require 'and' as it would place it before the first item
        if return_string == "":
            # randomly picks an item in the list
            return_string = random.choice(items)
            number = number - 1
        else:
            return_string = return_string + " and " + random.choice(items)
            number = number - 1
    return return_string


# Various table tests

# print("Printing 10 gp gems")
# print(ten_gp_gem(3))
# print("Printing 50 gp gems")
# print(fifty_gp_gem(3))
# print("Printing 100 gp gems")
# print(one_hundred_gp_gem(3))
# print("Printing 500 gp gems")
# print(five_hundred_gp_gem(3))
# print("Printing 1000 gp gems")
# print(one_thousand_gp_gem(3))
# print("Printing 5000 gp gems")
# print(five_thousand_gem(3))
# print("Printing 25 gp art")
# print(twenty_five_gp_art(3))
# print("Printing 250 gp art")
# print(two_hundred_fifty_gp_art(3))
# print("Printing 750 gp art")
# print(seven_hundred_fifty_gp_art(3))
# print("Printing 2500 gp art")
# print(two_thousand_five_hundred_gp_art(3))
# print("Printing 7500 gp art")
# print(seven_thousand_five_hundred_gp_art(3))