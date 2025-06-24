# Program on arguments
def add_fun(*args):
    return sum(args)


print(add_fun(5,10,15,20,25,30))
# 105

# Product of all numbers in a sequence
def product(*args):
    res = 1
    for i in args:
        res = res * i

    return res

print(product(2,3,4,5,6))

# a and b are pointing to the same object in memory, Both have the same address
a = 10
b = 10

print(a is b)
print(id(a))
print(id(b))

# True
# 140729160514264
# 140729160514264

print()
str1 = 'hello'
str2 = 'hello'

print(str1 is str2)
# True

print(id(str1))
print(id(str2))
# 2288655562288
# 2288655562288

print()
a = 10
b = 20
print(a is b)

print(id(a))
print(id(b))
# False
# 140729160514264
# 140729160514584


# To fetch last element
# list1=[10,20,30,40,50]
# len(list1)
# list1[4]
# list1[len(list1-1)]