import sys
from random import *

def d6(number):
    dice_roll = 0
    while number > 0:
        rando = randint(1,6)
        dice_roll = dice_roll + rando
        number = number - 1
    return dice_roll

def d100(number):
    dice_roll = 0
    while number > 0:
        rando = randint(1,100)
        dice_roll = dice_roll + rando
        number = number - 1
    return dice_roll



challenge_rating = int(input("Please enter a challenge rating between 0 and 20: "))
while challenge_rating < 0 or challenge_rating > 20:
	sys.exit("Please try again with proper input")
if challenge_rating >= 0 and challenge_rating <= 4:
    rando_hundred = d100(1)
    if rando_hundred >= 1 and rando_hundred <= 30:
        print("You gained: " + str(d6(5)) + " copper pieces.")
    if rando_hundred >= 31 and rando_hundred <= 60:
        print("You gained: " + str(d6(4)) + "silver pieces.")
    if rando_hundred >= 61 and rando_hundred <= 70:
        print("You gained: " + str(d6(3)) + "electrum pieces.")
    if rando_hundred >= 71 and rando_hundred <= 95:
        print("You gained: " + str(d6(3)) + "gold pieces.")
    if rando_hundred >= 96 and rando_hundred <= 100:
        print("You gained: " + str(d6(1)) + "platinum pieces.")


