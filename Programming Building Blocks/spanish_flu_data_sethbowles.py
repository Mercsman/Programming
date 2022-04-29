import statistics
import math
import sys
import itertools
print('--------------------------------------------------------------------------')
print('----------------------CHOICES---------------------------------------------')
# special year
chosen_year = int(input('Please enter the year of interest: '))
chosen_country = input('Please enter the country of interest: ')
max_life = 0
min_life = 999
chosen_max_life = 0
chosen_min_life = 999
chosen_max_life2 = 0
chosen_min_life2 = 999
life_list = []
life_list2 = []
drop = 0
drop_country_list = []
drop_year_list =[]
drop_life_list = []
dropdropcountry = ''
dropdropyear = 0
def skipLine(drop_life_list, skip):
	lines = drop_life_list.readlines()
	skip = skip - 1 #index of the list starts from 0

	for line_no, line in enumerate(lines):
		if line_no==skip:
			pass
		else:
			print(line, end="")
# country_bit = False # or 0
# country_index = 0
# drop_list = []
# drop = 0
# drop_items = {} ## ??
# max_drop = 0
with open('life-expectancy.csv') as spanish_flu:
# skip line 1
    next(spanish_flu)
    # identify parts
    for line in spanish_flu:
        line = line.strip()
        parts = line.split(',')
        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life = float(parts[3])
        # max/min
        if life > max_life:
            max_life = life
            max_country = country
            max_year = year
        elif life < min_life:
            min_life = life
            min_country = country
            min_year = year
        # interest year
        if year == chosen_year:
            life_list.append(life)
            if life > chosen_max_life:
                chosen_max_life = life
                chosen_max_country = country
            elif life < chosen_min_life:
                chosen_min_life = life
                chosen_min_country = country
        # interest country
        if country.strip() == chosen_country.capitalize():
            life_list2.append(life)
            if life > chosen_max_life2:
                chosen_max_life2 = life
                # chosen_max_country2 = country
            if life < chosen_min_life2:
                chosen_min_life2 = life
                # chosen_min_country2 = country
    average = statistics.mean(life_list)
    average2 = statistics.mean(life_list2)
# with open('life-expectancy.csv') as spanish_flu:
# # skip line 1
#     next(spanish_flu)
#     mega_drop = spanish_flu.readline()[2:]
#     for line in spanish_flu:
#         line = line.strip()
#         part = line.split(',')
#         drop_country = part[0]
#         drop_year = part[2]
#         drop_life = part[3]
#         # dropdrop = drop_life.readlines()[2:]
    
#         drop_country_list.append(part[0])
#         drop_year_list.append(part[2])
#         drop_life_list.append(part[3])
#         for line in itertools.islice(spanish_flu,3,None):
#             port = line.split(',')
#             dropdrop = port[3]
#             if drop_country.strip() == drop_country.strip():			
#                 drop_max = (float(dropdrop) - float(drop_life))
#                 if drop_max > drop:
#                     drop = drop_max
#                     dropdropcountry = drop_country
#                     dropdropyear = drop_year
                # print(f'{drop_max}')

# print(drop_max)

print('--------------------------------------------------------------------------')
print('----------------------SPECIFIC YEAR---------------------------------------')
print(f'For the year {chosen_year}:')
print(f'The average life expectancy across all countries was {average:.2f}')
print(f'The max life expectancy was in {chosen_max_country.strip()} with {chosen_max_life}')
print(f'The min life expectancy was in {chosen_min_country.strip()} with {chosen_min_life}')
print('--------------------------------------------------------------------------')
print('----------------------SPECIFIC COUNTRY------------------------------------')
print(f'For the country {chosen_country.strip().capitalize()}:')
print(f'The average life expectancy across {chosen_country.capitalize()} {average2:.2f}')
print(f'The max life expectancy in {chosen_country.strip().capitalize()} was {chosen_max_life2}')
print(f'The min life expectancy in {chosen_country.strip().capitalize()} was {chosen_min_life2:.2f}')
print('--------------------------------------------------------------------------')
print('----------------------OVERALL---------------------------------------------')
print(f'The overall max life expectancy is: {max_life} from {max_country.strip()} in {max_year}')
print(f'The overall min life expectancy is: {min_life} from {min_country.strip()} in {min_year}')
# print(f'The year and Country with the greatest drop in life expectancy was: {dropdropcountry.strip()} in {dropdropyear.strip()} with a life expectancy drop of {drop_max}')
print('--------------------------------------------------------------------------')
