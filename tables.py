# This will be the library for roll tables to be used throughout other programs.
# All roll tables will accept a variable to allow for the return of multiple
# items at once.  The returns are currently strings, but in the future (depending
# on how the programs play out) it will probably start returning lists to allow
# individual programs to decide how to manipulate the returns.

# Importing modules
import random
import dice_roller
import json

# takes a number and a list and returns the number of items randomly chosen from the list
def print_returns(number, list):
    return_string = ""
    while number > 0:
        # First round does not require 'and' as it would place it before the first item
        if return_string == "":
            # randomly picks an item in the list
            return_string = random.choice(list)
            number = number - 1
        else:
            return_string = "{} and {}".format(return_string, random.choice(list))
            number = number - 1
    return return_string


def ten_gp_gem(number=1):
    items = ["Azurite", "Banded agate", "Blue quartz", "Eyeagate", "Hematite",
             "Lapis lazuli", "Malachite", "Moss agate", "Obsidian", "Tiger eye",
             "Turquoise"]
    return print_returns(number, items)


def fifty_gp_gem(number=1):
    items = ["Bloodstone", "Carnelian", "Chalcedony", "Chrysoprase", "Citrine", "Jasper", "Moonstone", "Onyx", "Quartz",
             "Sardonyx", "Star rose quartz", "Zircon"]
    return print_returns(number, items)


def one_hundred_gp_gem(number=1):
    items = ["Amber", "Amethyst", "Chrysoberyl", "Coral", "Garnet", "Jade", "Jet", "Pearl", "Spinel", "Tourmaline"]
    return print_returns(number, items)


def five_hundred_gp_gem(number=1):
    items = ["Alexandrite", "Aquamarine", "Black pearl", "Blue spinel", "Peridot", "Topaz"]
    return print_returns(number, items)


def one_thousand_gp_gem(number=1):
    items = ["Black opal", "Blue sapphire", "Emerald", "Fire opal", "Opal", "Star ruby", "Star sapphire",
             "Yellow sapphire"]
    return print_returns(number, items)


def five_thousand_gem(number=1):
    items = ["Black sapphire", "Diamond", "Jacinth", "Ruby"]
    return print_returns(number, items)


def twenty_five_gp_art(number=1):
    items = ["Silver ewer", "Carved bone statuette", "Small gold bracelet", "Cloth-of-gold vestments",
             "Black velvet mask stitched with silver thread", "Copper chalice with silver filigree",
             "Pair of engraved bone dice", "Small mirror set in a painted wooden frame",
             "Embroidered silk handkerchief", "Gold locket with a painted portrait inside"]
    return print_returns(number, items)


def two_hundred_fifty_gp_art(number=1):
    items = ["Gold ring set with bloodstones", "Carved ivory statuette", "Large gold bracelet",
             "Silver necklace with a gemstone pendant", "Bronze crown", "Silk robe with gold embroidery",
             "Large well-made tapestry", "Brass mug with jade inlay", "Box of turquoise animal figurines",
             "Gold bird cage with electrum filigree"]
    return print_returns(number, items)


def seven_hundred_fifty_gp_art(number=1):
    items = ["Silver chalice set with moonstones", "Silver-plated steellongsword with jet set in hilt",
             "Carved harp of exotic wood with ivory inlay and zircon gems", "Small gold idol",
             "Gold dragon comb set with red garnets as eyes",
             "Bottle stopper cork embossed with gold leaf and set with amethysts",
             "Ceremonial electrum dagger with a black pearl in the pommel", "Silver and gold brooch",
             "Obsidian statuette with gold fittings and inlay", "Painted gold war mask"]
    return print_returns(number, items)


def two_thousand_five_hundred_gp_art(number=1):
    items = ["Fine gold chain set with a fire opal", "Old masterpiece painting",
             "Embroidered silk and velvet mantle set with numerous moonstones", "Platinum bracelet set with a sapphire",
             "Embroidered glove set with jewel chips", "Jeweled anklet", "Gold music box",
             "Gold circlet set with four aquamarines", "Eye patch with a mock eye set in blue sapphire and moonstone",
             "Eye patch with a mock eye set in blue sapphire and moonstone"]
    return print_returns(number, items)


