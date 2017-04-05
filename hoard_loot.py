# This will eventually be the hoard equivalent to individual_loot.py3

import tables
import dice_roller

# Prompting for challenge rating (determines what tables to pull from).
# Challenge rating (CR) determines which which loot table to use.
challenge_rating = int(input("\n\nPlease enter a challenge rating between 0 and 4: "))
# Simple check of the input
while challenge_rating < 0 or challenge_rating > 4:
    challenge_rating = int(input("Please enter a challenge rating between 0 and 4: "))



# Rolling on CR 0 - 4 table
if 0 <= challenge_rating <= 4:
    rando_hundred = dice_roller.d100()
    print("\n\nYou rolled a: {}\n\n".format(rando_hundred))
    if 1 <= rando_hundred <= 6:
        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
    if 7 <= rando_hundred <= 16:
        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
        print("Ten GP Gemstones - {}".format(tables.ten_gp_gem(dice_roller.d6(2))))
    if 17 <= rando_hundred <= 26:
        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
        print("Twenty-Five GP Art - {}".format(tables.twenty_five_gp_art(dice_roller.d4(2))))
    if 27 <= rando_hundred <= 36:
        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
        print("Fifty GP Gemstones - {}".format(tables.fifty_gp_gem(dice_roller.d6(2))))
    if 37 <= rando_hundred <= 44:
        magic_loot_roll = dice_roller.d6()
        magic_list = []

        while magic_loot_roll > 0:
            magic_list.append(tables.magic_table_a())
            magic_loot_roll = magic_loot_roll - 1

        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
        print("Ten GP Gemstones - {}".format(tables.ten_gp_gem(dice_roller.d6(2))))
        print(tables.print_magic_table(magic_list))
    if 45 <= rando_hundred <= 52:
        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
        print("Twenty-Five GP Art - {}".format(tables.twenty_five_gp_art(dice_roller.d4(2))))
    if 53 <= rando_hundred <= 60:
        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
        print("Fifty GP Gemstones - {}".format(tables.fifty_gp_gem(dice_roller.d6(2))))
    if 61 <= rando_hundred <= 65:
        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
        print("Ten GP Gemstones - {}".format(tables.ten_gp_gem(dice_roller.d6(2))))
    if 66 <= rando_hundred <= 70:
        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
        print("Twenty-Five GP Art - {}".format(tables.twenty_five_gp_art(dice_roller.d4(2))))
    if 71 <= rando_hundred <= 75:
        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
        print("Fifty GP Gemstones - {}".format(tables.fifty_gp_gem(dice_roller.d6(2))))
    if 76 <= rando_hundred <= 78:
        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
        print("Ten GP Gemstones - {}".format(tables.ten_gp_gem(dice_roller.d6(2))))
    if 79 <= rando_hundred <= 80:
        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
        print("Twenty-Five GP Art - {}".format(tables.twenty_five_gp_art(dice_roller.d4(2))))
    if 81 <= rando_hundred <= 85:
        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
        print("Fifty GP Gemstones - {}".format(tables.fifty_gp_gem(dice_roller.d6(2))))
    if 86 <= rando_hundred <= 92:
        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
        print("Twenty-Five GP Art - {}".format(tables.twenty_five_gp_art(dice_roller.d4(2))))
    if 93 <= rando_hundred <= 97:
        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
        print("TFifty GP Gemstones - {}".format(tables.fifty_gp_gem(dice_roller.d6(2))))
    if 98 <= rando_hundred <= 99:
        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
        print("Twenty-Five GP Art - {}".format(tables.twenty_five_gp_art(dice_roller.d4(2))))
    if rando_hundred == 100:
        print("Your hoard includes the following!")
        print(
            "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.d6(6) * 100, dice_roller.d6(3) * 100, dice_roller.d6(2) * 10))
        print("Fifty GP Gemstones - {}".format(tables.fifty_gp_gem(dice_roller.d6(2))))
