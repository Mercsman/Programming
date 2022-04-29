# tire_volume
import math


# inputs
width = float(input('Please enter the width of the tire in mm: '))
aspect = float(input('Please enter the aspect ratio of the tire: '))
diameter = float(input('Please enter the diameter of the wheel in inches: '))

# function and equation
pi = math.pi
volume = ((pi * (width ** 2) * aspect) * ((width * aspect) + (2540 * diameter))) / 10000000000

print (f'{volume:.2f} liters')