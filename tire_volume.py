# tire_volume
import math
from datetime import datetime

day = datetime.now().date()
today = day
price = 0
# inputs
width = float(input('Please enter the width of the tire in mm: '))
aspect = float(input('Please enter the aspect ratio of the tire: '))
diameter = float(input('Please enter the diameter of the wheel in inches: '))
answer = ''
# function and equation
pi = math.pi
volume = ((pi * (width ** 2) * aspect) * ((width * aspect) + (2540 * diameter))) / 10000000000

print (f'The approximate volume is {volume:.2f} liters')

with open('volumes.txt', mode='at') as data:
    print (f'Today: {today} Width: {width} Aspect: {aspect} Diameter: {diameter} Volume: {volume:.2f}', file=data)
    

if width >= 185 and width < 205:
    price = 90
    
elif width >= 205 and width < 225:
    price = 115
    
elif width >= 225 and width < 275:
    price = 140
    
elif width >= 275 and width < 295:
    price = 180
    
print(f'The price is ${price}')
answer = input('Do you want to purchase these tires at these dimensions?(Y/N) ')

if answer.upper() == 'Y':
    phone = input('Please enter your phone number: ')
    
with open('volumes.txt', mode='at') as data:
    print (f'Phone number: {phone}', file=data)