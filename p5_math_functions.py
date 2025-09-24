import math

pi = 3.14
x = 1
y = 2
z = 3

print(round(pi)) # rounds to the nearest integer
print(round(pi,3)) # rounds to 3 decimal places, in this case it stays the same
     #数值内部仍然是3位小数精度，只是显示时省略了末尾的0。Python在显示浮点数时会自动省略末尾无意义的零。
print(math.ceil(pi)) # rounds up to the nearest integer
print(math.floor(pi)) # rounds down to the nearest integer
print(abs(pi)) # returns the absolute value
print(pow(pi,2))# raises pi to the power of 2
print(math.sqrt(25)) # returns the square root of 25
print(max(x,y,z))
print(min(x,y,z))

print(math.pi)
print(math.e)

#excercise
import math
radius = float(input('enter the radius of a circle(cm): '))
circumference = 2 * math.pi * radius
area = math.pi * math.pow(radius,2)

print(f'The circumference is {circumference} cm')
print(f'The area is {area} cm^2')
