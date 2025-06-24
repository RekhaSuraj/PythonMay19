# Higher Order Functions
# 1. map
# 2. filter
# 3. reduce


# map
# The map(), filter() and reduce() functions bring a bit of functional programming to Python.
#  All three of these are convenience functions that can be replaced with List Comprehensions or loops,
# but provide a more elegant and short-hand approach to some problems.

# The map() Function
# The syntax is:
# The map() function iterates through all items in the given iterable and executes the function
# we passed as an argument on each of them.

# map(function, iterable(s))

list1 = ['hello','archana','hru','welcome']


def upper_fun(l):
    return l.upper()


print(map(upper_fun,list1))
# <map object at 0x000001C4A9407250>
print(list(map(upper_fun,list1)))
# ['HELLO', 'ARCHANA', 'HRU', 'WELCOME']

print(tuple(map(upper_fun,list1)))
# ('HELLO', 'ARCHANA', 'HRU', 'WELCOME')


# using lambda
print(list(map(lambda a:a.upper(),list1)))
# ['HELLO', 'ARCHANA', 'HRU', 'WELCOME']




