# even_odd program inside a function

def even_odd(n):
    if n % 2 == 0:
        print(f'{n} is an even number')
    else:
        print(f'{n} is an odd number')


even_odd(6)
# 6 is an even number

# take input from user
num1 = int(input('Enter a number'))
even_odd(num1)

# Enter a number7
# 7 is an odd number

# hw - generate even numbers upto a range taking input from user