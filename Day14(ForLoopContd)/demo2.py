# Even and odd numbers in separate lists

for i in range(0,21):
    if i % 2 == 0:
        print(i, end=' ')
# 0 2 4 6 8 10 12 14 16 18 20

print()
for j in range(0,21):
    if j % 2 != 0:
        print(j,end=' ')
# 1 3 5 7 9 11 13 15 17 19

print()
# in separate lists
even_list = []
odd_list = []
for i in range(0,21):
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print('Even list',even_list)
print('Odd list',odd_list)

# Even list [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# Odd list [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


