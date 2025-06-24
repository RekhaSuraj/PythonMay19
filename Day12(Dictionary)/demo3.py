dict1 = {10:'Cat',20:'Dog',30:'Cow',40:'Horse'}

print(dict1[40])
# Horse

print(dict1[20])
# Dog

# dict methods
# pop() - remove specified key and return the corresponding value
rem_value = dict1.pop(20)
print(rem_value)

print(dict1)
# {10: 'Cat', 30: 'Cow', 40: 'Horse'}

print()
# popitem() - Removes the last key value pair from dict
dict1.popitem()
print(dict1)