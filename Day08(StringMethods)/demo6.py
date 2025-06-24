# split()
str1 = 'Hello World of Python'
# split() - Return a list of the substrings in the string, using sep as the separator string
list1 = str1.split()
print(str1)
print(list1)

# sep: '-' is a separator. Based on this, a new list is created
str2 = 'Hello-World-of-Python'
print(str2.split('-'))

str3 = 'Hello&World&of&Python'
print(str3.split('&'))
# ['Hello', 'World', 'of', 'Python']

# join() - concatenates any number of strings
list1 = ['Hello', 'World', 'of', 'Python','Testing']
s1 = ' '.join(list1)
print(s1)
# Hello World of Python Testing

s2 = '-'.join(list1)
print(s2)
# Hello-World-of-Python-Testing





