# This will be the library for roll tables to be used throughout other programs.
# All roll tables will accept a variable to allow for the return of multiple
# items at once.  The returns are currently strings, but in the future (depending
# on how the programs play out) it will probably start returning lists to allow
# individual programs to decide how to manipulate the returns.

# Importing modules
import random
import dice_roller
import json

# Prints a human readable list
def print_returns(input_list):
    return_string = ""
    length = len(input_list)
    if length == 1:
        return_string ="{}".format(input_list[0])
    elif length == 2:
        print("{} and {}".format(input_list[0],input_list[1]))
    else:
        while length > 1:
            return_string = return_string + "{}, ".format(input_list[length-1])
            length -= 1
        return_string = return_string + "and {}".format(input_list[0])
    return return_string


def random_list_appender(input_list, number):
    return_list = []
    while number > 0:
        return_list.append(random.choice(input_list))
        number -= 1
    return return_list


def ten_gp_gem(number=1):
    items = ["Azurite", "Banded agate", "Blue quartz", "Eyeagate", "Hematite",
             "Lapis lazuli", "Malachite", "Moss agate", "Obsidian", "Tiger eye",
             "Turquoise"]
    return random_list_appender(items, number)


def fifty_gp_gem(number=1):
    items = ["Bloodstone", "Carnelian", "Chalcedony", "Chrysoprase", "Citrine", "Jasper", "Moonstone", "Onyx", "Quartz",
             "Sardonyx", "Star rose quartz", "Zircon"]
    return random_list_appender(items, number)


def one_hundred_gp_gem(number=1):
    items = ["Amber", "Amethyst", "Chrysoberyl", "Coral", "Garnet", "Jade", "Jet", "Pearl", "Spinel", "Tourmaline"]
    return random_list_appender(items, number)


def five_hundred_gp_gem(number=1):
    items = ["Alexandrite", "Aquamarine", "Black pearl", "Blue spinel", "Peridot", "Topaz"]
    return random_list_appender(items, number)


def one_thousand_gp_gem(number=1):
    items = ["Black opal", "Blue sapphire", "Emerald", "Fire opal", "Opal", "Star ruby", "Star sapphire",
             "Yellow sapphire"]
    return random_list_appender(items, number)


def five_thousand_gem(number=1):
    items = ["Black sapphire", "Diamond", "Jacinth", "Ruby"]
    return random_list_appender(items, number)


def twenty_five_gp_art(number=1):
    items = ["Silver ewer", "Carved bone statuette", "Small gold bracelet", "Cloth-of-gold vestments",
             "Black velvet mask stitched with silver thread", "Copper chalice with silver filigree",
             "Pair of engraved bone dice", "Small mirror set in a painted wooden frame",
             "Embroidered silk handkerchief", "Gold locket with a painted portrait inside"]
    return random_list_appender(items, number)


def two_hundred_fifty_gp_art(number=1):
    items = ["Gold ring set with bloodstones", "Carved ivory statuette", "Large gold bracelet",
             "Silver necklace with a gemstone pendant", "Bronze crown", "Silk robe with gold embroidery",
             "Large well-made tapestry", "Brass mug with jade inlay", "Box of turquoise animal figurines",
             "Gold bird cage with electrum filigree"]
    return random_list_appender(items, number)


def seven_hundred_fifty_gp_art(number=1):
    items = ["Silver chalice set with moonstones", "Silver-plated steellongsword with jet set in hilt",
             "Carved harp of exotic wood with ivory inlay and zircon gems", "Small gold idol",
             "Gold dragon comb set with red garnets as eyes",
             "Bottle stopper cork embossed with gold leaf and set with amethysts",
             "Ceremonial electrum dagger with a black pearl in the pommel", "Silver and gold brooch",
             "Obsidian statuette with gold fittings and inlay", "Painted gold war mask"]
    return random_list_appender(items, number)


def two_thousand_five_hundred_gp_art(number=1):
    items = ["Fine gold chain set with a fire opal", "Old masterpiece painting",
             "Embroidered silk and velvet mantle set with numerous moonstones", "Platinum bracelet set with a sapphire",
             "Embroidered glove set with jewel chips", "Jeweled anklet", "Gold music box",
             "Gold circlet set with four aquamarines", "Eye patch with a mock eye set in blue sapphire and moonstone",
             "Eye patch with a mock eye set in blue sapphire and moonstone"]
    return random_list_appender(items, number)


def seven_thousand_five_hundred_gp_art(number=1):
    items = ["Jeweled gold crown", "Jeweled platinum ring", "Small gold statuette set with rubies",
             "Gold cup set with emeralds", "Gold jewelry box with platinum filigree",
             "Painted gold child's sarcophagus", "jade game board with solid gold playing pieces",
             "Bejeweled ivory drinking horn with gold filigree"]
    return random_list_appender(items, number)


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


