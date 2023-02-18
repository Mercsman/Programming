
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
ch011()
# challenge set 2
# ch012()
# ch013()
# ch014()
