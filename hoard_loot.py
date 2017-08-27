# A loot roller for the hoard tables in D&D 5th Edition

import tables
import dice_roller

# Prompting for challenge rating (determines what tables to pull from).
# Challenge rating (CR) determines which which loot table to use.
# Catches incorrect input
while True:
    try:
        challenge_rating = int(input("\n\nPlease enter a challenge rating between 0 and 20: "))
        if challenge_rating < 0 or challenge_rating > 20:
            raise ValueError()
        else:
            break
    except ValueError:
        print("PLEASE ENTER A VALUE BETWEEN ZERO (0) AND TWENTY (20) INCLUSIVE\n")
        pass

# Coin loot for CR 0 - 4
def zero_four_print():
    print("Your hoard includes the following!")
    print(
        "{:,} Copper Pieces, {:,} Silver Pieces, and {:,} Gold Pieces".format(dice_roller.dx(6,6) * 100,
                                                                              dice_roller.dx(6,3) * 100,
                                                                              dice_roller.dx(6,2) * 10))
# Coin loot for CR 5 - 10
def five_ten_print():
    print("Your hoard includes the following!")
    print(
        "{:,} Copper Pieces, {:,} Silver Pieces, {:,} Gold Pieces, and {:,} Platinum Pieces".
            format(dice_roller.dx(6,2)*100,dice_roller.dx(6,2)*1000,
                   dice_roller.dx(6,6)*100,dice_roller.dx(6,3)*10))

def eleven_sixteen_print():
    print("Your hoard includes the following!")
    print(
        "{:,} Gold Pieces and {:,} Platinum Pieces".
            format(dice_roller.dx(6,4)*1000,dice_roller.dx(6,5)*100))

def seventeen_plus():
    print("Your hoard includes the following")
    print(
        "{:,} Gold Pieces and {:,} Platinum Pieces".
            format(dice_roller.dx(6,12)*1000,dice_roller.dx(6,8)*1000))

# Rolling on CR 0 - 4 table
if 0 <= challenge_rating <= 4:
    rando_hundred = dice_roller.dx(100,1)
    if 1 <= rando_hundred <= 6:
        zero_four_print()
    if 7 <= rando_hundred <= 16:
        zero_four_print()
        print(tables.print_returns(tables.ten_gp_gem(dice_roller.dx(6,2))))
    if 17 <= rando_hundred <= 26:
        zero_four_print()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(4,2))))
    if 27 <= rando_hundred <= 36:
        zero_four_print()
        print(tables.print_returns(tables.fifty_gp_gem(dice_roller.dx(6,2))))
    if 37 <= rando_hundred <= 44:
        zero_four_print()
        print(tables.print_returns(tables.ten_gp_gem(dice_roller.dx(6,2))))
        print(tables.print_returns(tables.magic_table_a(dice_roller.dx(6,1))))
    if 45 <= rando_hundred <= 52:
        zero_four_print()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_a(dice_roller.dx(6,1))))
    if 53 <= rando_hundred <= 60:
        zero_four_print()
        print(tables.print_returns(tables.fifty_gp_gem(dice_roller.dx(6,2))))
        print(tables.print_returns(tables.magic_table_a(dice_roller.dx(6,1))))
    if 61 <= rando_hundred <= 65:
        zero_four_print()
        print(tables.print_returns(tables.ten_gp_gem(dice_roller.dx(6,2))))
        print(tables.print_returns(tables.magic_table_b(dice_roller.dx(4,1))))
    if 66 <= rando_hundred <= 70:
        zero_four_print()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(6,2))))
        print(tables.print_returns(tables.magic_table_b(dice_roller.dx(4,1))))
    if 71 <= rando_hundred <= 75:
        zero_four_print()
        print(tables.print_returns(tables.fifty_gp_gem(dice_roller.dx(6,2))))
        print(tables.print_returns(tables.magic_table_b(dice_roller.dx(4,1))))
    if 76 <= rando_hundred <= 78:
        zero_four_print()
        print(tables.print_returns(tables.ten_gp_gem(dice_roller.dx(6,2))))
        print(tables.print_returns(tables.magic_table_c(dice_roller.dx(4,1))))
    if 79 <= rando_hundred <= 80:
        zero_four_print()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_c(dice_roller.dx(4,1))))
    if 81 <= rando_hundred <= 85:
        zero_four_print()
        print(tables.print_returns(tables.fifty_gp_gem(dice_roller.dx(6,2))))
        print(tables.print_returns(tables.magic_table_c(dice_roller.dx(4,1))))
    if 86 <= rando_hundred <= 92:
        zero_four_print()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_f(dice_roller.dx(4,1))))
    if 93 <= rando_hundred <= 97:
        zero_four_print()
        print(tables.print_returns(tables.fifty_gp_gem(dice_roller.dx(6,2))))
        print(tables.print_returns(tables.magic_table_f(dice_roller.dx(4,1))))
    if 98 <= rando_hundred <= 99:
        zero_four_print()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_g()))
    if rando_hundred == 100:
        zero_four_print()
        print(tables.print_returns(tables.fifty_gp_gem(dice_roller.dx(6,2))))
        print(tables.print_returns(tables.magic_table_g()))

