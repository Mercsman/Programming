x = 0
count = 0
while x != 435:
    x = ((x + 1) + x)
    count = count + 1
print (f'damage {x}; draws {count}')





# WindChill
# speed = 5
# temp = float(input('What is the temperature? '))
# # wind = (35.74 + (0.621 * temp) - (35.75 * (speed ** 0.16)) + ((0.4275 * temp) * (speed ** 0.16)))
# # print((f'{wind:.2f}'))
# wind = ''
# # while True:
#     # print(f'At temperature {temp}F, and wind speed 5 mph, the windchill is: -1.11F')
    
# # Celsius to Fahrenheit converter
# def converter(temp):
#     cf = input('Fahrenheit or Celsius (F/C)? ')
#     if cf.lower() == 'c':
#         temp = (temp * 1.8) + 32
#     else:
#         print('Please enter C or F')
#     return temp
# #  Wind Chill
# def windChill(wind):
#     # speed = 5
#     # temp = float(input('What is the temperature? '))
#     wind = (35.74 + (0.621 * temp) - (35.75 * (speed ** 0.16)) + ((0.4275 * temp) * (speed ** 0.16)))
#     return wind
#     # print((f'{wind:.2f}'))

# def windSpeed(speed):
#     speed = 5
#     # for x in range (5,60):
#     #     x = 5
#     #     x += 5
#     while speed != 60:
#         speed = speed + 5
#         # print(f'At temperature {temp:.1f}F, and wind speed of {speed} mph, the windchill is {wind:.2f}F')
#         return speed
# converter(temp)

# windChill(wind)

# windSpeed(speed)

# print(f'At temperature {temp:.1f}F, and wind speed of {speed} mph, the windchill is {wind}F')

# import math
# import sys

# def mainMenu():
#     while True:
#         # Welcome message
#         print('------------------------------------------------------------')
#         print('Area computer')
#         # Options
#         print('''Please select an option below:
#         1. Square
#         2. Rectangle
#         3. Circle
#         4. Area
#         5. Quit''')
        
#         choice = input('Please select an option (1-5): ')
#         # menu
#         if choice == '1':
#             square_side = float(input('What is the length of the side of the square? '))
#             area = rectangleArea(square_side, square_side)
#             print (f'The area of the square is: {area}')
#         elif choice == '2':
#             r_width = float(input('What is the width of the rectangle? '))
#             r_length = float(input('What is the length of the rectangle? '))
#             area = rectangleArea(r_length, r_width)
#             print (f'The area of the square is: {area}')
#         elif choice == '3':
#             radius = float(input('What is the radius of the circle? '))
#             area = circleArea(radius)
#             print (f'The area of the square is: {area:.2f}')
#         elif choice == '4':
#             a = float(input('What is the number for the area? '))
#             b = float(input('What is the second number for the area? '))
#             area = computeArea(shape, a, b)
#             print (f'The area of the square is: {area:.2f}')
#         # exit
#         elif choice == '5':
#             print('\nThank you\n')
#             sys.exit()
#         else:
#             print('Please select a valid option.')

# # area of the square
# def squareArea(square_side):
#     # area = (square_side * square_side)
#     return square_side * square_side
#     # print (f'The area of the square is: {area}')

# # area of a rectangle
# def rectangleArea(r_length, r_width):
#     # area = r_width * r_length
#     return r_width * r_length
#     # print (f'The area of the rectangle is: {area}')

# # area of a circle
# def circleArea(radius):
#     # area = (radius ** 2) * math.pi
#     return (radius ** 2) * math.pi
#     # print (f'The area of the circle is: {area}')
    
# def computeArea(shape, a, b=False):
#     shape = input('What shape do you have? ').lower()
#     if shape == 'square':
#         return a * a
#         # side = float(input('What is the length of the side? '))
#         # area = computeArea(shape, (side * side), False)
#     elif shape == 'rectangle':
#         return a * b
#         # width = float(input('What is the width of the rectangle? '))
#         # length = float(input('What is the length of the rectangle? '))
#         # area = computeArea(shape, width, length=True)
#     elif shape == 'circle':
#         return (a**2) * math.pi
#     else:
#         print('Not a valid option.')
# # square_side = float(input('What is the length of the side of the square? '))
# # r_width = float(input('What is the width of the rectangle? '))
# # r_length = float(input('What is the length of the rectangle? '))
# # radius = float(input('What is the radius of the circle? '))

# # def computeArea(shape, ):
# shape = ''
# mainMenu()






# string = input('What would you like to input? ')

# def displayRegular():
#     print (string)
#     print (string.upper())
#     print (string.lower())
    
# displayRegular()


# largest_chapter = 0
# largest_book = ''

# with open("books_and_chapters.txt") as books_file:

#     for line in books_file:
#         parts = line.split(":")
#         book = parts[0].strip()
#         chapters = int(parts[1])
#         scripture = parts[2].strip()

#         print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")
#         if chapters > max_chapters:
#             max_chapters = chapters
#             book_with_max = book
# print(f"The book with the most chapters is: {book_with_max}")
# print(f"It has {max_chapters} chapters.")



# people = [
#     "Stephanie 36",
#     "John 29",
#     "Emily 24",
#     "Gretchen 54",
#     "Noah 12",
#     "Penelope 32",
#     "Michael 2",
#     "Jacob 10"
# ]
# youngest = 200
# poi = ''
# for line in people:
# 	part = line.split()
# 	person = part[0]
# 	age = int(part[1])
# 	if age < youngest:
# 		youngest = age
# 		poi = person
# # print (person, age)
# print (f'The youngest person is: {poi} at age {youngest}.')










