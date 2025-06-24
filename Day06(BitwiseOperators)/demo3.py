#5. Bitwise shift left <<
#6. Bitwise shift right >>

# Bitwise shift left - Shifts the position of the binary to left (according to the number of positions given)
# This adds the bits 
v1 = 4
print(v1<<1)
# 8

# 4 << 1 
#    	0 1 0 0 (4 in binary) 
# << 1  
# ---------------
#       1 0 0 0 (8 in binary)

# One more example
var1 = 5
print(var1 << 2)
#    0 0 0 1 0 1   (5 in binary)
# << 2
# ---------------
#    0 1 0 1 0 0   (20 in binary)

print('shift left for 5-2bits',5<<2)
# shift left for 5-2bits 20


v2 = 24
print(v2<<2)
# 96


#6. Bitwise shift right - Shifts the position of the binary to right (according to the number of positions given)
# This looses the bits 
v3 = 5
print('shift right 1:',v3>>1)
# shift right 1: 2

print(8>>2)


#    0 1 0 1   (5 in binary)
# >> 1
# ---------------
#    0 0 1 0 --> (2 in binary, here we are loosing one bit)


