# For loop through a dictionary

dict1 = {1:'Red',2:'Blue',3:'Orange',4:'White',5:'Yellow'}

print(dict1[1])
# Loop through keys
for k in dict1:
    print(k)

# 1
# 2
# 3
# 4
# 5

print()
# Loop through all items
for v in dict1.items():
    print(v)

# (1, 'Red')
# (2, 'Blue')
# (3, 'Orange')
# (4, 'White')
# (5, 'Yellow')

# Loop through only values
for m in dict1:
    print(dict1[m])

# Red
# Blue
# Orange
# White
# Yellow

for k,v in dict1.items():
    print(k)

# 1
# 2
# 3
# 4
# 5

for k,v in dict1.items():
    print(v)

# Red
# Blue
# Orange
# White
# Yellow

for k,v in dict1.items():
    print(f'{k}-{v}')

# 1-Red
# 2-Blue
# 3-Orange
# 4-White
# 5-Yellowm