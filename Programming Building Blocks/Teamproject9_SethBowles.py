import math
import sys

def mainMenu():
    while True:
        # Welcome message
        print('------------------------------------------------------------')
        print('Area computer')
        # Options
        print('''Please select an option below:
        1. Square
        2. Rectangle
        3. Circle
        4. Area
        5. Quit''')
        
        choice = input('Please select an option (1-5): ')
        # menu
        if choice == '1':
            square_side = float(input('What is the length of the side of the square? '))
            area = rectangleArea(square_side, square_side)
            print (f'The area of the square is: {area}')
        elif choice == '2':
            r_width = float(input('What is the width of the rectangle? '))
            r_length = float(input('What is the length of the rectangle? '))
            area = rectangleArea(r_length, r_width)
            print (f'The area of the square is: {area}')
        elif choice == '3':
            radius = float(input('What is the radius of the circle? '))
            area = circleArea(radius)
            print (f'The area of the square is: {area:.2f}')
        elif choice == '4':
            a = float(input('What is the number for the area? '))
            b = float(input('What is the second number for the area? '))
            area = computeArea(shape, a, b)
            print (f'The area of the square is: {area:.2f}')
        # exit
        elif choice == '5':
            print('\nThank you\n')
            sys.exit()
        else:
            print('Please select a valid option.')

# area of the square
def squareArea(square_side):
    # area = (square_side * square_side)
    return square_side * square_side
    # print (f'The area of the square is: {area}')

# area of a rectangle
def rectangleArea(r_length, r_width):
    # area = r_width * r_length
    return r_width * r_length
    # print (f'The area of the rectangle is: {area}')

# area of a circle
def circleArea(radius):
    # area = (radius ** 2) * math.pi
    return (radius ** 2) * math.pi
    # print (f'The area of the circle is: {area}')
    
def computeArea(shape, a, b=False):
    shape = input('What shape do you have? ').lower()
    if shape == 'square':
        return a * a
        # side = float(input('What is the length of the side? '))
        # area = computeArea(shape, (side * side), False)
    elif shape == 'rectangle':
        return a * b
        # width = float(input('What is the width of the rectangle? '))
        # length = float(input('What is the length of the rectangle? '))
        # area = computeArea(shape, width, length=True)
    elif shape == 'circle':
        return (a**2) * math.pi
    else:
        print('Not a valid option.')
# square_side = float(input('What is the length of the side of the square? '))
# r_width = float(input('What is the width of the rectangle? '))
# r_length = float(input('What is the length of the rectangle? '))
# radius = float(input('What is the radius of the circle? '))

# def computeArea(shape, ):
shape = ''
mainMenu()