# Replace negative numbers in the list to 0 (For loop)
list1 = [10,-20,30,-40,50,-60]
len_list = len(list1)
print(len_list)

for i in range(len_list):
    if list1[i] < 0:
        list1[i] = 0

print(list1)

# [10, 0, 30, 0, 50, 0]



