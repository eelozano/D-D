# This is a dice roller for standard dice used in D&D 5th Edition.
# Each die takes a variable indicating how many are being rolled
# and returns a combined value.

from random import *

# Roll four-sided die
def d4(number=1):
    dice_roll = 0
    while number > 0:
        rando = randint(1,4)
        dice_roll = dice_roll + rando
        number = number - 1
    return dice_roll

# Roll six-sided die
def d6(number=1):
    dice_roll = 0
    while number > 0:
        rando = randint(1,6)
        dice_roll = dice_roll + rando
        number = number - 1
    return dice_roll

# Roll eight-sided die
def d8(number=1):
    dice_roll = 0
    while number > 0:
        rando = randint(1,8)
        dice_roll = dice_roll + rando
        number = number - 1
    return dice_roll

# Roll ten-sided die
def d10(number=1):
    dice_roll = 0
    while number > 0:
        rando = randint(1,10)
        dice_roll = dice_roll + rando
        number = number - 1
    return dice_roll

# Roll twelve-sided die
def d12(number=1):
    dice_roll = 0
    while number > 0:
        rando = randint(1,12)
        dice_roll = dice_roll + rando
        number = number - 1
    return dice_roll

# Roll twenty-sided die
def d20(number=1):
    dice_roll = 0
    while number > 0:
        rando = randint(1,20)
        dice_roll = dice_roll + rando
        number = number - 1
    return dice_roll

# Roll hundred-sided die
def d100(number=1):
    dice_roll = 0
    while number > 0:
        rando = randint(1,100)
        dice_roll = dice_roll + rando
        number = number - 1
    return dice_roll
