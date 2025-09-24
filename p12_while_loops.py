name = input('Enter your name: ')

while name == '':
    print('You did not enter your name!')
    name = input('Enter your name(-1 to quit): ')
    if name == '-1':
       print('Bye!')
       exit()

print(f'Hello {name}!')