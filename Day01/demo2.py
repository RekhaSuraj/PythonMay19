# Ways of creating a variable
# 1. Single value assigned to single variable
a = 10
x = 20
print(a)
print(x)
# 10
# 20

# 2. single value assigned to multiple variable
a=b=c=10
print(a)
print(b)
print(c)

# 10
# 10
# 10

print()
print('Multiple values assigned to multiple variable')
# 3.Mutilple values to assign multiple variables using the semicolan ;
v1 = 10 ; v2 = 20; v3 = 30
print(v1,v2,v3)
# print(v1)
# print(v2)
# print(v3)

# 4. String value assigned to a variable
a1 = 'Shalini' #string (inside a single quote or double quotes)
print(a1)
# Shalini

a2 = "Shalini"
print(a2)
# Shalini

# 5. Multiple values assigned to multiple variables in the same line without using semicolon
(x,y,z) = (10,20,30)
print(x,y,z)
# 10 20 30