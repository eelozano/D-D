# This is a simple program that takes as its input a challenge rating and returns
# the amount of loot you are getting.  This is based on the DMs Guide for the 5th
# edition of D&D.

# Currently this just rolls on the individual table, but I am also working on the
# group loot table which is much more complex as it rolls on several different
# tables for monetary and non-monetary tables.

from dice_roller import d100,d6



# Prompting for challenge rating (determines what tables to pull from).
# Challenge rating (CR) determines which which loot table to use.
challenge_rating = int(input("Please enter a challenge rating between 0 and 20: "))
# Simple check of the input
while challenge_rating < 0 or challenge_rating > 20:
    challenge_rating = int(input("Please enter a challenge rating between 0 and 20: "))

# Rolling a hundred-sided die to determine what on the loot table to return.
rando_hundred = d100()

# Tables based on DM Guide pg. 136

# Rolling on CR 0 - 4 table
# if challenge_rating >= 0 and challenge_rating <= 4:
if 0 <= challenge_rating <= 4:
    if 1 <= rando_hundred <= 30:
        print("You gained {:,} copper pieces.".format(d6(5)))
    if 31 <= rando_hundred <= 60:
        print("You gained {:,} silver pieces.".format(d6(4)))
    if 61 <= rando_hundred <= 70:
        print("You gained: {:,} electrum pieces.".format(d6(3)))
    if 71 <= rando_hundred <= 95:
        print("You gained: {:,} gold pieces.".format(d6(3)))
    if 96 <= rando_hundred <= 100:
        print("You gained: {:,} platinum pieces.".format(d6()))

# Rolling on CR 5-10 table
if 5 <= challenge_rating <= 10:
    if 1 <= rando_hundred <= 30:
        print("You gained: {:,} copper pieces and {:,} electrum pieces".format(d6(4)*100,(d6())))
    if 31 <= rando_hundred <= 60:
        print("You gained: {:,} silver pieces and {:,} gold pieces.".format(d6(6) * 10,d6(2) * 10))
    if 61 <= rando_hundred <= 70:
        print("You gained: {:,} electrum pieces and {:,} gold pieces".format(d6(3) * 10,d6(2) * 10))
    if 71 <= rando_hundred <= 95:
        print("You gained: {:,} gold pieces.".format(d6(4)*10))
    if 96 <= rando_hundred <= 100:
        print("You gained: {:,} gold pieces and {:,} platinum pieces".format(d6(2) * 10, d6(3)))

# Rolling on CR 11-16 table
if 11 <= challenge_rating <= 16:
    if 1 <= rando_hundred <= 20:
        print("You gained {:,} silver pieces and {:,} gold pieces.".format(d6(4)*100,d6()*100))
    if 21 <= rando_hundred <= 35:
        print("You gained {:,} electrum pieces and {:,} gold pieces".format(d6()*100,d6()*100))
    if 36 <= rando_hundred <= 75:
        print("You gained {:,} gold pieces and {:,} platinum pieces".format(d6(2)*100,d6()*10))
    if 76 <= rando_hundred <= 100:
        print("You gained {:,} gold pieces and {:,} platinum pieces.".format(d6(2)*100,d6(2)*10))

# Rolling on CR 17-20 table
if 17 <= challenge_rating <= 20:
    if 1 <= rando_hundred <= 15:
        print("You gained {:,} electrum pieces and {:,} gold pieces.".format(d6(2)*1000,d6(8)*100))
    if 16 <= rando_hundred <= 55:
        print("You gained {:,} gold pieces and {:,} platinum pieces.".format(d6()*1000,d6()*100))
    if 56 <= rando_hundred <= 100:
        print("You gained {:,} gold pieces and {:,} platinum pieces.".format(d6()*1000,d6(2)*100))
