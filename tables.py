# This will be the library for roll tables to be used throughout other programs.
# All roll tables will accept a variable to allow for the return of multiple
# items at once.  The returns are currently strings, but in the future (depending
# on how the programs play out) it will probably start returning lists to allow
# individual programs to decide how to manipulate the returns.

# Importing modules
import random
import dice_roller

# Ten GP gem list.  Variable number used to determine how gems to return.
def ten_gp_gem(number=1):
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

def fifty_gp_gem(number=1):
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


def one_hundred_gp_gem(number=1):
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

def five_hundred_gp_gem(number=1):
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

def one_thousand_gp_gem(number=1):
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

def five_thousand_gem(number=1):
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

def twenty_five_gp_art(number=1):
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

def two_hundred_fifty_gp_art(number=1):
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

def seven_hundred_fifty_gp_art(number=1):
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

def two_thousand_five_hundred_gp_art(number=1):
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

def seven_thousand_five_hundred_gp_art(number=1):
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
            return_string = "{} and {}".format(return_string,random.choice(items))
            number = number - 1
    return return_string

def magic_table_a():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "SPELL SCROLL (CANTRIP)"
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "SPELL SCROLL (1st LEVEL)"
    if 91 <= rando_hundred <= 94:
        return "SPELL SCROLL (2nd LEVEL)"
    if 95 <= rando_hundred <= 98:
        return "Potion of Greater Healing"
    if rando_hundred == 99:
        return "Bag of Holding"
    if rando_hundred == 100:
        return "Driftglobe"

def magic_table_b():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 15:
        return "Potion of Healing"
    if 16 <= rando_hundred <= 22:
        return "SPELL SCROLL (CANTRIP)"
    if 23 <= rando_hundred <= 29:
        return "Potion of Climbing"
    if 30 <= rando_hundred <= 34:
        return "SPELL SCROLL (1st LEVEL)"
    if 35 <= rando_hundred <= 39:
        return "SPELL SCROLL (2nd LEVEL)"
    if 40 <= rando_hundred <= 44:
        return "Potion of Greater Healing"
    if 45 <= rando_hundred <= 49:
        return "Potion of Healing"
    if 50 <= rando_hundred <= 54:
        return "SPELL SCROLL (CANTRIP)"
    if 55 <= rando_hundred <= 59:
        return "Potion of Climbing"
    if 60 <= rando_hundred <= 64:
        return "SPELL SCROLL (1st LEVEL)"
    if 65 <= rando_hundred <= 67:
        return "SPELL SCROLL (2nd LEVEL)"
    if 68 <= rando_hundred <= 70:
        return "Potion of Greater Healing"
    if 71 <= rando_hundred <= 73:
        return "Potion of Healing"
    if 74 <= rando_hundred <= 75:
        return "SPELL SCROLL (CANTRIP)"
    if 76 <= rando_hundred <= 77:
        return "Potion of Climbing"
    if 78 <= rando_hundred <= 79:
        return "SPELL SCROLL (1st LEVEL)"
    if 80 <= rando_hundred <= 81:
        return "SPELL SCROLL (2nd LEVEL)"
    if 82 <= rando_hundred <= 83:
        return "Potion of Greater Healing"
    if rando_hundred == 84:
        return "Bag of Holding"
    if rando_hundred == 85:
        return "Driftglobe"
    if rando_hundred == 84:
        return "Bag of Holding"
    if rando_hundred == 85:
        return "Driftglobe"
    if rando_hundred == 84:
        return "Bag of Holding"
    if rando_hundred == 85:
        return "Driftglobe"
    if rando_hundred == 84:
        return "Bag of Holding"
    if rando_hundred == 85:
        return "Driftglobe"
# This will be the library for roll tables to be used throughout other programs.
# All roll tables will accept a variable to allow for the return of multiple
# items at once.  The returns are currently strings, but in the future (depending
# on how the programs play out) it will probably start returning lists to allow
# individual programs to decide how to manipulate the returns.

# Importing modules
import random
import dice_roller

# Ten GP gem list.  Variable number used to determine how gems to return.
def ten_gp_gem(number=1):
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

def fifty_gp_gem(number=1):
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


def one_hundred_gp_gem(number=1):
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

def five_hundred_gp_gem(number=1):
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

def one_thousand_gp_gem(number=1):
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

def five_thousand_gem(number=1):
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

def twenty_five_gp_art(number=1):
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

def two_hundred_fifty_gp_art(number=1):
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

def seven_hundred_fifty_gp_art(number=1):
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

def two_thousand_five_hundred_gp_art(number=1):
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

def seven_thousand_five_hundred_gp_art(number=1):
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
            return_string = "{} and {}".format(return_string,random.choice(items))
            number = number - 1
    return return_string

