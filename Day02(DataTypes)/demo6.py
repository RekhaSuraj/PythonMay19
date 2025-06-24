# string(str) - A sequence of characters enclosed within single quotes or double quotes

# single quotes
s1 = 'Welcome'
print(type(s1))
# <class 'str'>

# double quotes
s2 = "Python"
print(type(s2))
# <class 'str'>

# convert string to int()
a = '5'
print('Before conversion',type(a))
# Before conversion <class 'str'>
b = int(a)
print(b)
# 5

print('After conversion',type(b))
# After conversion <class 'int'>

