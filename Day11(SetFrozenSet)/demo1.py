# Set

# Set is an unordered collection of unique elements, set does not support index
# set is declared inside flower braces
# insertion order is not preserved, does not allow duplicates
# Mutable: You can modify a set by adding or removing elements (add(), remove(), discard(), pop(), clear()).
# Elements Must Be Immutable: You cannot have lists or other sets as elements in a set because they are
# not hashable.

# Ways to create a set
s1 = {10,20,30,40}
print(type(s1))
# <class 'set'>

# If we define empty flower brackets, python return dict type
s2 = {}
print(type(s2))
# <class 'dict'>

# so to create an empty set,
s3 = set()
print(type(s3))
# <class 'set'>

# to create using constructor
s4 = set({11,22,33,44,55})
print(type(s4))
# <class 'set'>