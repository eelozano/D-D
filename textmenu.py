import dice_roller

def die_roller():
    print('\n' * 80)
    sides = input('How many sides on the die? ')
    num_die = input('How many die would you like to roll? ')
    result = dice_roller.dxplus(int(sides),int(num_die))
    question = input('Would you like to see the results of the individual die? [Y,N]')
    if (question == 'Y'):
        print('You rolled a total of: ' + str(result[0]) + '\n')
        print('Your individual rolls were: ' + str(result[1]) + '\n')


def main_menu():
    print(45 * '-')
    print('Welcome Dungeon Master\n')
    print('Please select from the following options\n')
    print('1. Dice Roller')
    print('2. Individual Loot Tables')
    print('3. Hoard Loot Tables')
    print('4. Spell Search')
    print('5. EXIT')
    print(45 * '-' + '\n')

main_menu()
answer = input("What is your selection? ")
print(answer)
if (int(answer) == 1):
    die_roller()

11