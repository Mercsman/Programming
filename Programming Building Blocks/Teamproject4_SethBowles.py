import math
print()
print('Welcome to the new ride')
#  questions
age_1 = float(input('What is the age of the first rider? '))
height_1 = float(input('What is the height of the first rider? '))
#  Stretch 2
if age_1 >= 12 and age_1 < 18:
    ticket = input ('Do they have a gold passport(yes/no)? ')
    if ticket.lower() == 'yes':
        age_1 = 18
riders = input('Is there a second rider (yes/no)? ')
if riders.lower() == 'yes':
    age_2 = float(input('What is the age of the second rider? '))
    height_2 = float(input('What is the height of the second rider? '))
    #  Stretch 2
    if age_2 >= 12 and age_2 < 18:
        ticket = input ('Do they have a gold passport(yes/no)? ')
        if ticket.lower() == 'yes':
            age_2 = 18

#  ifs
if riders.lower() == 'no' and age_1 >= 18 and height_1 >= 62:
    print ('Welcome! Please be safe and enjoy the ride.')
elif riders.lower() == 'yes' and (age_1 >=18 or age_2 >= 18) and height_1 >=36 and height_2 >= 36:
    print ('Welcome! Please be safe and enjoy the ride. ')
#  stretch 1
elif riders.lower() == 'yes' and age_1 >=12 and age_2 >= 12 and height_1 >= 52 and height_2 >= 52:
    print ('Welcome! Please be safe and enjoy the ride. ')
#  stretch 3
elif riders.lower() == 'yes' and ((age_1 >=16 and age_2 >= 14) or (age_1 >= 14 and age_2 >= 16)) and height_1 >= 36 and height_2 >=36:
    print ('Welcome! Please be safe and enjoy the ride. ')
else:
    print ('Sorry, but you may not ride. ')