def seven_thousand_five_hundred_gp_art(number=1):
    items = ["Jeweled gold crown", "Jeweled platinum ring", "Small gold statuette set with rubies",
             "Gold cup set with emeralds", "Gold jewelry box with platinum filigree",
             "Painted gold child's sarcophagus", "jade game board with solid gold playing pieces",
             "Bejeweled ivory drinking horn with gold filigree"]
    return print_returns(number,items)


# Pull a random magic spell of input level from a json file of all SRD spells
def magic_spell(inp_level):
    spell_list = json.loads(open('5e-SRD-Spells.json').read())
    temp_array = []
    for spell_object in spell_list:
        if spell_object['level'] == inp_level:
            temp_array.append(spell_object)
    array_length = len(temp_array)
    random_number = random.randint(0, array_length - 1)
    return (temp_array[random_number])['name']

# Formatter for magic table output
def print_magic_table(list):
    number = len(list)
    return_string = ""
    while number > 0:
        if return_string == "":
            return_string = list.pop()
            number = number - 1
        else:
            return_string = "{} and {}".format(return_string, list.pop())
            number = number - 1
    return return_string

def magic_table_a():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 50:
        return "Potion of Healing"
    if 51 <= rando_hundred <= 60:
        return "Spell Scroll - {} - Cantrip".format(magic_spell('Cantrip'))
    if 61 <= rando_hundred <= 70:
        return "Potion of Climbing"
    if 71 <= rando_hundred <= 90:
        return "Spell Scroll - {} - 1st Level".format(magic_spell('1st-level'))
    if 91 <= rando_hundred <= 94:
        return "Spell Scroll - {} - 2nd Level".format(magic_spell('2nd-level'))
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
        return "Spell Scroll - {} - 2nd Level".format(magic_spell('2nd-level'))
    if 60 <= rando_hundred <= 64:
        return "Spell Scroll - {} - 3rd Level".format(magic_spell('3rd-level'))
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
    if 1 <= rando_hundred <= 15:
        return "Potion of Superior Healing"
    if 16 <= rando_hundred <= 22:
        return "Spell Scroll - {} - 4th Level".format(magic_spell('4th-level'))
    if 23 <= rando_hundred <= 27:
        return "Ammunition +2"
    if 28 <= rando_hundred <= 32:
        return "Potion of Clairvoyance"
    if 33 <= rando_hundred <= 37:
        return "Potion of Diminution"
    if 38 <= rando_hundred <= 42:
        return "Potion of Gaseous Form"
    if 43 <= rando_hundred <= 47:
        return "Potion of Frost Giant Strength"
    if 48 <= rando_hundred <= 52:
        return "Potion of Stone Giant Strength"
    if 53 <= rando_hundred <= 57:
        return "Potion of Heroism"
    if 58 <= rando_hundred <= 62:
        return "Potion of Invulnerability"
    if 63 <= rando_hundred <= 67:
        return "Potion of Mind Reading"
    if 68 <= rando_hundred <= 72:
        return "Spell Scroll - {} - 5th Level".format(magic_spell('5th-level'))
    if 73 <= rando_hundred <= 75:
        return "Elixir of Health"
    if 76 <= rando_hundred <= 78:
        return "Oil of Etherealness"
    if 79 <= rando_hundred <= 81:
        return "Potion of Fire Giant Strength"
    if 82 <= rando_hundred <= 84:
        return "Quaal's Feather Token"
    if 85 <= rando_hundred <= 87:
        return "Scroll of Protection"
    if 88 <= rando_hundred <= 89:
        return "Bag of Beans"
    if 90 <= rando_hundred <= 91:
        return "Bead of Force"
    if rando_hundred == 92:
        return "Chime of Opening"
    if rando_hundred == 93:
        return "Decanter of Endless Water"
    if rando_hundred == 94:
        return "Eyes of Minute Seeing"
    if rando_hundred == 95:
        return "Folding Boat"
    if rando_hundred == 96:
        return "Heward's handy haversack"
    if rando_hundred == 97:
        return "Horseshoes of speed"
    if rando_hundred == 98:
        return "Necklace of fireballs"
    if rando_hundred == 99:
        return "Periapt of health"
    if rando_hundred == 100:
        return "Sending Stones"


