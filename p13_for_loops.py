# for loops = excute a block of code a fixed number of times
#              iterate over a range, string, sequence, etc.

for x in reversed(range(1,11)):
    print(x)

print('HAPPY NEW YEAR!')


for x in 'Hello World':
    if x == ' ':
        continue
    print(x)