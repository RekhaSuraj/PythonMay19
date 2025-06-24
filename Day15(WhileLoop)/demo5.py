# print all -ve numbers into a new list

list1 = [10,-2,31,9,-16,-50,-25]
neg_list = []
for i in list1:
    if i < 0:
        neg_list.append(i)


print(neg_list)
# [-2, -16, -50, -25]

print()
# using list comprehension:
neg_compList = [j for j in list1 if j < 0]
print(neg_compList)
# [-2, -16, -50, -25]

print()
# Print positive numbers
pos_list = [p for p in list1 if p > 0]
print(pos_list)
# [10, 31, 9]
