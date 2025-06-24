# Nested list - lists inside another list
l1 = [10,20,30,['hi','hello'],40,[50,60],[70,80]]

print(len(l1))
# 7

print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])
print(l1[4])
print(l1[5])
print(l1[6])

# 10
# 20
# 30
# ['hi', 'hello']
# 40
# [50, 60]
# [70, 80]
print('-------------------------------')

# fetch 'hello'
print(l1[3][1])
# hello

# fetch 70
print(l1[6][0])
# 70

# slicing
# fetch 40,[50,60]
print(l1[4:6])
# [40, [50, 60]]

# -ve slicing
print(l1[-3:-1])
# [40, [50, 60]]

# reverse or -1 step
print(l1[::-1])
# [[70, 80], [50, 60], 40, ['hi', 'hello'], 30, 20, 10]


# 40, ['hi', 'hello']
print(l1[4:2:-1])
# [40, ['hi', 'hello']]


# hw
l2 = [1,2,['a',2,[3],5,6],[3,'d','r','t','d',[[11,22,33],[12,13,14],[34,56,78],11,12,13],'abc'],'python','java']

# print 12 - first 12 using indexing

# print 22 - using indexing

# [2,[3],5,6] using slicing
