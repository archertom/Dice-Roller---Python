# This is a simple dice roller in the command line using Python's Random module.
# You should be asked how many dice you wish to roll,
# and then for the number of sides your dice should have.
# Both sides and dice should accept any positive integer
# (within reason! - but I have tested with 10d999999999999).
# The roller will then roll those dice and print the result.


import random


# number of dice
def get_dice():
    while True:
        dice_input = input("How many dice do you want? (integer)")
        try:
            dice_input = int(dice_input)
        except ValueError:
            pass
        else:
            if dice_input > 0:
                return dice_input
            else:
                pass


# number of sides
def get_sides():
    while True:
        side_input = input("How many sides should your dice have? (integer)")
        try:
            side_input = int(side_input)
        except ValueError:
            pass
        else:
            if side_input > 0:
                return side_input
            else:
                pass


# The number of sides variable must be global as roll_sides() will be called for each die.
n_sides = get_sides()


# set up dice roll
def roll_sides():
    return random.randint(1, n_sides)


# set up loop for number of dice
def roll_dice():
    n_dice = get_dice()
    result = []
    # for(i=0, i<nDice, i++):
    for i in range(n_dice):
        result.append(roll_sides())
    print(result)


roll_dice()


