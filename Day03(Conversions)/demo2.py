# Conversion from decimal to hexadecimal
# Hexadecimal will have values from 0-9 and A-F/a-f
# Hexadecimal values will be prefixed with 0x
# We use hex(<decimal_number>) to convert from decimal to hex number

v1 = 15
res = hex(v1)
print(res)

# 0xf

# directly
print(hex(35))
# 0x23

# Conversion from hex to decimal number
print(0x23)
# 35

print(0xf)
# 15