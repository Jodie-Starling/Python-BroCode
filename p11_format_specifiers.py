# format specifiers = {value:flags} format a value based on
#                       what flags are inserted

price1 = 3.14159
price2 = -4923.454
price3 = 12.34

print(f'Price 1 is ${price1:.2f}') # 保留两位小数
print(f'Price 1 is ${price1:10}') # 总宽度为10，右对齐
print(f'Price 1 is ${price1:010}') # 总宽度为10，右对齐, 前面补零

print(f'Price 2 is ${price2:,.1f}') # 逗号作为千位分隔符

print(f'Price 3 is ${price3:0>10.2f}') # 数字前面补零，总宽度为10，保留两位小数

print(f'Price 1 is ${price1:<10}') # 左对齐, 总宽度为10
print(f'Price 1 is ${price1:>10}') # 右对齐, 总宽度为10
print(f'Price 1 is ${price1:^10}') # 居中, 总宽度为10

print(f'Price 1 is ${price1:=+10}') # 符号位在最前面
print(f'Price 1 is ${price1:+}') # 总是显示符号

print(f'Price 1 is ${price1: }') # 正数前面加空格，负数前面加负号
print(f'Price 2 is ${price2: }') 
print(f'Price 3 is ${price3: }')