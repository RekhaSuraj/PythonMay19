# List comprehension - Shorter syntax in one line to create a new list based on an exiting list

# Using comprehension
# sy : [Expression for item in Iterable]
# Applied condition :
# sy : [Expression for item in iterable if condition]

# print numbers from 1 to 10 in a list
list1 = []
for i in range(11):
    list1.append(i)
print(list1)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# using list comprehension:
list2 = [j for j in range(11)]
print(list2)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
