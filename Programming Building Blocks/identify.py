print ('Please enter the following information:\n\n')

first = input ('First name: ')
last = input ('Last name: ')
email = input ('Email address: ')
phone = input ('Phone number: ')
job = input ('Job title: ')
id = input ('ID Number: ')
hair = input ('Hair color: ')
eye = input ('Eye color: ')
month = input ('Start month: ')
train = input ('Completed training y/n?: ')

print (f'\nThe ID card is:\n-------------------------------------\n{last.upper()}, {first}\n{job.title()}\nID: {id}\n\n{email.lower()}\n{phone}\n\n')
# Everything on one line for simplicity maybe?
print (f'Hair: {hair.capitalize():15} Eyes: {eye.capitalize()}\nMonth: {month.capitalize():14} Training: {train.capitalize()}\n-------------------------------------')