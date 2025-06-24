# Flow control statements:
# 1. Conditional statements
# 2. Iterable statements
# 3. Transfer statements

# Conditional statements
# There are 4 types:
# 1. if statement
# 2. if else statement
# 3. if elif else
# 4. nested if else

# if statement in python
# It takes a condition and evaluates to either True o False
# If the condition is True, then the True block of code will be executed, and if the condition is False, then
# that block of code will be skipped and control moves to next line

# Syntax of if statement:
# if condition:
#     statement1:
#     statement2
#     statement3

x = True
if x == True:
    print('Condition is True')

print('Outside if condition')

# Condition is True
# Outside if condition

print()
x = False
if x == True:
    print('Condition is True')

print('Outside if condition')
# Outside if condition