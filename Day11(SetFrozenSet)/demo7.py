# Typecasting - conversion from datatype to another

list1 = [10,20,30,40,50,60]
print(type(list1))
# <class 'list'>

print('convert list to tuple*******')
# convert list to tuple
t1 = tuple(list1)
print(t1)
print(type(t1))
# (10, 20, 30, 40, 50, 60)
# <class 'tuple'>

print('convert list to set*******')
# convert list to set
s1 = set(list1)
print(type(s1))
print(s1)
# <class 'set'>
# {40, 10, 50, 20, 60, 30}

print('convert set to list*******')
# convert set to list
s2 = {'a','b',10,'c',20}
print(type(s2))
l1 = list(s2)
print(type(l1))
# <class 'set'>
# <class 'list'>

