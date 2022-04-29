import sys
import statistics

def mainMenu():
    while True:
        # Welcome message
        print('------------------------------------------------------------')
        print('Welcome to the online banking system!')
        # Options
        print('''Please select an option below:
        1. Add an account + balance
        2. Display accounts
        3. Remove an account + balance
        4. Total balance and Average
        5. Update balances
        6. Quit''')
        
        choice = input('Please select an option (1-6): ')
        # menu
        if choice == '1':
                addAccount()
        elif choice == '2':
                displayList()
        elif choice == '3':
                removeAccount()
        elif choice == '4':
                totalPrice()
        elif choice == '5':
                updateBalance()
        # exit
        elif choice == '6':
                print('\nThank you for banking with us!\n')
                sys.exit()
        else:
                print('Please select a valid option.')
# dict = 
accounts = []
total_balance = []
# option 1 add
def addAccount() :
    account = input('What is the name of this account? ')
    balance = float(input('What is the balance? $'))
    accounts.append(account)
    total_balance.append(balance)
    
# option 2 display
def displayList() :
    print()
    print('--- ACCOUNTS AND BALANCES ---')
    for count,i in enumerate(accounts,0):
        print(f'{str(count)}. {i.capitalize()} - ${total_balance[count]:.2f}')
        
# option 3 remove
def removeAccount() :
    item = input('What account would you like to remove? ')
    del accounts[int(item)]
    del total_balance[int(item)]
    print(item.capitalize() + ' has been removed.')
    
# option 4 price total
def totalPrice() :
    # total
    total_amount = sum(total_balance)
    print (f'Total: ${total_amount:.2f}')
    # average
    average = statistics.mean(total_balance)
    print (f'Average: ${average:.2f}')
    # largest balance
    largest = -1
    largest_name = None
    for i in range(len(accounts)):
        account = accounts[i]
        balance = total_balance[i]
        if balance > largest:
            largest = balance
            largest_name = account
    print(f'Highest balance: {largest_name.capitalize()}' + '---' + f'{largest:.2f}')
    
# Option 5 update
def updateBalance():
    update = int(input('Which account do you want to update? '))
    # del total_balance[int(update)]
    new_balance = float(input('What is the new balance? $'))
    total_balance[update] = new_balance
mainMenu()