def magic_table_d():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 20:
        return "Potion of Supreme Healing"
    if 21 <= rando_hundred <= 30:
        return "Potion of Invisibility"
    if 31 <= rando_hundred <= 40:
        return "Potion of Speed"
    if 41 <= rando_hundred <= 50:
        return "Spell Scroll - {} - 6th Level".format(magic_spell('6th-level'))
    if 51 <= rando_hundred <= 57:
        return "Spell Scroll - {} - 7th Level".format(magic_spell('7th-level'))
    if 58 <= rando_hundred <= 62:
        return "Ammunition +3"
    if 63 <= rando_hundred <= 67:
        return "Oil of Sharpness"
    if 68 <= rando_hundred <= 72:
        return "Potion of Flying"
    if 73 <= rando_hundred <= 77:
        return "Potion of Cloud Giant Strength"
    if 78 <= rando_hundred <= 82:
        return "Potion of Longevity"
    if 83 <= rando_hundred <= 87:
        return "Potion of Vitality"
    if 88 <= rando_hundred <= 92:
        return "Spell Scroll - {} - 8th Level".format(magic_spell('8th-level'))
    if 93 <= rando_hundred <= 95:
        return "Horseshoes of a Zephyr"
    if 96 <= rando_hundred <= 98:
        return "Nolzur's Marvelous Pigments"
    if rando_hundred == 99:
        return "Bag of Devouring"
    if rando_hundred == 100:
        return "Portable Hole"

def magic_table_e():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 30:
        return "Spell Scroll - {} - 8th Level".format(magic_spell('8th-level'))
    if 31 <= rando_hundred <= 55:
        return "Potion of Storm Giant Strength"
    if 56 <= rando_hundred <= 70:
        return "Potion of Supreme Healing"
    if 71 <= rando_hundred <= 85:
        return "Spell Scroll - {} - 9th Level".format(magic_spell('9th-level'))
    if 86 <= rando_hundred <= 93:
        return "Universal Solvent"
    if 94 <= rando_hundred <= 98:
        return "Arrow of Slaying"
    if 99 <= rando_hundred <= 100:
        return "Sovereign Glue"

