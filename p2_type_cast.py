#type casting = converting a data type of a value to another data type
#               str(), int(), float(),bool()

name = 'Miranda Kerr'
age = 42
is_student = False

age = float(age)

print(age)
print(f'{name}\'s age is {age}') #转义单引号


name = bool(name)
print(name) #非空字符串转换为True,空格也是True