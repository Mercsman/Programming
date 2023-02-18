
# ch001
def ch001():
  name = input('Please enter your first name: ')
  print()
  print(f'Hello {name}')
  return name

# ch002
def ch002(first):
  last = input('Please enter your last name: ')
  print(f'\nHello {first} {last}\n')
  
# ch003
def ch003():
  print('What do you call a bear with no teeth?\n  A gummy bear!')

# ch004
def ch004():
  num_1 = float(input('Please \'enter\' a number: '))
  num_2 = float(input('Please enter a number: '))
  num_3 = num_1 + num_2
  print(f'The total is {num_3}')

# ch005
def ch005():
  num_1 = float(input('Please \'enter\' a number: '))
  num_2 = float(input('Please enter a number: '))
  num_3 = float(input('Please enter a number: '))
  num_4 = (num_1 + num_2) * num_3
  print(f'The total is {num_4:.2f}')

# ch006
def ch006():
  start = float(input('How many slices of pizza are you starting with? '))
  slices = float(input('How many slices of pizza have you eaten? '))
  leftover = start - slices
  print(f'There are {leftover} slices left.')

# ch007()
def ch007():
  name = input('Please enter your name: ')
  age = float(input('Please enter your age: '))
  new_age = age + 1
  print(f'{name}, next birthday you will be {new_age}.')
  
# ch008()
def ch008():
  total = float(input('Price of Bill (including tip): '))
  diners = int(input('How many (paying) diners? '))
  print(f'Each diner needs to contribute ${total / diners:.2f} for the meal.')
  # pass

# ch009()
def ch009():
  days = int(input('Enter a number of days: '))
  hours = days * 24
  minutes = hours * 60
  seconds = minutes * 60
  print(f'In {days} amount of days, there are {hours} hours, {minutes} minutes, and {seconds} seconds.')
  
# ch010()
def ch010():
  kilos = float(input('Enter a number of kilos: '))
  print(f'That is {kilos * 2.204} pounds')
  #pass
  
# ch011()
def ch011():
  x = int(input('Please enter a number over 100: '))
  y = int(input('Please enter a number under 10: '))
  a = x // y
  print(f'{y} goes into {x} {a} times.')
  # pass
  
# ch012
def ch012():
	num1 = float(input('Please enter a number: '))
	num2 = float(input('Please enter a number: '))
	
	if num1 > num2:
		print(f'{num2}, {num1}')
	else:
		print(f'{num1}, {num2}')
		
def ch013():
  num = float(input('Please enter a number under 20: '))
  if num >= 20:
    print('Too high, please choose a lower number.')
  else:
    print ('Thank you.')
    
def ch014():
  num = float(input('Please enter a number between 10 and 20: '))
  
  if num <= 20 and num >= 10:
    print('Thank you.')
  else:
    print('Error: Incorrect answer.')


def ch015():
  color = input('Please enter your favorite color: ')
  
  if color.capitalize() == 'Red':
    print('I like Red too.')
  else:
    print('I like Red better.')
    

def ch016():
  rain = input('Is it raining outside? (yes/no): ')
  
  if rain.lower() == 'yes':
    umb = input('Is it windy? (yes/no): ')
    if umb.lower() == 'yes':
      print('It is too windy for an umbrella. ')
    else:
      print('Take an umbrella.')
  else:
    print('Enjoy your day.')


def ch017():
  age = float(input('What is your age? '))
  
  if age >= 18:
    print('You can vote.')
  elif age == 17:
    print('You can learn to drive.')
  elif age == 16:
    print('You can buy a lottery ticket.')
  else:
    print('You can go trick-or-treating.')

def ch018():
  num = float(input('Please enter a number: '))
  
  if num > 20:
    print ('Error: Too high.')
  elif num >= 10 and num <= 20:
    print('Correct.')
  elif num < 10:
    print('Error: Too low.')


def ch019():
  num = float(input('Please enter 1, 2 or 3: '))
  
  if num == 1:
    print ('Thank you.')
  elif num == 2:
    print('Well done.')
  elif num == 3:
    print('Correct')
  else:
    print('Error: Please enter a valid option.')
    
def ch020():
  first = input('Please enter your first name: ')
  print (len(first))

def ch021():
  first = input('Please enter your first name: ')
  last = input('Please enter your last name: ')
  length = first+last
  print(f'{first} {last}')
  print (len(length))
  
def ch022():
  first = input('Please enter your first name in lower case: ')
  last = input('Please enter your last name in lower case: ')
  first_c = first.title()
  last_c = last.title()
  print(f'{first_c} {last_c}')

