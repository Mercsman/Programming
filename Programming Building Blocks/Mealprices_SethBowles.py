# Meal prices
import math
# inputs
print ()
child = float(input("What is the price of a child's meal? $"))
adult = float(input("What is the price of a adult's meal? $"))
num_c = float(input('How many children are there? '))
num_a = float(input('How many adults are there? '))
tax = float(input('What is the sales tax rate? '))
military = input ('Is there a veteran? (Y/N) ') or 'no'
# Equations
sub = child * num_c + adult * num_a
sale = sub * (tax * 0.01 )
M_discount = sub * 0.05
while (True):
    if(military == 'yes'):
        total = sub + sale - M_discount
        print (f'Discount applied: ${M_discount}')
        break
    if(military != 'yes'):
        print ('No discount applied.')
        total = sub + sale
        break
    # total = sub + sale - M_discount
    
    
# totals
print (f'\nSubtotal: ${round(sub, 2)}')
print (f'Sales Tax: ${round(sale, 2)}')
print (f'Total: ${round(total, 2)}')

# payment
pay = float(input('What is the payment amount? $'))
change = pay - total
print (f'Change: ${round(change, 2)}')