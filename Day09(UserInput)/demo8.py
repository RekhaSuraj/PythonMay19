list1 = [10,20,30,40,'hi','hello',50,'60']
# To access elements based on index
# syntax: list_name[index_number]

print(len(list1))
# 8

print('value at index 0',list1[0])
print('value at index 1',list1[1])
print('value at index 2',list1[2])
print('value at index 3',list1[3])
print('value at index 4',list1[4])
print('value at index 5',list1[5])
print('value at index 6',list1[6])
print('value at index 7',list1[7])

# value at index 0 10
# value at index 1 20
# value at index 2 30
# value at index 3 40
# value at index 4 hi
# value at index 5 hello
# value at index 6 50
# value at index 7 60

# print('value at index 8',list1[8])
# IndexError: list index out of range

# index() - Returns first index of value
print(list1.index('hi'))
# 4

