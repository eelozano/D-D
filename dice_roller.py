# This is a dice roller for standard dice used in D&D 5th Edition.
# Each die takes a variable indicating how many are being rolled
# and returns a combined value.

import random

# Dice Roller, it defaults to one six sided die
def dx(num_sides=6,num_dice=1):
    dice_roll = 0
    while num_dice > 0:
        rando = random.randint(1,num_sides)
        dice_roll = dice_roll + rando
        num_dice = num_dice - 1
    return dice_roll

# Dice Roller with added return string for the values of the roll.
def dxplus(num_sides=6,num_dice=1):
    dice_roll = 0
    numbers = []
    while num_dice > 0:
        rando = random.randint(1,num_sides)
        numbers.append(rando)
        dice_roll = dice_roll + rando
        num_dice = num_dice - 1
    return dice_roll,numbers