def magic_table_f():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 15:
        return "Weapon +1"
    if 16 <= rando_hundred <= 18:
        return "Shield +1"
    if 19 <= rando_hundred <= 21:
        return "Sentinel Shield"
    if 22 <= rando_hundred <= 23:
        return "Amulet of Proof Against Detection and Location"
    if 24 <= rando_hundred <= 25:
        return "Boots of Elvenkind"
    if 26 <= rando_hundred <= 27:
        return "Boots of Striding and Springing"
    if 28 <= rando_hundred <= 29:
        return "Bracers of Archery"
    if 30 <= rando_hundred <= 31:
        return "Brooch of Shielding"
    if 32 <= rando_hundred <= 33:
        return "Broom of Flying"
    if 34 <= rando_hundred <= 35:
        return "Cloak of Elvenkind"
    if 36 <= rando_hundred <= 37:
        return "Cloak of Protection"
    if 38 <= rando_hundred <= 39:
        return "Gauntlets of Ogre Power"
    if 40 <= rando_hundred <= 41:
        return "Hat of Disguise"
    if 42 <= rando_hundred <= 43:
        return "Javelin of Lightning"
    if 44 <= rando_hundred <= 45:
        return "Pearl of Power"
    if 46 <= rando_hundred <= 47:
        return "Rod of the Pact Keeper, +1"
    if 48 <= rando_hundred <= 49:
        return "Slippers of Spider Climbing"
    if 50 <= rando_hundred <= 51:
        return "Staff of the Adder"
    if 52 <= rando_hundred <= 53:
        return "Staff of the Python"
    if 54 <= rando_hundred <= 55:
        return "Sword of Vengeance"
    if 56 <= rando_hundred <= 57:
        return "Trident of Fish Command"
    if 58 <= rando_hundred <= 59:
        return "Wand of Magic Missles"
    if 60 <= rando_hundred <= 61:
        return "Wand of the War Mage, +1"
    if 62 <= rando_hundred <= 63:
        return "Wand of Web"
    if 64 <= rando_hundred <= 65:
        return "Weapon of Warning"
    if rando_hundred == 66:
        return "Adamantine Armor (chain mail)"
    if rando_hundred == 67:
        return "Adamantine Armor (chain shirt)"
    if rando_hundred == 68:
        return "Adamantine Armor (scale mail)"
    if rando_hundred == 69:
        return "Bag of tricks (gray)"
    if rando_hundred == 70:
        return "Bag of tricks (rust)"
    if rando_hundred == 71:
        return "Bag of tricks (tan)"
    if rando_hundred == 72:
        return "Boots of the Winterlands"
    if rando_hundred == 73:
        return "Circlet of Blasting"
    if rando_hundred == 74:
        return "Deck of Illusions"
    if rando_hundred == 75:
        return "Eversmoking Bottle"
    if rando_hundred == 76:
        return "Eyes of Charming"
    if rando_hundred == 77:
        return "Eyes of the Eagle"
    if rando_hundred == 78:
        return "Figurine of wondrous power (silver raven)"
    if rando_hundred == 79:
        return "Gem of Brightness"
    if rando_hundred == 80:
        return "Gloves of Missle Snaring"
    if rando_hundred == 81:
        return "Gloves of Swimming and Climbing"
    if rando_hundred == 82:
        return "Gloves of Thievery"
    if rando_hundred == 83:
        return "Headband of Intellect"
    if rando_hundred == 84:
        return "Helm of Intellect"
    if rando_hundred == 85:
        return "Instrument of the Bards (Doss Lute)"
    if rando_hundred == 86:
        return "Instrument of the Bards (Fochlucan Bandore)"
    if rando_hundred == 87:
        return "Instrument of the Bards (Mac-Fimidh Cittern)"
    if rando_hundred == 88:
        return "Medallion of Thoughts"
    if rando_hundred == 89:
        return "Necklace of Adaption"
    if rando_hundred == 90:
        return "Periapt of Wound Closure"
    if rando_hundred == 91:
        return "Pipes of Haunting"
    if rando_hundred == 92:
        return "Pipes of the Sewers"
    if rando_hundred == 93:
        return "Ring of Jumping"
    if rando_hundred == 94:
        return "Ring of Mind Shielding"
    if rando_hundred == 95:
        return "Ring of Warmth"
    if rando_hundred == 96:
        return "Ring of Water Walking"
    if rando_hundred == 97:
        return "Quiver of Ehlonna"
    if rando_hundred == 98:
        return "Stone of Good Luck"
    if rando_hundred == 99:
        return "Wind Fan"
    if rando_hundred == 100:
        return "Winged Boots"


