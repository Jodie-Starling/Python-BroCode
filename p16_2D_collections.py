# 2D Collections - List of Lists, Tuples，Sets，mixed
# 2D Collections - Tuple of the same to Lists
# 2D Collections - Set of Tuples
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "lettuce", "spinach"]
meats = ["chicken", "beef", "pork"]

groceries = [fruits, vegetables, meats]

# OR ---following is also valid---
# groceries = [["apple", "banana", "cherry"],
#               ["carrot", "lettuce", "spinach"],
#               ["chicken", "beef", "pork"]]

print(groceries)
print(groceries[0])
print(groceries[0][1])

fruits[0] = 'coconut'
print(groceries)
groceries[1][1] = 'broccoli'
print(vegetables)
print(groceries)

for collection in groceries:
    print(collection)   # prints each sublist


for category in groceries:
    for food in category:
        print(food, end = ' ') # prints each item in sublists
    print()