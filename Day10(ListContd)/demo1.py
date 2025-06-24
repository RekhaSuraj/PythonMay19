list1 = [10,20,30,40,50,20,40,20]
# copy() - creates a copy of list
l_copy = list1.copy()
print(l_copy)

# [10, 20, 30, 40, 50]

# count() - number of occurrences of the item in the list
print(list1.count(20))
# 3

# extend() - Extend list by appending elements from the iterable(list).
l2 = ['hi','hello','welcome']
list1.extend(l2)
print(list1)
# [10, 20, 30, 40, 50, 20, 40, 20, 'hi', 'hello', 'welcome']

print(l2)
# ['hi', 'hello', 'welcome']

# reverse() - reverses the original list
list1.reverse()
print(list1)