def magic_table_g():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 11:
        return "Weapon +2"
    if 12 <= rando_hundred <= 14:
        figurines = ['Bronze Griffon','Ebony Fly','Golden Lions','Ivory Goats','Marble Elephant','Onyx Dog','Onyx Dog','Serpentine Owl']
        return "Figurine of wondrous power ({})".format(random.choice(figurines))
    if rando_hundred == 15:
        return "Adamantine Armor (Breastplate)"
    if rando_hundred == 16:
        return "Adamantine Armor (Splint)"
    if rando_hundred == 17:
        return "Amulet of Health"
    if rando_hundred == 18:
        return "Armor of Vulnerability"
    if rando_hundred == 19:
        return "Arrow-catching Shield"
    if rando_hundred == 20:
        return "Belt of Dwarvenkind"
    if rando_hundred == 21:
        return "Belt of Hill Giant Strength"
    if rando_hundred == 22:
        return "Berserker Axe"
    if rando_hundred == 23:
        return "Boots of Levitation"
    if rando_hundred == 24:
        return "Boots of Speed"
    if rando_hundred == 25:
        return "Bowl of Commanding Water Elementals"
    if rando_hundred == 26:
        return "Bracers of Defense"
    if rando_hundred == 27:
        return "Brazier of Commanding Fire Elementals"
    if rando_hundred == 28:
        return "Cape of the Mountebank"
    if rando_hundred == 29:
        return "Censer of Controlling Air Elementals"
    if rando_hundred == 30:
        return "Armor, +1 Chain Mail"
    if rando_hundred == 31:
        return "Armor of Resistance (Chain Mail)"
    if rando_hundred == 32:
        return "Armor, +1 Chain Shirt"
    if rando_hundred == 33:
        return "Armor of Resistance (Chain Shirt)"
    if rando_hundred == 34:
        return "Cloak of Displacement"
    if rando_hundred == 35:
        return "Cloak of the Bat"
    if rando_hundred == 36:
        return "Cube of Force"
    if rando_hundred == 37:
        return "Daern's Instant Fortress"
    if rando_hundred == 38:
        return "Dagger of Venom"
    if rando_hundred == 39:
        return "Dimensional Shackles"
    if rando_hundred == 40:
        return "Dragon Slayer"
    if rando_hundred == 41:
        return "Elven Chain"
    if rando_hundred == 42:
        return "Flame Tongue"
    if rando_hundred == 43:
        return "Gem of Seeing"
    if rando_hundred == 44:
        return "Giant Slayer"
    if rando_hundred == 45:
        return "Glamoured Studded Leather"
    if rando_hundred == 46:
        return "Helm of Teleportation"
    if rando_hundred == 47:
        return "Horn of Blasting"
    if rando_hundred == 48:
        return "Horn of Valhalla (silver or brass)"
    if rando_hundred == 49:
        return "Instrument of the Bards (Canaith Mandolin)"
    if rando_hundred == 50:
        return "Instrument of the Bards (Cli Lye)"
    if rando_hundred == 51:
        return "loun stone (awareness)"
    if rando_hundred == 52:
        return "loun stone (protection)"
    if rando_hundred == 53:
        return "loun stone (reserve)"
    if rando_hundred == 54:
        return "loun stone (sustenance)"
    if rando_hundred == 55:
        return "Iron bands of Bilarro"
    if rando_hundred == 56:
        return "Armor, +1 Leather"
    if rando_hundred == 57:
        return "Armor of Resistance (Leather)"
    if rando_hundred == 58:
        return "Mace of Disruption"
    if rando_hundred == 59:
        return "Mace of Smithing"
    if rando_hundred == 60:
        return "Mace of Terror"
    if rando_hundred == 61:
        return "Mantle of Spell Resistance"
    if rando_hundred == 62:
        return "Necklace of Prayer Beads"
    if rando_hundred == 63:
        return "Periapt of Proof Against Poison"
    if rando_hundred == 64:
        return "Ring of Animal Influence"
    if rando_hundred == 65:
        return "Ring of Evasion"
    if rando_hundred == 66:
        return "Ring of Feather Falling"
    if rando_hundred == 67:
        return "Ring of Free Action"
    if rando_hundred == 68:
        return "Ring of Protection"
    if rando_hundred == 69:
        return "Ring of Resistance"
    if rando_hundred == 70:
        return "Ring of Spell Storing"
    if rando_hundred == 71:
        return "Ring of the Ram"
    if rando_hundred == 72:
        return "Ring of X-ray Vision"
    if rando_hundred == 73:
        return "Robe of Eyes"
    if rando_hundred == 74:
        return "Rod of Rulership"
    if rando_hundred == 75:
        return "Rod of the Pact Keeper, +2"
    if rando_hundred == 76:
        return "Rope of Entanglement"
    if rando_hundred == 77:
        return "Armor, +1 (Scale Mail)"
    if rando_hundred == 78:
        return "Armor of Resistance (Scale Mail)"
    if rando_hundred == 79:
        return "Shield, +2"
    if rando_hundred == 80:
        return "Shield of Missle Attraction"
    if rando_hundred == 81:
        return "Staff of Charming"
    if rando_hundred == 82:
        return "Staff of Healing"
    if rando_hundred == 83:
        return "Staff of Swarming Insects"
    if rando_hundred == 84:
        return "Staff of the Woodlands"
    if rando_hundred == 85:
        return "Staff of Withering"
    if rando_hundred == 86:
        return "Stone of Controlling Earth Elementals"
    if rando_hundred == 87:
        return "Sun Blade"
    if rando_hundred == 88:
        return "Sword of Life Stealing"
    if rando_hundred == 89:
        return "Sword of Wounding"
    if rando_hundred == 90:
        return "Tentacle Rod"
    if rando_hundred == 91:
        return "Vicious Weapon"
    if rando_hundred == 92:
        return "Wand of Binding"
    if rando_hundred == 93:
        return "Wand of Enemy Detection"
    if rando_hundred == 94:
        return "Wand of Fear"
    if rando_hundred == 95:
        return "Wand of Fireballs"
    if rando_hundred == 96:
        return "Wand of Lightning Bolts"
    if rando_hundred == 97:
        return "Wand of Paralysis"
    if rando_hundred == 98:
        return "Wand of the War Mage, +2"
    if rando_hundred == 99:
        return "Wand of Wonder"
    if rando_hundred == 100:
        return "Wings of Flying"



