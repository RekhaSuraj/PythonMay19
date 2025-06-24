# Check for even or odd number

n1 = int(input('Enter a number'))

if n1 > 0: #outer if
    if n1 % 2 == 0: # inner if
        print(f'{n1} is an even number')

    else: #inner else
        print(f'{n1} is an odd number')

else: #outer else
    print('Invalid input')


# Enter a number6
# 6 is an even number

# Enter a number9
# 9 is an odd number

# Enter a number-5
# Invalid input

# Enter a number0
# Invalid input