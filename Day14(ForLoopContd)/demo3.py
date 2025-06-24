# Separate positive and negative numbers in 2 different lists
list1 = [10,-25,-3,40,16,-30,70,-56]

pos_list = []
neg_list = []

for i in list1:
    if i > 0:
        pos_list.append(i)
    else:
        neg_list.append(i)


print(pos_list)
print(neg_list)

# [10, 40, 16, 70]
# [-25, -3, -30, -56]
