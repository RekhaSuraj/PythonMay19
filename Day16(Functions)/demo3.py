# Display if a number is prime number or not
n = int(input('Enter a number'))
is_prime = True
for i in range(2,n-1):
    if n % i == 0:
        is_prime = False
        break

if is_prime == True:
    print(f'{n} is a prime number')
else:
    print(f'{n} is not a prime number')

# Enter a number7
# 7 is a prime number

# Enter a number6
# 6 is not a prime number
