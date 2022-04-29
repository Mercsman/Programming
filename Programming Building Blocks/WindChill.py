# WindChill
def windChill():
    speed = 0
    temp = float(input('What is the temperature? '))
    cf = input('Fahrenheit or Celsius (F/C)? ')
    if cf.lower() == 'c':
        temp = (temp * 1.8) + 32
    else:
        print('Please enter C or F')
    while speed != 60:
        speed = speed + 5
        wind = (35.74 + (0.6215 * temp) - (35.75 * (speed ** 0.16)) + ((0.4275 * temp) * (speed ** 0.16)))
        print(f'At temperature {temp:.1f}F, and wind speed of {speed} mph, the windchill is {wind:.2f}F')

windChill()