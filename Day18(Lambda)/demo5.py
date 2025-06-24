# Filter () -
# The filter() Function
# Similar to map(), filter() takes a function object and an iterable and creates a new list.

# As the name suggests, filter() forms a new list that contains only elements that satisfy a certain condition,
 # i.e. the function we passed returns True.

# The syntax is:
# filter(function, iterable(s))

list1 = [2,4,3,5,10,7,13,12,16,20]

def even_fun(n):
    return n%2 == 0

print(list(filter(even_fun,list1)))
# [2, 4, 10, 12, 16, 20]

# hw - print odd numbers from the above list using filter()

# using lambda
print(tuple(filter(lambda n:n%2 == 0, list1)))
# (2, 4, 10, 12, 16, 20)