def magic_table_a(number=1):
    temp_array = []
    while number > 0:
        rando_hundred = dice_roller.d100()
        if 1 <= rando_hundred <= 50:
            temp_array.append("Potion of Healing")
        if 51 <= rando_hundred <= 60:
            temp_array.append("Spell Scroll - {} - Cantrip".format(magic_spell('Cantrip')))
        if 61 <= rando_hundred <= 70:
            temp_array.append("Potion of Climbing")
        if 71 <= rando_hundred <= 90:
            temp_array.append("Spell Scroll - {} - 1st Level".format(magic_spell('1st-level')))
        if 91 <= rando_hundred <= 94:
            temp_array.append("Spell Scroll - {} - 2nd Level".format(magic_spell('2nd-level')))
        if 95 <= rando_hundred <= 98:
            temp_array.append("Potion of Greater Healing")
        if rando_hundred == 99:
            temp_array.append("Bag of Holding")
        if rando_hundred == 100:
            temp_array.append("Driftglobe")
        number -= 1
    return temp_array


def magic_table_b(number=1):
    temp_array = []
    while number > 0:
        rando_hundred = dice_roller.d100()
        if 1 <= rando_hundred <= 15:
            temp_array.append("Potion of Healing")
        if 16 <= rando_hundred <= 22:
            temp_array.append("Potion of Firebreath")
        if 23 <= rando_hundred <= 29:
            temp_array.append("Potion of Resistance")
        if 30 <= rando_hundred <= 34:
            temp_array.append("Ammunition +1")
        if 35 <= rando_hundred <= 39:
            temp_array.append("Potion of Animal Friendship")
        if 40 <= rando_hundred <= 44:
            temp_array.append("Potion of Hill Giant Strength")
        if 45 <= rando_hundred <= 49:
            temp_array.append("Potion of Growth")
        if 50 <= rando_hundred <= 54:
            temp_array.append("Potion of Water Breathing")
        if 55 <= rando_hundred <= 59:
            temp_array.append("Spell Scroll - {} - 2nd Level".format(magic_spell('2nd-level')))
        if 60 <= rando_hundred <= 64:
            temp_array.append("Spell Scroll - {} - 3rd Level".format(magic_spell('3rd-level')))
        if 65 <= rando_hundred <= 67:
            temp_array.append("Bag of Holding")
        if 68 <= rando_hundred <= 70:
            temp_array.append("Keoghtom's ointment")
        if 71 <= rando_hundred <= 73:
            temp_array.append("Oil of Slipperiness")
        if 74 <= rando_hundred <= 75:
            temp_array.append("Dust of Disappearance")
        if 76 <= rando_hundred <= 77:
            temp_array.append("Dust of Dryness")
        if 78 <= rando_hundred <= 79:
            temp_array.append("Dust of Sneezing and Choaking")
        if 80 <= rando_hundred <= 81:
            temp_array.append("Elemental Gem")
        if 82 <= rando_hundred <= 83:
            temp_array.append("Philter of Love")
        if rando_hundred == 84:
            temp_array.append("Alchemy Jug")
        if rando_hundred == 85:
            temp_array.append("Cap of Water Breathing")
        if rando_hundred == 86:
            temp_array.append("Cloak of the Manta Ray")
        if rando_hundred == 87:
            temp_array.append("Driftglobe")
        if rando_hundred == 88:
            temp_array.append("Goggles of Night")
        if rando_hundred == 89:
            temp_array.append("Helm of Comprehending Languages")
        if rando_hundred == 90:
            temp_array.append("Immovable Rod")
        if rando_hundred == 91:
            temp_array.append("Lantern of Revealing")
        if rando_hundred == 92:
            temp_array.append("Mariner's Armor")
        if rando_hundred == 93:
            temp_array.append("Mithral Armor")
        if rando_hundred == 94:
            temp_array.append("Potion of Poison")
        if rando_hundred == 95:
            temp_array.append("Ring of Swimming")
        if rando_hundred == 96:
            temp_array.append("Robe of Useful Items")
        if rando_hundred == 97:
            temp_array.append("Rope of Climbing")
        if rando_hundred == 98:
            temp_array.append("Saddle of Cavalier")
        if rando_hundred == 99:
            temp_array.append("Wang of Magic Detection")
        if rando_hundred == 100:
            temp_array.append("Want of Secrets")
        number -= 1
    return temp_array


