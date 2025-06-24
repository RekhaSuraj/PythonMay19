# Converting float type to int type - int()
a = 2.5
print('Before conversion:',type(a))
# Before conversion: <class 'float'>
l = int(a)
print(l)
print('After conversion:',type(l))
# After conversion: <class 'int'>

# 2

# converting int to float - float()
print(float(5))
# 5.0

# Converting a str to bool
x = 'True'
print('Before conversion',type(x))
# Before conversion <class 'str'>
b = bool(x)

print(b)
# True
print('After conversion',type(b))
# After conversion <class 'bool'>