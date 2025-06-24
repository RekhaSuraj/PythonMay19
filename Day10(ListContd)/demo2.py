# slicing
# list[start:stop:step]

l1 = [20,10,'hello','hi','30',50, 'welcome']
print(len(l1))
# 7

print(l1[3])
# hi

# fetch 'hello','hi'
print(l1[2:4])
# ['hello', 'hi']

# fetch '30',50, 'welcome'
print(l1[4::])
# ['30', 50, 'welcome']


# -ve slicing
# fetch 'hello','hi'
print(l1[-5:-3])
# ['hello', 'hi']

# # fetch '30',50, 'welcome'
print(l1[-3::])
# ['30', 50, 'welcome']

# step: -1
print(l1[::-1])
# ['welcome', 50, '30', 'hi', 'hello', 10, 20]

# fetch 'hi', 'hello'
print(l1[::-1])

print(l1[3:1:-1])
# ['hi', 'hello']