# nested for loop
# A for loop inside a for loop is called a nested for loop. The inner loop runs completely for each iteration of
# the outer loop.

# for i in range(outer_loop_range):
#     for j in range(inner_loop_range):
#         # Code block to execute


for i in range(4):
    for j in range(4):
        print(f'{i}-{j}')
    print()

# 0-0
# 0-1
# 0-2
# 0-3
#
# 1-0
# 1-1
# 1-2
# 1-3
#
# 2-0
# 2-1
# 2-2
# 2-3
#
# 3-0
# 3-1
# 3-2
# 3-3
