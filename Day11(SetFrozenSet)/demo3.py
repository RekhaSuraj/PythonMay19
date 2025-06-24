s1 = {22,44,55,77,'hi',88,'hello'}
# add() -
# print(help(set))

# Add an element to a set.
#  |
#  |This has no effect if the element is already present.
s1.add(99)
# print(s1)

# If we try to add duplicate value, it will not throw error, but it will not add duplicate values
s1.add(55)
print(s1)
# {99, 22, 55, 88, 'hi', 44, 77, 'hello'}

# copy() - returns a shallow copy of the set
s2 = s1.copy()
print(s2)
# {99, 'hi', 44, 77, 'hello', 22, 55, 88}