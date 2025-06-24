# print even numbers from 0 to 10 using list comprehension

even_list = [i for i in range(11) if i % 2 == 0]
print(even_list)
# [0, 2, 4, 6, 8, 10]

# hw - odd numbers from 0 to 20 using list comprehension

print()
# print squares of numbers from 1 to 5
sq_list = []
for i in range(1,6):
    sq_list.append(i**2)

print(sq_list)
# [1, 4, 9, 16, 25]


# using list comprehension
sq_list_comp = [j**2 for j in range(1,6)]
print(sq_list_comp)
# [1, 4, 9, 16, 25]
