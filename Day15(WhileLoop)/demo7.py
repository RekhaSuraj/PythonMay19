# Print only capital letter animals into a new list
list1 = ['Cat','DOG','Sheep','GOAT','COW']

up_list = []
for i in list1:
    if i.isupper():
        up_list.append(i)

print(up_list)
# ['DOG', 'GOAT', 'COW']

print()
# using list comprehension
up_comp_list = [j for j in list1 if j.isupper()]
print(up_comp_list)
# ['DOG', 'GOAT', 'COW']

print()
# Replace negative numbers with 0
nums = [20,-10,30,-25,-70,50,-50]

new_list = [i if i>0 else 0 for i in nums]
print(new_list)
# [20, 0, 30, 0, 0, 50, 0]

# hw - using normal for loop



