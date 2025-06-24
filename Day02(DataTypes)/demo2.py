# complex numbers - are represented by a real part and an imaginary part
# used for performing complex mathematical operations

# Ex: 3+4j
# Here 3.0 is real part, 4j is the imaginary part

x = 3+4j
print(type(x))
# <class 'complex'>

# Fetch only the real part from a complex number
# syntax: <var_name.real>. Gives in float format
print(x.real)
# 3.0

# Fetch imaginary part from a complex number
# syntax:<var_name.imag>. Gives in float format
print(x.imag)
# 4.0

# complex() - converting numnber to a complex number
# Typecasting 

a = 6
b = 9
c = complex(a,b)
print('complex number output:',c)
# complex number output: (6+9j)