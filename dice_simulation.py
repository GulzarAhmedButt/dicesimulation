import random

min_value = 1
max_value = 6

roll_dice = 'yes'

while roll_dice =='yes' or roll_dice =='y':

    print('Rolling dice....')

    print(' Dice Values are: ')

    print(random.randint(min_value, max_value))

    roll_dice = input('Do you want to roll a dice again ?')
