# continue - skips the current iteration and moves to the next iteration of the loop

for i in range(5):
    if i == 3:
        continue # skips the current iteration

    print(i)

print('after the for loop execution')

# 0
# 1
# 2
# 4
# after the for loop execution