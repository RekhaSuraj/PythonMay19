# pop() - Remove and return an arbitrary set element.
# print(help(set.pop))
s1 = {5,10,15,20,'hi','hello'}
# var1 = s1.pop()
# print(var1)
# print(s1)

# 20
# {5, 10, 'hello', 'hi', 15}

# remove() - Remove an element from a set; it must be a member.
s1.remove('hi')
print(s1)
# {20, 5, 10, 'hello', 15}

# If we try to remove an item not present in the set
# s1.remove('abc')
# print(s1)
# KeyError: 'abc'

# clear() - removes all elements from the set and returns an empty set
s1.clear()
print(s1)
# set()

