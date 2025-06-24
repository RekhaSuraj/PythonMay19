# Pattern printing programs

# Square pattern print
for i in range(4):
    for j in range(4):
        print('*',end=' ')
    print() # next line

# * * * *
# * * * *
# * * * *
# * * * *

print()
# Print rectangle pattern
for i in range(5):
    for j in range(4):
        print('*',end=' ')
    print()

# * * * *
# * * * *
# * * * *
# * * * *
# * * * *

# Right angled triangle pattern
print()
for i in range(5):
    for j in range(i):
        print('*',end=' ')
        # print(i,j)
    print()

# *
# * *
# * * *
# * * * *