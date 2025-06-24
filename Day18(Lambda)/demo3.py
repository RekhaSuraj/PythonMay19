# square of all numbers in a list

list1 = [4,10,14,20,24,30]


def square_fun(n):
    return n**2


print(list(map(square_fun,list1)))
# [16, 100, 196, 400, 576, 900]

# hw - double numbers using map()

# using lambda
print(tuple(map(lambda n: n**2,list1)))
# (16, 100, 196, 400, 576, 900)