def magic_table_c(number=1):
    temp_array = []
    while number > 0:
        rando_hundred = dice_roller.d100()
        if 1 <= rando_hundred <= 15:
            temp_array.append("Potion of Superior Healing")
        if 16 <= rando_hundred <= 22:
            temp_array.append("Spell Scroll - {} - 4th Level".format(magic_spell('4th-level')))
        if 23 <= rando_hundred <= 27:
            temp_array.append("Ammunition +2")
        if 28 <= rando_hundred <= 32:
            temp_array.append("Potion of Clairvoyance")
        if 33 <= rando_hundred <= 37:
            temp_array.append("Potion of Diminution")
        if 38 <= rando_hundred <= 42:
            temp_array.append("Potion of Gaseous Form")
        if 43 <= rando_hundred <= 47:
            temp_array.append("Potion of Frost Giant Strength")
        if 48 <= rando_hundred <= 52:
            temp_array.append("Potion of Stone Giant Strength")
        if 53 <= rando_hundred <= 57:
            temp_array.append("Potion of Heroism")
        if 58 <= rando_hundred <= 62:
            temp_array.append("Potion of Invulnerability")
        if 63 <= rando_hundred <= 67:
            temp_array.append("Potion of Mind Reading")
        if 68 <= rando_hundred <= 72:
            temp_array.append("Spell Scroll - {} - 5th Level".format(magic_spell('5th-level')))
        if 73 <= rando_hundred <= 75:
            temp_array.append("Elixir of Health")
        if 76 <= rando_hundred <= 78:
            temp_array.append("Oil of Etherealness")
        if 79 <= rando_hundred <= 81:
            temp_array.append("Potion of Fire Giant Strength")
        if 82 <= rando_hundred <= 84:
            temp_array.append("Quaal's Feather Token")
        if 85 <= rando_hundred <= 87:
            temp_array.append("Scroll of Protection")
        if 88 <= rando_hundred <= 89:
            temp_array.append("Bag of Beans")
        if 90 <= rando_hundred <= 91:
            temp_array.append("Bead of Force")
        if rando_hundred == 92:
            temp_array.append("Chime of Opening")
        if rando_hundred == 93:
            temp_array.append("Decanter of Endless Water")
        if rando_hundred == 94:
            temp_array.append("Eyes of Minute Seeing")
        if rando_hundred == 95:
            temp_array.append("Folding Boat")
        if rando_hundred == 96:
            temp_array.append("Heward's handy haversack")
        if rando_hundred == 97:
            temp_array.append("Horseshoes of speed")
        if rando_hundred == 98:
            temp_array.append("Necklace of fireballs")
        if rando_hundred == 99:
            temp_array.append("Periapt of health")
        if rando_hundred == 100:
            temp_array.append("Sending Stones")
        number -= 1
    return temp_array


def magic_table_d(number=1):
    temp_array = []
    while number > 0:
        rando_hundred = dice_roller.d100()
        if 1 <= rando_hundred <= 20:
            temp_array.append("Potion of Supreme Healing")
        if 21 <= rando_hundred <= 30:
            temp_array.append("Potion of Invisibility")
        if 31 <= rando_hundred <= 40:
            temp_array.append("Potion of Speed")
        if 41 <= rando_hundred <= 50:
            temp_array.append("Spell Scroll - {} - 6th Level".format(magic_spell('6th-level')))
        if 51 <= rando_hundred <= 57:
            temp_array.append("Spell Scroll - {} - 7th Level".format(magic_spell('7th-level')))
        if 58 <= rando_hundred <= 62:
            temp_array.append("Ammunition +3")
        if 63 <= rando_hundred <= 67:
            temp_array.append("Oil of Sharpness")
        if 68 <= rando_hundred <= 72:
            temp_array.append("Potion of Flying")
        if 73 <= rando_hundred <= 77:
            temp_array.append("Potion of Cloud Giant Strength")
        if 78 <= rando_hundred <= 82:
            temp_array.append("Potion of Longevity")
        if 83 <= rando_hundred <= 87:
            temp_array.append("Potion of Vitality")
        if 88 <= rando_hundred <= 92:
            temp_array.append("Spell Scroll - {} - 8th Level".format(magic_spell('8th-level')))
        if 93 <= rando_hundred <= 95:
            temp_array.append("Horseshoes of a Zephyr")
        if 96 <= rando_hundred <= 98:
            temp_array.append("Nolzur's Marvelous Pigments")
        if rando_hundred == 99:
            temp_array.append("Bag of Devouring")
        if rando_hundred == 100:
            temp_array.append("Portable Hole")
        number -= 1
    return temp_array

def magic_table_e(number=1):
    temp_array = []
    while number > 0:
        rando_hundred = dice_roller.d100()
        if 1 <= rando_hundred <= 30:
            temp_array.append("Spell Scroll - {} - 8th Level".format(magic_spell('8th-level')))
        if 31 <= rando_hundred <= 55:
            temp_array.append("Potion of Storm Giant Strength")
        if 56 <= rando_hundred <= 70:
            temp_array.append("Potion of Supreme Healing")
        if 71 <= rando_hundred <= 85:
            temp_array.append("Spell Scroll - {} - 9th Level".format(magic_spell('9th-level')))
        if 86 <= rando_hundred <= 93:
            temp_array.append("Universal Solvent")
        if 94 <= rando_hundred <= 98:
            temp_array.append("Arrow of Slaying")
        if 99 <= rando_hundred <= 100:
            temp_array.append("Sovereign Glue")
        number -= 1
    return temp_array