# import statistics
# import math
# import sys
# import itertools
# print('--------------------------------------------------------------------------')
# print('----------------------CHOICES---------------------------------------------')
# # special year
# chosen_year = int(input('Please enter the year of interest: '))
# chosen_country = input('Please enter the country of interest: ')
# max_life = 0
# min_life = 999
# chosen_max_life = 0
# chosen_min_life = 999
# chosen_max_life2 = 0
# chosen_min_life2 = 999
# life_list = []
# life_list2 = []
# drop = 0
# drop_country_list = []
# drop_year_list =[]
# drop_life_list = []
# def skipLine(drop_life_list, skip):
# 	lines = drop_life_list.readlines()
# 	skip = skip - 1 #index of the list starts from 0

# 	for line_no, line in enumerate(lines):
# 		if line_no==skip:
# 			pass
# 		else:
# 			print(line, end="")
# # country_bit = False # or 0
# # country_index = 0
# # drop_list = []
# # drop = 0
# # drop_items = {} ## ??
# # max_drop = 0
# with open('life-expectancy.csv') as spanish_flu:
# # skip line 1
#     next(spanish_flu)
#     # identify parts
#     for line in spanish_flu:
#         line = line.strip()
#         parts = line.split(',')
#         country = parts[0]
#         code = parts[1]
#         year = int(parts[2])
#         life = float(parts[3])
#         # max/min
#         if life > max_life:
#             max_life = life
#             max_country = country
#             max_year = year
#         elif life < min_life:
#             min_life = life
#             min_country = country
#             min_year = year
#         # interest year
#         if year == chosen_year:
#             life_list.append(life)
#             if life > chosen_max_life:
#                 chosen_max_life = life
#                 chosen_max_country = country
#             elif life < chosen_min_life:
#                 chosen_min_life = life
#                 chosen_min_country = country
#         # interest country
#         if country.strip() == chosen_country.capitalize():
#             life_list2.append(life)
#             if life > chosen_max_life2:
#                 chosen_max_life2 = life
#                 # chosen_max_country2 = country
#             if life < chosen_min_life2:
#                 chosen_min_life2 = life
#                 # chosen_min_country2 = country
#     average = statistics.mean(life_list)
#     average2 = statistics.mean(life_list2)
# with open('life-expectancy.csv') as spanish_flu:
# # skip line 1
#     next(spanish_flu)
#     mega_drop = spanish_flu.readline()[2:]
#     for line in spanish_flu:
#         line = line.strip()
#         part = line.split(',')
#         drop_country = part[0]
#         drop_year = part[2]
#         drop_life = part[3]
#         # dropdrop = drop_life.readlines()[2:]
    
#         drop_country_list.append(part[0])
#         drop_year_list.append(part[2])
#         drop_life_list.append(part[3])
#         for line in itertools.islice(spanish_flu,3,None):
#             port = line.split(',')
#             dropdrop = port[3]
#         if drop_country.strip() == drop_country.strip():			
#             drop_max = (float(drop_life) - float(dropdrop))
#             if drop_max > drop:
#                 drop = drop_max
#                 print(f'{drop_max}')
# # with open('life-expectancy.csv') as spanish_flu:
# #     for line2 in spanish_flu:
# #         line2 = line2.strip()
# #         part2 = line2.split(',')
# #         country2 = part2[0]
# #         year2 = int(part2[2])
# #         life2 = float(part2[3])
# #     # Get current variables
# #         current_country = country2
# #         current_year = year2
# #         current_life = life2
# #     # set up a new country check
# #         if country_bit == False:    
# #             previous_country = country2 
# #             previous_year = year2
# #             previous_life = life2
# #             previous_drop = 0
# #             country_bit = True
# #             country_index
# #             continue

# #         if current_country != previous_country:
# #             drop_list.append(drop)
# #             country_index = 0
# #             previous_country = country2    
# #             previous_year = year2
# #             previous_life = life2
# #             continue
# #         else:
# #             current_drop = previous_life - current_life
# #             if current_drop > previous_drop:
# #                 max_drop = current_drop
# print(drop_max)
# # print(max_drop)






# print('--------------------------------------------------------------------------')
# print('----------------------SPECIFIC YEAR---------------------------------------')
# print(f'For the year {chosen_year}:')
# print(f'The average life expectancy across all countries was {average:.2f}')
# print(f'The max life expectancy was in {chosen_max_country.strip()} with {chosen_max_life}')
# print(f'The min life expectancy was in {chosen_min_country.strip()} with {chosen_min_life}')
# print('--------------------------------------------------------------------------')
# print('----------------------SPECIFIC COUNTRY------------------------------------')
# print(f'For the country {chosen_country.strip().capitalize()}:')
# print(f'The average life expectancy across {chosen_country.capitalize()} {average2:.2f}')
# print(f'The max life expectancy in {chosen_country.strip().capitalize()} was {chosen_max_life2}')
# print(f'The min life expectancy in {chosen_country.strip().capitalize()} was {chosen_min_life2:.2f}')
# print('--------------------------------------------------------------------------')
# print(f'The overall max life expectancy is: {max_life} from {max_country.strip()} in {max_year}')
# print(f'The overall min life expectancy is: {min_life} from {min_country.strip()} in {min_year}')
# print('--------------------------------------------------------------------------')
