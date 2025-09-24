# slicing = creates a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step] [起始：结束：步长] 正数从前数，负数从后数

name = "Miranda Kerr"

print(name[4])
print(name[-1])
print(name[:6])
print((name[7:]))
print(name[:]) # 默认：从头开始，到结尾，步长为1
print(name[::-1]) # 反转字符串
print(name[-4:]) # 从倒数第四个字符开始，到结尾
print(name[-4::-1]) # 从倒数第四个字符开始，反转字符串