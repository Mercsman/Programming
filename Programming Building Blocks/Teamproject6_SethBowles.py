import math


numbers = []

number = None
total = 0
largest = -1
smallest = 9999999999
while number != 0:
        number = int(input('Please enter a number: '))
        
        if number != 0:
                numbers.append(number)
        # else:
                # number = int(input('Please enter a number: '))
# total


for number in numbers:
        total += number
        if number > largest:
                largest = number
        if number > 0 and number < smallest:
                smallest = number
# average
count = len(numbers)
average = total / count

# largest number

        
# smallest number


# for number in numbers:
#         if number > 0 and number < smallest:
#                 smallest = number

# sort = numbers.sort()
sort =sorted(numbers)
print (f'The total is: {total:.2f}')
print (f'The average is: {average:.2f}')
print (f'The largest number is: {largest:.2f}')
print (f'The smallest positive number is: {smallest:.2f}')
# print(numbers.sort())
print(sort)