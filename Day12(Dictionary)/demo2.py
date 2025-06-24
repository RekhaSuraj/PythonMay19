d1 = {1: 'Mango',2:'Banana',3:'Strawberry',4:'Papaya'}

# keys() - a set-like object providing a view on Dict's keys
# To fetch only keys from the above dict
print(d1.keys())
# dict_keys([1, 2, 3, 4])

var1 = d1.keys()
print(var1)
# dict_keys([1, 2, 3, 4])

print()
# Fetch only values
print(d1.values())
# dict_values(['Mango', 'Banana', 'Strawberry', 'Papaya'])

print()
# Fetch all items from dict
print(d1.items())
# dict_items([(1, 'Mango'), (2, 'Banana'), (3, 'Strawberry'), (4, 'Papaya')])

