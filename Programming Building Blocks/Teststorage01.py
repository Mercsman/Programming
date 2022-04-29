
# value = 10
# while value < 20:
#    value = value + 1
# print(value)




# from turtle import xcor
# from PIL import Image
# image_cat = Image.open('cat.jpg')
# image_forest = Image.open('forest.jpeg')

# pixels_cat = image_cat.load()
# pixels_forest = image_forest.load()

# print (pixels_cat[100, 200][0])
# for y in range(0, 600):
#     for x in range(0, 100):
        # (r, g, b) = pixels_cat
        # print(r, g, b)
# # image_original.show()

# width, height = image_cat.size
# # print(image_original.size)
# pixels_original = image_cat.load()
# for y in range (0, 600):
#     for x in range(0, 800):
#         (r, g, b) = pixels_original [x, y]
#         pixels_original[x, y] = (r, g, 255)

# # pixels_original[100, 200] = (200, 0, 200)

# # r, g, b = pixels_original[100, 200]

# # print (r, g, b)

# image_cat.show()

# # image_original.save('the_file_goes_here.jpg')


























# import random


# play = 'yes'
# while play.lower() == 'yes':
#     number = random.randint(1, 100)
# # print (number)
#     guess = 0
#     chances = 0
#     while guess != number:
#         guess = int(input('What is the magic number? '))
#         chances += 1
#         if guess > number:
#             print ('Lower')
#         elif guess < number:
#             print ('Higher')
#     # elif guess == number:
#     print ('Correct!')
#     print (f'It took you {chances} tries to guess it right. ')
#         # guess = int(input('What is the magic number? '))
#     # else:
#     #     print ('Error')
#     play = input('Do you want to play again? (yes/no). ')
# print ('Thanks for playing!')





# candy = input('May I have a piece of candy? ')

# while candy.lower() == 'no':
#     candy = input('May I have a piece of candy? ')

# print ('Thank you')







# number = float(input('Please enter a positive number: '))

# while number < 0:
#     print ('Sorry that is a negative number. Please try again.')
#     number = float(input('Please enter a positive number: '))

# print (f'The number is {number}')




# import math
# print()
# print('Welcome to the new ride')
# #  questions
# age_1 = float(input('What is the age of the first rider? '))
# height_1 = float(input('What is the height of the first rider? '))
# if age_1 >= 12 and age_1 < 18:
#     ticket = input ('Do they have a gold passport(yes/no)? ')
#     if ticket.lower() == 'yes':
#         age_1 = 18
# riders = input('Is there a second rider (yes/no)? ')
# if riders.lower() == 'yes':
#     age_2 = float(input('What is the age of the second rider? '))
#     height_2 = float(input('What is the height of the second rider? '))
#     if age_2 >= 12 and age_2 < 18:
#         ticket = input ('Do they have a gold passport(yes/no)? ')
#         if ticket.lower() == 'yes':
#             age_2 = 18

# #  ifs
# if riders.lower() == 'no' and age_1 >= 18 and height_1 >= 36:
#     print ('Welcome! Please be safe and enjoy the ride.')
# elif riders.lower() == 'yes' and (age_1 >=18 or age_2 >= 18) and height_1 >=36 and height_2 >= 36:
#     print ('Welcome! Please be safe and enjoy the ride. ')
# #  stretch 1
# elif riders.lower() == 'yes' and age_1 >=12 and age_2 >= 12 and height_1 >= 52 and height_2 >= 52:
#     print ('Welcome! Please be safe and enjoy the ride. ')
# #  stretch 3
# elif riders.lower() == 'yes' and ((age_1 >=16 and age_2 >= 14) or (age_1 >= 14 and age_2 >= 16)) and height_1 >= 36 and height_2 >=36:
#     print ('Welcome! Please be safe and enjoy the ride. ')
# else:
#     print ('Sorry, but you may not ride. ')























# # import math
# # print()
# # loan = float(input('On a scale of 1-10 please indicate how large the loan will be. 1 being the smallest and 10 the greatest: '))
# # credit_h = float(input('On a scale of 1-10 please indicate how good your credit history. 1 being the worst and 10 the best: '))
# # income = float(input('On a scale of 1-10 please indicate how much income you have. 1 being the smallest and 10 the greatest: '))
# # downpay = float(input('On a scale of 1-10 please indicate how much the downpayment will be. 1 being the smallest and 10 the greatest: '))


# # if loan >= 5:
# #     if credit_h >= 7 and income >= 7:
# #         decision = True
# #     elif (credit_h >= 7 or income >= 7) and downpay >= 5:
# #         decision = True
# #     else:
# #         decision = False
    
