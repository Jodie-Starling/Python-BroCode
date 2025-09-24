weight = float(input('Enter your weight: '))
unit = input('Kilograms or Pounds? (K/P): ')

if unit == 'K':
    weight = weight * 2.205
    print(f'You are {round(weight,1)} pounds.')
elif unit == 'P':
    weight = weight / 2.205
    print(f'You are {round(weight,1)} kilograms.')
else:
    print('Invalid unit')
    exit()  #在您当前的代码中，exit() 是可选的，因为程序已经到达末尾。但使用它是一个好习惯，明确表示程序因错误而终止。