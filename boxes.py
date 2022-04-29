# boxes

import math


print('Welcome to the package helper!')
print('------------------------------')

items = int(input('How many manufactured items do you have? '))
per_box = int(input('How many will you pack per box? '))

box =  items / per_box
round_box = math.ceil(box)
print(f'\nFor {items} items, packing {per_box} items in each box, you will need {round_box} boxes.')
print('------------------------------')