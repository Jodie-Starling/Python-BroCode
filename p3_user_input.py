#input() always returns a string

name = input("Enter your name: ")
age = int(input('Enter your age: '))
height = float(input('Enter your height(cm): '))

print('hello '+name)
print('your are ' + str(age)+' years old')
print('you are '+str(height)+' cm tall')

full_name = input('What\'s your full name? ')

print(f'hello,{full_name}')
print('HAPPY BIRTHDAY')