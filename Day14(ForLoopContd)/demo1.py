# range()
# range(start,stop,step)
# start - optional - starting number, default is 0
# stop - the sequence stops before this number
# step - the increment between numbers(default is 1)

# to display numbers from 0 to 10
for i in range(11):
    print(i)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

print()
# print even numbers from 0 to 20 - using step - 2
for i in range(0,21,2):
    print(i)


# hw- print odd numbers from 0 to 20 using step - 2
print()
# print in reverse order
for i in range(20,0,-1):
    print(i, end=' ')