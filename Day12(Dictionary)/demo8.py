# Check for username and password from user
# considering un = 'python'
# pwd = 1234
un = input('Enter username')
pwd = int(input('Enter password'))

if un == 'python' and pwd == 1234:
    print('Access granted')
else:
    print('Access not granted, username or password is wrong')

# Enter usernamepython
# Enter password1234
# Access granted

# Enter usernamehello
# Enter password1234
# Access not granted, username or password is wrong

# Enter usernamepython
# Enter password6789
# Access not granted, username or password is wrong