# Rolling on CR 5-10
if 5 <= challenge_rating <= 10:
    rando_hundred = dice_roller.dx(100,1)
    if 1 <= rando_hundred <= 4:
        five_ten_print()
    if 5 <= rando_hundred <= 10:
        five_ten_print()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(6,2))))
    if 11 <= rando_hundred <= 16:
        five_ten_print()
        print(tables.print_returns(tables.fifty_gp_gem(dice_roller.dx(6,3))))
    if 17 <= rando_hundred <= 22:
        five_ten_print()
        print(tables.print_returns(tables.one_hundred_gp_gem(dice_roller.dx(6,3))))
    if 23 <= rando_hundred <= 28:
        five_ten_print()
        print(tables.print_returns(tables.two_hundred_fifty_gp_art(dice_roller.dx(4,2))))
    if 29 <= rando_hundred <= 32:
        five_ten_print()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_a(dice_roller.dx(6,1))))
    if 33 <= rando_hundred <= 36:
        five_ten_print()
        print(tables.print_returns(tables.fifty_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_a(dice_roller.dx(6,1))))
    if 37 <= rando_hundred <= 40:
        five_ten_print()
        print(tables.print_returns(tables.one_hundred_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_a(dice_roller.dx(6,1))))
    if 41 <= rando_hundred <= 44:
        five_ten_print()
        print(tables.print_returns(tables.two_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_a(dice_roller.dx(6,1))))
    if 45 <= rando_hundred <= 49:
        five_ten_print()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_b(dice_roller.dx(4,1))))
    if 50 <= rando_hundred <= 54:
        five_ten_print()
        print(tables.print_returns(tables.fifty_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_b(dice_roller.dx(4,1))))
    if 55 <= rando_hundred <= 59:
        five_ten_print()
        print(tables.print_returns(tables.one_hundred_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_b(dice_roller.dx(4,1))))
    if 60 <= rando_hundred <= 63:
        five_ten_print()
        print(tables.print_returns(tables.two_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_b(dice_roller.dx(4,1))))
    if 64 <= rando_hundred <= 66:
        five_ten_print()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_c(dice_roller.dx(4,1))))
    if 67 <= rando_hundred <= 69:
        five_ten_print()
        print(tables.print_returns(tables.fifty_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_c(dice_roller.dx(4,1))))
    if 70 <= rando_hundred <= 72:
        five_ten_print()
        print(tables.print_returns(tables.one_hundred_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_c(dice_roller.dx(4,1))))
    if 73 <= rando_hundred <= 74:
        five_ten_print()
        print(tables.print_returns(tables.two_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_c(dice_roller.dx(4,1))))
    if 75 <= rando_hundred <= 76:
        five_ten_print()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_d()))
    if 77 <= rando_hundred <= 78:
        five_ten_print()
        print(tables.print_returns(tables.fifty_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_d()))

    if rando_hundred == 79:
        five_ten_print()
        print(tables.print_returns(tables.one_hundred_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_d()))
    if rando_hundred == 80:
        five_ten_print()
        print(tables.print_returns(tables.two_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_d()))
    if 81 <= rando_hundred <= 84:
        five_ten_print()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_f(dice_roller.dx(4,1))))
    if 85 <= rando_hundred <= 88:
        five_ten_print()
        print(tables.print_returns(tables.fifty_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_f(dice_roller.dx(4,1))))
    if 89 <= rando_hundred <= 91:
        five_ten_print()
        print(tables.print_returns(tables.one_hundred_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_f(dice_roller.dx(4,1))))
    if 92 <= rando_hundred <= 94:
        five_ten_print()
        print(tables.print_returns(tables.two_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_f(dice_roller.dx(4,1))))
    if 95 <= rando_hundred <= 96:
        five_ten_print()
        print(tables.print_returns(tables.one_hundred_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_g(dice_roller.dx(4,1))))
    if 97 <= rando_hundred <= 98:
        five_ten_print()
        print(tables.print_returns(tables.two_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_g(dice_roller.dx(4,1))))
    if rando_hundred == 99:
        five_ten_print()
        print(tables.print_returns(tables.one_hundred_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_h()))
    if rando_hundred == 100:
        five_ten_print()
        print(tables.print_returns(tables.two_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_h()))