def magic_table_h():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 10:
        return "Weapon +3"
    if 11 <= rando_hundred <= 12:
        return "Amulet of the Planes"
    if 13 <= rando_hundred <= 14:
        return "Carpet of Flying"
    if 15 <= rando_hundred <= 16:
        return "Crystal Ball (Very Rare Version)"
    if 17 <= rando_hundred <= 18:
        return "Ring of Regeneration"
    if 19 <= rando_hundred <= 20:
        return "Ring of Shooting Stars"
    if 21 <= rando_hundred <= 22:
        return "Ring of Telekinesis"
    if 23 <= rando_hundred <= 24:
        return "Robe of Scintillating Colors"
    if 25 <= rando_hundred <= 26:
        return "Robe of Stars"
    if 27 <= rando_hundred <= 28:
        return "Rod of Absorbtion"
    if 29 <= rando_hundred <= 30:
        return "Rod of Alertness"
    if 31 <= rando_hundred <= 32:
        return "Rod of Security"
    if 33 <= rando_hundred <= 34:
        return "Rod of the Pact Keeper, +3"
    if 35 <= rando_hundred <= 36:
        return "Scimitar of Speed"
    if 37 <= rando_hundred <= 38:
        return "Shield, +3"
    if 39 <= rando_hundred <= 40:
        return "Staff of Fire"
    if 41 <= rando_hundred <= 42:
        return "Staff of Frost"
    if 43 <= rando_hundred <= 44:
        return "Staff of Power"
    if 45 <= rando_hundred <= 46:
        return "Staff of Striking"
    if 47 <= rando_hundred <= 48:
        return "Staff of Thunder and Lightning"
    if 49 <= rando_hundred <= 50:
        return "Sword of Sharpness"
    if 51 <= rando_hundred <= 52:
        return "Wand of Polymorph"
    if 53 <= rando_hundred <= 54:
        return "Wand of the War Mage, +3"
    if rando_hundred == 55:
        return "Adamantine Armor (Half Plate)"
    if rando_hundred == 56:
        return "Adamantine Armor (Plate)"
    if rando_hundred == 57:
        return "Animated Shield"
    if rando_hundred == 58:
        return "Belt of Fire Giant Strength"
    if rando_hundred == 59:
        return "Belt of Frost (or Stone) Giant Strength"
    if rando_hundred == 60:
        return "Armor, +1 Breastplate"
    if rando_hundred == 61:
        return "Armor of Resistance (Breastplate)"
    if rando_hundred == 62:
        return "Candle of Invocation"
    if rando_hundred == 63:
        return "Armor, +2 Chain Mail"
    if rando_hundred == 64:
        return "Armor, +2 Chain Shirt"
    if rando_hundred == 65:
        return "Cloak of Arachnida"
    if rando_hundred == 66:
        return "Dancing Sword"
    if rando_hundred == 67:
        return "Demon Armor"
    if rando_hundred == 68:
        return "Dragon Scale Mail"
    if rando_hundred == 69:
        return "Dwarven Plate"
    if rando_hundred == 70:
        return "Dwarven Thrower"
    if rando_hundred == 71:
        return "Efreeti Bottle"
    if rando_hundred == 72:
        return "Figurine of Wondrous Power (Obsidian Steed)"
    if rando_hundred == 73:
        return "Frost Brand"
    if rando_hundred == 74:
        return "Helm of Brilliance"
    if rando_hundred == 75:
        return "Horn of Valhalla (Bronze)"
    if rando_hundred == 76:
        return "Instrument of the Bards (Anstruth Harp)"
    if rando_hundred == 77:
        return "Loun Stone (Absorption)"
    if rando_hundred == 78:
        return "Loun Stone (Agility)"
    if rando_hundred == 79:
        return "Loun Stone (Fortitude)"
    if rando_hundred == 80:
        return "Loun Stone (Insight)"
    if rando_hundred == 81:
        return "Loun Stone (Intellect)"
    if rando_hundred == 82:
        return "Loun Stone (Leadership)"
    if rando_hundred == 83:
        return "Loun Stone (Strength)"
    if rando_hundred == 84:
        return "Armor, +2 Leather"
    if rando_hundred == 85:
        return "Manual of Bodily Health"
    if rando_hundred == 86:
        return "Manual of Gainful Exercise"
    if rando_hundred == 87:
        return "Manual of Golems"
    if rando_hundred == 88:
        return "Manual of Quickness of Action"
    if rando_hundred == 89:
        return "Mirror of Life Trapping"
    if rando_hundred == 90:
        return "Nine Lives Stealer"
    if rando_hundred == 91:
        return "Oathbow"
    if rando_hundred == 92:
        return "Armor, +2 Scale Mail"
    if rando_hundred == 93:
        return "Spellguard Shield"
    if rando_hundred == 94:
        return "Armor, +1 Splint"
    if rando_hundred == 95:
        return "Armor of Resistance (Splint)"
    if rando_hundred == 96:
        return "Armor, +1 Studded Leather"
    if rando_hundred == 97:
        return "Armor of Resistance (Studded Leather)"
    if rando_hundred == 98:
        return "Tome of Clear Thought"
    if rando_hundred == 99:
        return "Tome of Leadership and Influence"
    if rando_hundred == 100:
        return "Tome of Understanding"


