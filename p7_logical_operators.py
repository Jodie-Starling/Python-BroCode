# or and not 
temp = int(input('Enter the temperature: '))
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print('The event is cancelled.')
else:
    print('The event is still scheduled.')
