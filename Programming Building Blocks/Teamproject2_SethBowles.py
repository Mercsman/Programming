
import math
# v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
# Title
print ()
print ('        Velocity Calculator        ')
print ('-----------------------------------')

# Variables
m = float(input('Mass (in kg): '))
g = float(input('Gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter): '))
t = float(input('Time (in seconds): '))
p = float(input('Density of fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
A = float(input('Cross sectional area (in m^2): '))
C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

# calculations for the equation
c = (1/2) * p * A * C
# exp = the number e (2.71828) to the given exponent. This can be computed in Python with the Math library function math.exp(value).
# sqrt = the square root of the given expression. This can be computed in Python with the Math library function math.sqrt(value).
print ()
print (f'The inner value of c is: {c:.3f}')
# Main equation
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))
# Velocity
print (f'The velocity after {t} seconds is: {v:.3f} m/s')
print ()


# Stretch goal 1