def magic_table_i():
    rando_hundred = dice_roller.d100()
    if 1 <= rando_hundred <= 5:
        return "Defender"
    if 6 <= rando_hundred <= 10:
        return "Hammer of Thunderbolts"
    if 11 <= rando_hundred <= 15:
        return "Luck Blade"
    if 16 <= rando_hundred <= 20:
        return "Sword of Answering"
    if 21 <= rando_hundred <= 23:
        return "Holy Avenger"
    if 24 <= rando_hundred <= 26:
        return "Ring of Djinni Summoning"
    if 27 <= rando_hundred <= 29:
        return "Ring of Invisibility"
    if 30 <= rando_hundred <= 32:
        return "Ring of Spell Turning"
    if 33 <= rando_hundred <= 35:
        return "Rod of Lordly Might"
    if 36 <= rando_hundred <= 38:
        return "Staff of the Magi"
    if 39 <= rando_hundred <= 41:
        return "Vorpal Sword"
    if 42 <= rando_hundred <= 43:
        return "Belt of Cloud Giant Strength"
    if 44 <= rando_hundred <= 45:
        return "Armor, +2 Breastplate"
    if 46 <= rando_hundred <= 47:
        return "Armor, +3 Chain Mail"
    if 48 <= rando_hundred <= 49:
        return "Armor, +3 Chain Shirt"
    if 50 <= rando_hundred <= 51:
        return "Cloak of Invisibility"
    if 52 <= rando_hundred <= 53:
        return "Crystal Ball (Legendary Version)"
    if 54 <= rando_hundred <= 55:
        return "Armor, +1 Half Plate"
    if 56 <= rando_hundred <= 57:
        return "Iron Flask"
    if 58 <= rando_hundred <= 59:
        return "Armor, +3 Leather"
    if 60 <= rando_hundred <= 61:
        return "Armor, +1 Plate"
    if 62 <= rando_hundred <= 63:
        return "Robe of the Archmagi"
    if 64 <= rando_hundred <= 65:
        return "Rod of Ressurection"
    if 66 <= rando_hundred <= 67:
        return "Armor, +1 Scale Mail"
    if 68 <= rando_hundred <= 69:
        return "Scarab of Protection"
    if 70 <= rando_hundred <= 71:
        return "Armor, +2 Splint"
    if 72 <= rando_hundred <= 73:
        return "Armor, +2 Studded Leather"
    if 74 <= rando_hundred <= 75:
        return "Well of Many Worlds"
    if rando_hundred == 76:
        dice_roll = dice_roller.d12()
        if 1 <= dice_roll <= 2:
            return "Armor, +2 Half Plate"
        if 3 <= dice_roll <= 4:
            return "Armor, +2 Plate"
        if 5 <= dice_roll <= 6:
            return "Armor, +3 Studded Leather"
        if 7 <= dice_roll <= 8:
            return "Armor, +3 Breastplate"
        if 9 <= dice_roll <= 10:
            return "Armor, +3 Splint"
        if dice_roll = 11:
            return "Armor, +3 Half Plate"
        if dice_roll = 12:
            return "Armor, +3 Plate"
    if rando_hundred == 77:
        return "Apparatus of Kwalish"
    if rando_hundred == 78:
        return "Armor of Invulnerability"
    if rando_hundred == 79:
        return "Belt of Storm Giant Strength"
    if rando_hundred == 80:
        return "Cubic Gate"
    if rando_hundred == 81:
        return "Deck of Many Things"
    if rando_hundred == 82:
        return "Efreeti Chain"
    if rando_hundred == 83:
        return "Armor of Resistance (Half Plate)"
    if rando_hundred == 84:
        return "Horn of Valhalla (Iron)"
    if rando_hundred == 85:
        return "Instrument of the Bards (Ollamh Harp)"
    if rando_hundred == 86:
        return "loun stone (greater absorption)"
    if rando_hundred == 87:
        return "loun stone (mastery)"
    if rando_hundred == 88:
        return "loun stone (regeneration)"
    if rando_hundred == 89:
        return "Plate Armor of Etherealness"
    if rando_hundred == 90:
        return "Plate Armor of Resistance"
    if rando_hundred == 91:
        return "Ring of Air Elemental Command"
    if rando_hundred == 92:
        return "Ring of Earth Elemental Command"
    if rando_hundred == 93:
        return "Ring of Fire Elemental Command"
    if rando_hundred == 94:
        return "Ring of Three Wishes"
    if rando_hundred == 95:
        return "Ring of Water Elemental Command"
    if rando_hundred == 96:
        return "Sphere of Annihilation"
    if rando_hundred == 97:
        return "Talisman of Pure Good"
    if rando_hundred == 98:
        return "Talisman of the Sphere"
    if rando_hundred == 99:
        return "Talisman of Ultimate Evil"
    if rando_hundred == 100:
        return "Tome of the Stilled Tongue"

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
