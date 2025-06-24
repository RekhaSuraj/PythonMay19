# Bitwise operators:
# 1. Bitwise and (&)
# 2. Bitwise or (|)
# 3. Bitwise XOR (^)
# 4. Bitwise not (~)
# 5. Bitwise shiftleft (<<)
# 6. Bitwise shiftright (>>)

# Bitwise & (and)
# Performs and operation on binaries
x = 5
y = 3
print(x&y)
# 1

# 5 --> 0  1  0  1
# 3 --> 0  0  1  1
# & --------------
#       0  0  0  1 - > 1

a = 4
b = 8
print(a&b)
# 0

print(4&8)
# 0

#2. Bitwise | (or) - It performs or operation on binaries
b1 = 6
b2 = 9
print('bitwise or:',b1|b2)
# 15

# 6 --> 0 1 1 0
# 9 --> 1 0 0 1
# | ------------
# 		1 1 1 1 --> 15

