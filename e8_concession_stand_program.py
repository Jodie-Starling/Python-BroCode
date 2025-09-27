menu = {'pizza': 3.00,
        'soda': 1.50,
        'salad': 2.50,
        'hot dog': 2.00,
        'fries': 1.75,
        'chips': 1.25}

cart = []
total = 0.0

print('-----MENU-----')

for key, value in menu.items():
    print(f'{key}: ${value:.2f}')   # 序列解包

print('--------------')

while True:
    food = input('Select an item (q to quit): ').lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu[food]

print('---YOUR CART---')
for item in cart:
    print(f'{item}: ${menu[item]:.2f}')
print(f'Total: ${total:.2f}')
print('---------------')