# n1 = int(input('Enter a number'))
# n2 = int(input('Enter another number'))
#
# print(n1/n2)
#
# print('End line')
# Abnormal termination
# ZeroDivisionError: division by zero

n1 = int(input('Enter a number'))
n2 = int(input('Enter another number'))
try:
    print(n1 / n2)
except:
    print('Error occurred in class name')

finally:
    print('Finally block')

print('End line')

# Enter a number6
# Enter another number2
# 3.0
# End line


# Graceful termination
# Enter a number9
# Enter another number0
# Error occurred in class name
# Finally block
# End line