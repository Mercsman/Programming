# with open('books.txt') as books:
# 	for line in books:
# 		line = line.strip()
# 		print(line)



# with open('test.txt') as test_file:
# 	for line in test_file:
# 		line = line.strip()
# 		parts = line.split(' ')
# 		rank = parts[0]
# 		percent = float(parts[1])


# 		print(f'{rank} - how close to next rank? {percent}')
# print ('Complete')










# colors = 'red, blue, green, yellow'

# color_parts = colors.split(', ')

# print(colors)
# print(color_parts)

# second = color_parts[1]

# print(second)











# import sys

# def mainMenu():
#     while True:
#         # Welcome message
#         print('------------------------------------------------------------')
#         print('Welcome to the online shopping cart!')
#         # Options
#         print('''Please select an option below:
#         1. Add item
#         2. View cart
#         3. Remove item
#         4. Change item
#         5. Quit''')
        
#         choice = input('Please select an option (1-5): ')
#         # menu
#         if choice == '1':
#                 addItem()
#         elif choice == '2':
#                 displayList()
#         elif choice == '3':
#                 removeItem()
#         elif choice == '4':
#                 changeItem()
#                 # totalPrice()
#         # exit
#         elif choice == '5':
#                 print('\nThank you for shopping with us!\n')
#                 print('\nThe shopping list with Indexes is:')
#                 for i in range(len(cart)):
#                         item = cart[i]
#                         print(f'{i}. {item}')
#                 sys.exit()
#         else:
#                 print('Please select a valid option.')
# # dict = 
# cart = []
# # total = []
# # total_amount = 0
# # option 1 add
# def addItem() :
#     item = input('What item would you like to add to your cart? ')
# #     price = float(input('What is the price of the item? $'))
#     cart.append(item)
# #     total.append(price)
#     print(item.capitalize() + ' has been added to your cart.')
# # option 2 display
# def displayList() :
#     print()
#     print('--- ITEMS IN YOUR CART ---')
#     for count,i in enumerate(cart,0):
#         # print('•' + i + f' {x}')
#         # print(count + '. ' + i  + ' -')
#         print(f'{str(count)}. {i.capitalize()}')
#         # for x in total:
#                 # print('•' + i + f' {x}')
# # option 3 remove
# def removeItem() :
# #  item -1 = input
#     item = input('What item would you like to remove to your cart? ')
#     # price = float(input('How much did the item cost? $'))
#     del cart[int(item)] # cart.remove(item) # del cart[item - 1]
#     #del total[int(item)] # total.remove(price)  # del total[item - 1]
#     print(item.capitalize() + ' has been removed from your cart.')
# # option 4 price total
# # def totalPrice() :
# def changeItem():
#         index = int(input('What item would you like to change? '))
#         new_item = input('What is the new item? ')
#         cart[index] = new_item
# #     total_amount = sum(total)
# #     print ('--- YOUR TOTAL IS ---')
# #     print (f'${total_amount:.2f}')
#     # for i in range (0, len(total)):
#         # total_amount = total_amount + total[i]
#     # total_amount = 0
#     # total_amount = sum(total)
#     # for x in range(0, len(total)):
#         # total_amount = total_amount + total[x]
# mainMenu()














# import math


# numbers = []

# number = None
# total = 0
# largest = -1
# smallest = 9999999999
# while number != 0:
        # number = int(input('Please enter a number: '))
        
        # if number != 0:
                # numbers.append(number)
        # else:
                # number = int(input('Please enter a number: '))
# total


# for number in numbers:
        # total += number
        # if number > largest:
                # largest = number
        # if number > 0 and number < smallest:
                # smallest = number
# average
# count = len(numbers)
# average = total / count

# largest number

        
# smallest number


# for number in numbers:
#         if number > 0 and number < smallest:
#                 smallest = number

# sort = numbers.sort()
# sort =sorted(numbers)
# print (f'The total is: {total:.2f}')
# print (f'The average is: {average:.2f}')
# print (f'The largest number is: {largest:.2f}')
# print (f'The smallest positive number is: {smallest:.2f}')
# print(numbers.sort())
# print(sort)





















# name = []

# friend = None

# while friend != 'End':
#         friend = input('Please enter the name of a friend: ')
#         friend = friend.capitalize()
#         if friend != 'End':
#                 name.append(friend)
                
# print()
# print ('Your friends are:')



# for friends in name:
#         print(friends)














# import re
# import math
# from PIL import Image
# print()
# image_cat = Image.open('cat.jpg')
# image_forest = Image.open('forest.jpg')

# pixels_cat = image_cat.load()
# pixels_forest = image_forest.load()
# c_width, c_height = image_cat.size
# # print(image_cat.size)
# # print(image_forest.size)

# perc = 0

# for y in range(0, c_height):
#     for x in range(0, c_width):
#         perc += 1;
#         perc_left = f'{((perc / (c_height * c_width)) * 100):.2f}'
#         perc_left = (perc / (c_height * c_width)) * 100
#         (r, g, b) = pixels_cat[x, y]
#         # (r, g, b) = pixels_forest[x, y]
#         if (r, b, g) >= (r, b, 215):
#                 # pixels_cat[x, y] = pixels_forest[x, y]
#                 # r, g, b = pixels_forest
#                 # pixels_cat[x, y] = pixels_forest[x, y]
#                 pixels_cat[x, y] = pixels_forest[x, y]
#         # (r, g, b) = pixels_forest[x, y]
#                 print(f'forest RGB: {r:>3}, {g:>3}, {b:>3};                                                    ------------------ % remaining:{perc_left:>6.2f}% ------------------.\r', end = '')

# print ()
# image_cat.show()















# import math

# user = int(input('How many rows and columns do you want to have? '))
# max = user * user

# digits = int(math.log10(max)) + 1

# for rows in range(1, user+1):
#         for columns in range (1, user+1):
#                 num = rows * columns
#                 # if num >= 100:
#                 #         print (f'{num:3}', end='')
#                 # else:
#                 #         print (f'{num:2}', end='')
#                 print (f'{num:{digits}}', end=' ')
#         print ()