# #     if decision == True:
# #         print('Approved ')
# #     else:
# #         print('Not approved. ')
# # if loan < 5:
# #     if credit_h >= 4 and (income >= 7 or downpay >= 7):
# #         decision = True
# #     elif credit_h >= 4 and income >= 4 and downpay >= 4:
# #         decision = True
# #     else:
# #         decision = False
# #     if decision == True:
# #         print('Approved ')
# #     else:
# #         print('Not approved. ')












# # x = 6
# # y = 6

# # if x == 5:
# #     print("a")

# #     if y == 6:
# #         print("b")
# # else:
# #     print("c")

# #     if y == 10:
# #         print("d")





# # import math
# # print ()
# # int_1 = float(input('Please enter a number: '))
# # int_2 = float(input('Please enter another number: '))

# # if(int_1 > int_2 ):
# #     print ('The first number is greater.')
# # elif(int_1 <= int_2 ):
# #     print ('The first number is not greater.')
# # if(int_1 == int_2 ):
# #     print ('The numbers are equal.')
# # elif(int_1 != int_2 ):
# #     print ('The numbers are not equal.')
# # if(int_1 >= int_2 ):
# #     print ('The second number is not greater.')
# # elif(int_1 < int_2 ):
# #     print ('The second number is greater.')
# # print()
# # #  animal
# # animal = input('What is your favorite animal? ')
# # favorite = ('Fox')
# # if(animal.capitalize() == favorite):
# #     print ('That is my favorite animal as well.')
# # elif(animal != favorite):
# #     print ('That is not my favorite animal.')















# # # import math
# # # # v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
# # # # Title
# # # print ()
# # # print ('        Velocity Calculator        ')
# # # print ('-----------------------------------')

# # # # Variables
# # # m = float(input('Mass (in kg): '))
# # # g = float(input('Gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter): '))
# # # t = float(input('Time (in seconds): '))
# # # p = float(input('Density of fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
# # # A = float(input('Cross sectional area (in m^2): '))
# # # C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

# # # # calculations for the equation
# # # c = (1/2) * p * A * C
# # # # exp = the number e (2.71828) to the given exponent. This can be computed in Python with the Math library function math.exp(value).
# # # # sqrt = the square root of the given expression. This can be computed in Python with the Math library function math.sqrt(value).
# # # print ()
# # # print (f'The inner value of c is: {c:.3f}')
# # # # Main equation
# # # v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))
# # # print (f'The velocity after {t} seconds is: {v:.3f} m/s')
# # # print ()








# # # first_name = 'Seth'
# # # last_name = 'Bowles'

# # # print (first_name + ' ' + last_name)

# # # name = input ('enter name')
# # # output = ('seth')
# # # if name = ('seth')


# # # output = f'Hello, {first_name} {last_name}''
# # # output = 'Hello {1}, {0} '.format(first_name, last_name)
# # # output = f'Hello, {first_name} {last_name}'
# # # print (output)

# # # name1 = input ('enter name ')
# # # name2 = input ('enter last name ')


# # # name = input ('Please enter your password ')

# # # while (True):
# # # I need to have 'True' here instead of !=. the statement will always be true so it just needs to equal said if/elif functions. 
# #     # if(name == 'seth'):
# #         # print ('Welcome!')
# #         # break
# #     # elif(name != 'seth'):
# #         # name = input ('Please enter the correct password ')
# #     # else:
# #         # print('What?')
        
        
# # # num1 = input ('Please enter a number: ')
# # # num2 = input ('Please enter a second number: ')
# # # print (float(num1) + float(num2))

# # # pi = 3.14159
# # # print (pi)
# # # num1 = 5
# # # num2 = 6
# # # print (num1 + num2)

# # # print ('\n')
# # # age_num = int(input('How old are you? '))
# # # age2 = age_num + 1
# # # print (f'On your next birthday, you will be {age2}\n')
# # # egg_num = int(input('How many egg cartons do you have? '))
# # # egg2 = egg_num * 12
# # # print (f'You have {egg2} eggs\n')
# # # cookie_num = int(input('How many cookies do you have? '))
# # # people_num = int(input('How many people are there? '))
# # # cookie2 = cookie_num / people_num
# # # print (f'Each person may have {cookie2} cookies\n')



# # # doll = 5

# # # print ('there are' + doll + 'dolls')


# # # fahren = float(input('What is the temperature in Fahrenheit? '))
# # # celsius = (fahren - 32) * (5 / 9)
# # # 
# # # print (f'The temperature in Celsius is {round(celsius, 1)} degrees.')
# # # or {celsius:.1f}