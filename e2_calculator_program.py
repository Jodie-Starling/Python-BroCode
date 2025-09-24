operator = input('Enter an operator(+ - * /): ')
num1 = float(input('Enter the 1st number: '))
num2 = float(input('Enter the 2nd number: '))

if operator == '+':
    print(f'{num1}+{num2}={num1+num2}')
elif operator == '-':
    print(f'{num1}-{num2}={num1-num2}')
elif operator == '*':
    print(f'{num1}*{num2}={num1*num2}')
elif operator == '/':
    if num2 != 0:
        print(f'{num1}/{num2}={num1/num2}')
    else:
        print('Cannot divide by zero!')
else:
    print('Invalid operator!')