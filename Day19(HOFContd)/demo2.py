from functools import reduce
# reduce()
# SY: reduce(function,iterable[,initial])

# reduce() works by calling the function we passed for the first two items in the sequence.
# The result returned by the function is used in another call to function alongside with the
# next (third in this case), element. We have to import reduce() from functools

# Add all items in the list using reduce()
list1 = [10,20,30,40,50,60]


def sum_num(x,y):
    return x+y


print(reduce(sum_num,list1))

# First 10 + 20 = 30
# 30 + 30 = 60
# 60 + 40 = 100
# 100 + 50 = 150
# 150 + 60 = 210


# using lambda
print(reduce(lambda a,b:a+b, list1))
# 210



