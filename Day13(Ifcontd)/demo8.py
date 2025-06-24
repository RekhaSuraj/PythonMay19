# Simple Calculator program

num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))

operation = input('Enter the operation: +, -, *, /')

if operation == '+':
    print(f'Addition of {num1} and {num2} is {num1+num2}')

elif operation == '-':
    print(f'Subtraction of {num1} and {num2} is {num1 - num2} ')

elif operation == '*':
    print(f'Multiplication of {num1} and {num2} is {num1 * num2}')

elif operation == '/':
    print(f'Division of {num1} and {num2} is {num1/num2}')


else:
    print('Invalid Input')

# Enter first number10
# Enter second number20
# Enter the operation: +, -, *, /+
# Addition of 10 and 20 is 30

# Enter first number20
# Enter second number15
# Enter the operation: +, -, *, /*
# Multiplication of 20 and 15 is 300