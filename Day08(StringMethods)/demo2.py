s1 = 'today is a good day'

# capitalize - Return a capitalized version of the string.
# More specifically, make the first character have upper case and the rest lower case.

print(s1.capitalize())
# Today is a good day

# swapcase() - Convert uppercase characters to lowercase and lowercase characters to uppercase.
s2 = 'Today Is a GOod dAy'
print(s2.swapcase())
# tODAY iS A goOD DaY

# casefold - Return a version of the string suitable for caseless comparisons
# It returns a string where all the charcters are in lower case
# This is more aggressive and strong than lower()
print(s2.casefold())
# today is a good day

print('*****'*5)

print('ß'.casefold())
# ss

print('ß'.lower())
# ß