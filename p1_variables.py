#a variable is a container for a value
#str int float boolean

first_name = 'Jodie' #单引双引都可
last_name = 'Starling'
full_name = first_name + ' ' + last_name

print(type(full_name))
print('hello, ' + full_name)

print(f'hello,{full_name}')

food = 'pizza'
print(f'I love to eat {food}')

age = 18
age += 1

print(type(age))
print('your age is: ' + str(age))

height = 250.5

print(type(height))
print(f'your height is: {height}cm')

human = True # or False, should be capitalized

print(type(human))
print(f'are you a human: {human}')
if human:
    print('you are a human')
else:
    print('you are NOT a human')



#Multiple assignment to write the same thing using one line of code

name, age, height, human = 'Jodie', 18, 250.5, True

print(name)
print(age)
print(height)
print(human)



#multiple assignment to assign the same value to multiple variables

a = b = c = 10

print(a)
print(b)   
print(c)

email = 'angel_shxy@qq.com'
print(f'my email is {email}')

