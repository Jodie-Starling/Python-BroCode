# collection = single 'variable' used to store multiple values
# List = [] ordered, changeable, Duplicates OK
#            类似可涂改表格
# Set = {} unordered, immutable, but Add/Remove OK, NO duplicate
#            类似国家里的公民
# Tuple = () ordered, and unchangeable, Duplicates OK, FASTER
#            类似商品的条形码

# Variable
fruit = 'fruit'


print(fruit)


# List
fruits = ['apple', 'banana', 'cherry', 'orange','cherry']

print(fruits[0:3:2])
for x in fruits:
    print(x)

fruits[0] = 'coconut'

print(len(fruits))
print('apple' in fruits)
print('watermelon' not in fruits)

fruits.sort()   # alphabetical
print(fruits)
fruits.reverse() # reverse order
print(fruits)

fruits.append('watermelon') # add to end
fruits.remove('banana') # remove specific item
fruits.insert(1, 'blueberry') # add at specific index
print(fruits)

print(fruits.index('cherry'))   # first index of specific item, error if not found
print(fruits.count('cherry'))   # 0 if not found

fruits.clear()
print(fruits)

print(dir(fruits))  # list of all methods
print(help(fruits))  # description of all methods
print(help(fruits.append('strawberry')))  # help(method) for specific method


# Set
fruits = {'apple', 'banana', 'cherry', 'orange'}
print(fruits)

fruits.add('watermelon') # add item, ignore if already exists
fruits.remove('banana') # remove specific item, error if not found
fruits.pop() # remove random item, return it, error if empty, 弹出
fruits.clear()
print(fruits)


# Tuple, faster than list, use when data should not change
fruits = ('apple', 'banana', 'cherry', 'orange','cherry')
print(dir(fruits)) # list of all methods
print(help(fruits)) # description of all methods
print(help(fruits.count('apple'))) # help(method) for specific method

print(len(fruits))
print('apple' in fruits)

print(fruits[0:3:2])
print(fruits.index('cherry'))   # first index of specific item, error if not found
print(fruits.count('cherry'))   # 0 if not found

for fruit in fruits:
    print(fruit)


num_pad = ((1, 2, 3), 
           (4, 5, 6), 
           (7, 8, 9),
           ('*', 0, '#'))

for row in num_pad:
    for col in row:
        print(col, end = ' ')
    print()