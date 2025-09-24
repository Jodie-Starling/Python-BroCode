age = int(input('Enter your age: '))
if age >= 100:
    print('You are too old to sign up!')
elif age >= 18:
    print('You are now signed up!')
elif age < 0:
    print('You have not been born yet!')
else:
    print('You must be 18+ to sign up.')



response = input('Do you want to have some food? (Y/N): ')
if response == 'Y':
    print('Here is some food!')
elif response == 'N':
    print('No food for you!')
else:
    print('Invalid input!')



for_sale = True
if for_sale:
    print('This item is for sale!')
else:
    print('This item is not for sale!')