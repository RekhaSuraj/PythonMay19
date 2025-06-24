# String

# Strings - Strings are a sequence of characters(letters, alphabets) 
# enclosed within single quote or double quotes
# Ex : 'Welcome to Python learning'

s1 = 'Python Developer'
print(s1)
# Python Developer

print(type(s1))
# <class 'str'>

s2 = "Welcome"
print(s2)
print(type(s2))
# <class 'str'>
# Welcome

# Conversion or type casting of int to string:
v1 = 20
print('Before conversion',type(v1))
# Before conversion <class 'int'>
s1 = str(v1)
print('after conversion',type(s1))
# after conversion <class 'str'>

print(s1)
# 20