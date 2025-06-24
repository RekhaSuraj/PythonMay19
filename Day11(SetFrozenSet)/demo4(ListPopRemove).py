# pop() - Remove and return item at index (default last)
# list pop
l1 = [10,20,40,30,60,35,25]
del_var = l1.pop(2)
print(del_var)
print(l1)
# 40
# [10, 20, 30, 60, 35, 25]


# If we dont specify index, inside pop(), it will remove last element by default
var2 = l1.pop()
print(var2)
print(l1)
# 25
# [10, 20, 30, 60, 35]

l2 = [5,10,15,20,'hi','hello']
# remove() - Remove first occurrence of value
l2.remove('hi')
print(l2)
# [5, 10, 15, 20, 'hello']

l2.remove(10)
print(l2)
# [5, 15, 20, 'hello']
# print(help)

# l1.pop(7)
# print(l1)
# IndexError: pop index out of range

l2.remove(100)
print(l2)
# ValueError: list.remove(x): x not in list