def magic_table_a():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "SPELL SCROLL (CANTRIP)"
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "SPELL SCROLL (1st LEVEL)"
    if 91 <= rando_hundred <= 94:
        return "SPELL SCROLL (2nd LEVEL)"
    if 95 <= rando_hundred <= 98:
        return "Potion of Greater Healing"
    if rando_hundred == 99:
        return "Bag of Holding"
    if rando_hundred == 100:
        return "Driftglobe"

def magic_table_b():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 15:
        return "Potion of Healing"
    if 16 <= rando_hundred <= 22:
        return "Potion of Firebreath"
    if 23 <= rando_hundred <= 29:
        return "Potion of Resistance"
    if 30 <= rando_hundred <= 34:
        return "Ammunition +1"
    if 35 <= rando_hundred <= 39:
        return "Potion of Animal Friendship"
    if 40 <= rando_hundred <= 44:
        return "Potion of Hill Giant Strength"
    if 45 <= rando_hundred <= 49:
        return "Potion of Growth"
    if 50 <= rando_hundred <= 54:
        return "Potion of Water Breathing"
    if 55 <= rando_hundred <= 59:
        return "SPELL SCROLL (2nd LEVEL)"
    if 60 <= rando_hundred <= 64:
        return "SPELL SCROLL (3rd LEVEL)"
    if 65 <= rando_hundred <= 67:
        return "Bag of Holding"
    if 68 <= rando_hundred <= 70:
        return "Keoghtom's ointment"
    if 71 <= rando_hundred <= 73:
        return "Oil of Slipperiness"
    if 74 <= rando_hundred <= 75:
        return "Dust of Disappearance"
    if 76 <= rando_hundred <= 77:
        return "Dust of Dryness"
    if 78 <= rando_hundred <= 79:
        return "Dust of Sneezing and Choaking"
    if 80 <= rando_hundred <= 81:
        return "Elemental Gem"
    if 82 <= rando_hundred <= 83:
        return "Philter of Love"
    if rando_hundred == 84:
        return "Alchemy Jug"
    if rando_hundred == 85:
        return "Cap of Water Breathing"
    if rando_hundred == 86:
        return "Cloak of the Manta Ray"
    if rando_hundred == 87:
        return "Driftglobe"
    if rando_hundred == 88:
        return "Goggles of Night"
    if rando_hundred == 89:
        return "Helm of Comprehending Languages"
    if rando_hundred == 90:
        return "Immovable Rod"
    if rando_hundred == 91:
        return "Lantern of Revealing"
    if rando_hundred == 92:
        return "Mariner's Armor"
    if rando_hundred == 93:
        return "Mithral Armor"
    if rando_hundred == 94:
        return "Potion of Poison"
    if rando_hundred == 95:
        return "Ring of Swimming"
    if rando_hundred == 96:
        return "Robe of Useful Items"
    if rando_hundred == 97:
        return "Rope of Climbing"
    if rando_hundred == 98:
        return "Saddle of Cavalier"
    if rando_hundred == 99:
        return "Wang of Magic Detection"
    if rando_hundred == 100:
        return "Want of Secrets"

def magic_table_c():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "SPELL SCROLL (CANTRIP)"
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "SPELL SCROLL (1st LEVEL)"
    if 91 <= rando_hundred <= 94:
        return "SPELL SCROLL (2nd LEVEL)"
    if 95 <= rando_hundred <= 98:
        return "Potion of Greater Healing"
    if rando_hundred == 99:
        return "Bag of Holding"
    if rando_hundred == 100:
        return "Driftglobe"

def magic_table_d():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "SPELL SCROLL (CANTRIP)"
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "SPELL SCROLL (1st LEVEL)"
    if 91 <= rando_hundred <= 94:
        return "SPELL SCROLL (2nd LEVEL)"
    if 95 <= rando_hundred <= 98:
        return "Potion of Greater Healing"
    if rando_hundred == 99:
        return "Bag of Holding"
    if rando_hundred == 100:
        return "Driftglobe"

def magic_table_e():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "SPELL SCROLL (CANTRIP)"
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "SPELL SCROLL (1st LEVEL)"
    if 91 <= rando_hundred <= 94:
        return "SPELL SCROLL (2nd LEVEL)"
    if 95 <= rando_hundred <= 98:
        return "Potion of Greater Healing"
    if rando_hundred == 99:
        return "Bag of Holding"
    if rando_hundred == 100:
        return "Driftglobe"

