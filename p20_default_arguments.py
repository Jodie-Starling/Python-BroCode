# 默认参数必须在非默认参数之后
# 默认参数不能是可变对象

def net_price(list_price, discount=0.0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(100))

import time

def cout(start=0, end=10):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)
    print("Done!")

cout(5, 10)