# Check if a string is a Palindrome or not

s1 = input('Enter a string')
print(s1[::-1])

if s1[::-1] == s1:
    print('String is a Palindrome')
else:
    print('String is not a Palindrome')

# Enter a stringmom
# mom
# String is a Palindrome

# Enter a stringdam
# mad
# String is not a Palindrome

# Enter a stringlevel
# level
# String is a Palindrome