def magic_table_f(number=1):
    temp_array = []
    while number > 0:
        rando_hundred = dice_roller.d100()
        if 1 <= rando_hundred <= 15:
            temp_array.append("Weapon +1")
        if 16 <= rando_hundred <= 18:
            temp_array.append("Shield +1")
        if 19 <= rando_hundred <= 21:
            temp_array.append("Sentinel Shield")
        if 22 <= rando_hundred <= 23:
            temp_array.append("Amulet of Proof Against Detection and Location")
        if 24 <= rando_hundred <= 25:
            temp_array.append("Boots of Elvenkind")
        if 26 <= rando_hundred <= 27:
            temp_array.append("Boots of Striding and Springing")
        if 28 <= rando_hundred <= 29:
            temp_array.append("Bracers of Archery")
        if 30 <= rando_hundred <= 31:
            temp_array.append("Brooch of Shielding")
        if 32 <= rando_hundred <= 33:
            temp_array.append("Broom of Flying")
        if 34 <= rando_hundred <= 35:
            temp_array.append("Cloak of Elvenkind")
        if 36 <= rando_hundred <= 37:
            temp_array.append("Cloak of Protection")
        if 38 <= rando_hundred <= 39:
            temp_array.append("Gauntlets of Ogre Power")
        if 40 <= rando_hundred <= 41:
            temp_array.append("Hat of Disguise")
        if 42 <= rando_hundred <= 43:
            temp_array.append("Javelin of Lightning")
        if 44 <= rando_hundred <= 45:
            temp_array.append("Pearl of Power")
        if 46 <= rando_hundred <= 47:
            temp_array.append("Rod of the Pact Keeper, +1")
        if 48 <= rando_hundred <= 49:
            temp_array.append("Slippers of Spider Climbing")
        if 50 <= rando_hundred <= 51:
            temp_array.append("Staff of the Adder")
        if 52 <= rando_hundred <= 53:
            temp_array.append("Staff of the Python")
        if 54 <= rando_hundred <= 55:
            temp_array.append("Sword of Vengeance")
        if 56 <= rando_hundred <= 57:
            temp_array.append("Trident of Fish Command")
        if 58 <= rando_hundred <= 59:
            temp_array.append("Wand of Magic Missles")
        if 60 <= rando_hundred <= 61:
            temp_array.append("Wand of the War Mage, +1")
        if 62 <= rando_hundred <= 63:
            temp_array.append("Wand of Web")
        if 64 <= rando_hundred <= 65:
            temp_array.append("Weapon of Warning")
        if rando_hundred == 66:
            temp_array.append("Adamantine Armor (chain mail)")
        if rando_hundred == 67:
            temp_array.append("Adamantine Armor (chain shirt)")
        if rando_hundred == 68:
            temp_array.append("Adamantine Armor (scale mail)")
        if rando_hundred == 69:
            temp_array.append("Bag of tricks (gray)")
        if rando_hundred == 70:
            temp_array.append("Bag of tricks (rust)")
        if rando_hundred == 71:
            temp_array.append("Bag of tricks (tan)")
        if rando_hundred == 72:
            temp_array.append("Boots of the Winterlands")
        if rando_hundred == 73:
            temp_array.append("Circlet of Blasting")
        if rando_hundred == 74:
            temp_array.append("Deck of Illusions")
        if rando_hundred == 75:
            temp_array.append("Eversmoking Bottle")
        if rando_hundred == 76:
            temp_array.append("Eyes of Charming")
        if rando_hundred == 77:
            temp_array.append("Eyes of the Eagle")
        if rando_hundred == 78:
            temp_array.append("Figurine of wondrous power (silver raven)")
        if rando_hundred == 79:
            temp_array.append("Gem of Brightness")
        if rando_hundred == 80:
            temp_array.append("Gloves of Missle Snaring")
        if rando_hundred == 81:
            temp_array.append("Gloves of Swimming and Climbing")
        if rando_hundred == 82:
            temp_array.append("Gloves of Thievery")
        if rando_hundred == 83:
            temp_array.append("Headband of Intellect")
        if rando_hundred == 84:
            temp_array.append("Helm of Intellect")
        if rando_hundred == 85:
            temp_array.append("Instrument of the Bards (Doss Lute)")
        if rando_hundred == 86:
            temp_array.append("Instrument of the Bards (Fochlucan Bandore)")
        if rando_hundred == 87:
            temp_array.append("Instrument of the Bards (Mac-Fimidh Cittern)")
        if rando_hundred == 88:
            temp_array.append("Medallion of Thoughts")
        if rando_hundred == 89:
            temp_array.append("Necklace of Adaption")
        if rando_hundred == 90:
            temp_array.append("Periapt of Wound Closure")
        if rando_hundred == 91:
            temp_array.append("Pipes of Haunting")
        if rando_hundred == 92:
            temp_array.append("Pipes of the Sewers")
        if rando_hundred == 93:
            temp_array.append("Ring of Jumping")
        if rando_hundred == 94:
            temp_array.append("Ring of Mind Shielding")
        if rando_hundred == 95:
            temp_array.append("Ring of Warmth")
        if rando_hundred == 96:
            temp_array.append("Ring of Water Walking")
        if rando_hundred == 97:
            temp_array.append("Quiver of Ehlonna")
        if rando_hundred == 98:
            temp_array.append("Stone of Good Luck")
        if rando_hundred == 99:
            temp_array.append("Wind Fan")
        if rando_hundred == 100:
            temp_array.append("Winged Boots")
        number -= 1
    return temp_array

