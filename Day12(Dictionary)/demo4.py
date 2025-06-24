d1 = {'Kar':'Blr','Kerala':'TVM','AP':'Amaravathi','TN':'Chennai'}

# copy() - a shallow copy of dict
new_copy = d1.copy()
print(new_copy)
# {'Kar': 'Blr', 'Kerala': 'TVM', 'AP': 'Amaravathi', 'TN': 'Chennai'}

# update() - Adds another dictioanry or a key value pair
d1.update({'Telangana':'Hyderabad'})
print(d1)
# {'Kar': 'Blr', 'Kerala': 'TVM', 'AP': 'Amaravathi', 'TN': 'Chennai', 'Telangana': 'Hyderabad'}

print()
d2 = {'DEL':'Delhi'}
d1.update(d2)
print(d1)
# {'Kar': 'Blr', 'Kerala': 'TVM', 'AP': 'Amaravathi', 'TN': 'Chennai', 'Telangana': 'Hyderabad', 'DEL': 'Delhi'}

# clear() - clears all the key value pairs and returns an empty dict
# d1.clear()
# print(d1)
# {}

# Loop through dictionaries
# for k,v in d1.items():
#     print(k,v)