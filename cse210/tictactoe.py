# Author and title
# Seth Bowles, Tic-Tac-Toe
from array import array
import sys
import random
# Main function
def main():
    # Welcome message
    print('Welcome to Tic-Tac-Toe!')
    # Menu Loop
    while True:
        print('''Menu:
        (1) Start:
        (2) Credits:
        (3) Exit:''')
        menu = input('Please select an option (1,2,3): ')
        if menu == '1':
            game()
        elif menu =='2':
            print('This game was created by Seth Bowles')
            print('Current Version 1.4')
        elif menu == '3':
            sys.exit()
        else:
            print('Please select a valid option (1,2,3): ')

def game():
    # Who goes first coinflip
    player1 = coinflip()
    if player1 == 1:
        p1 = 'X'
        p2 = 'O'
        print('X goes first')
    else:
        p1 = 'O'
        p2 = 'X'
        print('O goes first')
    # array for board
    array = [0,1,2,3,4,5,6,7,8,9]
    # print('''
    # 1 | 2 | 3
    # --+---+--
    # 4 | 5 | 6
    # --+---+--
    # 7 | 8 | 9
    # ''')
    # print board
    print(
    '',array[1],'|',array[2],'|',array[3],
    '\n---+---+---\n',
    array[4],'|',array[5],'|',array[6],
    '\n---+---+---\n',
    array[7],'|',array[8],'|',array[9]
    )
    # loop intro
    # print(f'{p1} goes first, please select a square [1-9]: ')
    counter = 0
    # loop start
    while counter <= 10:
    # victory checker
        if array[1] == array[2] == array[3] or array[1] == array[4] == array[7] or array[1] == array[5] == array[9] or array[3] == array[6] == array[9] or array[3] == array[5] == array[7] or array[2] == array[5] == array[8] or array[4] == array[5] == array[6] or array[7] == array[8] == array[9]:
            if not counter % 2 == 0:
                print(f'{p1} Victory!')
                # break
            else:
                print(f'{p2} Victory!')
                # break
            break
        elif counter % 2 == 0:
            grid = int(input(f"{p1}'s turn, please select a square [1-9]: "))
            array[grid] = p1
            print(
            '',array[1],'|',array[2],'|',array[3],
            '\n---+---+---\n',
            array[4],'|',array[5],'|',array[6],
            '\n---+---+---\n',
            array[7],'|',array[8],'|',array[9]
            )
        else:
            grid = int(input(f"{p2}'s turn, please select a square [1-9]: "))
            array[grid] = p2
            print(
            '',array[1],'|',array[2],'|',array[3],
            '\n---+---+---\n',
            array[4],'|',array[5],'|',array[6],
            '\n---+---+---\n',
            array[7],'|',array[8],'|',array[9]
            )
        counter += 1
        
    
    # user_number = input("Player one's turn, please select a square [1-9]: ")
    # user_number2 = input("Player two's turn, please select a square [1-9]: ")
    # if array[0] == array[1] == array[2]:
        # print('Victory')
    

def coinflip():
    coin = [1,2]
    flip = random.choice(coin)
    return flip




if __name__ == "__main__":
    main()