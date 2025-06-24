# control flow statements
# In Python, continue, break, and pass are control flow statements used in loops and conditional statements, but they behave differently:
#
# 1. break
# Exits the loop completely.

for i in range(5):
    print(i)
    if i == 3:
        break

print('after for check')

# 0
# 1
# 2
# 3
# after for check