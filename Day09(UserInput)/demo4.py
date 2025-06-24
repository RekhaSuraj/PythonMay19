# For integer operation, we have to convert input to int

n1 = int(input('Enter first number'))
n2 = int(input('Enter second number'))

print(type(n1))
print(type(n2))

res = n1+n2
print(f'Addition of {n1} and {n2} is {res}')

# Enter first number10
# Enter second number5
# <class 'int'>
# <class 'int'>
# Addition of 10 and 5 is 15

# hw - Multiplication, division, floor division and exponentation