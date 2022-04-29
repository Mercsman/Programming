import math
print()
grade = float(input('What is the grade percentage? '))
if(grade >= 90):
    letter = 'A'
elif(grade >= 80):
    letter = 'B'
elif(grade >= 70):
    letter = 'C'
elif(grade >= 60):
    letter = 'D'
elif(grade < 60):
    letter = 'F'
    
    # Stretch 1
modifier = ''
int_mod = grade % 10

if int_mod >= 7:
    modifier = '+'
elif int_mod < 3:
    modifier = '-'
else:
    modifier = ''
    
# stretch 2
    
if grade >= 93:
    modifier = ''

# stretch 3

if letter == 'F':
    modifier = ''
    
print(f'This assignment received an {letter}{modifier}.')
# pass or no pass
if(grade >= 70):
    print ('This assignment passed, congratulations!')
elif(grade < 70):
    print ('This assignment did not pass. Keep trying and you will get it next time!')

