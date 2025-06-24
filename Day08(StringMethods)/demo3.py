s1 = 'Python Automation Testing'

print(len(s1))
# find() - Returns the index number of the specified character('o')
print(s1.find('o'))
# 4

print(s1.find('o',5))
# 10

print(s1.find('o',11,20))
# 15

print('FInd Z using find()')
print(s1.find('z'))
# If the substring is not found, it returns -1

# index()
print(s1.index('o'))
# 4

print(s1.index('o',5))
# 10

# print(s1.index('z'))
# If the substring is not found, it throws the below error and stops the execution
# ValueError: substring not found

print('hello')