if 11 <= challenge_rating <= 16:
    rando_hundred = dice_roller.dx(100,1)
    if 1 <= rando_hundred <= 3:
        eleven_sixteen_print()
    if 4 <= rando_hundred <= 6:
        eleven_sixteen_print()
        print(tables.print_returns(tables.two_hundred_fifty_gp_art(dice_roller.dx(4,2))))
    if 7 <= rando_hundred <= 9:
        eleven_sixteen_print()
        print(tables.print_returns(tables.seven_hundred_fifty_gp_art(dice_roller.dx(4,2))))
    if 10 <= rando_hundred <= 12:
        eleven_sixteen_print()
        print(tables.print_returns(tables.five_hundred_gp_gem(dice_roller.dx(6,3))))
    if 13 <= rando_hundred <= 15:
        eleven_sixteen_print()
        print(tables.print_returns(tables.one_thousand_gp_gem(dice_roller.dx(6,3))))
    if 16 <= rando_hundred <= 19:
        eleven_sixteen_print()
        print(tables.print_returns(tables.two_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_a(dice_roller.dx(4,1))+
                                   tables.magic_table_b(dice_roller.dx(6,1))))
    if 20 <= rando_hundred <= 23:
        eleven_sixteen_print()
        print(tables.print_returns(tables.seven_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_a(dice_roller.dx(4,1))+
                                   tables.magic_table_b(dice_roller.dx(6,1))))
    if 24 <= rando_hundred <= 26:
        eleven_sixteen_print()
        print(tables.print_returns(tables.five_hundred_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_a(dice_roller.dx(4,1))+
                                   tables.magic_table_b(dice_roller.dx(6,1))))
    if 27 <= rando_hundred <= 29:
        eleven_sixteen_print()
        print(tables.print_returns(tables.one_thousand_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_a(dice_roller.dx(4,1))+
                                   tables.magic_table_b(dice_roller.dx(6,1))))
    if 30 <= rando_hundred <= 35:
        eleven_sixteen_print()
        print(tables.print_returns(tables.two_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_c(dice_roller.dx(6,1))))
    if 36 <= rando_hundred <= 40:
        eleven_sixteen_print()
        print(tables.print_returns(tables.seven_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_c(dice_roller.dx(6,1))))
    if 41 <= rando_hundred <= 45:
        eleven_sixteen_print()
        print(tables.print_returns(tables.five_hundred_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_c(dice_roller.dx(6,1))))
    if 46 <= rando_hundred <= 50:
        eleven_sixteen_print()
        print(tables.print_returns(tables.one_thousand_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_c(dice_roller.dx(6,1))))
    if 51 <= rando_hundred <= 54:
        eleven_sixteen_print()
        print(tables.print_returns(tables.two_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_d(dice_roller.dx(4,1))))
    if 55 <= rando_hundred <= 58:
        eleven_sixteen_print()
        print(tables.print_returns(tables.seven_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_d(dice_roller.dx(4,1))))
    if 59 <= rando_hundred <= 62:
        eleven_sixteen_print()
        print(tables.print_returns(tables.five_hundred_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_d(dice_roller.dx(4,1))))
    if 63 <= rando_hundred <= 66:
        eleven_sixteen_print()
        print(tables.print_returns(tables.one_thousand_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_d(dice_roller.dx(4,1))))
    if 67 <= rando_hundred <= 68:
        eleven_sixteen_print()
        print(tables.print_returns(tables.two_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_e()))
    if 69 <= rando_hundred <= 70:
        eleven_sixteen_print()
        print(tables.print_returns(tables.seven_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_e()))
    if 71 <= rando_hundred <= 72:
        eleven_sixteen_print()
        print(tables.print_returns(tables.five_hundred_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_e()))
    if 73 <= rando_hundred <= 74:
        eleven_sixteen_print()
        print(tables.print_returns(tables.one_thousand_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_e()))
    if 75 <= rando_hundred <= 76:
        eleven_sixteen_print()
        print(tables.print_returns(tables.two_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_f() +
                                   tables.magic_table_g(dice_roller.dx(4,1))))
    if 77 <= rando_hundred <= 78:
        eleven_sixteen_print()
        print(tables.print_returns(tables.seven_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_f() +
                                   tables.magic_table_g(dice_roller.dx(4,1))))
    if 79 <= rando_hundred <= 80:
        eleven_sixteen_print()
        print(tables.print_returns(tables.five_hundred_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_f() +
                                   tables.magic_table_g(dice_roller.dx(4,1))))
    if 81 <= rando_hundred <= 82:
        eleven_sixteen_print()
        print(tables.print_returns(tables.one_thousand_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_f() +
                                   tables.magic_table_g(dice_roller.dx(4,1))))
    if 83 <= rando_hundred <= 85:
        eleven_sixteen_print()
        print(tables.print_returns(tables.two_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_h(dice_roller.dx(4,1))))
    if 86 <= rando_hundred <= 88:
        eleven_sixteen_print()
        print(tables.print_returns(tables.seven_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_h(dice_roller.dx(4,1))))
    if 89 <= rando_hundred <= 90:
        eleven_sixteen_print()
        print(tables.print_returns(tables.five_hundred_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_h(dice_roller.dx(4,1))))
    if 91 <= rando_hundred <= 92:
        eleven_sixteen_print()
        print(tables.print_returns(tables.one_thousand_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_h(dice_roller.dx(4,1))))
    if 93 <= rando_hundred <= 94:
        eleven_sixteen_print()
        print(tables.print_returns(tables.two_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_i()))
    if 95 <= rando_hundred <= 96:
        eleven_sixteen_print()
        print(tables.print_returns(tables.seven_hundred_fifty_gp_art(dice_roller.dx(4,2))))
        print(tables.print_returns(tables.magic_table_i()))
    if 97 <= rando_hundred <= 98:
        eleven_sixteen_print()
        print(tables.print_returns(tables.five_hundred_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_i()))
    if 99 <= rando_hundred <= 100:
        eleven_sixteen_print()
        print(tables.print_returns(tables.one_thousand_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_i()))