def ch023():
  rhyme = input('Please enter the first line of a nursery rhyme: ')
  print(len(rhyme))
  start = int(input('Please pick a starting number from the length above. (You can start at 0): '))
  end = int(input('Please pick a ending number from the length above: '))
  print(rhyme[start:end])

def ch024():
  word = input('Please enter a word: ')
  print(word.upper())
  
def ch025():
  first = input('Please enter your first name: ') 
  if len(first) < 5:
    last = input('Please enter your last name: ')
    print(f'{first.upper()}{last.upper()}')
  else:
    print(f'{first.lower()}')

def ch026():
  word = input('Please enter a word: ')
  first = word[0]
  length = len(word)
  pig = word[1:length]
  if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
    print(word + 'way')
  else:
    print(f'{pig}{first}ay')
    
def ch027():
  num = float(input('Please enter a number with multiple decimal places: '))
  num2 = num * 2
  print(num2)

def ch028():
  num = float(input('Please enter a number with multiple decimal places: '))
  num2 = num * 2
  print(f'{num2:.2f}')
  
def ch029():
  import math
  num = float(input('Please enter a number over 500: '))
  num2 = math.sqrt(num)
  print(f'{num2:.2f}')

def ch030():
  import math
  num = math.pi
  print(f'{num:.5f}')

def ch031():
  import math
  rad = float(input('Please enter a number: '))
  pi = math.pi
  area_c = pi * (rad ** 2)
  print(area_c)

def ch032():
  import math
  rad = float(input('Please enter a number: '))
  depth = float(input('Please enter a second number: '))
  pi = math.pi
  area_c = pi * (rad ** 2)
  cyl= area_c * depth
  print(f'{cyl:.3f}')

def ch033():
  import math
  num = float(input('Please enter a number: '))
  num2 = float(input('Please enter a second number: '))
  num3 = num // num2
  num4 = num % num2
  print(f'{num} divided by {num2} is {num3:.0f}, with {num4} remaining.')

def ch034():
  import math
  import sys
  print('''Welcome
  Please select an option:
  1) Square
  2) Triangle
  3) Exit''')
  while True:
    option = input('Please select an option (1/2/3): ')
    if option == '1':
      num = float(input('What is the length? '))
      area = num * num
      print(f'The area of this square is: {area}')
    elif option == '2':
      num = float(input('What is the length? '))
      area = (num * num) // 2
      print(f'The area of this triangle is: {area}')
    elif option == '3':
      sys.exit()
    else:
      print('Please select a valid option.')
      
def ch035():
  name = input('Please enter your name: ')
  for _ in range(3):
    print(name)
    
def ch036():
  name = input('Please enter your name: ')
  number = int(input('Please enter a number: '))
  for _ in range(number):
    print(name)
    
def ch037():
  name = input('Please enter your name: ')
  # for _ in name:
  for i in range(len(name)):
    print(name[i])
    # print(_)
    
def ch038():
  name = input('Please enter your name: ')
  number = int(input('Please enter a number: '))
  for _ in range(number):
    for i in range(len(name)):
      print(name[i])
      
def ch039():
  number = int(input('Please enter a whole number between 1 and 12: '))
  if number > 12 or number < 1:
    print('Please select a valid option between 1 and 12.')
  else:
    for _ in range(1):
      # print('[1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12]')
      print(f'[{1 * number}] [{2 * number}] [{3 * number}] [{4 * number}] [{5 * number}] [{6 * number}] [{7 * number}] [{8 * number}] [{9 * number}] [{10 * number}] [{11 * number}] [{12 * number}]')
    
def ch040():
  number = int(input('Please enter a whole number under 50: '))
  if number > 50:
    print('Please select a valid option under 50.')
  else:
    start = 50
    while start > number:
      print(start)
      start -= 1
    print(number)

# ch001()
# first = ch001()
# ch002(first)
# ch003()
# ch004()
# ch005()
# ch006()
# ch007()
# ch008()
# ch009()
# ch010()
# ch011()
# challenge set 2
# ch012()
# ch013()
# ch014()
# ch015()
# ch016()
# ch017()
# ch018()
# ch019()
# challenge set 3
# ch020()
# ch021()
# ch022()
# ch023()
# ch024()
# ch025()
# ch026()
# challenge set 4
# ch027()
# ch028()
# ch029()
# ch030()
# ch031()
# ch032()
# ch033()
# ch034()
# challenge set 5
# ch035()
# ch036()
# ch037()
# ch038()
# ch039()
ch040()
# ch041()
# ch042()
# ch043()
# ch044()
# challenge set 6
# ch045()
# ch046()
# ch047()
# ch048()
# ch049()
# ch050()
# ch051()