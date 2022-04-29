# Teamproject5
import random


play = 'yes'
while play.lower() == 'yes':
    number = random.randint(1, 100)
# print (number)
    guess = 0
    chances = 0
    while guess != number:
        guess = int(input('What is the magic number? '))
        chances += 1
        if guess > number:
            print ('Lower')
        elif guess < number:
            print ('Higher')
    # elif guess == number:
    print ('Correct!')
    print (f'It took you {chances} tries to guess it right. ')
        # guess = int(input('What is the magic number? '))
    # else:
    #     print ('Error')
    play = input('Do you want to play again? (yes/no). ')
print ('Thanks for playing!')