def magic_table_g(number=1):
    temp_array = []
    while number > 0:
        rando_hundred = dice_roller.d100()
        if 1 <= rando_hundred <= 11:
            temp_array.append("Weapon +2")
        if 12 <= rando_hundred <= 14:
            figurines = ['Bronze Griffon','Ebony Fly','Golden Lions','Ivory Goats','Marble Elephant','Onyx Dog','Onyx Dog','Serpentine Owl']
            temp_array.append("Figurine of wondrous power ({})".format(random.choice(figurines)))
        if rando_hundred == 15:
            temp_array.append("Adamantine Armor (Breastplate)")
        if rando_hundred == 16:
            temp_array.append("Adamantine Armor (Splint)")
        if rando_hundred == 17:
            temp_array.append("Amulet of Health")
        if rando_hundred == 18:
            temp_array.append("Armor of Vulnerability")
        if rando_hundred == 19:
            temp_array.append("Arrow-catching Shield")
        if rando_hundred == 20:
            temp_array.append("Belt of Dwarvenkind")
        if rando_hundred == 21:
            temp_array.append("Belt of Hill Giant Strength")
        if rando_hundred == 22:
            temp_array.append("Berserker Axe")
        if rando_hundred == 23:
            temp_array.append("Boots of Levitation")
        if rando_hundred == 24:
            temp_array.append("Boots of Speed")
        if rando_hundred == 25:
            temp_array.append("Bowl of Commanding Water Elementals")
        if rando_hundred == 26:
            temp_array.append("Bracers of Defense")
        if rando_hundred == 27:
            temp_array.append("Brazier of Commanding Fire Elementals")
        if rando_hundred == 28:
            temp_array.append("Cape of the Mountebank")
        if rando_hundred == 29:
            temp_array.append("Censer of Controlling Air Elementals")
        if rando_hundred == 30:
            temp_array.append("Armor, +1 Chain Mail")
        if rando_hundred == 31:
            temp_array.append("Armor of Resistance (Chain Mail)")
        if rando_hundred == 32:
            temp_array.append("Armor, +1 Chain Shirt")
        if rando_hundred == 33:
            temp_array.append("Armor of Resistance (Chain Shirt)")
        if rando_hundred == 34:
            temp_array.append("Cloak of Displacement")
        if rando_hundred == 35:
            temp_array.append("Cloak of the Bat")
        if rando_hundred == 36:
            temp_array.append("Cube of Force")
        if rando_hundred == 37:
            temp_array.append("Daern's Instant Fortress")
        if rando_hundred == 38:
            temp_array.append("Dagger of Venom")
        if rando_hundred == 39:
            temp_array.append("Dimensional Shackles")
        if rando_hundred == 40:
            temp_array.append("Dragon Slayer")
        if rando_hundred == 41:
            temp_array.append("Elven Chain")
        if rando_hundred == 42:
            temp_array.append("Flame Tongue")
        if rando_hundred == 43:
            temp_array.append("Gem of Seeing")
        if rando_hundred == 44:
            temp_array.append("Giant Slayer")
        if rando_hundred == 45:
            temp_array.append("Glamoured Studded Leather")
        if rando_hundred == 46:
            temp_array.append("Helm of Teleportation")
        if rando_hundred == 47:
            temp_array.append("Horn of Blasting")
        if rando_hundred == 48:
            temp_array.append("Horn of Valhalla (silver or brass)")
        if rando_hundred == 49:
            temp_array.append("Instrument of the Bards (Canaith Mandolin)")
        if rando_hundred == 50:
            temp_array.append("Instrument of the Bards (Cli Lye)")
        if rando_hundred == 51:
            temp_array.append("loun stone (awareness)")
        if rando_hundred == 52:
            temp_array.append("loun stone (protection)")
        if rando_hundred == 53:
            temp_array.append("loun stone (reserve)")
        if rando_hundred == 54:
            temp_array.append("loun stone (sustenance)")
        if rando_hundred == 55:
            temp_array.append("Iron bands of Bilarro")
        if rando_hundred == 56:
            temp_array.append("Armor, +1 Leather")
        if rando_hundred == 57:
            temp_array.append("Armor of Resistance (Leather)")
        if rando_hundred == 58:
            temp_array.append("Mace of Disruption")
        if rando_hundred == 59:
            temp_array.append("Mace of Smithing")
        if rando_hundred == 60:
            temp_array.append("Mace of Terror")
        if rando_hundred == 61:
            temp_array.append("Mantle of Spell Resistance")
        if rando_hundred == 62:
            temp_array.append("Necklace of Prayer Beads")
        if rando_hundred == 63:
            temp_array.append("Periapt of Proof Against Poison")
        if rando_hundred == 64:
            temp_array.append("Ring of Animal Influence")
        if rando_hundred == 65:
            temp_array.append("Ring of Evasion")
        if rando_hundred == 66:
            temp_array.append("Ring of Feather Falling")
        if rando_hundred == 67:
            temp_array.append("Ring of Free Action")
        if rando_hundred == 68:
            temp_array.append("Ring of Protection")
        if rando_hundred == 69:
            temp_array.append("Ring of Resistance")
        if rando_hundred == 70:
            temp_array.append("Ring of Spell Storing")
        if rando_hundred == 71:
            temp_array.append("Ring of the Ram")
        if rando_hundred == 72:
            temp_array.append("Ring of X-ray Vision")
        if rando_hundred == 73:
            temp_array.append("Robe of Eyes")
        if rando_hundred == 74:
            temp_array.append("Rod of Rulership")
        if rando_hundred == 75:
            temp_array.append("Rod of the Pact Keeper, +2")
        if rando_hundred == 76:
            temp_array.append("Rope of Entanglement")
        if rando_hundred == 77:
            temp_array.append("Armor, +1 (Scale Mail)")
        if rando_hundred == 78:
            temp_array.append("Armor of Resistance (Scale Mail)")
        if rando_hundred == 79:
            temp_array.append("Shield, +2")
        if rando_hundred == 80:
            temp_array.append("Shield of Missle Attraction")
        if rando_hundred == 81:
            temp_array.append("Staff of Charming")
        if rando_hundred == 82:
            temp_array.append("Staff of Healing")
        if rando_hundred == 83:
            temp_array.append("Staff of Swarming Insects")
        if rando_hundred == 84:
            temp_array.append("Staff of the Woodlands")
        if rando_hundred == 85:
            temp_array.append("Staff of Withering")
        if rando_hundred == 86:
            temp_array.append("Stone of Controlling Earth Elementals")
        if rando_hundred == 87:
            temp_array.append("Sun Blade")
        if rando_hundred == 88:
            temp_array.append("Sword of Life Stealing")
        if rando_hundred == 89:
            temp_array.append("Sword of Wounding")
        if rando_hundred == 90:
            temp_array.append("Tentacle Rod")
        if rando_hundred == 91:
            temp_array.append("Vicious Weapon")
        if rando_hundred == 92:
            temp_array.append("Wand of Binding")
        if rando_hundred == 93:
            temp_array.append("Wand of Enemy Detection")
        if rando_hundred == 94:
            temp_array.append("Wand of Fear")
        if rando_hundred == 95:
            temp_array.append("Wand of Fireballs")
        if rando_hundred == 96:
            temp_array.append("Wand of Lightning Bolts")
        if rando_hundred == 97:
            temp_array.append("Wand of Paralysis")
        if rando_hundred == 98:
            temp_array.append("Wand of the War Mage, +2")
        if rando_hundred == 99:
            temp_array.append("Wand of Wonder")
        if rando_hundred == 100:
            temp_array.append("Wings of Flying")
        number -= 1
    return temp_array


