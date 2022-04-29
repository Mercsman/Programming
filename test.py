import sys
def mainMenu():
    while True:
        # Welcome message
        print('------------------------------------------------------------')
        print('Welcome to the online shopping cart!')
        # Options
        print('''Please select an option below:
        1. Add item
        2. View cart
        3. Remove item
        4. Compute total
        5. Quit''')
        
        choice = input('Please select an option (1-5): ')
        # menu
        if choice == '1':
                addItem()
        elif choice == '2':
                displayList()
        elif choice == '3':
                removeItem()
        elif choice == '4':
                totalPrice()
        # exit
        elif choice == '5':
                print('\nThank you for shopping with us!\n')
                sys.exit()
        else:
                print('Please select a valid option.')
# dict = 
cart = []
total = []
total_amount = 0
# option 1 add
def addItem() :
    item = input('What item would you like to add to your cart? ')
    price = float(input('What is the price of the item? $'))
    cart.append(item)
    total.append(price)
    print(item.capitalize() + ' has been added to your cart.')
# option 2 display
def displayList() :
    print()
    print('--- ITEMS IN YOUR CART ---')
    for count,i in enumerate(cart,1):
        # print('•' + i + f' {x}')
        # print(count + '. ' + i  + ' -')
        print(f'{str(count)}. {i.capitalize()} - ${total[count-1]:.2f}')
        # for x in total:
                # print('•' + i + f' {x}')
# option 3 remove
def removeItem() :
#  item -1 = input
    item = input('What item would you like to remove to your cart? ')
    # price = float(input('How much did the item cost? $'))
    del cart[int(item) - 1] # cart.remove(item) # del cart[item - 1]
    del total[int(item) - 1] # total.remove(price)  # del total[item - 1]
    print(item.capitalize() + ' has been removed from your cart.')
# option 4 price total
def totalPrice() :
    total_amount = sum(total)
    print ('--- YOUR TOTAL IS ---')
    print (f'${total_amount:.2f}')
mainMenu()

























# a = 1
# b = 3
# c = -2
# result = a + b * 7 % 4 - c


# print (result)


# """
# When you physically exercise to strengthen your heart, you
# should maintain your heart rate within a range for at least 20
# minutes. To find that range, subtract your age from 220. This
# difference is your maximum heart rate per minute. Your heart
# simply will not beat faster than this maximum (220 - age).
# When exercising to strengthen your heart, you should keep your
# heart rate between 65% and 85% of your heart's maximum rate.
# """

# print()
# print('Welcome to the heart rate test!\n---------------------------------')
# age = input('Please enter your age: ')
# age = int(age)
# max = 220 - age
# slow_goal = max * 0.65
# fast_goal = max * 0.85

# print(f'When you exercise, to best strengthen your heart you should keep your heart rate between {slow_goal} and {fast_goal} beats per minute.')
# print()