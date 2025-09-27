# dictionary = a collection of {key:value} pairs
#              ordered and changeable, No duplicates


capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

print(dir(capitals))
print(help(capitals))

print(capitals.get('USA'))
print(capitals.get('Germany'))  # returns None if not found

if capitals.get('Japan'):
    print('That capital exists.')
else:
    print("That capital doesn't exist.")

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'})

print(capitals)

capitals.pop('China')
capitals.popitem()  # removes last item
capitals.clear()  # empties the dictionary
del capitals  # deletes the entire dictionary
            # 报错是因为上面del了，capitals不存在了

keys = capitals.keys()
values = capitals.values()
items = capitals.items()
print(keys)
print(values)   
print(items)  # list of tuples

for key in keys:
    print(capitals[key])

for key, value in capitals.items():
    print(f'{key}:{value}')