def magic_table_h(number=1):
    temp_array = []
    while number > 0:
        rando_hundred = dice_roller.d100()
        if 1 <= rando_hundred <= 10:
            temp_array.append("Weapon +3")
        if 11 <= rando_hundred <= 12:
            temp_array.append("Amulet of the Planes")
        if 13 <= rando_hundred <= 14:
            temp_array.append("Carpet of Flying")
        if 15 <= rando_hundred <= 16:
            temp_array.append("Crystal Ball (Very Rare Version)")
        if 17 <= rando_hundred <= 18:
            temp_array.append("Ring of Regeneration")
        if 19 <= rando_hundred <= 20:
            temp_array.append("Ring of Shooting Stars")
        if 21 <= rando_hundred <= 22:
            temp_array.append("Ring of Telekinesis")
        if 23 <= rando_hundred <= 24:
            temp_array.append("Robe of Scintillating Colors")
        if 25 <= rando_hundred <= 26:
            temp_array.append("Robe of Stars")
        if 27 <= rando_hundred <= 28:
            temp_array.append("Rod of Absorbtion")
        if 29 <= rando_hundred <= 30:
            temp_array.append("Rod of Alertness")
        if 31 <= rando_hundred <= 32:
            temp_array.append("Rod of Security")
        if 33 <= rando_hundred <= 34:
            temp_array.append("Rod of the Pact Keeper, +3")
        if 35 <= rando_hundred <= 36:
            temp_array.append("Scimitar of Speed")
        if 37 <= rando_hundred <= 38:
            temp_array.append("Shield, +3")
        if 39 <= rando_hundred <= 40:
            temp_array.append("Staff of Fire")
        if 41 <= rando_hundred <= 42:
            temp_array.append("Staff of Frost")
        if 43 <= rando_hundred <= 44:
            temp_array.append("Staff of Power")
        if 45 <= rando_hundred <= 46:
            temp_array.append("Staff of Striking")
        if 47 <= rando_hundred <= 48:
            temp_array.append("Staff of Thunder and Lightning")
        if 49 <= rando_hundred <= 50:
            temp_array.append("Sword of Sharpness")
        if 51 <= rando_hundred <= 52:
            temp_array.append("Wand of Polymorph")
        if 53 <= rando_hundred <= 54:
            temp_array.append("Wand of the War Mage, +3")
        if rando_hundred == 55:
            temp_array.append("Adamantine Armor (Half Plate)")
        if rando_hundred == 56:
            temp_array.append("Adamantine Armor (Plate)")
        if rando_hundred == 57:
            temp_array.append("Animated Shield")
        if rando_hundred == 58:
            temp_array.append("Belt of Fire Giant Strength")
        if rando_hundred == 59:
            temp_array.append("Belt of Frost (or Stone) Giant Strength")
        if rando_hundred == 60:
            temp_array.append("Armor, +1 Breastplate")
        if rando_hundred == 61:
            temp_array.append("Armor of Resistance (Breastplate)")
        if rando_hundred == 62:
            temp_array.append("Candle of Invocation")
        if rando_hundred == 63:
            temp_array.append("Armor, +2 Chain Mail")
        if rando_hundred == 64:
            temp_array.append("Armor, +2 Chain Shirt")
        if rando_hundred == 65:
            temp_array.append("Cloak of Arachnida")
        if rando_hundred == 66:
            temp_array.append("Dancing Sword")
        if rando_hundred == 67:
            temp_array.append("Demon Armor")
        if rando_hundred == 68:
            temp_array.append("Dragon Scale Mail")
        if rando_hundred == 69:
            temp_array.append("Dwarven Plate")
        if rando_hundred == 70:
            temp_array.append("Dwarven Thrower")
        if rando_hundred == 71:
            temp_array.append("Efreeti Bottle")
        if rando_hundred == 72:
            temp_array.append("Figurine of Wondrous Power (Obsidian Steed)")
        if rando_hundred == 73:
            temp_array.append("Frost Brand")
        if rando_hundred == 74:
            temp_array.append("Helm of Brilliance")
        if rando_hundred == 75:
            temp_array.append("Horn of Valhalla (Bronze)")
        if rando_hundred == 76:
            temp_array.append("Instrument of the Bards (Anstruth Harp)")
        if rando_hundred == 77:
            temp_array.append("Loun Stone (Absorption)")
        if rando_hundred == 78:
            temp_array.append("Loun Stone (Agility)")
        if rando_hundred == 79:
            temp_array.append("Loun Stone (Fortitude)")
        if rando_hundred == 80:
            temp_array.append("Loun Stone (Insight)")
        if rando_hundred == 81:
            temp_array.append("Loun Stone (Intellect)")
        if rando_hundred == 82:
            temp_array.append("Loun Stone (Leadership)")
        if rando_hundred == 83:
            temp_array.append("Loun Stone (Strength)")
        if rando_hundred == 84:
            temp_array.append("Armor, +2 Leather")
        if rando_hundred == 85:
            temp_array.append("Manual of Bodily Health")
        if rando_hundred == 86:
            temp_array.append("Manual of Gainful Exercise")
        if rando_hundred == 87:
            temp_array.append("Manual of Golems")
        if rando_hundred == 88:
            temp_array.append("Manual of Quickness of Action")
        if rando_hundred == 89:
            temp_array.append("Mirror of Life Trapping")
        if rando_hundred == 90:
            temp_array.append("Nine Lives Stealer")
        if rando_hundred == 91:
            temp_array.append("Oathbow")
        if rando_hundred == 92:
            temp_array.append("Armor, +2 Scale Mail")
        if rando_hundred == 93:
            temp_array.append("Spellguard Shield")
        if rando_hundred == 94:
            temp_array.append("Armor, +1 Splint")
        if rando_hundred == 95:
            temp_array.append("Armor of Resistance (Splint)")
        if rando_hundred == 96:
            temp_array.append("Armor, +1 Studded Leather")
        if rando_hundred == 97:
            temp_array.append("Armor of Resistance (Studded Leather)")
        if rando_hundred == 98:
            temp_array.append("Tome of Clear Thought")
        if rando_hundred == 99:
            temp_array.append("Tome of Leadership and Influence")
        if rando_hundred == 100:
            temp_array.append("Tome of Understanding")
        number -= 1
    return temp_array