if 17 <= challenge_rating <= 20:
    rando_hundred = dice_roller.dx(100,1)
    if 1 <= rando_hundred <= 2:
        seventeen_plus()
    if 3 <= rando_hundred <= 5:
        seventeen_plus()
        print(tables.print_returns(tables.one_thousand_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_c(dice_roller.dx(8,1))))
    if 6 <= rando_hundred <= 8:
        seventeen_plus()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(10,1))))
        print(tables.print_returns(tables.magic_table_c(dice_roller.dx(8,1))))
    if 9 <= rando_hundred <= 11:
        seventeen_plus()
        print(tables.print_returns(tables.seven_thousand_five_hundred_gp_art(dice_roller.dx(4,1))))
        print(tables.print_returns(tables.magic_table_c(dice_roller.dx(8,1))))
    if 12 <= rando_hundred <= 14:
        seventeen_plus()
        print(tables.print_returns(tables.five_thousand_gem(dice_roller.dx(8,1))))
        print(tables.print_returns(tables.magic_table_c(dice_roller.dx(8,1))))
    if 15 <= rando_hundred <= 22:
        seventeen_plus()
        print(tables.print_returns(tables.one_thousand_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_d(dice_roller.dx(6,1))))
    if 23 <= rando_hundred <= 30:
        seventeen_plus()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(10,1))))
        print(tables.print_returns(tables.magic_table_d(dice_roller.dx(6,1))))
    if 31 <= rando_hundred <= 38:
        seventeen_plus()
        print(tables.print_returns(tables.seven_thousand_five_hundred_gp_art(dice_roller.dx(4,1))))
        print(tables.print_returns(tables.magic_table_d(dice_roller.dx(6,1))))
    if 39 <= rando_hundred <= 46:
        seventeen_plus()
        print(tables.print_returns(tables.five_thousand_gem(dice_roller.dx(8,1))))
        print(tables.print_returns(tables.magic_table_d(dice_roller.dx(6,1))))
    if 47 <= rando_hundred <= 52:
        seventeen_plus()
        print(tables.print_returns(tables.one_thousand_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_e(dice_roller.dx(6,1))))
    if 53 <= rando_hundred <= 58:
        seventeen_plus()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(10,1))))
        print(tables.print_returns(tables.magic_table_e(dice_roller.dx(6,1))))
    if 59 <= rando_hundred <= 63:
        seventeen_plus()
        print(tables.print_returns(tables.seven_thousand_five_hundred_gp_art(dice_roller.dx(4,1))))
        print(tables.print_returns(tables.magic_table_e(dice_roller.dx(6,1))))
    if 64 <= rando_hundred <= 68:
        seventeen_plus()
        print(tables.print_returns(tables.five_thousand_gem(dice_roller.dx(8,1))))
        print(tables.print_returns(tables.magic_table_e(dice_roller.dx(6,1))))
    if rando_hundred == 69:
        seventeen_plus()
        print(tables.print_returns(tables.one_thousand_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_g(dice_roller.dx(4,1))))
    if rando_hundred == 70:
        seventeen_plus()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(10,1))))
        print(tables.print_returns(tables.magic_table_g(dice_roller.dx(4,1))))
    if rando_hundred == 71:
        seventeen_plus()
        print(tables.print_returns(tables.seven_thousand_five_hundred_gp_art(dice_roller.dx(4,1))))
        print(tables.print_returns(tables.magic_table_g(dice_roller.dx(4,1))))
    if rando_hundred == 72:
        seventeen_plus()
        print(tables.print_returns(tables.five_thousand_gem(dice_roller.dx(8,1))))
        print(tables.print_returns(tables.magic_table_g(dice_roller.dx(4,1))))
    if 73 <= rando_hundred <= 74:
        seventeen_plus()
        print(tables.print_returns(tables.one_thousand_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_h(dice_roller.dx(4,1))))
    if 75 <= rando_hundred <= 76:
        seventeen_plus()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(10,1))))
        print(tables.print_returns(tables.magic_table_h(dice_roller.dx(4,1))))
    if 77 <= rando_hundred <= 78:
        seventeen_plus()
        print(tables.print_returns(tables.seven_thousand_five_hundred_gp_art(dice_roller.dx(4,1))))
        print(tables.print_returns(tables.magic_table_h(dice_roller.dx(4,1))))
    if 79 <= rando_hundred <= 80:
        seventeen_plus()
        print(tables.print_returns(tables.five_thousand_gem(dice_roller.dx(8,1))))
        print(tables.print_returns(tables.magic_table_h(dice_roller.dx(4,1))))
    if 81 <= rando_hundred <= 85:
        seventeen_plus()
        print(tables.print_returns(tables.one_thousand_gp_gem(dice_roller.dx(6,3))))
        print(tables.print_returns(tables.magic_table_i(dice_roller.dx(4,1))))
    if 86 <= rando_hundred <= 90:
        seventeen_plus()
        print(tables.print_returns(tables.twenty_five_gp_art(dice_roller.dx(10,1))))
        print(tables.print_returns(tables.magic_table_i(dice_roller.dx(4,1))))
    if 91 <= rando_hundred <= 95:
        seventeen_plus()
        print(tables.print_returns(tables.seven_thousand_five_hundred_gp_art(dice_roller.dx(4,1))))
        print(tables.print_returns(tables.magic_table_i(dice_roller.dx(4,1))))
    if 96 <= rando_hundred <= 100:
        seventeen_plus()
        print(tables.print_returns(tables.five_thousand_gem(dice_roller.dx(8,1))))
        print(tables.print_returns(tables.magic_table_i(dice_roller.dx(4,1))))