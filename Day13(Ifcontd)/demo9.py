# Simple ATM program

balance = 1000
num1 = int(input('Enter amount to withdraw'))

if num1 < balance:
    print('Transaction successful')
    balance = balance - num1
    print('Your balance is:',balance)

else:
    print('Insufficient balance')


# Enter amount to withdraw400
# Transaction successful
# Your balance is: 600

# Enter amount to withdraw1500
# Insufficient balance