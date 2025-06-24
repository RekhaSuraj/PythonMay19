# update() - Update a set with the union of itself and others.(same as extend in list)
set1 = {22,33,44,55,66,77,88}
set2 = {99,11,101}
# set1.update(set2)
# print(set1)

# Remove an element from a set if it is a member.
# Unlike set. remove(), the discard() method does not raise an exception when an element is missing from the set.
set1.discard(66)
# print(set1)

# If an item is not present, it wil not throw error like below:
set1.discard(500)
print(set1)
# {33, 22, 55, 88, 44, 77}