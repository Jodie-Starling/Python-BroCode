# help(str) #查看字符串的内置方法

name = 'Jodie Starling'


print(len(name))

print(name.find('o')) #查找字符首次出现的位置，没有结果返回-1
print(name.rfind('o')) #查找字符最后一次出现的位置,没有结果返回-1

print(name.capitalize()) #首字母大写
print(name.upper())
print(name.lower())

print(name.isdigit()) #是否只包含数字字符
print(name.isalpha()) #是否只包含字母字符

print(name.count('i')) #统计某个字符出现的次数

print(name.replace('o', '0')) #替换字符

print(name*3)