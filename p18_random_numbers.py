import random

print(dir(random))
print(help(random))


options = ['rock', 'paper', 'scissors']
option = random.choice(options)

print(option)


cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(cards) # 洗牌

print(cards)


number = random.randint(1, 6)
number = random.random() # 0.0 to 1.0(not including 1.0) 随机浮点数

print(number)