def magic_table_f():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "SPELL SCROLL (CANTRIP)"
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "SPELL SCROLL (1st LEVEL)"
    if 91 <= rando_hundred <= 94:
        return "SPELL SCROLL (2nd LEVEL)"
    if 95 <= rando_hundred <= 98:
        return "Potion of Greater Healing"
    if rando_hundred == 99:
        return "Bag of Holding"
    if rando_hundred == 100:
        return "Driftglobe"

def magic_table_g():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "SPELL SCROLL (CANTRIP)"
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "SPELL SCROLL (1st LEVEL)"
    if 91 <= rando_hundred <= 94:
        return "SPELL SCROLL (2nd LEVEL)"
    if 95 <= rando_hundred <= 98:
        return "Potion of Greater Healing"
    if rando_hundred == 99:
        return "Bag of Holding"
    if rando_hundred == 100:
        return "Driftglobe"

def magic_table_h():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "SPELL SCROLL (CANTRIP)"
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "SPELL SCROLL (1st LEVEL)"
    if 91 <= rando_hundred <= 94:
        return "SPELL SCROLL (2nd LEVEL)"
    if 95 <= rando_hundred <= 98:
        return "Potion of Greater Healing"
    if rando_hundred == 99:
        return "Bag of Holding"
    if rando_hundred == 100:
        return "Driftglobe"

def magic_table_i():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "SPELL SCROLL (CANTRIP)"
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "SPELL SCROLL (1st LEVEL)"
    if 91 <= rando_hundred <= 94:
        return "SPELL SCROLL (2nd LEVEL)"
    if 95 <= rando_hundred <= 98:
        return "Potion of Greater Healing"
    if rando_hundred == 99:
        return "Bag of Holding"
    if rando_hundred == 100:
        return "Driftglobe"

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



def magic_table_c():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "SPELL SCROLL (CANTRIP)"
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "SPELL SCROLL (1st LEVEL)"
    if 91 <= rando_hundred <= 94:
        return "SPELL SCROLL (2nd LEVEL)"
    if 95 <= rando_hundred <= 98:
        return "Potion of Greater Healing"
    if rando_hundred == 99:
        return "Bag of Holding"
    if rando_hundred == 100:
        return "Driftglobe"

def magic_table_d():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "SPELL SCROLL (CANTRIP)"
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "SPELL SCROLL (1st LEVEL)"
    if 91 <= rando_hundred <= 94:
        return "SPELL SCROLL (2nd LEVEL)"
    if 95 <= rando_hundred <= 98:
        return "Potion of Greater Healing"
    if rando_hundred == 99:
        return "Bag of Holding"
    if rando_hundred == 100:
        return "Driftglobe"

def magic_table_e():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "SPELL SCROLL (CANTRIP)"
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "SPELL SCROLL (1st LEVEL)"
    if 91 <= rando_hundred <= 94:
        return "SPELL SCROLL (2nd LEVEL)"
    if 95 <= rando_hundred <= 98:
        return "Potion of Greater Healing"
    if rando_hundred == 99:
        return "Bag of Holding"
    if rando_hundred == 100:
        return "Driftglobe"

def magic_table_f():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "SPELL SCROLL (CANTRIP)"
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "SPELL SCROLL (1st LEVEL)"
    if 91 <= rando_hundred <= 94:
        return "SPELL SCROLL (2nd LEVEL)"
    if 95 <= rando_hundred <= 98:
        return "Potion of Greater Healing"
    if rando_hundred == 99:
        return "Bag of Holding"
    if rando_hundred == 100:
        return "Driftglobe"

def magic_table_g():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "SPELL SCROLL (CANTRIP)"
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "SPELL SCROLL (1st LEVEL)"
    if 91 <= rando_hundred <= 94:
        return "SPELL SCROLL (2nd LEVEL)"
    if 95 <= rando_hundred <= 98:
        return "Potion of Greater Healing"
    if rando_hundred == 99:
        return "Bag of Holding"
    if rando_hundred == 100:
        return "Driftglobe"

def magic_table_h():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "SPELL SCROLL (CANTRIP)"
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "SPELL SCROLL (1st LEVEL)"
    if 91 <= rando_hundred <= 94:
        return "SPELL SCROLL (2nd LEVEL)"
    if 95 <= rando_hundred <= 98:
        return "Potion of Greater Healing"
    if rando_hundred == 99:
        return "Bag of Holding"
    if rando_hundred == 100:
        return "Driftglobe"

def magic_table_i():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "SPELL SCROLL (CANTRIP)"
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "SPELL SCROLL (1st LEVEL)"
    if 91 <= rando_hundred <= 94:
        return "SPELL SCROLL (2nd LEVEL)"
    if 95 <= rando_hundred <= 98:
        return "Potion of Greater Healing"
    if rando_hundred == 99:
        return "Bag of Holding"
    if rando_hundred == 100:
        return "Driftglobe"

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