def magic_table_i(number=1):
    temp_array = []
    while number > 0:
        rando_hundred = dice_roller.d100()
        if 1 <= rando_hundred <= 5:
            temp_array.append("Defender")
        if 6 <= rando_hundred <= 10:
            temp_array.append("Hammer of Thunderbolts")
        if 11 <= rando_hundred <= 15:
            temp_array.append("Luck Blade")
        if 16 <= rando_hundred <= 20:
            temp_array.append("Sword of Answering")
        if 21 <= rando_hundred <= 23:
            temp_array.append("Holy Avenger")
        if 24 <= rando_hundred <= 26:
            temp_array.append("Ring of Djinni Summoning")
        if 27 <= rando_hundred <= 29:
            temp_array.append("Ring of Invisibility")
        if 30 <= rando_hundred <= 32:
            temp_array.append("Ring of Spell Turning")
        if 33 <= rando_hundred <= 35:
            temp_array.append("Rod of Lordly Might")
        if 36 <= rando_hundred <= 38:
            temp_array.append("Staff of the Magi")
        if 39 <= rando_hundred <= 41:
            temp_array.append("Vorpal Sword")
        if 42 <= rando_hundred <= 43:
            temp_array.append("Belt of Cloud Giant Strength")
        if 44 <= rando_hundred <= 45:
            temp_array.append("Armor, +2 Breastplate")
        if 46 <= rando_hundred <= 47:
            temp_array.append("Armor, +3 Chain Mail")
        if 48 <= rando_hundred <= 49:
            temp_array.append("Armor, +3 Chain Shirt")
        if 50 <= rando_hundred <= 51:
            temp_array.append("Cloak of Invisibility")
        if 52 <= rando_hundred <= 53:
            temp_array.append("Crystal Ball (Legendary Version)")
        if 54 <= rando_hundred <= 55:
            temp_array.append("Armor, +1 Half Plate")
        if 56 <= rando_hundred <= 57:
            temp_array.append("Iron Flask")
        if 58 <= rando_hundred <= 59:
            temp_array.append("Armor, +3 Leather")
        if 60 <= rando_hundred <= 61:
            temp_array.append("Armor, +1 Plate")
        if 62 <= rando_hundred <= 63:
            temp_array.append("Robe of the Archmagi")
        if 64 <= rando_hundred <= 65:
            temp_array.append("Rod of Ressurection")
        if 66 <= rando_hundred <= 67:
            temp_array.append("Armor, +1 Scale Mail")
        if 68 <= rando_hundred <= 69:
            temp_array.append("Scarab of Protection")
        if 70 <= rando_hundred <= 71:
            temp_array.append("Armor, +2 Splint")
        if 72 <= rando_hundred <= 73:
            temp_array.append("Armor, +2 Studded Leather")
        if 74 <= rando_hundred <= 75:
            temp_array.append("Well of Many Worlds")
        if rando_hundred == 76:
            dice_roll = dice_roller.d12()
            if 1 <= dice_roll <= 2:
                temp_array.append("Armor, +2 Half Plate")
            if 3 <= dice_roll <= 4:
                temp_array.append("Armor, +2 Plate")
            if 5 <= dice_roll <= 6:
                temp_array.append("Armor, +3 Studded Leather")
            if 7 <= dice_roll <= 8:
                temp_array.append("Armor, +3 Breastplate")
            if 9 <= dice_roll <= 10:
                temp_array.append("Armor, +3 Splint")
            if dice_roll == 11:
                temp_array.append("Armor, +3 Half Plate")
            if dice_roll == 12:
                temp_array.append("Armor, +3 Plate")
        if rando_hundred == 77:
            temp_array.append("Apparatus of Kwalish")
        if rando_hundred == 78:
            temp_array.append("Armor of Invulnerability")
        if rando_hundred == 79:
            temp_array.append("Belt of Storm Giant Strength")
        if rando_hundred == 80:
            temp_array.append("Cubic Gate")
        if rando_hundred == 81:
            temp_array.append("Deck of Many Things")
        if rando_hundred == 82:
            temp_array.append("Efreeti Chain")
        if rando_hundred == 83:
            temp_array.append("Armor of Resistance (Half Plate)")
        if rando_hundred == 84:
            temp_array.append("Horn of Valhalla (Iron)")
        if rando_hundred == 85:
            temp_array.append("Instrument of the Bards (Ollamh Harp)")
        if rando_hundred == 86:
            temp_array.append("loun stone (greater absorption)")
        if rando_hundred == 87:
            temp_array.append("loun stone (mastery)")
        if rando_hundred == 88:
            temp_array.append("loun stone (regeneration)")
        if rando_hundred == 89:
            temp_array.append("Plate Armor of Etherealness")
        if rando_hundred == 90:
            temp_array.append("Plate Armor of Resistance")
        if rando_hundred == 91:
            temp_array.append("Ring of Air Elemental Command")
        if rando_hundred == 92:
            temp_array.append("Ring of Earth Elemental Command")
        if rando_hundred == 93:
            temp_array.append("Ring of Fire Elemental Command")
        if rando_hundred == 94:
            temp_array.append("Ring of Three Wishes")
        if rando_hundred == 95:
            temp_array.append("Ring of Water Elemental Command")
        if rando_hundred == 96:
            temp_array.append("Sphere of Annihilation")
        if rando_hundred == 97:
            temp_array.append("Talisman of Pure Good")
        if rando_hundred == 98:
            temp_array.append("Talisman of the Sphere")
        if rando_hundred == 99:
            temp_array.append("Talisman of Ultimate Evil")
        if rando_hundred == 100:
            temp_array.append("Tome of the Stilled Tongue")
        number -= 1
    return temp_array