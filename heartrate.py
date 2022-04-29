"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

print()
print('Welcome to the heart rate test!\n---------------------------------')
age = input('Please enter your age: ')
age = int(age)
max = 220 - age
slow_goal = max * 0.65
fast_goal = max * 0.85

print(f'When you exercise, to best strengthen your heart you should keep your heart rate between {slow_goal:.0f} and {fast_goal:.0f} beats per minute.')
print()